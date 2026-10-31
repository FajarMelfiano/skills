---
name: prompt-engineering
description: Merancang prompt yang efektif untuk model AI: konteks, peran, constraint, format output, contoh, dan iterasi. TRIGGER: butuh prompt, buatkan prompt, prompt yang bagus, instruksi untuk AI, system prompt.
---

# Prompt Engineering

## Purpose

Mengubah keinginan yang samar menjadi instruksi yang bisa dieksekusi model secara andal: konteks cukup, batasan eksplisit, format output terdefinisi, dan strategi iterasi saat hasil belum tepat.

## Workflow

1. **Definisikan tugas atomik.** Satu prompt = satu pekerjaan yang jelas. Jika tugas punya 3 output berbeda, buat 3 prompt atau 1 prompt dengan 3 bagian output eksplisit.
2. **Tulis konteks yang dibutuhkan saja.** Sertakan: latar belakang, audiens, dan materi acuan. Buang konteks yang tidak mengubah output — noise menurunkan kualitas.
3. **Tetapkan peran & sudut pandang.** Awali dengan peran yang relevan ("Bertindaklah sebagai editor teknis...") agar nada dan kedalaman tepat.
4. **Rumuskan constraint eksplisit.** Nyatakan: batasan panjang, bahasa, format, hal yang dilarang, dan kriteria kualitas. Constraint implisit ("yang bagus") tidak bisa dieksekusi.
5. **Spesifikasikan format output.** Berikan struktur/skema yang diinginkan, termasuk contoh output ideal (few-shot) untuk tugas yang kompleks atau bergaya khusus.
6. **Atur penanganan ketidakpastian.** Instruksikan model untuk bertanya/menyatakan tidak tahu daripada mengarang saat informasi kurang.
7. **Iterasi terukur.** Uji prompt, identifikasi satu kegagalan dominan per iterasi, perbaiki instruksi spesifiknya, uji ulang. Jangan ubah 5 hal sekaligus.

## Output Contract

- Prompt final yang siap pakai, lengkap dan mandiri.
- Catatan singkat: untuk apa prompt ini dan asumsi konteksnya.
- Jika diminta: 1-2 contoh output yang diharapkan.

## Contoh Trigger

- "Buatkan prompt untuk AI yang bisa meringkas hasil rapat."
- "Prompt seperti apa yang bagus untuk brainstorming ide konten?"
- "Perbaiki prompt ini agar outputnya konsisten."

## Operating Rules

- Prompt harus bisa dipahami tanpa penjelasan lisan tambahan.
- Hindari instruksi bertentangan; jika ada trade-off, nyatakan prioritasnya eksplisit.
- Jangan meminta model melakukan hal di luar kemampuannya lalu menyalahkan output.
- Simpan prompt yang berhasil dipakai ulang sebagai pola, bukan ditulis ulang dari nol tiap kali.
