---
name: ux-flow
description: Merancang alur pengguna (user flow), journey map, dan wireframe dalam bentuk teks terstruktur sebelum coding/desain visual. Trigger: pengguna membahas alur aplikasi, navigasi, atau berkata "gambarkan alurnya", "user flow-nya gimana", "bikin wireframe".
---

# UX Flow

## Purpose

Memetakan perjalanan pengguna dari awal sampai tujuan dalam bentuk teks
terstruktur yang mudah dibaca: user flow langkah demi langkah, journey map
dengan emosi pengguna, dan wireframe tekstual per layar. Tujuannya agar
alur logis dan tidak ada jalan buntu sebelum masuk ke desain atau kode.

## Workflow

1. **Tentukan skenario.** Pilih satu alur utama (happy path) + maksimal
   2 alur alternatif/error. Tulis tujuan pengguna dalam satu kalimat.
2. **Petakan user flow.** Tulis langkah bernomor dari entry point sampai
   goal. Tandai decision point dengan format `IF ... THEN ... ELSE ...`.
3. **Susun journey map.** Untuk tiap tahap tulis: aksi pengguna, apa yang
   dipikirkan, emosi (skala 1–5 + emoji), dan pain point.
4. **Wireframe tekstual.** Untuk tiap layar kunci, deskripsikan dalam
   blok teks: nama layar, elemen dari atas ke bawah (header, konten,
   CTA), dan aksi yang tersedia.
5. **Cek jalan buntu.** Verifikasi: setiap error/empty state punya jalan
   keluar, setiap form punya validasi, dan pengguna selalu tahu langkah
   berikutnya.
6. **Ringkas temuan.** Tulis 3–5 insight: di mana pengguna paling mungkin
   drop-off dan apa perbaikannya.

## Output Contract

- Satu skenario utama + alur alternatif dalam langkah bernomor.
- Journey map berbentuk tabel teks: Tahap | Aksi | Pikiran | Emosi | Pain point.
- Wireframe tekstual per layar kunci (maksimal 6 layar).
- Daftar cek jalan buntu: tiap masalah + solusinya.
- Ditulis murni teks/markdown, tanpa gambar.

## Operating Rules

- Satu skill run = satu skenario. Jangan campur banyak alur sekaligus.
- Maksimal 3–5 langkah per tahap journey; pecah jika terlalu panjang.
- Selalu sertakan empty state, error state, dan loading state.
- CTA utama hanya satu per layar; jika ada dua, beri hirarki jelas.
- Gunakan bahasa pengguna sehari-hari, bukan istilah sistem.
- Tawarkan: "mau saya lanjutkan ke desain visual (web-design)?"
