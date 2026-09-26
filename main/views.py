import datetime
import os

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Certification
from main.forms import CertificationForm


def show_main(request):
    # baca cookie last_login dari browser, kalau gak ada pakai tulisan default
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


# Lapis 1: harus login. Belum login -> dialihkan ke halaman login.
@login_required(login_url="/login/")
def create_certification(request):
    # Lapis 2: harus pemilik (superuser). Login biasa doang -> 403 Forbidden.
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


@login_required(login_url="/login/")
def update_certification(request, id):
    if not request.user.is_superuser:
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

    return redirect("main:show_certification")


# Tutorial 4: fitur star. Cukup login (gak perlu superuser), semua pengguna
# terdaftar boleh star/unstar sertifikat.
@login_required(login_url="/login/")
def toggle_star(request, id):
    certification = get_object_or_404(Certification, pk=id)

    if request.method == "POST":
        # kalau user ini udah pernah star, klik lagi = batalin star
        # kalau belum pernah, klik = kasih star
        if request.user in certification.starred_by.all():
            certification.starred_by.remove(request.user)
        else:
            certification.starred_by.add(request.user)

    return redirect("main:show_certification")


def get_certifications_json(request):
    certifications = Certification.objects.all().order_by("-issue_date")
    certifications_json = serializers.serialize(
        "json", certifications, use_natural_foreign_keys=True
    )
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


# ===== Tutorial 4: autentikasi (register, login, logout) =====

def register(request):
    # kalau baru buka halaman (GET) formnya kosong, kalau habis submit (POST) formnya berisi data
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()  # bikin akun baru, password otomatis di-hash
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
        user = form.get_user()  # akun yang username & password-nya cocok
        login(request, user)

        # redirect-nya disimpan dulu ke variabel response, biar bisa ditempelin cookie
        response = redirect("main:show_main")
        # cookie last_login isinya waktu sekarang, format tahun-bulan-tanggal jam:menit:detik
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
    logout(request)  # hapus catatan login di session

    response = redirect("main:show_main")
    response.delete_cookie("last_login")  # suruh browser buang cookie last_login
    return response