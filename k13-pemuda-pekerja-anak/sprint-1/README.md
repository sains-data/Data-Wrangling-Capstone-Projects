# Kunci Sprint 1 — Kasus 13 Pemuda dan pekerja anak

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 13
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 16 / 16 |
| Baris mentah di berkas data | 1.426 |
| Baris Silver | 720 (7 seri, 6 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 10 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±1.9 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 16 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (2 JSON, 1 catatan unduhan, 2 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca ILOSTAT (3 CSV, 4 JSON) | `src/ekstraksi/ilostat.py` | CSV SDMX dibaca utuh; dimensi lewat `src/kamus_ilo.py`; `OBS_STATUS` ke kolom `status_obs`; DSD dan dataflow untuk definisi |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 72 calon anomali dengan alasan |
| Profil seri pembanding (5 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 58 sel kosong: 44 belum_ada, 8 batas_lama, 0 tidak_diterbitkan, 6 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 55 outlier, 0 patahan seri, 4 patahan wilayah, 0 galat input |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 2 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 2 pasangan selisih, 1 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Kelompok umur pekerja anak berbeda (K-003).** BPS 5–17 tahun (judul `var2658`). Kedua seri ILO hanya memuat
   umur 15–17 (`AGE_CLDVERSION_Y15-17`), walaupun definisi di DSD mencakup 5–17; WDI 7–14 tahun (2000–2010). P2
   dikategorikan selisih definisi, dan P3 konteks karena tahunnya tidak tumpang tindih dengan BPS (bukan missing).
2. **Dua definisi ILO 8.7.1 (K-006).** A871 = kegiatan ekonomi; B871 = kegiatan ekonomi atau pekerjaan rumah tangga
   ≥ 21 jam (umur 5–14). Untuk umur 15–17 keduanya sama, sehingga B871 2009 = A871 2009; aturan validasi menjaga
   B871 ≥ A871.
3. **NEET 15–24 di tiga sumber (K-014).** Kelompok umur sama; BPS dan ILO (olahan Sakernas yang sama) berdekatan kecuali
   2020 (24,28 vs 21,80, peringatan validasi).
4. **Pekerja anak BPS kehilangan provinsi 2024–2025 (K-013).** DKI Jakarta dan DI Yogyakarta (2024–2025), Kepulauan
   Riau dan Papua Barat Daya (2025) tidak ada tanpa catatan: `missing` (6 sel), tidak diisi.
5. **Berkas ILO pendek ditangani pembaca yang sama (K-002).** B871 hanya 3 baris; tidak ada kasus khusus di pembaca.
   Judul `var2658` menyebut "Persentase dan Jumlah", tetapi berkas hanya berisi persentase.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Menyimpan umur ILO sebagai cakupan seri (karena hanya satu nilai) alih-alih rincian, asalkan tercatat di docs/seri.csv.
- Tidak memasukkan B871 ke Gold karena sama dengan A871 untuk umur 15–17, asalkan kesamaannya tercatat.
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
