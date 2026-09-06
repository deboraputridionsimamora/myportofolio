# Personal Portfolio Website

Website portofolio pribadi milik **Debora Putri Dion Simamora**, dibuat menggunakan Django sebagai bagian dari tugas mata kuliah Pemrograman Berbasis Platform (CSGE602022), Fakultas Ilmu Komputer, Universitas Indonesia.

**Nama:** Debora Putri Dion Simamora
**NPM:** 2506544126
**Kelas:** PBP A

## Deskripsi Proyek

Website ini adalah portofolio pribadi statis (HTML5 + CSS3, dengan sedikit JavaScript untuk interaktivitas) yang menampilkan profil, cerita singkat tentang diri saya, dan pengalaman organisasi serta kepanitiaan yang pernah saya ikuti. Desain visualnya terinspirasi dari gaya editorial hangat dengan latar gradasi warna lembut, wave divider antar section, dan tipografi serif dipadukan dengan aksen tulisan tangan. Skema warna (terracotta, navy, dan cream) diambil dari warna-warna yang muncul di foto profil saya sendiri.

## Fitur

- **Profile (Hero)** — nama, program studi, NPM, foto, dan link kontak (GitHub, LinkedIn, Email) dalam bentuk tombol pil, dengan latar gradasi warna lembut (blob) dan wave divider di bagian bawah
- **About Me** — cerita singkat tentang diri saya dengan layout rata tengah, garis pembatas dekoratif, dan highlight teks pada frasa penting
- **Experience** — pengalaman organisasi dan kepanitiaan, ditampilkan dalam 2 kategori (Organizations & Volunteering) dengan animasi marquee berjalan otomatis berlawanan arah, foto asli dokumentasi kegiatan sebagai latar tiap kartu, serta modal detail (foto + deskripsi lengkap) saat kartu diklik
- **Sticky navbar** dengan smooth scroll ke tiap section, menyesuaikan tampilan di layar mobile
- **Scroll fade-in animation** pada tiap section
- **Back-to-top button** yang muncul saat halaman discroll ke bawah
- Tampilan responsif untuk desktop maupun mobile

## Cara Menjalankan

1. Clone repository ini
2. Buat virtual environment dan aktifkan
3. Install dependencies: `pip install -r requirements.txt`
4. Jalankan server: `python manage.py runserver`
5. Buka `http://localhost:8000/` di browser

## Progres Mingguan

### Tutorial 0 & Tutorial 1
Setup project Django awal, membuat halaman "About Me" (hero section) dengan HTML5 semantik dan styling CSS3 dasar (Flexbox, Grid, custom properties), lalu deploy ke PWS.

### Individual Assignment 1
Melanjutkan halaman dari Tutorial 1 dengan menambahkan section About Me dan Experience secara lengkap, beserta styling CSS khusus untuk masing-masing (layout Flexbox untuk marquee, custom animation, hover effect, modal). Saya mengeksplorasi beberapa arah desain visual (palet warna, tipografi, elemen dekoratif) sebelum menetapkan gaya akhir yang mengambil warna dari foto profil saya sendiri. Di luar instruksi minimum, saya menambahkan beberapa fitur ekstra: sticky navbar dengan smooth scroll, modal detail berisi foto dan deskripsi untuk tiap pengalaman, scroll fade-in animation, back-to-top button, serta elemen dekoratif seperti gradient blob dan wave divider antar section.

## Pertanyaan Reflektif

### Tugas 1

1. Saya menggunakan beberapa elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, dan `<footer>`, serta `<dl>`/`<dt>`/`<dd>` untuk pasangan label-nilai seperti NPM dan Program. Elemen-elemen ini membantu saya membagi halaman menjadi bagian-bagian yang punya makna yang jelas (bukan cuma tumpukan `<div>`), sehingga struktur halaman lebih mudah dipahami baik saat menulis CSS maupun oleh teknologi bantu seperti screen reader. Saya belum menggunakan `<article>` atau `<aside>`, karena konten yang saya tampilkan bukan konten yang berdiri sendiri secara independen, dan saya belum punya konten pelengkap yang cocok masuk ke `<aside>`.

2. Tantangan terbesar dalam membuat layout tetap responsive ada di bagian hero (CSS Grid dengan `grid-template-areas`), navbar, dan bagian Experience (marquee berjalan horizontal). Untuk hero, saya perlu memikirkan urutan mana yang paling penting dilihat duluan di layar sempit, sehingga foto dipindah ke antara nama dan bio, bukan tetap di samping seperti di desktop. Untuk navbar, saya mengubah arah tata letaknya dari sejajar horizontal menjadi bertumpuk vertikal khusus di layar kecil, agar nama dan menu tidak berebutan ruang. Untuk mengevaluasi elemen mana yang perlu diubah ukurannya, saya memprioritaskan keterbacaan teks di atas elemen dekoratif.

3. Batasan utama dari static web murni adalah semua konten harus ditulis langsung di kode HTML — untuk menambah atau mengubah satu pengalaman saja, saya harus mengedit file HTML secara manual, bukan lewat suatu formulir atau panel admin. Ini juga berarti tidak ada tempat untuk menyimpan data secara terstruktur, sehingga sulit berkembang kalau daftar pengalaman bertambah banyak. Untuk iterasi selanjutnya, fungsionalitas dinamis yang paling ingin saya tambahkan adalah menyimpan data pengalaman di database (menggunakan model Django), sehingga saya bisa menambah/mengubah konten tanpa mengedit kode HTML secara langsung.

## AI Disclosure

Saya menggunakan **Claude (Anthropic)** sebagai alat bantu sepanjang proses pengembangan Individual Assignment 1 ini.

Proses saya dimulai dengan meminta Claude me-review kode Tutorial 1 saya dan memberi rekomendasi section serta fitur yang cocok untuk portofolio, sebelum implementasi apa pun dimulai. Saya kemudian mengembangkan section satu per satu, membawa data dan konten saya sendiri (riwayat organisasi dari LinkedIn, foto dokumentasi kegiatan), dan meminta Claude membantu menyusun struktur HTML/CSS-nya. Untuk desain visual, saya membawa beberapa referensi gaya yang saya sukai dan mengeksplorasi beberapa arah (termasuk beberapa skema warna) sebelum menetapkan versi akhir yang terinspirasi dari warna di foto profil saya sendiri.

**Bagian yang dibantu AI:** struktur HTML/CSS untuk seluruh section (About Me, Experience, navbar, modal, animasi, elemen dekoratif), penerapan skema warna dan tipografi berdasarkan referensi visual yang saya berikan, penulisan ulang teks bio ke Bahasa Inggris dengan nada profesional, serta debugging saat ada CSS yang tidak terbaca dengan benar atau foto yang terpotong tidak sesuai.

**Bagian yang saya kerjakan/putuskan sendiri:** seluruh data dan foto pengalaman organisasi, pengelompokan pengalaman menjadi kategori Organizations dan Volunteering, penulisan deskripsi detail untuk tiap pengalaman, pemilihan arah desain akhir dari beberapa opsi yang dieksplorasi, serta verifikasi setiap tampilan secara manual di browser dan perangkat mobile karena AI tidak dapat melihat hasil visual project secara langsung.

**Keterbatasan AI yang saya sadari:** karena Claude tidak bisa menjalankan atau melihat tampilan project Django saya secara langsung, setiap kali ada bug tampilan saya perlu menjelaskan apa yang terlihat, sehingga proses debugging kadang membutuhkan beberapa iterasi sebelum akar masalahnya ditemukan dengan tepat.