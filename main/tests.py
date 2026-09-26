import json
import os

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Certification


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")


class CertificationTest(TestCase):
    def setUp(self):
        self.certification = Certification.objects.create(
            title="TOEFL ITP (Institutional Testing Program)",
            issuer="Educational Testing Service (ETS) Global B.V.",
            issue_date="2025-12-01",
        )

    def test_certification_model(self):
        self.assertEqual(str(self.certification), "TOEFL ITP (Institutional Testing Program)")
        self.assertEqual(self.certification.issuer, "Educational Testing Service (ETS) Global B.V.")

    def test_certification_url_is_accessible(self):
        response = self.client.get(reverse("main:show_certification"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certification.html")

    def test_certification_appears_when_data_exists(self):
        response = self.client.get(reverse("main:show_certification"))

        self.assertContains(response, self.certification.title)
        self.assertContains(response, self.certification.issuer)

    def test_empty_certification_page(self):
        Certification.objects.all().delete()
        response = self.client.get(reverse("main:show_certification"))

        self.assertContains(response, "Belum ada sertifikat yang ditambahkan.")


# Tutorial 4 / Individual Assignment 4: tes buat mastiin 4 peran (pengunjung,
# pengguna biasa, editor, pemilik) beneran dibatasi sesuai aturannya.
# Akun-akun di sini cuma buat testing, gak nyangkut ke database asli.
class AuthorizationTest(TestCase):
    def setUp(self):
        self.certification = Certification.objects.create(
            title="Sertifikat Uji Coba",
            issuer="Penerbit Uji Coba",
            issue_date="2026-01-01",
        )

        # akun biasa: bukan editor, bukan superuser
        self.regular_user = User.objects.create_user(
            username="pengguna_biasa", password="testpass123"
        )

        # akun editor: dimasukin ke Group "Editor"
        self.editor_user = User.objects.create_user(
            username="editor_uji", password="testpass123"
        )
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        self.editor_user.groups.add(editor_group)

        # akun pemilik: superuser
        self.owner_user = User.objects.create_superuser(
            username="pemilik_uji", password="testpass123", email="owner@example.com"
        )

        self.add_url = reverse("main:create_certification")
        self.update_url = reverse(
            "main:update_certification", args=[self.certification.id]
        )
        self.delete_url = reverse(
            "main:delete_certification", args=[self.certification.id]
        )
        self.star_url = reverse("main:toggle_star", args=[self.certification.id])

    # ---- Pengunjung yang belum login ----
    def test_visitor_redirected_to_login_on_add(self):
        response = self.client.get(self.add_url)

        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_visitor_redirected_to_login_on_star(self):
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    # ---- Pengguna biasa: cuma boleh star, gak boleh ubah data ----
    def test_regular_user_cannot_add(self):
        self.client.login(username="pengguna_biasa", password="testpass123")
        response = self.client.get(self.add_url)

        self.assertEqual(response.status_code, 403)

    def test_regular_user_cannot_update(self):
        self.client.login(username="pengguna_biasa", password="testpass123")
        response = self.client.get(self.update_url)

        self.assertEqual(response.status_code, 403)

    def test_regular_user_cannot_delete(self):
        self.client.login(username="pengguna_biasa", password="testpass123")
        response = self.client.post(self.delete_url)

        self.assertEqual(response.status_code, 403)

    def test_regular_user_can_star(self):
        self.client.login(username="pengguna_biasa", password="testpass123")
        response = self.client.post(self.star_url)

        self.assertEqual(response.status_code, 302)
        self.assertIn(self.regular_user, self.certification.starred_by.all())

    # ---- Editor: boleh buka form edit, gak boleh tambah/hapus ----
    def test_editor_cannot_add(self):
        self.client.login(username="editor_uji", password="testpass123")
        response = self.client.get(self.add_url)

        self.assertEqual(response.status_code, 403)

    def test_editor_can_open_update_form(self):
        self.client.login(username="editor_uji", password="testpass123")
        response = self.client.get(self.update_url)

        self.assertEqual(response.status_code, 200)

    def test_editor_cannot_delete(self):
        self.client.login(username="editor_uji", password="testpass123")
        response = self.client.post(self.delete_url)

        self.assertEqual(response.status_code, 403)

    # ---- Pemilik (superuser): boleh buka semua form ----
    def test_owner_can_open_add_form(self):
        self.client.login(username="pemilik_uji", password="testpass123")
        response = self.client.get(self.add_url)

        self.assertEqual(response.status_code, 200)

    def test_owner_can_open_update_form(self):
        self.client.login(username="pemilik_uji", password="testpass123")
        response = self.client.get(self.update_url)

        self.assertEqual(response.status_code, 200)


# Individual Assignment 3: tes CRUD (create, update, delete) dan JSON API
# buat Certification. Password FORM_PASSWORD diambil dari .env, bukan
# ditulis manual di sini, biar aman kalau file ini ikut di-push ke GitHub.
class CertificationCRUDTest(TestCase):
    def setUp(self):
        self.certification = Certification.objects.create(
            title="Sertifikat Awal",
            issuer="Penerbit Awal",
            issue_date="2026-01-01",
        )

        self.owner_user = User.objects.create_superuser(
            username="pemilik_crud", password="testpass123", email="owner2@example.com"
        )
        self.client.login(username="pemilik_crud", password="testpass123")

        self.correct_password = os.getenv("FORM_PASSWORD")
        self.add_url = reverse("main:create_certification")
        self.update_url = reverse(
            "main:update_certification", args=[self.certification.id]
        )
        self.delete_url = reverse(
            "main:delete_certification", args=[self.certification.id]
        )

    def test_create_certification_with_correct_password(self):
        # kalau FORM_PASSWORD belum diset di .env, test ini dilewatin
        # (skip), bukan dianggap gagal
        if not self.correct_password:
            self.skipTest("FORM_PASSWORD belum diset di .env")

        data = {
            "title": "Sertifikat Baru",
            "issuer": "Penerbit Baru",
            "issue_date": "2026-02-01",
            "credential_id": "",
            "description": "",
            "image": "",
            "password": self.correct_password,
        }
        response = self.client.post(self.add_url, data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Certification.objects.filter(title="Sertifikat Baru").exists()
        )

    def test_create_certification_with_wrong_password_not_saved(self):
        data = {
            "title": "Sertifikat Gagal",
            "issuer": "Penerbit Gagal",
            "issue_date": "2026-02-01",
            "credential_id": "",
            "description": "",
            "image": "",
            "password": "password-yang-pasti-salah",
        }
        response = self.client.post(self.add_url, data)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            Certification.objects.filter(title="Sertifikat Gagal").exists()
        )

    def test_update_certification_with_correct_password(self):
        if not self.correct_password:
            self.skipTest("FORM_PASSWORD belum diset di .env")

        data = {
            "title": "Sertifikat Sudah Diubah",
            "issuer": self.certification.issuer,
            "issue_date": "2026-01-01",
            "credential_id": "",
            "description": "",
            "image": "",
            "password": self.correct_password,
        }
        response = self.client.post(self.update_url, data)

        self.certification.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.certification.title, "Sertifikat Sudah Diubah")

    def test_delete_certification_with_correct_password(self):
        if not self.correct_password:
            self.skipTest("FORM_PASSWORD belum diset di .env")

        response = self.client.post(self.delete_url, {"password": self.correct_password})

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Certification.objects.filter(pk=self.certification.id).exists()
        )

    def test_delete_certification_with_wrong_password_not_deleted(self):
        response = self.client.post(self.delete_url, {"password": "salah-total"})

        self.assertTrue(
            Certification.objects.filter(pk=self.certification.id).exists()
        )

    def test_certifications_json_endpoint(self):
        response = self.client.get(reverse("main:get_certifications_json"))
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data) >= 1)
        self.assertEqual(data[0]["model"], "main.certification")