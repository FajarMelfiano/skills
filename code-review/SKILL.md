---
name: code-review
description: Review kode sistematis: correctness, readability, keamanan, performa, dan saran perbaikan konkret. TRIGGER: review kode, cek kode, periksa code, code review, tolong lihat kode ini.
---

# Code Review

## Purpose

Menemukan masalah nyata pada kode sebelum merugikan: bug logika, celah keamanan, dan utang keterbacaan — lalu memberi saran perbaikan yang konkret dan bisa langsung diterapkan, bukan komentar samar.

## Workflow

1. **Pahami konteks perubahan.** Baca deskripsi/PR: apa tujuan perubahan, apa yang berubah, dan area mana yang sensitif. Review tanpa konteks menghasilkan komentar noise.
2. **Cek correctness dulu.** Telusuri logika: edge cases, kondisi batas, error handling, dan asumsi implisit. Tanyakan "kapan ini gagal?" untuk tiap fungsi penting.
3. **Cek keamanan.** Cari: input yang tidak divalidasi, kredensial/secrets yang terekspos, injeksi (SQL/command), otorisasi yang terlewat, dan logging data sensitif.
4. **Cek readability & maintainability.** Nama yang jelas, fungsi yang fokus, duplikasi, komentar yang menjelaskan "mengapa" bukan "apa", dan konsistensi gaya dengan codebase.
5. **Cek performa seperlunya.** Soroti hanya masalah nyata (N+1 query, loop boros, alokasi berlebih di hot path). Jangan mikro-optimasi tanpa bukti.
6. **Klasifikasikan temuan.** Tandai tiap temuan: blocker (harus diperbaiki), saran (sebaiknya), nitpick (opsional). Satu temuan = satu lokasi + dampak + saran kode konkret.
7. **Apresiasi yang baik.** Sebutkan bagian yang dikerjakan dengan baik — review bukan daftar celaan.

## Output Contract

- Ringkasan verdict: approve / approve dengan catatan / perlu perbaikan.
- Daftar temuan terklasifikasi (blocker, saran, nitpick), tiap item berisi lokasi, masalah, dampak, dan saran perbaikan konkret (idealnya cuplikan kode).
- Tidak ada komentar tanpa aksi yang jelas.

## Contoh Trigger

- "Review kode Python ini sebelum saya merge."
- "Cek apakah ada masalah keamanan di fungsi ini."
- "Tolong periksa pull request ini."

## Operating Rules

- Kritik kode, bukan penulisnya. Bahasa netral dan profesional.
- Jangan meminta perubahan gaya yang murni preferensi pribadi bila codebase tidak punya aturannya.
- Saran harus realistis dalam cakupan perubahan; jangan meminta refactor besar tanpa alasan blocker.
- Jika konteks kurang untuk menilai, tanyakan dulu sebelum menandai sebagai masalah.
