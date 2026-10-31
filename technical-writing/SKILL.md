---
name: technical-writing
description: Penulisan dokumentasi teknis yang jelas: README, panduan pengguna, referensi API, dan struktur dokumen. TRIGGER: tulis dokumentasi, buat README, dokumentasikan, panduan penggunaan, docs, user manual.
---

# Technical Writing

## Purpose

Menghasilkan dokumentasi teknis yang bisa langsung dipakai pembaca: akurat, terstruktur, bebas jargon yang tidak dijelaskan, dan selalu menjawab "bagaimana cara memakainya" sebelum "bagaimana cara kerjanya".

## Workflow

1. **Kenali pembaca.** Tentukan profil: pemula, pengguna rutin, atau developer. Catat prasyarat pengetahuan mereka. Satu dokumen = satu tingkat pembaca.
2. **Tentukan cakupan.** Daftar pertanyaan yang harus dijawab dokumen. Apa pun di luar daftar masuk ke dokumen terpisah atau bagian "Lihat juga".
3. **Susun kerangka.** Urutan baku: ringkasan (apa & untuk siapa) → mulai cepat (minimal steps to value) → panduan per fitur → referensi detail → troubleshooting → FAQ.
4. **Tulis dengan contoh nyata.** Setiap konsep abstrak ditemani contoh konkret yang bisa dijalankan/dicoba. Contoh kode harus lengkap dan teruji logikanya, bukan potongan khayalan.
5. **Gunakan bahasa presisi.** Kalimat pendek, suara aktif, satu instruksi per langkah bernomor. Hindari "mudah", "cukup", "hanya" — yang mudah bagi penulis belum tentu bagi pembaca.
6. **Tambahkan navigasi.** Daftar isi untuk dokumen panjang, heading deskriptif, dan tautan silang antar bagian. Pembaca harus bisa melompat, bukan dipaksa membaca berurutan.
7. **Verifikasi & rapikan.** Uji setiap langkah/instruksi seolah-olah pembaca baru. Periksa konsistensi istilah, ejaan, dan format kode.

## Output Contract

- Dokumen dengan struktur: ringkasan → mulai cepat → detail → troubleshooting.
- Contoh yang konkret dan dapat dieksekusi/diikuti.
- Daftar prasyarat di awal dokumen.
- Bahasa Indonesia, istilah teknis asing dipertahankan bila baku.

## Contoh Trigger

- "Tuliskan README untuk proyek ini."
- "Buatkan panduan penggunaan fitur X untuk pemula."
- "Dokumentasikan API ini."

## Operating Rules

- Jangan mendokumentasikan perilaku yang belum diverifikasi dari sumber/kode aslinya.
- Setiap langkah prosedural harus bisa diikuti tanpa pengetahuan yang tidak tertulis di dokumen.
- Istilah yang sama harus dipakai konsisten di seluruh dokumen; daftarkan di glosarium bila perlu.
- Pisahkan tutorial (belajar sambil praktik), panduan how-to (selesaikan tugas), dan referensi (cari fakta) — jangan campur ketiganya dalam satu alur.
