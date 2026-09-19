import os

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Certification
from main.forms import CertificationForm


def show_main(request):
    context = {
        "name": "Debora Putri Dion Simamora",
        "npm": "2506544126",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Debora Putri Dion Simamora",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def create_certification(request):
    form = CertificationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        if form.cleaned_data["password"] != os.getenv("FORM_PASSWORD"):
            messages.error(request, "Password salah! Sertifikat tidak ditambahkan.")
        else:
            form.save()
            messages.success(request, "Sertifikat baru berhasil ditambahkan!")
            return redirect("main:show_certification")

    context = {
        "name": "Debora Putri Dion Simamora",
        "form": form,
        "form_action": reverse("main:create_certification"),
        "form_title": "Add New Certification",
        "submit_label": "Tambah Sertifikat",
    }
    return render(request, "certification_form.html", context)


def update_certification(request, id):
    certification = get_object_or_404(Certification, pk=id)
    form = CertificationForm(request.POST or None, instance=certification)

    if request.method == "POST" and form.is_valid():
        if form.cleaned_data["password"] != os.getenv("FORM_PASSWORD"):
            messages.error(request, "Password salah! Perubahan tidak disimpan.")
        else:
            form.save()
            messages.success(request, "Sertifikat berhasil diperbarui!")
            return redirect("main:show_certification")

    context = {
        "name": "Debora Putri Dion Simamora",
        "form": form,
        "form_action": reverse("main:update_certification", args=[id]),
        "form_title": "Edit Certification",
        "submit_label": "Simpan Perubahan",
    }
    return render(request, "certification_form.html", context)


def delete_certification(request, id):
    certification = get_object_or_404(Certification, pk=id)

    if request.method == "POST":
        password_input = request.POST.get("password", "")
        if password_input != os.getenv("FORM_PASSWORD"):
            messages.error(request, "Password salah! Sertifikat tidak dihapus.")
        else:
            certification.delete()
            messages.success(request, "Sertifikat berhasil dihapus!")
        return redirect("main:show_certification")

    return redirect("main:show_certification")


def get_certifications_json(request):
    certifications = Certification.objects.all().order_by("-issue_date")
    certifications_json = serializers.serialize("json", certifications)
    return HttpResponse(certifications_json, content_type="application/json")


def show_certification(request):
    json_response = get_certifications_json(request)

    certifications = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    certifications = [cert.object for cert in certifications]

    context = {
        "name": "Debora Putri Dion Simamora",
        "certification_list": certifications,
    }
    return render(request, "certification.html", context)