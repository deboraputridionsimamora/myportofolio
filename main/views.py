from django.shortcuts import render

from main.models import Experience, Certification


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


def show_certification(request):
    context = {
        "name": "Debora Putri Dion Simamora",
        "certification_list": Certification.objects.all().order_by("-issue_date"),
    }
    return render(request, "certification.html", context)