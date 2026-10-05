from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, QueryDict
from django.views.decorators.http import require_http_methods
from .models import Contact


# halaman utama, nampilin semua kontak
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/index.html", {"contacts": contacts})


# tambah kontak
# latihan 2: cuma balikin baris baru
# latihan 3: sekalian bawa pesan sukses pake oob swap
@require_http_methods(["POST"])
def contact_add(request):
    contact = Contact.objects.create(
        name=request.POST.get("name"),
        email=request.POST.get("email"),
        phone=request.POST.get("phone", ""),
    )
    return render(request, "contacts/_contact_added.html", {"contact": contact})


# hapus kontak, balikin string kosong biar barisnya ilang
# jangan pake status 204 ya, nanti htmx ga swap
@require_http_methods(["DELETE"])
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return HttpResponse("")


# cari kontak berdasarkan nama (ga peduli huruf besar kecil)
def contact_search(request):
    query = request.GET.get("q", "")
    if query:
        contacts = Contact.objects.filter(name__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, "contacts/_contact_rows.html", {"contacts": contacts})


# balikin baris versi form edit
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/_contact_edit_row.html", {"contact": contact})


# balikin baris versi normal (dipake pas klik batal)
def contact_row(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, "contacts/_contact_row.html", {"contact": contact})


# update kontak pake PUT
# request.POST ga keisi kalo PUT, jadi datanya diambil dari request.body
@require_http_methods(["PUT"])
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    data = QueryDict(request.body)
    contact.name = data.get("name", contact.name)
    contact.email = data.get("email", contact.email)
    contact.phone = data.get("phone", contact.phone)
    contact.save()
    return render(request, "contacts/_contact_row.html", {"contact": contact})