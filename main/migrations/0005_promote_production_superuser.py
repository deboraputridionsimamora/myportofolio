from django.db import migrations


def promote_to_superuser(apps, schema_editor):
    # Cariin akun yang tadi kita daftar lewat halaman Register di production,
    # terus jadiin dia superuser (is_staff & is_superuser = True)
    User = apps.get_model("auth", "User")
    User.objects.filter(username="admin").update(
        is_staff=True, is_superuser=True
    )


def undo_promote(apps, schema_editor):
    # Kalau migration ini di-rollback, balikin lagi jadi user biasa
    User = apps.get_model("auth", "User")
    User.objects.filter(username="test").update(
        is_staff=False, is_superuser=False
    )


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_certification_starred_by"),
    ]

    operations = [
        migrations.RunPython(promote_to_superuser, undo_promote),
    ]