# Skills

Koleksi skill untuk diimport ke Cue by Manus (dan agen lain yang mendukung import skill dari GitHub).

Tiap folder berisi satu skill, dengan `SKILL.md` sebagai instruksinya. `INDEX.md` adalah indeks kurasi untuk routing cepat; sisanya bisa dicari dari nama folder / isi `SKILL.md`.

## Cara import ke Cue / Manus

1. Buka **Skills → + Add → Import from GitHub**
2. Tempel URL repo ini: `https://github.com/FajarMelfiano/skills`
3. Audit dulu skill yang akan dipakai: baca `SKILL.md`-nya sebelum pemakaian pertama, terutama skill yang menjalankan perintah, mengakses jaringan, atau mengubah file.

Catatan: repo ini **private**. Kalau Cue tidak bisa mengimport repo private, ubah repo ini jadi public di Settings GitHub, atau beri akses repo ini ke akun/aplikasi Cue yang dipakai, lalu ulangi import.

## Isi

- Sekitar 2.400+ skill (6.391 file, ~73 MB pada saat push awal, 31 Oktober 2026).
- Sumber utama, sesuai `INDEX.md`:
  - 18 skill resmi Anthropic (`anthropics/skills`)
  - 23 skill kustom
  - 48 skill dari `weisser-dev/awesome-opencode`
  - 2.317 skill dari `FrancoStino/opencode-skills-collection`
  - 5 skill dari `Leonxlnx/taste-skill`
  - 1 skill dari `pbakaus/impeccable` (Apache 2.0)
  - 1 skill dari `vercel-labs/skills` (`find-skills`)
- Skill-skill ini **bukan semuanya karya pemilik repo ini** — atribusi dan lisensi masing-masing tetap milik penulis aslinya. Jangan klaim koleksi ini sebagai karya sendiri.
- 281 kandidat dari koleksi opencode **tidak** ikut di sini karena ditolak skrining keamanan otomatis saat impor awal (pola kredensial, prompt-injection, eksekusi remote, dan sejenisnya).

## Catatan kompatibilitas

- Banyak skill impor memakai format opencode. Kalau sebuah skill merujuk tool yang tidak ada di Cue/Manus, abaikan bagian itu dan pakai tool yang setara di platform tersebut.
- Sebagian skill hanya berupa `SKILL.md` singkat (stub). Itu kondisi apa adanya dari sumbernya, bukan janji kualitas per skill.
- Tidak ada kredensial, token, atau kunci API di repo ini — hasil scan sebelum push: 0 pola token GitHub / AWS / kunci API presisi yang ditemukan.
