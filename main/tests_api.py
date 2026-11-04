import os

from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Certification


class CertificationAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner_api", password="test-password", email="owner_api@example.com",
        )
        self.editor = User.objects.create_user(username="editor_api", password="test-password")
        self.editor.groups.add(Group.objects.create(name="Editor"))
        self.visitor = User.objects.create_user(username="visitor_api", password="test-password")

        self.certification = Certification.objects.create(
            title="Sertifikat Awal",
            issuer="Penerbit Awal",
            issue_date="2026-01-01",
        )

        self.list_url = reverse("api:certification-list")
        self.detail_url = reverse("api:certification-detail", args=[self.certification.id])
        self.star_url = reverse("api:certification-star", args=[self.certification.id])

        self.correct_password = os.getenv("FORM_PASSWORD")
        self.payload = {
            "title": "Sertifikat Baru",
            "issuer": "Penerbit Baru",
            "issue_date": "2026-02-01",
            "credential_id": "",
            "description": "",
            "image": "",
            "password": self.correct_password,
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], self.certification.id)
        self.assertFalse(response.data[0]["is_starred"])
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)

    def test_search_and_empty_results(self):
        response = self.client.get(self.list_url, {"title": "AWAL"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"title": "tidak-ada"})
        self.assertEqual(response.data, [])

    def test_missing_certification(self):
        url = reverse("api:certification-detail", args=[self.certification.id + 9999])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(
                self.client.post(self.list_url, self.payload, format="json").status_code, 403,
            )
            self.assertEqual(
                self.client.patch(
                    self.detail_url, {"title": "Berubah", "password": self.correct_password}, format="json",
                ).status_code, 403,
            )
            self.assertEqual(
                self.client.delete(
                    self.detail_url, {"password": self.correct_password}, format="json",
                ).status_code, 403,
            )
        self.assertEqual(Certification.objects.count(), 1)
        self.certification.refresh_from_db()
        self.assertEqual(self.certification.title, "Sertifikat Awal")

    def test_owner_can_create_with_correct_password(self):
        if not self.correct_password:
            self.skipTest("FORM_PASSWORD belum diset di .env")
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Certification.objects.filter(pk=response.data["id"]).exists())

    def test_owner_cannot_create_with_wrong_password(self):
        self.client.force_authenticate(user=self.owner)
        data = {**self.payload, "password": "salah-total"}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Certification.objects.filter(title="Sertifikat Baru").exists())

    def test_validation(self):
        if not self.correct_password:
            self.skipTest("FORM_PASSWORD belum diset di .env")
        self.client.force_authenticate(user=self.owner)
        data = {**self.payload, "title": "   "}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)
        self.assertEqual(Certification.objects.count(), 1)

    def test_editor_can_patch_but_not_create_or_delete(self):
        if not self.correct_password:
            self.skipTest("FORM_PASSWORD belum diset di .env")
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url, {"title": "Diubah Editor", "password": self.correct_password}, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.certification.refresh_from_db()
        self.assertEqual(self.certification.title, "Diubah Editor")

        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(self.detail_url, {"password": self.correct_password}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_owner_patch_and_delete(self):
        if not self.correct_password:
            self.skipTest("FORM_PASSWORD belum diset di .env")
        self.client.force_authenticate(user=self.owner)

        response = self.client.patch(
            self.detail_url, {"title": "Sudah Diubah", "password": self.correct_password}, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.certification.refresh_from_db()
        self.assertEqual(self.certification.issuer, "Penerbit Awal")

        response = self.client.delete(self.detail_url, {"password": self.correct_password}, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Certification.objects.filter(pk=self.certification.id).exists())

    def test_star_requires_login_and_toggles(self):
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_computed_fields_are_read_only(self):
        if not self.correct_password:
            self.skipTest("FORM_PASSWORD belum diset di .env")
        self.client.force_authenticate(user=self.owner)
        data = {**self.payload, "star_count": 99, "is_starred": True, "starred_by_names": "forged"}
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner_api", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Certification.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        if not self.correct_password:
            self.skipTest("FORM_PASSWORD belum diset di .env")
        client = APIClient(enforce_csrf_checks=True)
        client.login(username="owner_api", password="test-password")
        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)