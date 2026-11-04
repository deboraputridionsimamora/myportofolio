from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Certification


class CertificationSerializer(serializers.ModelSerializer):
    # 3 field ini dihitung, gak disimpen langsung di tabel Certification
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Certification
        fields = [
            "id",
            "title",
            "issuer",
            "issue_date",
            "credential_id",
            "description",
            "image",
            "star_count",
            "is_starred",
            "starred_by_names",
        ]
        read_only_fields = ["id"]

    # proteksi XSS, sama kayak clean_title/clean_issuer/dkk di forms.py
    # tapi ini jalan buat request API, forms.py tetap jalan buat form HTML biasa
    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Nama sertifikat tidak boleh hanya berisi tag HTML.")
        return value

    def validate_issuer(self, value):
        return strip_tags(value).strip()

    def validate_credential_id(self, value):
        return strip_tags(value).strip() if value else value

    def validate_description(self, value):
        return strip_tags(value).strip() if value else value

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())