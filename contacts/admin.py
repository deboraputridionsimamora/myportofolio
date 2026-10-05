from django.contrib import admin
from .models import Contact

# biar bisa nambah data kontak lewat /admin
admin.site.register(Contact)