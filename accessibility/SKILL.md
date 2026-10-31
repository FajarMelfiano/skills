---
name: accessibility
description: Checklist aksesibilitas praktis: kontras warna, navigasi keyboard, ARIA, dan HTML semantik agar web bisa dipakai semua orang. Trigger: pengguna membahas aksesibilitas/a11y, atau berkata "bikin ramah disabilitas", "cek aksesibilitas", "keyboard navigation".
---

# Accessibility

## Purpose

Memastikan antarmuka web bisa digunakan semua orang, termasuk pengguna
keyboard-only dan pembaca layar (screen reader). Berupa checklist praktis
yang bisa langsung diterapkan pada kode yang sedang dikerjakan.

## Workflow

1. **Audit cepat.** Telusuri halaman/komponen dan catat masalah dalam
   4 kategori: visual, keyboard, screen reader, dan konten.
2. **Perbaiki kontras & visual.** Pastikan rasio kontras teks ≥ 4.5:1
   (teks besar ≥ 3:1). Jangan sampaikan info hanya lewat warna;
   tambahkan ikon/teks. Sediakan mode fokus yang terlihat jelas.
3. **Amankan navigasi keyboard.** Semua elemen interaktif harus bisa
   dijangkau dengan Tab dalam urutan logis. Pastikan ada visible focus
   indicator, tombol bisa di-Enter/Space, dan modal menjebak fokus
   (focus trap) + bisa ditutup dengan Esc.
4. **Lengkapi ARIA & semantik.** Gunakan HTML semantik dulu
   (`<button>`, `<nav>`, `<label>`); ARIA hanya sebagai pelengkap.
   Tambahkan `aria-label` untuk tombol ikon, `aria-expanded` untuk
   accordion, dan `role="alert"` untuk pesan error penting.
5. **Rapikan konten.** Setiap input punya `<label>` terasosiasi.
   Error form dijelaskan dengan teks, bukan cuma warna merah.
   Animasi bisa dimatikan via `prefers-reduced-motion`.
6. **Verifikasi.** Uji tanpa mouse (keyboard saja) dan simulasikan
   screen reader. Tandai tiap item checklist: lolos / perlu perbaikan.

## Output Contract

- Hasil audit: daftar temuan per kategori + tingkat keparahan.
- Perbaikan konkret per temuan (kode sebelum → sesudah bila perlu).
- Checklist final dengan status tiap item.
- Hal yang sengaja dikecualikan + alasannya.

## Operating Rules

- HTML semantik selalu didahulukan; ARIA bukan pengganti tag yang benar.
- Jangan hapus outline fokus CSS tanpa mengganti dengan indikator lain.
- Setiap gambar informatif wajib alt text; gambar dekoratif pakai alt="".
- Uji dengan keyboard sungguhan, bukan sekadar teori.
- Aksesibilitas bukan fitur tambahan — perlakukan sebagai bug jika gagal.
