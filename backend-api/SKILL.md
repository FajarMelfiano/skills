---
name: backend-api
description: Merancang REST API: endpoint, skema JSON request/response, error handling standar, dan versioning. Trigger: pengguna butuh API/backend, atau berkata "buatkan API-nya", "endpoint untuk ...", "rancang backend".
---

# Backend API

## Purpose

Merancang REST API yang konsisten dan mudah dipakai: daftar endpoint
lengkap dengan method dan path, skema JSON request/response, format error
yang standar, serta strategi versioning dan autentikasi. Output-nya adalah
kontrak API yang bisa langsung diimplementasikan.

## Workflow

1. **Identifikasi resource.** Daftarkan entitas utama dari kebutuhan
   (contoh: users, songs, playlists). Satu resource = satu kata benda jamak.
2. **Desain endpoint.** Untuk tiap resource tulis CRUD + aksi khusus.
   Ikuti konvensi: `GET /resources`, `GET /resources/:id`,
   `POST /resources`, `PATCH /resources/:id`, `DELETE /resources/:id`.
3. **Skema JSON.** Untuk tiap endpoint tulis contoh request body dan
   response body. Tandai field wajib vs opsional, sertakan tipe data.
4. **Standarkan error.** Gunakan format error seragam:
   `{ "error": { "code": "not_found", "message": "..." } }` dengan
   HTTP status yang tepat (400, 401, 403, 404, 409, 422, 500).
5. **Auth & versioning.** Tentukan skema auth (mis. Bearer JWT) dan
   endpoint mana yang butuh auth. Tetapkan versioning via path
   (`/v1/...`) sejak awal.
6. **Aturan main.** Tulis: format pagination (`?page&limit` + meta),
   filtering/sorting, rate limit, dan idempotency untuk POST penting.

## Output Contract

- Tabel endpoint: Method | Path | Auth | Deskripsi.
- Contoh JSON request & response untuk tiap endpoint utama.
- Katalog error code + kapan dipakai.
- Keputusan auth, versioning, pagination dalam 1 bagian ringkas.

## Operating Rules

- Gunakan kata benda jamak untuk path; kata kerja hanya untuk aksi khusus
  (`POST /playlists/:id/play`).
- Jangan kembalikan stack trace / detail internal di response error.
- Setiap response list wajib punya pagination; tanpa kecuali.
- Status code harus tepat: jangan pakai 200 untuk error.
- Minta konfirmasi sebelum menambah endpoint di luar CRUD standar.
