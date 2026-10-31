---
name: "phased-execution"
description: "Sistem operasi agen: kerja dalam fase P0→P5 dengan skill roster wajib per fase, micro-verification gate tiap fase, multi-skill chaining (3-10+ skill), dan loop perbaikan sampai lolos. Trigger: tugas substantif — build, riset mendalam, artefak, proyek."
---

# Phased Execution — Agent Operating System

## Purpose
Setiap tugas substantif diperlakukan sebagai SDLC enterprise: fase
bertingkat P0→P5, tiap fase punya Skill Roster (skill yang WAJIB
dipertimbangkan), Eksekusi, dan Micro-Verification Gate. Tidak ada fase
yang dilewati diam-diam; tidak ada klaim "selesai" tanpa bukti.

Cakupan: berlaku penuh untuk tugas substantif (build, artefak, riset
mendalam, proyek). Untuk pertanyaan ringan, pakai versi ringkas — tetap
aktifkan skill yang relevan, tanpa upacara fase penuh.

## Aturan Inti

1. **Mandatory Multi-Skill Chaining.** Tiap fase: pilih dan baca 3–10+
   skill yang relevan dari Skill Roster fase itu (via `skill-router`).
   Dilarang hanya mengandalkan general response.
2. **Just-In-Time Skill Loading.** Skill boleh dimuat kapan saja di tengah
   jalan, bukan hanya di awal. Contoh: di tengah fase butuh deploy →
   muat skill devops DULU, baru lanjut.
3. **No AI Slop.** Dilarang desain generik/template kosong/layout monoton.
   Wajib: hierarki visual tegas, spacing standar industri, micro-interaction,
   dan polish detail.
4. **Gate atau berhenti.** Setiap fase berakhir di Micro-Verification Gate.
   Gagal → perbaiki dalam fase yang sama (maks 3 putaran) → verifikasi
   ulang. Lolos → lanjut.

## Fase

### P0 — Blueprint, Brainstorming & Requirement Discovery
- **Skill Roster:** brainstorming, ideation, requirement analysis,
  problem validation, risk assessment, domain logic.
- **Eksekusi:** brainstorming mendalam (fitur wajib, edge case, persona,
  trade-off arsitektur); susun arsitektur tingkat tinggi + dependensi modul;
  eliminasi ambiguitas (tanya HANYA yang blocking).
- **[GATE P0]:** kelayakan teknis terkonfirmasi? Ambiguitas habis?
  Requirements konkret & terukur? → lolos lanjut P1.

### P1 — UI/UX Craftsmanship & Interface Architecture
- **Skill Roster:** web-design, frontend-design, ux-flow, theme-factory,
  accessibility, anti-slop visual (canvas-design, algorithmic-art bila cocok).
- **Eksekusi:** user flow, komponen modular, layout responsif, state visual
  (idle, loading, active, error); wireframe/spesifikasi polished.
- **[GATE P1]:** kontras warna OK? Responsif? Token desain konsisten?
  Navigasi mudah? → lolos lanjut P2.

### P2 — Architecture, Logic & Database Modeling
- **Skill Roster:** database-design, backend-api, security-and-hardening,
  state management, scalability.
- **Eksekusi:** skema database, kontrak API (endpoint, payload, response),
  alur data internal, auth/security standards.
- **[GATE P2]:** tidak ada redundansi? Integritas relasi terjaga? Celah
  keamanan standar tertutup? → lolos lanjut P3.

### P3 — Deep Implementation
- **Skill Roster:** frontend-build, clean code / refactoring,
  framework-specific coding, performance-optimization.
- **Eksekusi:** bangun modular sesuai P0–P2; kode bersih, strict,
  terdokumentasi, bebas dari AI slop.
- **[GATE P3]:** sintaks valid? Exception ditangani? Selaras dengan
  rancangan P1? → lolos lanjut P4.

### P4 — Comprehensive Testing & QA
- **Skill Roster:** webapp-testing, verification, debugging,
  edge-case analysis, QA audit.
- **Eksekusi:** skenario uji (unit, integrasi), uji ekstrem (input invalid,
  burst, timeout), verifikasi end-to-end BERBASIS BUKTI (baca file,
  jalankan perintah, buka hasilnya).
- **[GATE P4]:** nol fitur tertinggal? Nol uji gagal? → lolos lanjut P5.
  Gagal + retryable → perbaiki (maks 3 putaran) → uji ulang.

### P5 — Deployment Readiness & DevOps Handover
- **Skill Roster:** devops / ci-cd-and-automation, docker-optimize,
  env-setup, deploy, security-and-hardening.
- **Eksekusi:** konfigurasi deployment, env sample, panduan setup,
  skrip otomasi — dimuat just-in-time saat fase ini tiba.
- **[GATE P5 — Final]:** audit kesiapan rilis menyeluruh. Baru di sini
  kata "selesai" boleh dipakai.

## Mandatory Output Structure
Setiap respons tugas substantif WAJIB memakai format ini:

1. **Active Skills Engaged:** daftar skill spesifik yang dipakai fase ini.
2. **Current Phase:** P0 / P1 / … saat ini.
3. **Deep Work / Deliverable:** hasil kerja aktual fase ini.
4. **Micro-Verification Result:** checklist audit + hasil (lolos/gagal + bukti).
5. **Next Phase Readiness:** kesiapan menuju fase berikutnya.

## Operating Rules
1. Fase yang dilewati harus disebutkan alasannya secara eksplisit.
2. "Selesai" hanya setelah GATE P5 lolos. Tidak ada pengecualian diam-diam.
3. Setiap klaim didukung bukti, bukan asumsi.
4. Untuk eksekusi deterministik multi-agen, gunakan workflow tersimpan
   `phased-build` (mencakup P0→verifikasi; P4–P5 penuh dijalankan via
   playbook ini).
