from django import forms
from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput

from main.models import Certification

class CertificationForm(ModelForm):
    # Field password ini sengaja gak nyambung ke model Certification.
    # Cuma dipakai buat ngecek di views.py, gak ikut kesimpen ke database.
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Masukkan password"}),
        label="Password",
        required=True,
    )

    class Meta:
        model = Certification
        fields = [
            "title",
            "issuer",
            "issue_date",
            "credential_id",
            "description",
            "image",
        ]

        labels = {
            "title": "Nama Sertifikat",
            "issuer": "Penerbit",
            "issue_date": "Tanggal Terbit",
            "credential_id": "ID Kredensial",
            "description": "Deskripsi",
            "image": "Nama File Gambar",
        }

        widgets = {
            "title": TextInput(attrs={"placeholder": "TOEFL ITP", "maxlength": 255}),
            "issuer": TextInput(attrs={"placeholder": "Educational Testing Service (ETS)"}),
            "issue_date": DateInput(attrs={"type": "date"}),
            "credential_id": TextInput(attrs={"placeholder": "SD-BB-0985769"}),
            "description": Textarea(attrs={"placeholder": "Deskripsi singkat sertifikat (opsional)", "rows": 3}),
            "image": TextInput(attrs={"placeholder": "toefl.jpg"}),
        }