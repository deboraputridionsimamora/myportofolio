import datetime
import json
import os

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.utils.html import escape
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_http_methods

from main.models import Experience, Certification
from main.forms import CertificationForm


def show_main(request):
    # baca cookie last_login, kalau gak ada pakai tulisan default
    last_login = request.COOKIES.get(
        "last_login", "Belum ada sesi login / Cookie tidak ditemukan"
    )

    context = {
        "name": "Debora Putri Dion Simamora",
        "npm": "2506544126",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Debora Putri Dion Simamora",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


# cek apakah user masuk group Editor (dari Tugas 4)
def is_user_editor(request):
    if not request.user.is_authenticated:
        return False
    return request.user.groups.filter(name="Editor").exists()


@login_required(login_url="/login/")
def create_certification(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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


# Tutorial 5: versi AJAX dari create_certification, balesnya JSON bukan halaman
# sengaja gak pakai @login_required, soalnya itu nge-redirect ke halaman login
# dan fetch jadi dapet HTML, bukan JSON
@require_POST
def create_certification_ajax(request):
    # user belum login juga is_superuser-nya False, jadi ketolak di sini
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan sertifikat."},
            status=403,
        )

    form = CertificationForm(request.POST)
    if form.is_valid():
        # password tambahan dari Tugas 3 tetap dicek
        if form.cleaned_data["password"] != os.getenv("FORM_PASSWORD"):
            return JsonResponse(
                {"message": "Password salah! Sertifikat tidak ditambahkan."},
                status=400,
            )
        certification = form.save()
        return JsonResponse(
            {"message": "Sertifikat berhasil ditambahkan.", "pk": certification.id},
            status=201,
        )

    # kalau form gak valid, kirim pesan error tiap field
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


@login_required(login_url="/login/")
def update_certification(request, id):
    if not (request.user.is_superuser or is_user_editor(request)):
        raise PermissionDenied

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


# versi lama (pakai reload), tetap disimpen buat cadangan & test Tugas 4
@login_required(login_url="/login/")
def delete_certification(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    certification = get_object_or_404(Certification, pk=id)

    if request.method == "POST":
        password_input = request.POST.get("password", "")
        if password_input != os.getenv("FORM_PASSWORD"):
            messages.error(request, "Password salah! Sertifikat tidak dihapus.")
        else:
            certification.delete()
            messages.success(request, "Sertifikat berhasil dihapus!")

    return redirect("main:show_certification")


# Tugas 5: hapus lewat AJAX, balesnya JSON jadi halaman gak perlu reload
@require_POST
def delete_certification_ajax(request, id):
    # cuma pemilik yang boleh hapus, dicek di sini juga (bukan cuma sembunyiin tombol)
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menghapus sertifikat."},
            status=403,
        )

    certification = get_object_or_404(Certification, pk=id)

    # password tambahan dari Tugas 3 tetap dicek
    if request.POST.get("password", "") != os.getenv("FORM_PASSWORD"):
        return JsonResponse(
            {"message": "Password salah! Sertifikat tidak dihapus."},
            status=400,
        )

    certification.delete()
    return JsonResponse({"message": "Sertifikat berhasil dihapus."}, status=200)


# versi lama (pakai reload), tetap disimpen buat cadangan & test Tugas 4
@login_required(login_url="/login/")
def toggle_star(request, id):
    certification = get_object_or_404(Certification, pk=id)

    if request.method == "POST":
        # udah pernah star -> unstar, belum pernah -> star
        if request.user in certification.starred_by.all():
            certification.starred_by.remove(request.user)
        else:
            certification.starred_by.add(request.user)

    return redirect("main:show_certification")


# Tugas 5: star/unstar lewat AJAX, balesnya JSON jadi halaman gak perlu reload
@require_POST
def toggle_star_ajax(request, id):
    # yang belum login dikasih 401 (bukan redirect), biar JavaScript bisa baca
    if not request.user.is_authenticated:
        return JsonResponse(
            {"message": "Silakan login dulu untuk memberi star."},
            status=401,
        )

    certification = get_object_or_404(Certification, pk=id)

    if certification.starred_by.filter(pk=request.user.pk).exists():
        certification.starred_by.remove(request.user)
        is_starred = False
    else:
        certification.starred_by.add(request.user)
        is_starred = True

    starred_users = certification.starred_by.all()
    return JsonResponse({
        "is_starred": is_starred,
        "star_count": starred_users.count(),
        "starred_by_names": ", ".join([u.username for u in starred_users]),
    })


# Tutorial 5: JSON dirakit manual biar bisa nyelipin info star
# punya user yang lagi login. Bisa juga ?title= (search) dan ?sort= (urutan)
def get_certifications_json(request):
    title_query = request.GET.get("title", "").strip()
    sort_option = request.GET.get("sort", "terbaru")
    if sort_option not in ("terbaru", "stars"):
        sort_option = "terbaru"

    certifications = Certification.objects.prefetch_related("starred_by").annotate(
        star_total=Count("starred_by")
    )

    if title_query:
        certifications = certifications.filter(title__icontains=title_query)

    if sort_option == "stars":
        certifications = certifications.order_by("-star_total", "-issue_date")
    else:
        certifications = certifications.order_by("-issue_date")

    data = []
    for cert in certifications:
        starred_users = cert.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": cert.id,
            "fields": {
                "title": cert.title,
                "issuer": cert.issuer,
                "issue_date": cert.issue_date.strftime("%B %Y"),
                "credential_id": cert.credential_id or "",
                "description": cert.description or "",
                "image": cert.image or "",
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)


# Tutorial 6: halaman sertifikat sekarang pakai HTMX
# daftar kartu langsung dirender di server (bukan dirakit JavaScript lagi)
def show_certification(request):
    title_query, sort_option = get_filter_params(request)

    context = {
        "name": "Debora Putri Dion Simamora",
        "title_query": title_query,
        "sort_option": sort_option,
        "is_editor": is_user_editor(request),
        "certifications": filter_certifications(title_query, sort_option),
        "form": CertificationForm(),  # form kosong buat ditampilin di modal
    }
    return render(request, "certification.html", context)


# =====================================================================
# Tutorial 6: view-view HTMX
# bedanya sama versi AJAX: balesannya potongan HTML, bukan JSON
# view AJAX & JSON yang lama sengaja gak dihapus (buat test & cadangan)
# =====================================================================

# ambil ?title= dan ?sort= dari url, sort yang aneh-aneh dibalikin ke terbaru
def get_filter_params(request):
    title_query = request.GET.get("title", "").strip()
    sort_option = request.GET.get("sort", "terbaru")
    if sort_option not in ("terbaru", "stars"):
        sort_option = "terbaru"
    return title_query, sort_option


# query sertifikat sesuai kata kunci & urutan (dipakai halaman utama & HTMX)
def filter_certifications(title_query, sort_option):
    certifications = Certification.objects.prefetch_related("starred_by").annotate(
        star_total=Count("starred_by")
    )

    if title_query:
        certifications = certifications.filter(title__icontains=title_query)

    if sort_option == "stars":
        return certifications.order_by("-star_total", "-issue_date")
    return certifications.order_by("-issue_date")


# pasang header HX-Trigger biar browser nyalain event (misal munculin toast)
# events contohnya: {"showToast": {...}, "certListChanged": True}
def add_htmx_events(response, events):
    response["HX-Trigger"] = json.dumps(events)
    return response


def make_toast(title, message, toast_type="success"):
    return {"title": title, "message": message, "type": toast_type}


# live search + sort: balikin potongan daftar kartu doang
def certification_list_htmx(request):
    title_query, sort_option = get_filter_params(request)

    context = {
        "title_query": title_query,
        "is_editor": is_user_editor(request),
        "certifications": filter_certifications(title_query, sort_option),
    }
    return render(request, "certifications/_cert_list.html", context)


# star / unstar: balikin tombol star yang udah keupdate
@require_POST
def toggle_star_htmx(request, id):
    # belum login -> suruh htmx pindah ke halaman login
    if not request.user.is_authenticated:
        response = HttpResponse("")
        response["HX-Redirect"] = reverse("main:login")
        return response

    cert = get_object_or_404(Certification, pk=id)

    if cert.starred_by.filter(pk=request.user.pk).exists():
        cert.starred_by.remove(request.user)
        toast = make_toast("Star dibatalkan", "Star kamu udah dihapus.", "normal")
    else:
        cert.starred_by.add(request.user)
        toast = make_toast("Star ditambahkan", "Makasih udah ngasih star!")

    response = render(request, "certifications/_star_button.html", {"cert": cert})
    return add_htmx_events(response, {"showToast": toast})


# tambah sertifikat dari modal
# sukses -> balikin kosong + suruh daftar kartu reload
# gagal  -> balikin pesan error (status 200 biar htmx mau nempelin ke modal)
@require_POST
def create_certification_htmx(request):
    if not request.user.is_superuser:
        return HttpResponse("Hanya pemilik portofolio yang dapat menambahkan sertifikat.", status=403)

    form = CertificationForm(request.POST)

    if not form.is_valid():
        # gabungin semua pesan error jadi satu kalimat
        error_list = [error for errors in form.errors.values() for error in errors]
        return HttpResponse(escape(" ".join(error_list)))

    if form.cleaned_data["password"] != os.getenv("FORM_PASSWORD"):
        return HttpResponse("Password salah! Sertifikat tidak ditambahkan.")

    form.save()
    response = HttpResponse("")
    return add_htmx_events(response, {
        "showToast": make_toast("Berhasil", "Sertifikat baru berhasil ditambahkan!"),
        "certListChanged": True,
        "closeModals": True,
    })


# hapus sertifikat
# GET  -> balikin isi modal (form password) buat sertifikat ini
# POST -> cek password, terus hapus
@require_http_methods(["GET", "POST"])
def delete_certification_htmx(request, id):
    if not request.user.is_superuser:
        return HttpResponse("Hanya pemilik portofolio yang dapat menghapus sertifikat.", status=403)

    cert = get_object_or_404(Certification, pk=id)

    if request.method == "GET":
        return render(request, "certifications/_delete_form.html", {"cert": cert})

    if request.POST.get("password", "") != os.getenv("FORM_PASSWORD"):
        return HttpResponse("Password salah! Sertifikat tidak dihapus.")

    cert.delete()
    response = HttpResponse("")
    return add_htmx_events(response, {
        "showToast": make_toast("Berhasil", "Sertifikat berhasil dihapus!"),
        "certListChanged": True,
        "closeModals": True,
    })


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Debora Putri Dion Simamora",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        response = redirect("main:show_main")
        response.set_cookie(
            "last_login", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        return response

    context = {
        "name": "Debora Putri Dion Simamora",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)

    response = redirect("main:show_main")
    response.delete_cookie("last_login")
    return response