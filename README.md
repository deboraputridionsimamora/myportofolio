# Individual Assignment 1: Personal Portfolio Website

Website portofolio pribadi milik **Debora Putri Dion Simamora**, dibuat menggunakan Django sebagai bagian dari tugas mata kuliah Pemrograman Berbasis Platform (CSGE602022), Fakultas Ilmu Komputer, Universitas Indonesia.

**Nama:** Debora Putri Dion Simamora
**NPM:** 2506544126
**Kelas:** PBP A

## Deskripsi Proyek

Website ini merupakan portofolio pribadi yang dibangun menggunakan **Django**, dan dikembangkan secara bertahap mengikuti tutorial serta tugas mingguan. Awalnya website ini berupa halaman statis dengan HTML5 dan CSS3, kemudian berkembang menggunakan database untuk menyimpan data, form untuk mengelola data, sistem login dengan pembagian peran, hingga JavaScript dan AJAX agar halaman lebih interaktif. Website menampilkan profil, cerita singkat tentang diri saya, pengalaman organisasi dan volunteering, serta sertifikat yang pernah saya terima.

Desain visual website menggunakan gaya editorial yang hangat, dengan gradasi warna lembut, wave divider antar-section, serta perpaduan tipografi serif dan aksen tulisan tangan. Warna utama yang digunakan, yaitu terracotta, navy, dan cream, terinspirasi dari warna pada foto profil saya.

## Fitur

Website memiliki beberapa fitur utama:

* **Profile (Hero):** menampilkan nama, program studi, NPM, foto, serta link GitHub, LinkedIn, dan Email dalam bentuk tombol pil. Bagian ini juga menggunakan latar gradasi dan wave divider.
* **About Me:** berisi cerita singkat tentang diri saya dengan layout rata tengah, garis pembatas dekoratif, dan highlight pada beberapa frasa penting.
* **Navigation & Animation:** terdapat sticky navbar dengan smooth scroll, responsive navigation, serta animasi fade-in ketika section mulai masuk ke area layar.
* **Responsive Design:** layout website disesuaikan agar tetap rapi dan nyaman digunakan pada desktop maupun mobile.
* **Experience:** menampilkan pengalaman organisasi dan volunteering pada halaman tersendiri (My Journey), terpisah dari halaman profil. Setiap kategori menggunakan animasi marquee dengan arah yang berbeda dan foto dokumentasi sebagai latar kartu.
* **Licenses & Certifications:** menampilkan sertifikat dan penghargaan yang pernah saya terima, masing-masing dengan gambar sertifikat, nama, penerbit, tanggal terbit, nomor kredensial (jika ada), dan deskripsi singkat. Data diambil dari database menggunakan pola Model-View-Template.
* **Authentication & Authorization:** pengguna dapat membuat akun (Register), login, dan logout menggunakan sistem autentikasi bawaan Django. Status login ditampilkan di navbar, beserta waktu login terakhir yang disimpan lewat cookie. Akses terhadap fitur Create, Update, dan Delete pada Certification dibatasi berdasarkan 4 peran: Visitor (hanya baca), Regular User (baca + star), Editor (baca + star + update), dan Owner/Superuser (akses penuh).
* **Star Feature:** pengguna yang sudah login dapat memberi atau membatalkan star pada sebuah sertifikat. Jumlah star dan status star pengguna ditampilkan secara real-time, lengkap dengan tooltip yang menunjukkan siapa saja yang sudah memberi star.
* **Sort Certifications:** pengunjung dapat mengurutkan daftar sertifikat berdasarkan yang terbaru (Newest) atau yang paling banyak di-star (Most Starred).
* **Web Interactivity (AJAX):** halaman Certifications memuat data lewat `fetch()` dari endpoint JSON, dilengkapi kondisi loading, kosong, dan error (dengan tombol "Coba lagi"), pencarian dengan debouncing, jumlah hasil pencarian, form tambah dan konfirmasi hapus di dalam modal yang dikirim lewat AJAX, notifikasi toast, serta perlindungan terhadap serangan XSS.

Seluruh interaktivitas pada implementasi akhir dibuat tanpa JavaScript. Modal menggunakan teknik CSS `:target`, sedangkan animasi scroll menggunakan `animation-timeline: view()`. Saya juga menggunakan `@supports` sebagai fallback untuk browser yang belum mendukung fitur tersebut.

## Cara Menjalankan

1. Clone repository ini.
2. Buat dan aktifkan virtual environment.
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Jalankan server:
```bash
python manage.py runserver
```
5. Buka `http://localhost:8000/` pada browser.
6. Buat file `.env` di root folder project, isi dengan:
```bash
FORM_PASSWORD=isi_password_bebas_di_sini
```
File ini **tidak ikut di-push ke GitHub** (sudah masuk `.gitignore`), jadi setiap yang mau menjalankan project ini secara lokal perlu membuat sendiri file `.env` miliknya dengan password bebas.
7. Untuk mencoba role **Editor**, buat akun baru melalui halaman Register, lalu buka `/admin/`, login sebagai superuser, masuk ke bagian **Groups**, buat/pilih group bernama `Editor`, dan tambahkan akun tersebut ke group itu.

## Progres Mingguan

### Tutorial 0 & Tutorial 1

Pada Tutorial 0 dan Tutorial 1, saya melakukan setup project Django dan mulai membuat halaman portfolio sederhana. Saya membuat bagian awal halaman atau hero section menggunakan HTML5 semantik dan CSS3 dengan beberapa teknik dasar seperti Flexbox, Grid, dan custom properties. Setelah itu, project juga saya deploy ke PWS.

### Individual Assignment 1

Pada Individual Assignment 1, saya melanjutkan project dari Tutorial 1 dengan mengembangkan bagian About Me dan menambahkan section Experience. Pada awal pengerjaan, saya mencoba mengikuti struktur dan pola kode dari Tutorial 1 sambil menentukan sendiri isi dan konsep portfolio yang ingin saya buat.

Selama proses pengerjaan, saya mengeksplorasi beberapa referensi portfolio melalui browser dan Pinterest untuk mendapatkan inspirasi mengenai layout, tipografi, kombinasi warna, dan elemen dekoratif. Setelah membandingkan beberapa gaya, saya menentukan arah desain akhir yang menggunakan warna terracotta, navy, dan cream yang terinspirasi dari foto profil saya.

Pada section Experience, saya mengembangkan tampilan pengalaman organisasi dan volunteering dalam kategori Organizations dan Volunteering. Data pengalaman dan foto dokumentasi yang digunakan berasal dari saya sendiri. Saya juga menambahkan beberapa fitur seperti marquee animation, hover effect, dan modal detail untuk membuat section tersebut lebih interaktif.

Dalam proses pengembangan, saya menggunakan Claude sebagai alat bantu untuk memberikan masukan terhadap struktur dan tampilan website serta membantu mengembangkan beberapa bagian HTML dan CSS. Pada implementasi awal, modal dan animasi scroll yang dibantu oleh Claude masih menggunakan JavaScript. Karena saya belum memahami bagian tersebut dengan baik dan implementasinya tidak sesuai dengan requirement tugas yang menggunakan HTML5 dan CSS3, saya meminta alternatif yang tidak menggunakan JavaScript. Modal kemudian menggunakan teknik `:target`, sedangkan animasi scroll menggunakan `animation-timeline: view()` dengan `@supports` sebagai fallback.

Di luar kebutuhan minimum tugas, saya juga menambahkan beberapa fitur seperti sticky navbar dengan smooth scroll, modal detail untuk setiap pengalaman, scroll-linked fade-in animation, gradient blob, dan wave divider antar-section.

### Tutorial 02

Pada Tutorial 02, saya belajar konsep Model-View-Template (MVT) di Django untuk pertama kalinya. Saya membuat model `Experience` untuk menyimpan data pengalaman di database, view `show_experience` yang mengambil data tersebut dan mengirimkannya ke template, serta routing baru di `main/urls.py`. Karena ini konsep yang benar-benar baru buat saya, saya banyak bertanya ke Claude soal bagaimana urls.py, view, model, dan template ini saling terhubung sebelum mulai coding. Saya juga menambahkan unit test untuk memastikan halaman bisa diakses, data yang saya masukkan muncul dengan benar, dan pesan kondisi kosong muncul saat belum ada data.

Saya juga sempat menemukan bahwa data yang saya masukkan melalui Django shell di local tidak otomatis muncul ketika project di-deploy ke PWS, karena `db.sqlite3` di local tidak ikut ter-push ke repository. Karena masalah ini belum pernah dibahas di tutorial manapun, saya bertanya ke Claude bagaimana cara mengisi data ke database production tanpa perlu akses langsung ke server PWS. Dari situ saya diperkenalkan dengan konsep migrasi data menggunakan `migrations.RunPython()`, yang saya terapkan pada file `main/migrations/0004_seed_certifications_and_experiences.py` untuk mengisi data Experience dan Certification secara terprogram. Karena proses deploy PWS otomatis menjalankan `python manage.py migrate` setiap kali menerima push baru, data ini ikut terisi secara otomatis ke database production.

### Individual Assignment 2

Pada Individual Assignment 2, saya menerapkan pola MVT yang sama untuk bagian portfolio baru, yaitu Licenses & Certifications, lengkap dengan gambar untuk setiap sertifikat. Saya membuat model `Certification` dengan field title, issuer, issue_date, credential_id, description, dan image, kemudian view dan template baru untuk menampilkannya, serta rute baru yang bisa diakses lewat navbar. Data lima sertifikat saya (TOEFL ITP, finalis International Science Olympiad, Student Council Executive Committee, UKBI, dan Super Mentor Staff DDP0) saya masukkan melalui Django shell, bukan ditulis langsung di HTML.

Di luar kebutuhan minimum tugas, saya juga menata ulang halaman Experience. Bagian marquee foto yang sebelumnya ada di halaman profil saya pindahkan ke halaman My Journey tersendiri, sedangkan data dari model `Experience` tetap dirender di halaman yang sama untuk memenuhi ketentuan Tutorial 02, tetapi disembunyikan secara visual karena informasinya sudah terwakili oleh marquee. Saya juga menambahkan tiga unit test baru untuk memastikan halaman Certifications bisa diakses, datanya muncul dengan benar, dan pesan kondisi kosong berfungsi.

### Tutorial 03

Pada Tutorial 03, saya belajar konsep Data Delivery menggunakan JSON dan menerapkan skeleton template (`base.html`) supaya navbar dan footer tidak ditulis berulang di setiap halaman. Saya awalnya mengikuti contoh dari modul yang menggunakan section Projects sebagai latihan (Create, Delete, dan JSON delivery), namun karena section ini belum pernah ada di portofolio saya sebelumnya, section tersebut kemudian saya hapus setelah Individual Assignment 3 selesai, dan digantikan sepenuhnya oleh section Licenses & Certifications yang sudah ada sejak Tutorial 02.

Proses refactor ke `base.html` sempat menimbulkan beberapa error yang tidak saya duga, seperti `TemplateSyntaxError` karena saya lupa menghapus tag HTML lama sebelum menambahkan `{% extends %}`, dan `NoReverseMatch` karena ada nama URL yang tidak sinkron antara template dan `urls.py`. Saya juga sempat mengalami error `CSRF verification failed` ketika mencoba submit form di PWS, yang ternyata disebabkan oleh trailing slash pada `CSRF_TRUSTED_ORIGINS` di `settings.py`.

Menjelang akhir Tutorial 03, saya baru menyadari bahwa `experience.html` dan `certification.html` (yang dibuat sebelum Tutorial 03) belum mengikuti struktur `extends base.html`, sehingga navbar di kedua halaman tersebut tidak konsisten dengan halaman lain. Saya kemudian melakukan refactor pada kedua berkas tersebut. Saat menjalankan `python manage.py test`, saya juga menemukan dua test yang gagal: satu karena navbar masih menggunakan tautan `#profile` alih-alih tautan URL yang sebenarnya, dan satu lagi karena migrasi `0004_seed_certifications_and_experiences.py` yang berisi data seed ikut dijalankan pada database sementara saat testing, sehingga data uji coba tercampur dengan data seed. Saya memperbaiki keduanya dengan mengubah tautan navbar dan memindahkan migrasi berikutnya supaya tidak lagi bergantung pada migrasi seed tersebut, sebelum menghapus berkas migrasi seed itu.

### Individual Assignment 3

Pada Individual Assignment 3, saya menerapkan mekanisme Form dan Data Delivery pada section Licenses & Certifications, karena section ini sudah memiliki variasi tipe data (`CharField`, `DateField`, `TextField`) yang sesuai dengan ketentuan tugas dan sudah ada datanya sejak Individual Assignment 2. Saya membuat `CertificationForm` di `forms.py`, serta fungsi Create, **Update**, Delete, dan JSON delivery untuk Certification.

Fitur Update merupakan hal baru yang belum diajarkan di Tutorial 03 (yang hanya mencontohkan Create dan Delete), sehingga saya perlu memahami konsep `instance=` pada ModelForm untuk mengisi form dengan data lama sebelum disimpan ulang. Saya sempat membuat kesalahan pada tahap awal, yaitu `action` pada form Create dan Update yang sama-sama mengarah ke fungsi create, sehingga proses update yang saya lakukan justru menghasilkan data baru, bukan memperbarui data lama. Saya memperbaikinya dengan mengirim `form_action`, `form_title`, dan `submit_label` yang berbeda dari masing-masing view melalui context, sehingga satu template form (`certification_form.html`) dapat dipakai ulang untuk Create maupun Update.

Setelah checklist utama tugas selesai, saya menghapus section Projects yang sebelumnya dibuat sebagai latihan di Tutorial 03, karena portofolio ini sudah memiliki section Certifications yang lebih relevan dan sudah menerapkan mekanisme yang sama. Proses ini melibatkan penghapusan model, view, form, url, dan template terkait Projects, serta migrasi terkait yang perlu ditelusuri satu per satu supaya tidak meninggalkan referensi yang rusak.

Di luar ketentuan minimum tugas, saya juga menambahkan proteksi sederhana berupa field password pada form Create, Update, dan Delete Certification. Password disimpan di `.env` sebagai `FORM_PASSWORD` dan dicocokkan secara manual di view sebelum data disimpan atau dihapus. Ini bukan sistem autentikasi sesungguhnya, melainkan langkah antisipasi sementara mengingat konsep Authentication, Session, dan Cookies belum diajarkan sampai tutorial ini, sehingga sebenarnya siapa pun yang mengetahui URL dapat menambah, mengubah, atau menghapus data pada portofolio saya.

### Tutorial 04

Pada Tutorial 04, saya mempelajari konsep Authentication, Session, dan Cookies di Django. Saya menerapkan Register, Login, dan Logout menggunakan `UserCreationForm` dan `AuthenticationForm` bawaan Django, menampilkan status login pengguna di navbar, serta menyimpan waktu login terakhir menggunakan cookie `last_login` yang di-set saat login dan dihapus saat logout. Saya juga menambahkan pembatasan akses sederhana pada fitur Create, Update, dan Delete Certification menggunakan `@login_required` dan pengecekan `request.user.is_superuser`, sehingga hanya pemilik portofolio yang bisa mengakses fitur tersebut, serta menambahkan field `starred_by` (`ManyToManyField` ke model `User`) pada model `Certification` beserta view `toggle_star` untuk memberi dan membatalkan star.

Saat pertama kali mengetes fitur ini dengan akun lain, saya sempat bingung karena tombol Add/Edit/Delete jadi tidak muncul sama sekali, padahal saya pikir pembatasannya cukup lewat password saja seperti yang saya tambahkan di Assignment 3. Setelah ditelusuri, saya baru menyadari bahwa Tutorial 04 memang mengharuskan pembatasan di level peran/role, bukan hanya di level password, sehingga keduanya perlu berjalan berdampingan: role menentukan siapa yang boleh melihat dan mengakses tombolnya, sedangkan password tetap menjadi lapisan tambahan seperti sebelumnya.

### Individual Assignment 4

Pada Individual Assignment 4, saya melanjutkan pola autentikasi dari Tutorial 04 dengan menambahkan peran baru bernama Editor, yang berada di antara Regular User dan Owner (superuser). Peran ini saya implementasikan menggunakan Django Group yang dibuat dan di-assign melalui halaman `/admin/`, kemudian dicek di view menggunakan `request.user.groups.filter(name="Editor").exists()`. Saya menerapkan pengecekan ini di seluruh view yang relevan sehingga Visitor diarahkan ke halaman login saat mencoba melakukan aksi yang butuh akun, Regular User bisa membaca data dan memberi/membatalkan star tetapi mendapat `403 Forbidden` saat mencoba create, update, atau delete, Editor memiliki hak yang sama seperti Regular User ditambah bisa membuka dan menyimpan form Update, tetapi tetap mendapat `403 Forbidden` saat mencoba create atau delete, dan Owner memiliki akses penuh ke semua aksi. Tombol Tambah, Edit, dan Delete pada template `certification.html` juga saya sembunyikan secara kondisional sesuai peran yang sedang login.

Saya sempat mempertimbangkan untuk menghapus field password `FORM_PASSWORD` dari Assignment 3 karena merasa sudah tidak relevan setelah ada role-based access control, namun setelah berkonsultasi dengan asisten dosen, saya mendapat konfirmasi bahwa field tersebut boleh tetap dipertahankan sebagai lapisan tambahan semacam "2FA sederhana", sehingga saya memutuskan untuk tidak menghapusnya. Untuk memastikan seluruh logika otorisasi ini benar, saya menambahkan automated test baru di `main/tests.py` yang mencakup keempat peran tersebut beserta fitur Create/Update/Delete/JSON dari Assignment 3, dengan `FORM_PASSWORD` yang dibaca lewat `os.getenv()` alih-alih ditulis langsung di kode, mengingat repository ini bersifat publik.

Ketika memeriksa ulang checklist "API Integrity & Data Security", saya menyadari bahwa penambahan field `starred_by` pada model `Certification` membuat JSON endpoint `/api/certifications/` ikut menampilkan daftar pengguna yang memberi star pada tiap sertifikat, padahal ini tidak seharusnya ada di endpoint tersebut. Saya kemudian memperbaikinya dengan menyebutkan secara eksplisit field mana saja yang boleh ikut di-serialize pada `get_certifications_json`, sehingga output JSON-nya kembali seperti pada Assignment 3, sementara fitur star di halaman Certifications tetap berjalan normal karena datanya diambil langsung dari database, bukan dari hasil serialize tersebut.

Di luar kebutuhan minimum tugas, saya menambahkan dua fitur kreativitas pada halaman Certifications, yaitu tooltip pada tombol star yang menampilkan daftar nama pengguna yang sudah memberi star, dan kontrol sort untuk mengurutkan sertifikat berdasarkan yang terbaru atau yang paling banyak di-star, menggunakan query parameter URL tanpa JavaScript.

### Tutorial 05

Pada Tutorial 05, saya mempelajari JavaScript untuk pertama kalinya di project ini, khususnya AJAX dengan Fetch API, `async`/`await`, serta perlindungan dari serangan XSS. Karena section Projects yang dipakai sebagai contoh di modul sudah saya hapus sejak Individual Assignment 3, saya menerapkan seluruh langkah tutorial pada section Licenses & Certifications yang sudah memiliki fitur autentikasi, role, dan star dari Tutorial 04.

Saya membuat komponen toast (`toast.html` dan `static/js/toast.js`) yang dimasukkan ke `base.html`, lalu mengubah `get_certifications_json` dari `serializers.serialize` menjadi JSON yang dirakit manual dengan `JsonResponse` supaya bisa menyisipkan informasi star milik pengguna yang sedang login, sekaligus mendukung pencarian (`?title=`) dan sort (`?sort=`). Berbeda dengan Individual Assignment 4, daftar username pemberi star kali ini memang perlu ikut dikirim di JSON karena tooltip star sekarang dirender oleh JavaScript, bukan lagi oleh template Django. View `show_certification` juga saya sederhanakan sehingga hanya merender kerangka halaman, sedangkan kartu sertifikat dirakit oleh JavaScript lengkap dengan kondisi loading, kosong, dan error. Selain itu, saya menambahkan debouncing pada pencarian, memindahkan form tambah sertifikat ke dalam modal yang dikirim lewat view baru `create_certification_ajax`, serta menambahkan `escapeHtml` di JavaScript dan `strip_tags` pada method `clean_<field>` di `CertificationForm`.

Setelah perubahan ini, beberapa test lama gagal karena data sertifikat tidak lagi muncul di HTML awal, sehingga saya mengubahnya agar memeriksa endpoint JSON. Saya juga sempat bingung karena satu test tetap gagal padahal sudah saya ganti, dan ternyata method `test_empty_certification_page` tertulis dua kali di dua class berbeda karena salah tempel. Saat mengetes di browser, saya juga menemukan bahwa form di modal tambah sertifikat terpotong di atas dan bawah layar, karena modal tersebut memakai ulang CSS modal hapus dari Tutorial 03 yang dulu isinya pendek dan tidak bisa di-scroll.

### Individual Assignment 5

Karena pola AJAX dari Tutorial 05 sudah langsung saya terapkan pada section Certifications (section yang saya kerjakan di Tugas 3 dan Tugas 4), checklist minimal Individual Assignment 5 sudah terpenuhi dari hasil tutorial. Hak akses dari Tugas 4 tetap berlaku, sehingga pengunjung yang belum login tetap bisa membaca data, sedangkan penambahan data hanya bisa dilakukan oleh Owner dan pengecekannya tetap dilakukan di dalam view.

Di luar kebutuhan minimum tugas, saya menambahkan beberapa fitur supaya semua aksi di halaman Certifications konsisten tanpa reload. Tombol star sekarang dikirim lewat endpoint baru `toggle_star_ajax`, sehingga angka star langsung berubah dan muncul toast, sedangkan pengunjung yang belum login mendapat respons `401` lalu diarahkan ke halaman login. Fitur hapus juga saya ubah menjadi AJAX lewat `delete_certification_ajax`, yang tetap memeriksa role Owner dan `FORM_PASSWORD`. Saya juga menambahkan tombol "Coba lagi" pada kondisi error, tulisan jumlah hasil pencarian di atas kartu, dan membuat tombol sort dari Tugas 4 ikut berjalan lewat AJAX. Terakhir, fungsi `getCookie` dan `escapeHtml` saya pindahkan ke `static/js/utils.js` supaya bisa dipakai ulang di halaman lain, sesuai petunjuk pada soal. View lama `toggle_star` dan `delete_certification` tetap saya pertahankan supaya test dari Tugas 4 tetap berjalan.

## Pertanyaan Reflektif

### Tugas 1

**1. Penggunaan Semantic HTML5**

Saya menggunakan beberapa elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, dan `<footer>`. Saya juga menggunakan `<dl>`, `<dt>`, dan `<dd>` untuk menampilkan informasi seperti NPM dan program studi. Saya memilih elemen-elemen tersebut supaya struktur HTML lebih jelas dan tidak semuanya menggunakan `<div>`. Misalnya, `<header>` digunakan untuk bagian atas halaman, sedangkan `<section>` digunakan untuk memisahkan bagian Profile, About, dan Experience. Menurut saya, penggunaan elemen semantik juga membuat struktur halaman lebih mudah dipahami ketika saya mengembangkan CSS. Saya belum menggunakan `<article>` atau `<aside>` karena konten pada website ini belum membutuhkan elemen tersebut.

**2. Responsive CSS**

Bagian yang paling menantang untuk dibuat responsive adalah hero section dan navbar. Pada hero section, saya perlu mengatur ulang posisi foto dan teks ketika ukuran layar mengecil supaya tampilannya tetap rapi dan urutan kontennya masih nyaman dibaca. Pada navbar, saya mengubah layout menjadi vertikal di layar kecil karena nama saya cukup panjang dan menu bisa terlalu sempit jika tetap dibuat horizontal. Saya beberapa kali mencoba ukuran dan posisi yang berbeda untuk melihat bagaimana tampilannya pada ukuran layar yang berbeda sampai menemukan layout yang menurut saya paling nyaman untuk desktop maupun mobile.

**3. Keterbatasan Static Web**

Karena website ini masih berupa static web, kontennya masih ditulis langsung di HTML. Jadi, ketika saya ingin menambahkan atau mengubah pengalaman, saya harus mengubah kode HTML secara manual. Menurut saya, cara ini masih cukup untuk portfolio sederhana, tetapi akan kurang praktis jika jumlah pengalaman saya semakin banyak. Untuk pengembangan selanjutnya, saya ingin menyimpan data pengalaman menggunakan model Django dan database, sehingga konten dapat dikelola tanpa harus mengubah HTML secara manual setiap kali ada perubahan.

### Tugas 2

**1. Alur MVT dari Request sampai Ditampilkan**

Ketika pengguna membuka halaman `/certification/`, permintaan pertama diterima oleh `urls.py` milik proyek (`portofolio/urls.py`), yang meneruskan permintaan tersebut ke `urls.py` milik aplikasi `main` melalui `include("main.urls")`. Di `main/urls.py`, path `"certification/"` dicocokkan dan memanggil fungsi view `show_certification`. View ini mengambil seluruh data dari model `Certification` menggunakan `Certification.objects.all()`, memasukkannya ke dalam context, lalu mengirim context tersebut ke template `certification.html` melalui fungsi `render()`. Template kemudian memproses context ini menggunakan perulangan `{% for %}` untuk menampilkan setiap data, dan hasil akhirnya dikirim sebagai response HTML ke browser.

**2. Kenapa Data Sebaiknya di Model, Bukan Hardcode di Template**

Menurut saya, menyimpan data di model membuat portfolio lebih mudah dikembangkan ke depannya. Kalau saya ingin menambah atau mengubah satu sertifikat, saya cukup melakukannya lewat Django shell atau admin panel, tanpa perlu membuka dan mengedit file HTML secara manual. Selain itu, karena semua data ditampilkan lewat satu blok template yang sama menggunakan perulangan, tampilannya jadi lebih konsisten dan saya tidak perlu menyalin-tempel HTML untuk setiap item baru. Cara ini juga membuat project tetap sederhana meskipun jumlah data bertambah banyak, karena yang bertambah hanya baris data di database, bukan baris kode di template.

**3. Perbedaan makemigrations dan migrate**

`makemigrations` digunakan untuk membuat berkas migrasi baru yang mencatat perubahan pada model, misalnya field atau tabel baru, berdasarkan perbandingan antara kode model saat ini dengan riwayat migrasi sebelumnya. Perintah ini belum benar-benar mengubah database, hanya menyiapkan instruksi perubahannya dalam bentuk berkas Python. Sementara itu, `migrate` menjalankan instruksi dari berkas migrasi tersebut ke database yang sesungguhnya. Contoh perubahan yang mengharuskan saya menjalankan keduanya adalah saat saya menambahkan field `image` pada model `Certification`. Setelah menambahkan field tersebut di `models.py`, saya menjalankan `makemigrations` untuk membuat berkas migrasinya, kemudian `migrate` supaya kolom `image` benar-benar ditambahkan ke tabel `Certification` di `db.sqlite3`.

### Tugas 3

1. **ModelForm vs HTML Manual, dan Alasan `{% csrf_token %}`**

ModelForm dipakai karena dia otomatis menyalin struktur dari model (`Certification`) menjadi form, jadi saya tidak perlu menulis satu per satu tag `<input>` untuk setiap field secara manual. Field seperti `issue_date` otomatis menjadi kalender picker, dan kalau nanti ada field baru ditambahkan ke model, form-nya tinggal disesuaikan di `fields = [...]`, tanpa perlu membongkar ulang HTML. ModelForm juga otomatis memvalidasi input (misalnya `issue_date` harus berformat tanggal yang valid) tanpa saya perlu menulis validasi manual.

`{% csrf_token %}` wajib ada karena form yang mengirim data lewat method POST rawan disalahgunakan lewat serangan CSRF (Cross-Site Request Forgery), misalnya situs jahat yang membuat form tersembunyi untuk diam-diam mengirim request ke server kita menggunakan sesi login korban. Token ini berfungsi seperti kode rahasia sekali pakai yang dibuat server, dan submit form hanya diterima kalau token-nya cocok, sehingga request dari luar situs kita otomatis ditolak.

2. **Kenapa JSON Lebih Disukai Dibanding XML**

JSON lebih ringkas karena tidak perlu menulis closing tag di setiap elemen seperti XML, sehingga ukuran datanya lebih kecil dan lebih cepat dikirim. JSON juga lebih mudah di-parsing oleh JavaScript, karena struktur JSON memang berasal dari cara JavaScript menulis object, sehingga begitu data JSON sampai di browser, bisa langsung dipakai tanpa proses konversi tambahan. Ini penting untuk arsitektur web modern (seperti REST API) yang banyak mengirim data bolak-balik antara server dan frontend.

3. **Alur View Mengembalikan Data JSON dan Alasan Serialization**

Alurnya, ketika ada request ke endpoint (misalnya `/api/certifications/`), view mengambil data dari database (`Certification.objects.all()`). Data ini masih berbentuk objek Python/Django, bukan teks. Kemudian `serializers.serialize("json", ...)` dipanggil untuk mengubah objek tersebut menjadi teks berformat JSON. Setelah itu, teks JSON tersebut dibungkus menggunakan `HttpResponse` dengan `content_type="application/json"` supaya browser atau aplikasi lain tahu bahwa ini format JSON, lalu dikirim kembali sebagai response.

Serialization perlu dilakukan karena objek Python (seperti instance model Django) strukturnya hanya "dikenali" oleh Python saja, tidak bisa langsung dikirim lewat internet. Data yang dikirim lewat HTTP harus berbentuk teks (string), sehingga objek tersebut perlu "diterjemahkan" dulu menjadi teks JSON yang formatnya universal, supaya bisa dibaca oleh bahasa pemrograman lain juga, tidak hanya Python.

### Tugas 5

1. **Debouncing dan Kenapa Penting untuk Pencarian AJAX**

Debouncing adalah teknik untuk menunda sebuah fungsi sampai pengguna berhenti melakukan aksi selama jeda waktu tertentu. Di portofolio saya, setiap kali pengguna mengetik di kolom pencarian, timer sebelumnya dibatalkan dengan `clearTimeout` lalu dimulai ulang dengan `setTimeout` selama 300 milidetik, sehingga permintaan ke server baru dikirim setelah pengguna benar-benar berhenti mengetik.

Teknik ini penting karena tanpa debouncing, mengetik kata "toefl" saja sudah mengirim lima permintaan berturut-turut ke server, padahal yang dibutuhkan hanya hasil untuk kata terakhir. Dengan debouncing, server tidak dibanjiri permintaan yang tidak perlu, dan kemungkinan hasil pencarian lama muncul belakangan lalu menimpa hasil terbaru juga berkurang.

2. **Fungsi `await` pada `fetch()`**

`fetch()` tidak langsung mengembalikan respons dari server, melainkan sebuah Promise, yaitu semacam janji bahwa hasilnya akan datang nanti. `await` membuat JavaScript menunggu sampai Promise tersebut selesai sebelum lanjut ke baris berikutnya, sehingga variabel `response` benar-benar berisi respons dari server.

Kalau tidak menggunakan `await`, variabel tersebut masih berisi Promise, bukan respons. Akibatnya, pengecekan seperti `response.ok` tidak berjalan dengan benar, `response.json()` akan error, dan kode di bawahnya langsung dijalankan sebelum data sampai, misalnya kartu sertifikat jadi dirender dengan data kosong. Karena `await` hanya bisa dipakai di dalam fungsi `async`, fungsi seperti `fetchCertifications` dan `addCertification` saya tandai sebagai `async`.

3. **Serangan XSS dan Kenapa Data dari AJAX Lebih Rentan**

XSS (Cross-Site Scripting) adalah serangan ketika penyerang menyisipkan kode JavaScript ke dalam data, misalnya judul sertifikat seperti `<img src="x" onerror="alert('XSS!')">`, lalu kode tersebut ikut dijalankan di browser pengguna lain yang membuka halaman itu. Penyerang bisa memanfaatkannya untuk membaca cookie `csrftoken` dan mengirim permintaan atas nama korban.

Data yang ditampilkan lewat template Django lebih aman karena Django otomatis melakukan escaping pada setiap `{{ variabel }}`, misalnya mengubah `<` menjadi `&lt;`, sehingga browser hanya menampilkannya sebagai teks. Sementara itu, ketika data dimasukkan lewat JavaScript menggunakan `innerHTML`, tidak ada lagi escaping otomatis dari Django, sehingga browser akan menganggap tag HTML di dalam data sebagai kode sungguhan. Karena itu, saya membungkus setiap nilai teks dengan `escapeHtml()` sebelum dimasukkan ke `innerHTML`, dan juga membersihkan input di server menggunakan `strip_tags` pada `CertificationForm`.

## AI Disclosure

Saya menggunakan **Claude** sebagai AI assistant selama proses pengembangan Individual Assignment 1. Saya menggunakannya terutama ketika mengalami kesulitan dalam mengembangkan ide desain menjadi implementasi HTML dan CSS, serta untuk mendapatkan masukan, melakukan review kode, dan mencari alternatif ketika suatu bagian belum berjalan sesuai yang saya inginkan.

Saya memulai project dari hasil pengerjaan Tutorial 1, kemudian mengembangkan portfolio berdasarkan ide dan kebutuhan saya sendiri. Saya menentukan informasi yang ditampilkan, pengalaman organisasi dan volunteering yang dimasukkan, foto dokumentasi, serta pembagian section pada website. Untuk menentukan tampilan visual, saya juga mencari berbagai referensi portfolio melalui browser dan Pinterest, kemudian memilih dan menyesuaikan gaya yang paling sesuai dengan konsep yang saya inginkan. Dari proses tersebut, saya menentukan kombinasi warna terracotta, navy, dan cream yang terinspirasi dari foto profil saya sendiri.

Dalam proses coding, saya mengerjakan dan menyesuaikan project secara bertahap. Ketika mengalami kesulitan pada bagian tertentu, saya memberikan kode atau menjelaskan masalahnya kepada Claude untuk mendapatkan masukan. Hasil dari bantuan tersebut kemudian saya sesuaikan kembali dengan struktur project dan tampilan yang saya inginkan.

Salah satu contohnya terjadi pada fitur modal dan animasi scroll. Pada proses pengembangan awal, implementasi yang dibantu Claude masih menggunakan JavaScript. Karena saya belum memahami bagian tersebut dengan baik dan tugas mengharuskan penggunaan HTML5 dan CSS3, saya meminta alternatif yang tidak menggunakan JavaScript. Setelah mencoba beberapa pendekatan, modal menggunakan `:target`, sedangkan animasi scroll menggunakan `animation-timeline: view()` dengan `@supports` sebagai fallback.

### Bagian yang Dibantu AI

Claude membantu memberikan masukan terhadap struktur dan tampilan website, melakukan review kode, mencari alternatif implementasi, serta membantu mengembangkan beberapa bagian HTML/CSS ketika saya mengalami kesulitan. Bantuan tersebut digunakan pada beberapa bagian seperti Experience, marquee animation, modal, scroll animation, dan elemen dekoratif.

### Bagian yang Saya Kerjakan dan Putuskan Sendiri

Saya menentukan konsep dan tujuan portfolio, isi setiap section, data pribadi, pengalaman yang ditampilkan, foto dokumentasi, serta kategori Organizations dan Volunteering. Saya juga mencari referensi desain sendiri melalui browser dan Pinterest, kemudian menentukan arah visual, warna, tipografi, dan elemen yang ingin digunakan.

Saya memilih solusi yang digunakan ketika terdapat beberapa alternatif dari AI dan melakukan penyesuaian terhadap hasil implementasinya. Setelah itu, saya mengecek website secara langsung melalui browser dan perangkat mobile untuk memastikan layout, responsive design, dan fitur yang digunakan berjalan sesuai dengan yang saya inginkan.

### Contoh Penggunaan AI / Prompting

Saya menggunakan prompt secara bertahap sesuai dengan kebutuhan yang muncul selama pengerjaan. Beberapa contohnya adalah meminta Claude melakukan review terhadap project dari Tutorial 1, memberikan rekomendasi pengembangan portfolio, membantu mengembangkan section Experience, serta menjelaskan dan mencari alternatif implementasi ketika terdapat bagian kode yang belum saya pahami.

Salah satu proses yang cukup penting adalah ketika Claude melakukan review terhadap implementasi modal dan animasi. Dari review tersebut diketahui bahwa implementasi awal masih menggunakan JavaScript. Saya kemudian meminta agar fitur tersebut dibuat dalam versi yang murni menggunakan HTML5 dan CSS3. Setelah itu, saya juga meminta alternatif agar efek fade-in dapat muncul setiap kali saya melakukan scroll ke suatu section. Dari beberapa pendekatan yang diberikan, saya memilih menggunakan `animation-timeline: view()`.

### AI Chat / Prompting Log

Berikut beberapa contoh prompt yang mewakili proses penggunaan AI selama pengerjaan. Prompt ditulis kembali secara ringkas agar menunjukkan tujuan dari masing-masing percakapan.

1. **Review project**

   > "Saya ingin mengembangkan project dari Tutorial 1 menjadi portfolio pribadi. Bisa review kode yang sudah saya buat dan memberikan rekomendasi bagian yang dapat dikembangkan?"

   Digunakan untuk mendapatkan masukan mengenai section dan fitur yang dapat ditambahkan pada portfolio.

2. **Mencari alternatif tanpa JavaScript**

   > "Bisa dibuat dalam versi yang murni menggunakan HTML5 dan CSS3 tanpa JavaScript?"

   Digunakan ketika saya ingin mengubah implementasi awal agar sesuai dengan requirement tugas.

3. **Mengubah modal menjadi CSS-only**

   > "Bagaimana cara membuat modal ini tanpa JavaScript tetapi tetap bisa dibuka ketika kartu Experience diklik?"

   Dari proses ini saya menggunakan teknik CSS `:target` untuk modal.

4. **Membuat fade-in ketika scrolling**

   > "Saya ingin efek fade-in muncul ketika setiap section mulai masuk ke viewport saat user melakukan scroll. Ada pendekatan CSS yang bisa digunakan?"

   Prompt ini digunakan ketika saya ingin mengubah efek fade-in dari yang sebelumnya berjalan saat halaman dimuat menjadi efek yang mengikuti posisi section ketika di-scroll.

5. **Memahami solusi yang dipilih**

   > "Bisa jelaskan cara kerja `animation-timeline: view()` dan bagaimana fallback `@supports` bekerja pada browser yang belum mendukung fitur tersebut?"

   Prompt ini digunakan agar saya memahami implementasi yang digunakan dan tidak hanya menerima hasil kode dari AI.

Prompt diberikan secara bertahap sesuai dengan kebutuhan dan masalah yang muncul selama proses pengerjaan. Saya menggunakan AI sebagai alat bantu untuk berdiskusi, mengeksplorasi alternatif, dan menyelesaikan bagian tertentu, kemudian menyesuaikan hasilnya dengan kebutuhan project.

### Keterbatasan AI dan Pemahaman Saya

Claude tidak dapat menjalankan atau melihat tampilan project Django saya secara langsung. Karena itu, ketika terdapat masalah pada tampilan, saya perlu menjelaskan kondisi yang saya lihat dan hasil yang ingin saya capai agar Claude dapat memberikan saran yang lebih sesuai.

Saya juga menyadari bahwa masih ada beberapa bagian teknis yang perlu saya pahami lebih dalam, terutama CSS Grid/Flexbox, animasi, `:target`, dan `animation-timeline`. Karena beberapa bagian kode dikembangkan dengan bantuan AI, saya perlu mempelajari kembali cara kerja bagian-bagian tersebut agar dapat memahami dan menjelaskan project saya secara mandiri.

Menurut saya, penggunaan AI membantu mempercepat proses eksplorasi dan troubleshooting, terutama ketika saya mengalami kesulitan dalam menemukan pendekatan yang sesuai. Namun, AI tidak selalu memberikan solusi yang langsung sesuai dengan kebutuhan project. Saya tetap perlu menentukan apa yang ingin dibuat, memilih alternatif yang sesuai dengan requirement, menyesuaikan hasilnya dengan project, dan mengecek hasil akhirnya secara langsung melalui browser dan perangkat mobile.

## Update AI Disclosure: Tutorial 02 & Individual Assignment 2

Pada Tutorial 02 dan Individual Assignment 2, saya kembali menggunakan Claude sebagai alat bantu, kali ini untuk mempelajari konsep Model-View-Template (MVT) di Django yang benar-benar baru buat saya. Saya juga sempat kebingungan soal kenapa data sertifikat tidak muncul di PWS padahal sudah ada di local, dan setelah bertanya ke Claude, saya baru tahu bahwa ini soal database local dan production yang terpisah, lalu dibantu memahami cara mengisi data lewat migrasi Django.

### Bagian yang Dibantu AI

Claude membantu menjelaskan bagaimana model, view, template, dan urls.py saling terhubung, serta membantu menuliskan kode untuk model `Experience` dan `Certification`, view, template, dan unit test. Claude juga membantu saya menata ulang halaman Experience ketika saya merasa tampilan marquee dan data dari database terlihat dobel di halaman yang sama, sampai akhirnya ditemukan solusi memisahkan tampilan visual (marquee) dari data teknis untuk keperluan Tutorial 02.

### Bagian yang Saya Kerjakan dan Putuskan Sendiri

Saya menentukan sendiri bagian portfolio yang ingin dijadikan fitur baru, yaitu Licenses & Certifications, serta membawa seluruh data sertifikat saya sendiri (dari LinkedIn dan sertifikat fisik yang saya scan). Saya juga menentukan kategori untuk setiap pengalaman (internship atau volunteer) berdasarkan pemahaman saya sendiri terhadap masing-masing peran, serta status pengalaman mana yang masih berjalan dan mana yang sudah selesai.

Untuk bagian implementasi, saya tidak hanya menyalin kode yang diberikan, tetapi juga mengerjakan sendiri beberapa bagian secara manual di VS Code, seperti memindahkan section Experience dari halaman profil ke halaman baru, menghapus bagian modal yang sudah tidak diperlukan, serta menyesuaikan nav dan struktur HTML ketika hasil pertama belum sesuai dengan yang saya inginkan. Ketika ada bagian yang errornya belum jelas penyebabnya atau saya ingin memastikan pendekatan yang saya pilih sudah tepat, barulah saya berdiskusi dengan Claude. Sebelum melakukan commit, saya selalu mengecek tampilan di browser dan menjalankan `python manage.py test` untuk memastikan semuanya berjalan dengan benar.

### AI Chat / Prompting Log

1. **Memahami alur MVT**

   > "Bisa jelasin dulu ga kaya apa tugas di assignment 2 ini?"

   Digunakan untuk memahami keseluruhan requirement sebelum mulai menentukan pendekatan implementasi.

2. **Menentukan field model Certification**

   > "Coba jelasin dulu ya, biar aku bisa kategoriin sertifikat-sertifikat ini."

   Digunakan saat menentukan field apa saja yang dibutuhkan model `Certification` berdasarkan data sertifikat yang saya miliki.

3. **Menata ulang halaman Experience**

   > "Kayanya aku malah gasuka penempatannya gini, saran dong."

   Setelah mendapat beberapa opsi dari Claude, saya mencoba sendiri memindahkan bagian HTML-nya secara manual di VS Code terlebih dahulu, dan baru kembali bertanya ketika hasilnya belum sesuai dengan yang saya bayangkan.

4. **Menambahkan gambar ke sertifikat**

   > "Gimana caranya biar ada gambar sertifnya juga di kartu Certification?"

   Digunakan untuk menentukan field `image` pada model dan cara menghubungkannya ke file gambar; proses menyiapkan dan mengonversi file gambar sertifikatnya sendiri saya lakukan secara manual.

### Keterbatasan AI dan Pemahaman Saya

Sama seperti pada Individual Assignment 1, Claude tidak dapat menjalankan atau melihat langsung tampilan project saya, sehingga saya perlu menjelaskan apa yang terlihat setiap kali ada error atau tampilan yang tidak sesuai. Karena konsep MVT ini benar-benar baru buat saya, saya menyadari masih perlu mempelajari lebih dalam bagaimana model, view, template, dan urls.py bekerja bersama, khususnya bagian migrasi database dan Django Template Language, agar saya bisa menjelaskan dan mengembangkan bagian ini secara mandiri ke depannya.

## Update AI Disclosure: Tutorial 03 & Individual Assignment 3

Pada Tutorial 03 dan Individual Assignment 3, saya menggunakan Claude terutama untuk membantu debugging, karena banyak error yang muncul justru dari proses refactor kode lama (dari Tutorial 2) ke struktur baru yang menggunakan `base.html`, bukan dari materi baru itu sendiri.

### Bagian yang Dibantu AI

Claude membantu menjelaskan penyebab beberapa error yang saya temui, seperti `TemplateSyntaxError`, `NoReverseMatch`, `TemplateDoesNotExist`, dan `CSRF verification failed`, serta membantu menulis kode untuk `CertificationForm`, view Create/Update/Delete/JSON Certification, dan modal konfirmasi delete. Claude juga membantu saya memahami kenapa dua unit test gagal setelah refactor (navbar yang masih menggunakan tautan `#profile`, dan migrasi seed data yang ikut berjalan saat testing), serta membantu saya menelusuri langkah-langkah yang perlu diperiksa satu per satu ketika saya memutuskan menghapus section Projects di akhir pengerjaan.

### Bagian yang Saya Kerjakan dan Putuskan Sendiri

Saya memutuskan sendiri untuk tetap menggunakan section Certifications (bukan section baru) untuk Individual Assignment 3, karena field yang sudah ada dinilai cukup bervariasi, dan pada akhirnya memutuskan untuk menghapus section Projects karena sudah tergantikan oleh Certifications. Setelah mendapat penjelasan dari Claude soal penyebab suatu error, saya sendiri yang membuka dan mengedit berkas terkait (`views.py`, `urls.py`, `forms.py`, `admin.py`, template), menjalankan `python manage.py test` dan `python manage.py runserver` untuk memastikan perbaikannya benar, serta mengecek tampilan langsung di browser (local maupun PWS) setelah setiap perubahan.

Saat menghapus section Projects, saya juga sempat salah langkah dengan menghapus berkas migrasi `0005_project.py` secara manual tanpa membuat migrasi baru terlebih dahulu, yang sebenarnya bisa membuat riwayat migrasi dan database menjadi tidak sinkron. Saya kemudian memeriksa sendiri status migrasi menggunakan `python manage.py showmigrations` dan membandingkannya dengan berkas yang ada di folder `migrations`, untuk memastikan tidak ada referensi yang rusak sebelum melanjutkan.

Saya juga menentukan sendiri untuk menambahkan proteksi password sederhana sebagai fitur tambahan di luar requirement minimum, meskipun saya menyadari ini bukan solusi keamanan yang sesungguhnya.

### AI Chat / Prompting Log

1. **Debugging error setelah refactor**

   > "Saya sempat bingung karena setelah refactor ke base.html, alurnya terasa lompat-lompat. Saya juga menempelkan pesan error yang muncul di terminal maupun browser untuk ditelusuri bersama."

   Digunakan berulang kali sepanjang Tutorial 03 untuk memahami penyebab error setelah proses refactor, seperti `TemplateSyntaxError`, `NoReverseMatch`, dan `CSRF verification failed`.

2. **Memahami hasil test yang gagal**

   > "Tutorial ini sudah dinilai, tetapi ada feedback bahwa salah satu test (`test_completed_experience`) gagal. Saya menempelkan pesan error lengkapnya untuk ditelusuri penyebabnya."

   Digunakan untuk memahami pesan error dari `python manage.py test` dan menemukan bahwa penyebabnya adalah migrasi seed data yang ikut berjalan di database testing.

3. **Menentukan section untuk Individual Assignment 3**

   > "Saya meminta pendapat apakah sebaiknya tetap menggunakan section Certifications atau mengganti ke section lain untuk Individual Assignment 3."

   Digunakan untuk meminta pertimbangan sebelum memutuskan tetap menggunakan section Certifications.

4. **Menanyakan keterbatasan keamanan**

   > "Saya menanyakan apakah section yang bisa diisi lewat form ini berarti bisa diubah-ubah oleh siapa saja yang mengetahui URL-nya, dan apa yang bisa dilakukan untuk mengantisipasinya."

   Digunakan untuk memahami bahwa keterbatasan ini memang belum bisa diatasi karena materi Authentication belum diajarkan, sebelum memutuskan menambahkan proteksi password sederhana sebagai langkah sementara.

### Keterbatasan AI dan Pemahaman Saya

Pada tutorial ini, saya menyadari bahwa proses refactor kode lama ternyata lebih rawan menimbulkan error dibanding menulis kode baru dari nol, karena ada bagian-bagian yang mudah terlewat, seperti berkas HTML yang belum ikut di-extend, migrasi yang saling bergantung, atau referensi ke model yang sudah dihapus namun masih tertinggal di berkas lain (seperti `admin.py`). Claude membantu saya menelusuri error tersebut satu per satu, tetapi saya tetap perlu memeriksa kembali setiap berkas secara manual untuk memastikan tidak ada bagian lain yang tertinggal. Saya juga menyadari bahwa proteksi password yang saya tambahkan bukan solusi keamanan yang sesungguhnya, dan saya perlu mempelajari konsep Authentication, Session, dan Cookies lebih lanjut di tutorial-tutorial berikutnya untuk benar-benar membatasi akses ke fitur Create, Update, dan Delete pada portofolio saya.

## Update AI Disclosure: Tutorial 04 & Individual Assignment 4

Pada Tutorial 04 dan Individual Assignment 4, saya menggunakan Claude terutama untuk memahami konsep Authentication, Session, Cookies, dan Role-Based Access Control, karena ini pertama kalinya saya menerapkan sistem login sungguhan pada project ini, serta untuk membantu menelusuri satu kejanggalan logika otorisasi dan satu celah keamanan pada JSON endpoint yang saya temukan sendiri saat menguji ulang checklist tugas.

### Bagian yang Dibantu AI

Claude membantu menjelaskan cara kerja `UserCreationForm`, `AuthenticationForm`, `login()`, `logout()`, serta perbedaan konsep session dan cookie, dan membantu menuliskan kode untuk view `register`, `login_user`, `logout_user`, `toggle_star`, serta penambahan field `starred_by` pada model `Certification`. Untuk Assignment 4, Claude membantu menjelaskan cara kerja Django Group untuk peran Editor, membantu menyusun logic pengecekan keempat peran di view, serta membantu menuliskan automated test baru (`AuthorizationTest`, `CertificationCRUDTest`). Claude juga membantu saya memahami kenapa JSON endpoint bisa ikut membocorkan data `starred_by`, dan menjelaskan bahwa perbaikannya cukup dengan menyebutkan field yang boleh di-serialize secara eksplisit, tanpa mengganggu fitur star yang sudah berjalan.

### Bagian yang Saya Kerjakan dan Putuskan Sendiri

Sebelum bertanya ke Claude, saya membaca dulu modul Tutorial 04 di website PBP dan mencoba mengikuti langkah-langkahnya sendiri di VS Code, seperti membuat `register.html` dan `login.html`, menambahkan routing baru di `main/urls.py`, serta menuliskan sendiri view `register`, `login_user`, dan `logout_user` berdasarkan contoh di modul, sebelum menerapkan pola yang sama ke bagian Certification milik saya sendiri yang strukturnya tidak persis sama dengan contoh di modul. Saya juga yang menguji sendiri satu per satu perilaku setiap peran secara manual di browser menggunakan beberapa akun berbeda yang saya buat sendiri, sebelum menyadari ada kejanggalan pada logika otorisasi awal dan baru menanyakannya ke Claude. Pembuatan Group `Editor` melalui halaman `/admin/` beserta penambahan akun ke group tersebut juga saya lakukan sendiri, mengikuti hint yang diberikan pada soal tugas.

Saya memutuskan sendiri untuk berkonsultasi dengan asisten dosen mengenai field `FORM_PASSWORD`, dan setelah mendapat konfirmasi boleh dipertahankan, saya memutuskan untuk tidak menghapusnya. Saya juga yang menemukan sendiri bahwa JSON endpoint ikut membocorkan data `starred_by` saat memeriksa ulang checklist "API Integrity & Data Security" pada soal tugas, sebelum menanyakannya ke Claude untuk memastikan cara memperbaikinya tanpa merusak fitur star yang sudah berjalan. Untuk fitur kreativitas, saya sendiri yang memilih dua fitur yang ingin ditambahkan (tooltip star dan sort) dari beberapa opsi yang didiskusikan, dengan pertimbangan keduanya bisa diimplementasikan murni menggunakan Django template dan query parameter URL, konsisten dengan pendekatan HTML5/CSS3-first yang saya pakai sejak Tutorial 1. Sebelum melakukan commit, saya selalu menjalankan `python manage.py test` dan mengecek ulang tampilan tiap peran secara manual di browser.

### AI Chat / Prompting Log

1. **Memahami dasar Authentication di Tutorial 04**

   > "Saya ingin mengerjakan Tutorial 04 tentang Authentication, Session, dan Cookies. Bisa dijelaskan dulu konsep dasarnya sebelum saya mulai coding sambil mengikuti modulnya di website PBP?"

   Digunakan untuk memahami alur register, login, logout, session, dan cookie sebelum mulai mengetik kode sendiri di VS Code.

2. **Menemukan kejanggalan logika otorisasi**

   > "Saya perhatikan tombol Tambah/Edit/Hapus jadi tidak muncul sama sekali untuk akun lain, padahal sebelumnya saya kira cukup dibatasi lewat password saja. Apakah memang seharusnya begitu?"

   Digunakan setelah saya menguji sendiri dengan akun lain di browser dan menemukan bahwa logic pengecekan role di view dan template perlu disesuaikan.

3. **Menentukan nasib field password lama**

   > "Field password `FORM_PASSWORD` ini kan fitur tambahan dari Assignment 3 saya. Sekarang sudah ada role-based access control, apakah sebaiknya saya hapus atau tetap dipertahankan?"

   Digunakan untuk mendiskusikan opsi mempertahankan atau menghapus `FORM_PASSWORD`, sebelum akhirnya saya memutuskan berkonsultasi dulu dengan asisten dosen.

4. **Menambahkan automated test untuk role**

   > "Logic role-nya sudah benar. Bisa dibantu buatkan automated test di `tests.py` untuk memastikan keempat peran ini berjalan sesuai fungsinya masing-masing?"

   Digunakan untuk meminta dibuatkan automated test yang mencakup keempat peran beserta fitur CRUD dari Assignment 3.

5. **Menemukan kebocoran data di JSON endpoint**

   > "Saya perhatikan JSON di `/api/certifications/` sekarang ikut menampilkan daftar user yang nge-star. Apakah ini termasuk masalah keamanan, dan bagaimana cara memperbaikinya tanpa merusak fitur star di halaman Certifications?"

   Digunakan setelah saya memeriksa ulang checklist "API Integrity & Data Security" dan menyadari ada field baru yang ikut bocor ke JSON.

6. **Memilih fitur kreativitas**

   > "Dari beberapa ide fitur tambahan yang ditawarkan, saya mau pakai yang tooltip star sama yang sort itu saja."

   Digunakan untuk memilih dua fitur tambahan (tooltip star dan sort) dari beberapa opsi yang ditawarkan.

### Keterbatasan AI dan Pemahaman Saya

Sama seperti tutorial-tutorial sebelumnya, Claude tidak dapat menjalankan project atau melihat tampilan browser saya secara langsung, sehingga saya perlu menjelaskan atau mengirimkan pesan error yang saya temukan sendiri untuk ditelusuri bersama. Saya juga menyadari bahwa memahami role-based access control butuh lebih dari sekadar menyalin kode: saya perlu benar-benar menguji sendiri setiap peran satu per satu di browser dengan akun berbeda untuk memastikan logikanya sudah benar. Temuan soal kebocoran data di JSON endpoint juga mengajarkan saya bahwa menambahkan field baru ke model bisa punya efek samping yang tidak terduga pada bagian lain seperti API, sehingga saya perlu memeriksa ulang setiap checklist tugas secara menyeluruh, bukan hanya memastikan fitur utamanya berjalan. Saya juga belajar pentingnya tidak menyimpan secret seperti `FORM_PASSWORD` langsung di dalam kode yang akan di-push ke repository publik, sehingga saya menggunakan `.env` dan `os.getenv()` baik di `views.py` maupun di `tests.py`.

## Update AI Disclosure: Tutorial 05 & Individual Assignment 5

Pada Tutorial 05 dan Individual Assignment 5, saya menggunakan Claude terutama untuk menyesuaikan contoh kode dari modul (yang memakai section Projects) ke section Certifications milik saya, karena strukturnya sudah cukup berbeda dari contoh modul, seperti adanya role Editor, field `FORM_PASSWORD`, dan fitur sort dari tugas sebelumnya. Ini juga pertama kalinya saya menulis JavaScript di project ini, sehingga saya cukup banyak bertanya soal konsep dasarnya.

### Bagian yang Dibantu AI

Claude membantu menyesuaikan kode toast, `get_certifications_json` yang dirakit manual, `create_certification_ajax`, modal tambah dan hapus, debouncing, serta `escapeHtml` dan `strip_tags` ke struktur project saya. Claude juga membantu menjelaskan penyebab test yang gagal setelah perpindahan ke AJAX, memperbaiki modal yang terpotong, serta membantu menulis kode untuk fitur tambahan Individual Assignment 5 seperti star dan hapus tanpa reload, tombol "Coba lagi", jumlah hasil pencarian, dan `utils.js`.

### Bagian yang Saya Kerjakan dan Putuskan Sendiri

Saya memutuskan sendiri untuk menerapkan Tutorial 05 langsung pada section Certifications, karena section Projects sudah saya hapus dan Certifications memang section yang saya kerjakan di Tugas 3 dan Tugas 4. Di awal pengerjaan, beberapa kode yang diberikan sempat tidak cocok dengan kode yang sudah saya punya, misalnya nama class CSS modal yang berbeda dari yang ada di `style.css` saya, sehingga saya meminta panduan ulang yang benar-benar disesuaikan dengan kode terakhir saya di Tugas 4.

Saya sendiri yang menjalankan `python manage.py test` setelah setiap perubahan dan mengirimkan hasilnya ketika ada yang gagal, termasuk saat menemukan test yang tertulis dua kali. Saya juga yang menemukan sendiri bahwa modal tambah sertifikat terpotong saat mengetes di browser, serta menguji semua fitur secara manual, mulai dari pencarian, sort, tambah dan hapus dengan password benar maupun salah, star dengan akun yang belum dan sudah login, sampai tombol "Coba lagi" dengan cara mematikan server saat halaman masih terbuka. Untuk fitur tambahan, saya memilih mengikuti kombinasi fitur yang direkomendasikan dari beberapa opsi yang ditawarkan, karena semuanya masih berkaitan dengan materi JavaScript dan AJAX minggu ini.

### AI Chat / Prompting Log

1. **Menelusuri test yang gagal**

   > "Bantu periksa kesalahan test aku, dengan error seperti berikut ..."

   Dari sini ditemukan bahwa `test_empty_certification_page` tertulis dua kali di dua class berbeda.

2. **Memperbaiki modal yang terpotong**

   > "Kenapa modul ini tetap kaya kepotong?"

   Digunakan sambil mengirim screenshot browser saat judul modal dan tombol submit tidak terlihat.


### Keterbatasan AI dan Pemahaman Saya

Pada tutorial ini, saya melihat sendiri bahwa AI bisa memberikan kode yang tidak konsisten kalau tidak tahu kondisi terbaru project saya, sehingga saya perlu memastikan kode yang diberikan memang cocok dengan berkas yang ada di laptop saya sebelum menempelkannya. Claude juga tidak bisa melihat tampilan browser saya, jadi masalah seperti modal yang terpotong baru ketahuan setelah saya mengetesnya sendiri. Saya juga menyadari bahwa pindah dari template Django ke JavaScript membuat perlindungan auto-escaping dari Django hilang, sehingga saya perlu menambahkan escaping secara manual. Karena ini pertama kalinya saya menulis JavaScript, saya masih perlu memperdalam konsep Promise, `async`/`await`, dan event listener supaya bisa menjelaskan dan mengembangkan bagian ini secara mandiri, terutama untuk persiapan Kuis 2.
