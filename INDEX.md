# Skill Index — ~/workspace/skills

Total: 2419 skill.
- 18 resmi Anthropic (GitHub anthropics/skills)
- 23 kustom (dibuat untuk user: 20 domain + skill-router, phased-execution, skill-importer)
- 48 dari weisser-dev/awesome-opencode (44 lolos skrining + 4 lolos review manual)
- 2317 dari FrancoStino/opencode-skills-collection (lolos skrining; 281 ditolak — lihat bawah)
- 5 dari Leonxlnx/taste-skill (2026-10-18, dari rekomendasi TikTok @shad_ai_dev)
- 1 dari pbakaus/impeccable (2026-10-18, dari rekomendasi TikTok @shad_ai_dev; Apache 2.0)
- 1 dari vercel-labs/skills (2026-10-29, atas permintaan Fajar: find-skills)

Tabel di bawah ini adalah skill KURASI (sinyal tertinggi) untuk routing cepat.
Untuk sisanya, andalkan `muse.skill_search` — itulah cara router menemukan mereka.

## Catatan impor massal (2026-10-10)
- Sumber: awesome-opencode (48 skill, duplikat antar-subdir diatasi) dan
  opencode-skills-collection (2644 kandidat → 2317 diimpor, 46 duplikat/nama-kembar dilewati).
- 281 kandidat DITOLAK oleh skrining keamanan otomatis (pola: kredensial,
  prompt-injection, eksekusi remote, dsb). Sebagian kemungkinan false positive
  (mis. panduan security yang membahas pola serangan); sebagian adalah
  ancaman nyata (contoh: fork bomb di loki-mode). Jangan impor buta —
  review manual dulu via skill `skill-importer`.
- Banyak skill impor memakai format opencode; jika sebuah skill merujuk tool
  yang tidak ada di sini, abaikan bagian itu dan pakai tool yang setara.

## Skill sistem (cara kerja agen)
- **skill-router** — playbook memilih & memuat skill yang relevan per tugas.
- **phased-execution** — aturan fase P0→P4 + verifikasi + loop perbaikan.
- **skill-importer** — impor skill baru dari repo GitHub dengan skrining.
- **antislop** — filter anti-AI-slop: SELALU dimuat (mode during) untuk SEMUA kerja UI/visual/copy/responsive/aksesibilitas/komentar kode (WAJIB untukku dan OpenCode, perintah Fajar 2026-10-17; sub-skill: antislop-ui, antislop-copywriting, antislop-human, antislop-layoutmobile, antislop-code).

## Skill resmi (anthropics/skills, GitHub)
| Skill | Kegunaan singkat |
|---|---|
| academy-guide | Panduan gaya belajar / kursus |
| algorithmic-art | Seni generatif algoritmik |
| brand-guidelines | Membuat/menerapkan brand guidelines |
| canvas-design | Desain visual di kanvas |
| claude-api | Memakai Claude API |
| discernment-nudge | Nudge pengambilan keputusan |
| doc-coauthoring | Co-authoring dokumen |
| docx | Baca/tulis file Word |
| frontend-design | Desain frontend |
| internal-comms | Komunikasi internal (pengumuman, memo) |
| mcp-builder | Membangun MCP server |
| pdf | Baca/tulis file PDF |
| pptx | Baca/tulis file PowerPoint |
| slack-gif-creator | Membuat GIF untuk Slack |
| theme-factory | Membuat tema visual |
| web-artifacts-builder | Membangun web artifact |
| webapp-testing | Testing aplikasi web |
| xlsx | Baca/tulis file Excel |

## Skill kustom — produk & web
| Skill | Kegunaan singkat |
|---|---|
| brainstorming | Ideasi terstruktur (SCAMPER, clustering) |
| product-planning | PRD mini: scope, user, success criteria |
| ux-flow | User flow, journey map, wireframe teks |
| web-design | Prinsip desain web modern |
| frontend-build | Bangun kode frontend |
| backend-api | Desain REST API |
| database-design | Desain skema database |
| copywriting-id | Copywriting Bahasa Indonesia |
| seo-basics | SEO dasar |
| accessibility | Checklist aksesibilitas |
| landing-page | Struktur & anatomi landing page |

## Skill kustom — riset, tulis, kode
| Skill | Kegunaan singkat |
|---|---|
| deep-research | Metodologi riset & sintesis |
| data-analysis | Analisis data & insight |
| presentation-design | Desain slide presentasi |
| technical-writing | Dokumentasi teknis |
| prompt-engineering | Merancang prompt efektif |
| code-review | Review kode |
| debugging | Debugging sistematis |
| verification | Verifikasi & acceptance criteria |
| project-plan | Rencana fase P0/P1/P2 |

## Anti-slop premium (rekomendasi TikTok 2026-10-18, video @shad_ai_dev)
Lapisan desain taste di atas skill `antislop` (wajib tetap dimuat duluan, mode
during). Dari video "Three anti AI slop skills": TasteSkill.dev, Impeccable.style,
Awesome Design.md (sudah ada sebagai `design-md-reference` dari
VoltAgent/awesome-design-md sejak 2026-10-17 — tidak perlu diimpor ulang).
| Skill | Kegunaan singkat |
|---|---|
| impeccable | "The missing design vocabulary for agents" (Paul Bakaus, Apache 2.0): 24+ command desain (/impeccable craft|shape|polish|audit|bolder|quieter...), 61+ rule deterministik pendeteksi AI-slop (gradient ungu, side-tab, bounce-easing...), /impeccable init menulis PRODUCT.md agar desain konsisten antar sesi |
| design-taste-frontend (sudah ada) | Skill rasa desain default taste-skill v2 (Leonxlnx) |
| design-taste-frontend-v1 | Arsip taste-skill v1 (pakai hanya bila proyek bergantung pada v1) |
| design-taste-frontend-v2-experimental | Arsip taste-skill v2 eksperimental dial-driven (sudah usang vs default) |
| imagegen-frontend-web | Generate reference image desain web premium per-section untuk diberikan ke agen coding |
| imagegen-frontend-mobile | Generate reference image layar aplikasi mobile (iOS/Android) untuk agen coding |
| brandkit | Generate brand-guidelines board, logo system, identity deck |
| design-md-reference (sudah ada) | Library DESIGN.md per produk web (VoltAgent/awesome-design-md): warna, tipografi, spacing produk nyata sebagai visual language |

## Routing cepat (kata kunci → skill)
- ide, brainstorm, opsi, stuck, "kasih ide" → brainstorming
- produk, fitur, PRD, scope → product-planning, project-plan
- alur, flow, navigasi, journey → ux-flow
- web, website, tampilan, UI, desain web → web-design, frontend-design, ux-flow, web-artifacts-builder, impeccable, design-taste-frontend
- kode frontend, HTML, CSS, komponen → frontend-build
- API, backend, endpoint → backend-api
- database, tabel, skema, model data → database-design
- teks marketing, headline, CTA → copywriting-id
- SEO, meta, ranking → seo-basics
- aksesibilitas, disabilitas, kontras → accessibility
- landing page → landing-page, copywriting-id, web-design
- riset, cari info, kumpulkan data → deep-research
- analisis, statistik, pola → data-analysis
- presentasi, slide, PPT → presentation-design, pptx
- dokumentasi, README, panduan → technical-writing
- prompt → prompt-engineering
- review kode → code-review
- bug, error, rusak → debugging
- verifikasi, QA, cek hasil, "apakah sudah benar" → verification
- lagu, request lagu, playlist → brainstorming, product-planning, ux-flow, web-design, frontend-build, backend-api, database-design
- PDF → pdf | Word → docx | Excel → xlsx
- tema, brand → theme-factory, brand-guidelines
- test web → webapp-testing
