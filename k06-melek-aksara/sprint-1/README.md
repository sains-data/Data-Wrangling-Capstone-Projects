# Kunci Sprint 1 — Kasus 06 Melek aksara

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 6
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 9 / 9 |
| Baris mentah di berkas data | 12.860 |
| Baris Silver | 5.762 (3 seri, 9 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 10 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±2.4 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 9 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (2 JSON, 1 catatan unduhan, 2 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 133 calon anomali dengan alasan |
| Profil seri pembanding (1 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 107 sel kosong: 96 belum_ada, 11 batas_lama, 0 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 88 outlier, 0 patahan seri, 6 patahan wilayah, 0 galat input; uji silang HTML vs CSV 0 beda; 645 sel kosong tabel rinci tidak masuk Silver |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 1 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 3 pasangan selisih, 0 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Tabel rinci dibaca dari HTML, diuji silang dengan CSV (K-002, K-003).** JSON tabel statis berisi tabel Excel
   dalam HTML yang di-*escape*, tersusun tiga blok bertumpuk (perkotaan, perdesaan, gabungan) dengan header
   bertingkat. Pembaca di `src/ekstraksi/bps.py` (`baca_json_statis`) meratakannya. Hasilnya cocok sel demi sel
   dengan CSV pratampil (`reports/uji-silang-statis.csv`: 0 beda). Kolom `cek` di CSV kosong
   untuk tabel ini dan tidak dipakai.
2. **Total kanonik = `var1458` (K-005).** Tabel ringkas punya kode wilayah dan menjadi angka total per provinsi ×
   tahun; tabel rinci dipakai untuk rincian daerah dan jenis kelamin serta untuk tahun 2009–2013.
3. **Dua tabel BPS berbeda hanya pada 2017 (K-006).** Semua provinsi berbeda tipis (sampai 0,21 poin), tahun lain
   identik. Selisihnya dilaporkan sebagai peringatan, tidak disamakan paksa.
4. **DKI Jakarta tanpa perdesaan (K-007).** Tabel rinci Jakarta hanya enam rincian. Aturan validasi memeriksa
   susunan rincian konsisten per provinsi, bukan memaksa sembilan.
5. **WDI meneruskan angka BPS (K-010).** Nilai `SE.ADT.LITR.ZS` untuk 2014–2020 sama dengan `var1458`, tetapi
   tersimpan dengan derau *float32* (95.120002746582). Nilai disimpan apa adanya; pembulatan untuk perbandingan
   dilakukan di Gold.

## Pilihan lain yang juga sah

- Memakai CSV pratampil sebagai sumber Silver tabel rinci, asalkan HTML tetap dibaca untuk uji silang.
- Menjadikan total tabel rinci sebagai angka kanonik (lebih panjang, 2009–2025), asalkan selisih 2017 dicatat.
- Label rincian asli (`daerah=Perkotaan`) alih-alih kode `URBAN`/`MALE`, asalkan satu kamus dipakai.
- z-score dengan ambang tertulis, atau IQR dengan pengali lain, selama konsisten dan dicatat.
- SQLite atau PostgreSQL alih-alih DuckDB.

## Urutan merge yang disarankan (integrator)

1. `src/ekstraksi/` (komponen ekstraksi) — semua tes ekstraksi lolos.
2. `src/silver/metadata.py` dan `src/konfigurasi.py` (transformasi) — satuan dan SDG.
3. `src/silver/bangun.py` (transformasi) — Silver lolos pemeriksa skema.
4. `src/silver/profil.py`, `grid.py`, `anomali.py`, `pembanding.py` (pembersihan).
5. `src/gold/` (integrasi) dan `src/validasi/`, `tests/` (validasi).

Setelah setiap merge: `python pipeline.py && python -m pytest -q` di `main`.

## Belum dikerjakan di Sprint 1

Panel Gold provinsi × periode × indikator, selisih di tabel rekonsiliasi, dan Gold di SQL (Sprint 2);
arsip WDI (bila kasus punya pembanding WDI), pandas vs DuckDB/Dask, laporan akhir (Sprint 3).
