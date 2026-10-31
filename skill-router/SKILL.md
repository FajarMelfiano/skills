---
name: "skill-router"
description: "Memilih dan memuat skill yang relevan dari ~/workspace/skills untuk sebuah tugas. Trigger: setiap tugas substantif — sebelum mengerjakan, jalankan router ini agar skill yang tepat aktif otomatis."
---

# Skill Router

## Purpose
Memastikan setiap tugas dikerjakan dengan skill yang tepat dari perpustakaan
`~/workspace/skills`, bukan dari hafalan. Router ini adalah jawaban atas
"skill aktif otomatis saat agen mengerjakan sesuatu".

## Workflow
1. Pecah tugas menjadi 2–4 sudut query:
   - (a) kata kunci tugas apa adanya,
   - (b) domain/bidang (mis. "desain web", "riset", "presentasi"),
   - (c) jenis output (mis. "website", "laporan", "slide"),
   - (d) sinonim Bahasa Inggris dari (a)–(c).
2. Panggil `muse.skill_search` untuk tiap sudut (maks 3 query per panggilan).
3. Kumpulkan kandidat. Baca `SKILL.md` dari kandidat yang deskripsinya
   benar-benar cocok dengan maksud tugas — bukan sekadar mirip kata.
4. Muat SEMUA skill yang relevan. Tidak ada batas artifisial 1–2 skill;
   untuk tugas besar, 10+ skill yang aktif itu normal dan diharapkan.
5. Abaikan kandidat yang hanya cocok sebagian kata tapi tidak cocok maksud.
6. Jika ragu antara dua skill yang mirip, baca keduanya sekilas lalu pilih
   yang scope-nya paling pas.

## Output Contract
- Daftar skill yang dimuat, masing-masing dengan satu baris alasan
  ("dipakai untuk ...").
- Sampaikan daftar ini secara transparan saat mulai mengerjakan.

## Operating Rules
1. Jalankan router untuk setiap tugas substantif. Obrolan ringan tidak perlu.
2. Jangan mengarang isi skill — baca `SKILL.md`-nya sebelum mengklaim bisa.
3. Jika tidak ada skill yang cocok, kerjakan langsung dan pertimbangkan
   membuat skill baru (lihat skill `skill-creator`).
4. Skill resmi (mis. dari Anthropic) dan skill kustom diperlakukan setara —
   yang menentukan adalah kecocokan, bukan sumber.
5. **Just-in-time loading:** router boleh dijalankan ulang kapan saja di
   tengah fase. Kebutuhan baru muncul di tengah jalan (mis. tiba-tiba perlu
   deploy) → cari & muat skill yang relevan DULU, baru lanjut kerja.
