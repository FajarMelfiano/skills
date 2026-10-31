---
name: database-design
description: Merancang skema database: tabel, relasi, indexing, dan normalisasi praktis tanpa over-engineering. Trigger: pengguna butuh desain database/model data, atau berkata "rancang databasenya", "tabelnya apa saja", "skema DB".
---

# Database Design

## Purpose

Merancang skema database relasional yang praktis: tabel dan kolom yang
tepat, relasi antar tabel, index untuk query cepat, dan normalisasi
seperlunya tanpa over-engineering. Output-nya siap diterjemahkan ke
migration/SQL.

## Workflow

1. **Daftar entitas.** Ekstrak kata benda dari kebutuhan menjadi entitas
   (User, Song, Playlist...). Maksimal 8–10 tabel untuk satu run.
2. **Tentukan kolom.** Untuk tiap tabel tulis: nama kolom, tipe data,
   nullable/tidak, default, dan mana primary key. Gunakan `id` UUID/integer
   konsisten di semua tabel.
3. **Petakan relasi.** Tentukan one-to-many vs many-to-many. Untuk
   many-to-many buat tabel pivot (contoh: `playlist_songs`).
   Tambahkan foreign key dengan aturan hapus yang jelas.
4. **Normalisasi praktis.** Hilangkan duplikasi data yang jelas
   (mis. alamat jangan diulang di tiap order). Berhenti di 3NF kecuali
   ada alasan kuat.
5. **Rencanakan index.** Tambahkan index untuk: primary key (otomatis),
   foreign key, kolom yang sering di-filter/sort (email, created_at),
   dan unique constraint (email, slug).
6. **Tulis DDL ringkas.** Sajikan CREATE TABLE per tabel + relasi dalam
   SQL standar yang mudah dibaca.

## Output Contract

- Daftar tabel + kolom (tipe, constraint) dalam format ringkas.
- Diagram relasi dalam teks (mis. `users 1──* playlists`).
- Daftar index & unique constraint dengan alasannya.
- SQL DDL siap pakai untuk tiap tabel.

## Operating Rules

- Nama tabel jamak snake_case (`songs`), kolom snake_case (`created_at`).
- Selalu sertakan `created_at`/`updated_at`; soft delete (`deleted_at`)
  hanya jika diminta.
- Jangan buat tabel "serbaguna" (EAV); pecah jadi tabel eksplisit.
- Jika ragu antara normalisasi vs denormalisasi, pilih normalisasi dulu.
- Tanyakan database target (Postgres/MySQL/SQLite) sebelum tulis DDL final.
