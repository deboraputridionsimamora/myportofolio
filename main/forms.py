from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput
from django.utils.html import strip_tags

from main.models import Certification


class CertificationForm(ModelForm):
    # field password ini gak nyambung ke model, cuma buat dicek di views.py
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

    # Tutorial 5: buang tag HTML dari input teks (proteksi XSS di server)
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        # kalau isinya cuma tag HTML doang, abis dibuang jadi kosong -> tolak
        if not title:
            raise ValidationError("Nama sertifikat tidak boleh hanya berisi tag HTML.")
        return title

    def clean_issuer(self):
        return strip_tags(self.cleaned_data["issuer"]).strip()

    def clean_credential_id(self):
        value = self.cleaned_data.get("credential_id") or ""
        return strip_tags(value).strip()

    def clean_description(self):
        value = self.cleaned_data.get("description") or ""
        return strip_tags(value).strip()