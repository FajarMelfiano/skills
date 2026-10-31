---
name: web-design
description: Prinsip desain web modern: layout, tipografi, warna, spacing, dan visual hierarchy untuk tampilan yang rapi dan profesional. Trigger: pengguna membahas desain tampilan web/UI, atau berkata "desainkan tampilannya", "bikin mockup", "warnanya gimana", "kurang menarik".
---

# Web Design

## Purpose

Memberikan arahan desain antarmuka web yang modern dan konsisten:
sistem layout, pilihan tipografi, palet warna, skala spacing, dan hirarki
visual. Output-nya berupa design direction + spesifikasi konkret yang bisa
langsung dipakai membangun frontend.

## Workflow

1. **Pahami konteks.** Identifikasi jenis halaman (landing, dashboard,
   form, dll), target user, dan mood yang diinginkan (playful, formal,
   premium, minimalis).
2. **Tentukan design tokens.** Tetapkan: 1 font heading + 1 font body
   (atau satu font dua weight), palet 5 warna (primary, secondary,
   accent, netral terang, netral gelap), dan skala spacing berbasis 8px.
3. **Susun layout.** Pilih pola layout per section (hero, fitur, testimoni,
   CTA, footer). Tentukan grid: 12 kolom desktop, 1 kolom mobile.
4. **Bangun visual hierarchy.** Untuk tiap section tentukan: satu pesan
   utama, urutan baca (F/Z pattern), ukuran heading vs body, dan
   penempatan CTA.
5. **Aturan komponen.** Spesifikasikan tombol (primary/secondary/ghost),
   kartu, input form, dan navigasi: radius, padding, warna state
   (default, hover, disabled).
6. **Review konsistensi.** Cek: kontras cukup, maksimal 2 font, spacing
   konsisten kelipatan 8, tidak ada lebih dari 3 warna aksen.

## Output Contract

- Design tokens: font, palet warna (kode hex), skala spacing.
- Deskripsi tiap section halaman dari atas ke bawah + pola layout-nya.
- Spesifikasi komponen kunci (tombol, kartu, form, nav).
- Daftar "jangan" (anti-pattern) spesifik untuk desain ini.
- Siap diteruskan ke skill frontend-build tanpa info hilang.

## Operating Rules

- Mobile-first dalam berpikir, tapi spesifikasikan juga tampilan desktop.
- Jangan pakai lebih dari 2 keluarga font dalam satu proyek.
- Setiap warna harus punya peran; warna dekoratif tanpa fungsi dilarang.
- White space adalah fitur: jangan takut ruang kosong.
- Selalu sebutkan kode hex, bukan "biru muda" saja.
- Jika pengguna minta "yang keren", tanyakan 1 preferensi gaya dulu.
