---
name: project-plan
description: Menyusun rencana proyek bertahap P0/P1/P2: tujuan tiap fase, kriteria selesai, dependensi, dan risiko. TRIGGER: butuh rencana proyek, susun plan, roadmap, fase pengerjaan, breakdown tugas, P0 P1 P2, planning.
---

# Project Plan

## Purpose

Mengubah tujuan besar menjadi rencana eksekusi bertahap yang realistis: fase P0/P1/P2 dengan tujuan jelas per fase, kriteria selesai yang terukur, dependensi yang dipetakan, dan risiko yang diantisipasi — sehingga progres bisa dilacak dan diverifikasi.

## Workflow

1. **Rumuskan tujuan akhir.** Tulis definisi sukses dalam 1-2 kalimat yang terukur. Tanpa ini, fase-fase hanya jadi daftar keinginan.
2. **Petakan cakupan & batasan.** Daftar yang termasuk dan yang eksplisit TIDAK termasuk. Asumsi, dependensi eksternal, dan kendala (waktu, resource) dicatat di awal.
3. **Breakdown menjadi fase.**
   - **P0 — Fondasi:** hal yang harus ada agar proyek bisa berjalan (setup, riset, keputusan arsitektur). Tanpa P0, fase lain tidak bisa mulai.
   - **P1 — Inti:** deliverable utama yang mewujudkan nilai proyek. Ini fase terbesar.
   - **P2 — Penguatan:** polish, edge cases, dokumentasi, optimasi. Hanya dikerjakan setelah P1 selesai dan terverifikasi.
4. **Detailkan tiap fase.** Per fase tulis: tujuan, daftar tugas konkret, estimasi usaha, owner/PIC bila ada, dan kriteria selesai (definition of done) yang bisa dicek.
5. **Petakan dependensi.** Tandai tugas yang memblokir tugas lain. Susun urutan kritis (critical path) — keterlambatan di sini menggeser semuanya.
6. **Identifikasi risiko.** Untuk tiap fase: apa yang bisa gagal, seberapa besar dampaknya, dan rencana mitigasi/cadangan.
7. **Tetapkan checkpoint verifikasi.** Setiap akhir fase ada gerbang: kriteria selesai dicek (pakai pola verification) sebelum lanjut ke fase berikutnya. Fase tidak "dianggap selesai".

## Output Contract

- Tujuan akhir + cakupan (termasuk/tidak termasuk).
- Rencana P0/P1/P2: tujuan, tugas, estimasi, kriteria selesai per fase.
- Peta dependensi dan critical path.
- Daftar risiko + mitigasi, dan jadwal checkpoint verifikasi.

## Contoh Trigger

- "Susun rencana proyek pembuatan aplikasi X dalam fase P0/P1/P2."
- "Buatkan roadmap untuk peluncuran produk ini."
- "Breakdown tugas besar ini menjadi rencana bertahap."

## Operating Rules

- Jangan memasukkan tugas P2 ke P1 agar terlihat progres; urutan fase melindungi kualitas.
- Estimasi harus jujur: pecah tugas yang estimasinya lebih dari 1-2 hari menjadi sub-tugas.
- Kriteria selesai harus terukur, bukan "sudah dikerjakan" atau "hampir jadi".
- Rencana adalah dokumen hidup: saat realitas berubah, perbarui rencana — jangan biarkan basi.
