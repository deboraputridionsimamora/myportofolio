from django.db import models


# model kontak, sekarang ada nomor hp juga
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # pake CharField bukan IntegerField soalnya nomor hp bisa diawali 0 atau +62
    # default "" biar data lama (debora, budi) ga error pas migrasi
    phone = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return self.name