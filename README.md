# Individual Assignment 1: Personal Portfolio Website

Website portofolio pribadi milik **Debora Putri Dion Simamora**, dibuat menggunakan Django sebagai bagian dari tugas mata kuliah Pemrograman Berbasis Platform (CSGE602022), Fakultas Ilmu Komputer, Universitas Indonesia.

**Nama:** Debora Putri Dion Simamora
**NPM:** 2506544126
**Kelas:** PBP A

## Deskripsi Proyek

Website ini merupakan portofolio pribadi statis yang dibangun menggunakan **HTML5 dan CSS3**. Website menampilkan profil, cerita singkat tentang diri saya, serta pengalaman organisasi dan volunteering yang pernah saya ikuti.

Desain visual website menggunakan gaya editorial yang hangat, dengan gradasi warna lembut, wave divider antar-section, serta perpaduan tipografi serif dan aksen tulisan tangan. Warna utama yang digunakan, yaitu terracotta, navy, dan cream, terinspirasi dari warna pada foto profil saya.

## Fitur

Website memiliki beberapa fitur utama:

* **Profile (Hero):** menampilkan nama, program studi, NPM, foto, serta link GitHub, LinkedIn, dan Email dalam bentuk tombol pil. Bagian ini juga menggunakan latar gradasi dan wave divider.
* **About Me:** berisi cerita singkat tentang diri saya dengan layout rata tengah, garis pembatas dekoratif, dan highlight pada beberapa frasa penting.
* **Experience:** menampilkan pengalaman organisasi dan volunteering. Setiap kategori menggunakan animasi marquee dengan arah yang berbeda, foto dokumentasi sebagai latar kartu, serta modal berisi foto dan deskripsi ketika kartu diklik.
* **Navigation & Animation:** terdapat sticky navbar dengan smooth scroll, responsive navigation, serta animasi fade-in ketika section mulai masuk ke area layar.
* **Responsive Design:** layout website disesuaikan agar tetap rapi dan nyaman digunakan pada desktop maupun mobile.

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

## Progres Mingguan

### Tutorial 0 & Tutorial 1

Pada Tutorial 0 dan Tutorial 1, saya melakukan setup project Django dan mulai membuat halaman portfolio sederhana. Saya membuat bagian awal halaman atau hero section menggunakan HTML5 semantik dan CSS3 dengan beberapa teknik dasar seperti Flexbox, Grid, dan custom properties. Setelah itu, project juga saya deploy ke PWS.

### Individual Assignment 1

Pada Individual Assignment 1, saya melanjutkan project dari Tutorial 1 dengan mengembangkan bagian About Me dan menambahkan section Experience. Pada awal pengerjaan, saya mencoba mengikuti struktur dan pola kode dari Tutorial 1 sambil menentukan sendiri isi dan konsep portfolio yang ingin saya buat.

Selama proses pengerjaan, saya mengeksplorasi beberapa referensi portfolio melalui browser dan Pinterest untuk mendapatkan inspirasi mengenai layout, tipografi, kombinasi warna, dan elemen dekoratif. Setelah membandingkan beberapa gaya, saya menentukan arah desain akhir yang menggunakan warna terracotta, navy, dan cream yang terinspirasi dari foto profil saya.

Pada section Experience, saya mengembangkan tampilan pengalaman organisasi dan volunteering dalam kategori Organizations dan Volunteering. Data pengalaman dan foto dokumentasi yang digunakan berasal dari saya sendiri. Saya juga menambahkan beberapa fitur seperti marquee animation, hover effect, dan modal detail untuk membuat section tersebut lebih interaktif.

Dalam proses pengembangan, saya menggunakan Claude sebagai alat bantu untuk memberikan masukan terhadap struktur dan tampilan website serta membantu mengembangkan beberapa bagian HTML dan CSS. Pada implementasi awal, modal dan animasi scroll yang dibantu oleh Claude masih menggunakan JavaScript. Karena saya belum memahami bagian tersebut dengan baik dan implementasinya tidak sesuai dengan requirement tugas yang menggunakan HTML5 dan CSS3, saya meminta alternatif yang tidak menggunakan JavaScript. Modal kemudian menggunakan teknik `:target`, sedangkan animasi scroll menggunakan `animation-timeline: view()` dengan `@supports` sebagai fallback.

Di luar kebutuhan minimum tugas, saya juga menambahkan beberapa fitur seperti sticky navbar dengan smooth scroll, modal detail untuk setiap pengalaman, scroll-linked fade-in animation, gradient blob, dan wave divider antar-section.

## Pertanyaan Reflektif

### Tugas 1

**1. Penggunaan Semantic HTML5**

Saya menggunakan beberapa elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, dan `<footer>`. Saya juga menggunakan `<dl>`, `<dt>`, dan `<dd>` untuk menampilkan informasi seperti NPM dan program studi. Saya memilih elemen-elemen tersebut supaya struktur HTML lebih jelas dan tidak semuanya menggunakan `<div>`. Misalnya, `<header>` digunakan untuk bagian atas halaman, sedangkan `<section>` digunakan untuk memisahkan bagian Profile, About, dan Experience. Menurut saya, penggunaan elemen semantik juga membuat struktur halaman lebih mudah dipahami ketika saya mengembangkan CSS. Saya belum menggunakan `<article>` atau `<aside>` karena konten pada website ini belum membutuhkan elemen tersebut.

**2. Responsive CSS**

Bagian yang paling menantang untuk dibuat responsive adalah hero section dan navbar. Pada hero section, saya perlu mengatur ulang posisi foto dan teks ketika ukuran layar mengecil supaya tampilannya tetap rapi dan urutan kontennya masih nyaman dibaca. Pada navbar, saya mengubah layout menjadi vertikal di layar kecil karena nama saya cukup panjang dan menu bisa terlalu sempit jika tetap dibuat horizontal. Saya beberapa kali mencoba ukuran dan posisi yang berbeda untuk melihat bagaimana tampilannya pada ukuran layar yang berbeda sampai menemukan layout yang menurut saya paling nyaman untuk desktop maupun mobile.

**3. Keterbatasan Static Web**

Karena website ini masih berupa static web, kontennya masih ditulis langsung di HTML. Jadi, ketika saya ingin menambahkan atau mengubah pengalaman, saya harus mengubah kode HTML secara manual. Menurut saya, cara ini masih cukup untuk portfolio sederhana, tetapi akan kurang praktis jika jumlah pengalaman saya semakin banyak. Untuk pengembangan selanjutnya, saya ingin menyimpan data pengalaman menggunakan model Django dan database, sehingga konten dapat dikelola tanpa harus mengubah HTML secara manual setiap kali ada perubahan.

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
