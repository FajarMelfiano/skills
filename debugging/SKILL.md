---
name: debugging
description: Debugging sistematis: reproduksi masalah, bangun hipotesis, isolasi penyebab, verifikasi perbaikan. TRIGGER: ada bug, error, tidak jalan, gagal, kenapa begini, debug, troubleshooting, fix.
---

# Debugging

## Purpose

Menyelesaikan bug dengan metode, bukan tebakan: pastikan masalah bisa direproduksi, persempit penyebab lewat hipotesis yang teruji, perbaiki akar masalahnya, lalu buktikan perbaikan benar-benar bekerja.

## Workflow

1. **Pahami gejalanya.** Kumpulkan fakta: pesan error persis, langkah reproduksi, kapan mulai terjadi, dan apa yang berubah terakhir (kode, config, environment, data).
2. **Reproduksi.** Buat kasus reproduksi minimal dan andal. Jika tidak bisa direproduksi, catat kondisi yang dicurigai dan cari pola kemunculannya. Jangan perbaiki hal yang belum bisa direproduksi.
3. **Bangun hipotesis.** Daftar 2-4 kemungkinan penyebab, urutkan dari yang paling mungkin/mudah diuji. Satu hipotesis = satu prediksi yang bisa diobservasi.
4. **Uji satu per satu.** Lakukan eksperimen terkecil yang bisa membuktikan/menggugurkan tiap hipotesis: log tambahan, isolasi komponen, bisect perubahan terakhir. Catat hasil tiap uji.
5. **Isolasi akar masalah.** Persempit hingga ke penyebab tunggal yang menjelaskan semua gejala. Bedakan akar masalah dari gejala dan dari faktor pemicu.
6. **Perbaiki akarnya.** Terapkan fix minimal yang menyasar penyebab, bukan menambal gejala. Pertimbangkan: apakah fix menimbulkan efek samping? Perlukah regression test?
7. **Verifikasi.** Jalankan ulang kasus reproduksi → pastikan hilang. Jalankan skenario terkait → pastikan tidak ada regresi. Dokumentasikan penyebab + fix singkat.

## Output Contract

- Ringkasan: gejala → akar masalah → perbaikan yang diterapkan.
- Bukti verifikasi: apa yang dites dan hasilnya.
- Jika belum selesai: hipotesis yang tersisa dan langkah uji berikutnya.

## Contoh Trigger

- "Aplikasi saya error saat login, tolong debug."
- "Kenapa fungsi ini tidak jalan padahal kemarin bisa?"
- "Bantu cari penyebab data tidak tersimpan."

## Operating Rules

- Jangan mengubah banyak hal sekaligus saat menguji hipotesis; satu variabel per eksperimen.
- Jangan menebak fix lalu berharap berhasil — setiap perbaikan harus punya alasan kausal.
- Prioritaskan reproduksi di atas teori: log dan fakta mengalahkan asumsi.
- Jika stuck > 3 hipotesis gagal, mundur selangkah: verifikasi ulang asumsi dasar (environment, versi, data).
