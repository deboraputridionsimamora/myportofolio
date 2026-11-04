import os

from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Certification
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import CertificationSerializer


# dicek manual di sini, soalnya "password" bukan field model,
# jadi gak bisa divalidasi lewat serializer
def _password_is_correct(request):
    return request.data.get("password") == os.getenv("FORM_PASSWORD")


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def certification_list(request):
    if request.method in ("GET", "HEAD"):
        certifications = Certification.objects.prefetch_related("starred_by")

        title = request.query_params.get("title", "").strip()
        if title:
            certifications = certifications.filter(title__icontains=title)

        sort_option = request.query_params.get("sort", "terbaru")
        if sort_option == "stars":
            certifications = certifications.annotate(
                star_total=Count("starred_by")
            ).order_by("-star_total", "-issue_date")
        else:
            certifications = certifications.order_by("-issue_date")

        serializer = CertificationSerializer(
            certifications, many=True, context={"request": request},
        )
        return Response(serializer.data)

    # sampai sini cuma superuser yang lolos (Editor ketolak permission di atas)
    if not _password_is_correct(request):
        return Response(
            {"password": ["Password salah! Sertifikat tidak ditambahkan."]},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = CertificationSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def certification_detail(request, certification_id):
    certification = get_object_or_404(
        Certification.objects.prefetch_related("starred_by"), pk=certification_id,
    )

    if request.method in ("GET", "HEAD"):
        serializer = CertificationSerializer(certification, context={"request": request})
        return Response(serializer.data)

    # PUT/PATCH/DELETE semuanya butuh password yang benar
    if not _password_is_correct(request):
        return Response(
            {"password": ["Password salah! Perubahan tidak disimpan."]},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if request.method == "DELETE":
        certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = CertificationSerializer(
        certification,
        data=request.data,
        partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def certification_star(request, certification_id):
    certification = get_object_or_404(Certification, pk=certification_id)

    if certification.starred_by.filter(pk=request.user.pk).exists():
        certification.starred_by.remove(request.user)
    else:
        certification.starred_by.add(request.user)

    serializer = CertificationSerializer(certification, context={"request": request})
    return Response(serializer.data)