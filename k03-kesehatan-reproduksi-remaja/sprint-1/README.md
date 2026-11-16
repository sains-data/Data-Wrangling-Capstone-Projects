# Kunci Sprint 1 — Kasus 03 Kesehatan reproduksi remaja

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 3
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 13 / 13 |
| Baris mentah di berkas data | 374 |
| Baris Silver | 235 (5 seri, 3 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 12 aturan: 12 lolos, 0 peringatan |
| Waktu `python pipeline.py` | ±1.8 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 13 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (2 JSON, 1 catatan unduhan, 2 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| Pembaca WHO GHO (2 CSV, 2 JSON) | `src/ekstraksi/who_gho.py` | kolom nilai dikenali dari akhiran `_N/_NL/_NU`; kolom `DIM_*` utuh |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 3 calon anomali dengan alasan |
| Profil seri pembanding (3 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 18 sel kosong: 18 belum_ada, 0 batas_lama, 0 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 3 outlier, 0 patahan seri, 2 patahan wilayah, 0 galat input |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 2 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 4 pasangan selisih, 0 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 2 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Kelompok umur `var1353` (K-003).** Judul JSON: "Angka Kelahiran Pada Perempuan Usia 15-19 Tahun". Seri BPS
   hanya 15–19 (umur dicatat sebagai cakupan seri, rincian `total`); pembanding WHO yang sebanding adalah
   rincian `umur=15-19`, bukan baris 10–14 atau gabungan.
2. **Satuan ketika metadata BPS diam (K-007).** `var.unit` dan kolom satuan CSV kosong. Satuan ditetapkan
   `per_1000_perempuan_seumur` dari tiga bukti: definisi baku indikator yang sama di metadata WHO, nama WDI,
   dan besaran angkanya (puluhan). Satu satuan dipakai untuk BPS, WDI, dan kedua kelompok umur WHO, karena
   penyebutnya selalu perempuan pada kelompok umur yang sama (69 baris BPS dikoreksi).
3. **KB BPS bukan ukuran yang sama dengan WHO (K-009).** Penyebut `SDGFPALL` adalah permintaan KB total; judul
   `var1394` tidak menyebut penyebutnya, dan angka BPS Indonesia jauh di bawah WHO pada tahun yang sama.
   Pasangan P3 tetap dihitung selisihnya di Sprint 2 dengan kategori *definisi*, bukan dianggap galat.
4. **Panel dua titik survei (K-005, K-013).** Hanya 2012 dan 2017; Kalimantan Utara 2012 `belum_ada`,
   Kalimantan Timur 2012→2017 ditandai `patahan_wilayah` karena angka 2012 masih mencakup Kalimantan Utara.
   Tahun antarsurvei tidak diisi; uji patahan seri tidak dapat dilakukan dengan dua titik.
5. **WHO dan BPS tidak punya tahun bersama (K-014).** WHO angka kelahiran remaja tidak punya 2012 dan 2017;
   P2 punya 0 tahun beririsan, jadi perbandingan di Gold memakai tahun terdekat dengan penanda.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Menulis umur BPS di rincian (`umur=15-19`) alih-alih sebagai cakupan seri; pemilihan pasangan di Gold lalu
  mencocokkan rincian yang sama persis.
- Satuan dengan kelompok umur di namanya (`per_1000_perempuan_15_19`), dengan konsekuensi baris WHO 10–14
  perlu satuan sendiri atau seri terpisah.
- Kode umur WHO apa adanya (`Y15T19`) asalkan kamus kodenya tertulis di data dictionary.
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
