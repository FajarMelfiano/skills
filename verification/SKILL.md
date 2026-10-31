---
name: verification
description: Verifikasi sebelum pekerjaan dinyatakan selesai: acceptance criteria, checklist bukti, dan definisi "done" yang ketat. TRIGGER: verifikasi, cek hasil, QA, quality check, pastikan sudah benar, definisi selesai, acceptance criteria.
---

# Verification

## Purpose

Menjadi gerbang kualitas terakhir: tidak ada pekerjaan yang dinyatakan selesai sebelum memenuhi kriteria penerimaan yang eksplisit, dengan bukti yang bisa diperiksa ulang — bukan sekadar "kelihatannya sudah benar".

## Workflow

1. **Tetapkan acceptance criteria.** Turunkan dari permintaan awal menjadi kriteria yang terukur dan bisa dicek ya/tidak. Jika permintaan awal samar, tulis interpretasi yang dipakai dan minta konfirmasi bila berisiko.
2. **Susun checklist bukti.** Untuk tiap kriteria, tentukan bukti apa yang menunjukkannya terpenuhi (output tool, file, screenshot, test result, kutipan). Tanpa bukti = belum terverifikasi.
3. **Eksekusi pemeriksaan.** Jalankan setiap cek dan catat hasilnya: lolos/gagal, beserta buktinya. Jangan mengandalkan ingatan "tadi sudah dicek".
4. **Uji sisi negatif.** Selain "apakah yang diminta ada", cek juga: tidak ada efek samping, tidak ada file sampah tertinggal, tidak ada asumsi yang bocor ke output.
5. **Keputusan.** Semua kriteria lolos → nyatakan selesai dengan ringkasan bukti. Ada yang gagal → kembali perbaiki, lalu verifikasi ulang dari checklist (bukan dari ingatan).
6. **Loop sampai hijau.** Ulangi perbaiki → verifikasi hingga semua checklist lolos. Batasi loop yang tak berujung: jika 3x gagal di titik yang sama, eskalasikan dengan laporan akar masalah.

## Output Contract

- Daftar acceptance criteria + status tiap item (lolos/gagal) + bukti singkat.
- Keputusan akhir: SELESAI atau BELUM (dengan item yang gagal dan rencana perbaikan).
- Tidak ada klaim "selesai" tanpa checklist yang hijau semua.

## Contoh Trigger

- "Verifikasi apakah pekerjaan ini sudah selesai dengan benar."
- "Cek hasil kerja saya sebelum diserahkan ke klien."
- "Buatkan acceptance criteria untuk fitur ini."

## Operating Rules

- Kriteria harus ditulis SEBELUM pekerjaan diverifikasi, bukan disesuaikan agar lolos.
- Bukti harus spesifik dan bisa direproduksi pihak lain.
- "Hampir benar" = gagal. Tidak ada nilai parsial dalam verifikasi.
- Verifikasi menilai hasil, bukan usaha: proses yang panjang tidak menggantikan bukti.
