---
name: data-analysis
description: Analisis data terstruktur: pahami dataset, identifikasi pola dan anomali, hitung statistik ringkas, rekomendasikan visualisasi. TRIGGER: analisis data, analisis angka, olah data, insight dari data, tren data, statistik.
---

# Data Analysis

## Purpose

Mengubah data mentah menjadi insight yang bisa ditindaklanjuti lewat alur analisis yang disiplin: pahami struktur data, ukur kualitasnya, temukan pola, lalu komunikasikan temuan dengan jujur tentang keterbatasannya.

## Workflow

1. **Inventarisasi data.** Identifikasi sumber, format, jumlah baris/kolom, rentang waktu, dan definisi tiap kolom. Tulis asumsi yang dipakai.
2. **Cek kualitas.** Periksa missing values, duplikat, outlier, inkonsistensi tipe/format, dan rentang nilai yang tidak masuk akal. Laporkan temuan kualitas data sebelum analisis.
3. **Statistik deskriptif.** Hitung ukuran yang relevan: count, mean/median, min/max, distribusi, tren waktu, atau perbandingan antar segmen. Pilih metrik yang menjawab pertanyaan, bukan sekadar yang mudah dihitung.
4. **Cari pola & anomali.** Identifikasi tren, musiman, korelasi, segmen yang menonjol, dan outlier. Bedakan pola yang kuat dari noise.
5. **Uji interpretasi.** Untuk tiap temuan, tanyakan: apakah didukung data yang cukup? Adakah penjelasan alternatif? Apakah korelasi disalahartikan sebagai kausalitas?
6. **Rekomendasikan visualisasi.** Usulkan chart yang tepat per temuan (tren → line, komposisi → bar/pie, distribusi → histogram, perbandingan → grouped bar). Satu chart, satu pesan.
7. **Susun narasi.** Sajikan: temuan utama → bukti angka → implikasi → rekomendasi langkah. Akhiri dengan batasan analisis.

## Output Contract

- Ringkasan temuan utama (3-7 poin) dengan angka pendukung.
- Catatan kualitas data dan asumsi yang dipakai.
- Rekomendasi visualisasi per temuan penting.
- Pernyataan batasan: apa yang tidak bisa disimpulkan dari data ini.

## Contoh Trigger

- "Analisis data penjualan 6 bulan terakhir, cari polanya."
- "Dari angka survei ini, insight apa yang bisa diambil?"
- "Bandingkan performa tiap cabang berdasarkan data ini."

## Operating Rules

- Jangan memanipulasi atau membuang outlier tanpa alasan yang dinyatakan eksplisit.
- Korelasi bukan kausalitas: jangan klaim sebab-akibat tanpa dasar.
- Angka penting (total, rata-rata, persen) harus bisa dilacak ke perhitungannya.
- Jika data tidak cukup untuk menjawab, katakan terus terang dan sebut data tambahan yang dibutuhkan.
