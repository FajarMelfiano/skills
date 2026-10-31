---
name: frontend-build
description: Membangun frontend (HTML/CSS/JS): struktur file, komponen reusable, dan best practice agar kode rapi dan mudah dirawat. Trigger: pengguna minta kode tampilan web, atau berkata "buatkan halamannya", "coding frontend-nya", "bikin komponen".
---

# Frontend Build

## Purpose

Menghasilkan kode frontend yang bersih, terstruktur, dan siap jalan:
struktur file yang jelas, komponen yang reusable, styling konsisten,
dan JavaScript yang mudah dirawat. Fokus pada kualitas kode, bukan
sekadar "bisa tampil".

## Workflow

1. **Rencanakan struktur.** Tentukan struktur file/direktori dulu
   (contoh: `index.html`, `css/`, `js/`, `assets/`) dan daftar komponen
   yang akan dibuat. Tampilkan rencana sebelum menulis kode panjang.
2. **Bangun kerangka HTML.** Tulis HTML semantik (`header`, `main`,
   `section`, `footer`). Satu file = satu tanggung jawab.
3. **Styling sistematis.** Gunakan CSS variables untuk warna/spacing/font.
   Mobile-first dengan media query di breakpoint jelas (mis. 768px).
   Hindari `!important` dan inline style.
4. **Komponen reusable.** Ekstrak pola berulang (tombol, kartu, navbar)
   jadi komponen/kelas yang bisa dipakai ulang, bukan copy-paste.
5. **Interaksi JavaScript.** Tambahkan JS secukupnya: event listener,
   validasi form, toggle UI. Pisahkan data, logika, dan tampilan.
6. **Uji cepat.** Cek: tampil benar di mobile & desktop, tidak ada error
   console, semua tombol/CTA berfungsi, gambar punya alt text.

## Output Contract

- Kode lengkap per file dengan nama file yang jelas.
- CSS memakai variables; tidak ada magic number tanpa komentar.
- Komponen kunci diberi komentar singkat cara pakainya.
- Daftar file yang dibuat + cara menjalankan/membuka hasilnya.

## Operating Rules

- Jangan menulis satu file raksasa; pecah per tanggung jawab.
- Setiap kode yang dihasilkan harus bisa langsung dijalankan/disimpan.
- Jelaskan singkat (2–3 kalimat) sebelum blok kode besar, bukan sesudah.
- Utamakan vanilla HTML/CSS/JS kecuali pengguna minta framework.
- Jangan tambahkan dependensi eksternal tanpa persetujuan pengguna.
- Jika desain belum ada, tawarkan skill web-design dulu.
