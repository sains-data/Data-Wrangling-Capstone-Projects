# Kunci Sprint 1 — Kasus 10 Kesetaraan gender

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 10
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 15 / 15 |
| Baris mentah di berkas data | 1.720 |
| Baris Silver | 840 (6 seri, 1 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 10 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±1.9 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 15 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (2 JSON, 1 catatan unduhan, 2 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca ILOSTAT (2 CSV, 3 JSON) | `src/ekstraksi/ilostat.py` | CSV SDMX dibaca utuh; dimensi lewat `src/kamus_ilo.py`; `OBS_STATUS` ke kolom `status_obs`; DSD dan dataflow untuk definisi |
| Pembaca WDI (5 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 49 calon anomali dengan alasan |
| Profil seri pembanding (4 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 74 sel kosong: 64 belum_ada, 8 batas_lama, 0 tidak_diterbitkan, 2 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 47 outlier, 0 patahan seri, 4 patahan wilayah, 0 galat input |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 3 koreksi katalog dengan bukti dari berkas mentah |
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

1. **Dua definisi ILO dibaca dari DSD (K-003).** `SDG_0552` = manajer senior dan menengah (tanpa manajer junior),
   `SDG_T552` = seluruh manajemen (ISCO kategori 1). Angka BPS `var2003` (seluruh lapangan usaha) hampir sama dengan
   T552, jadi T552 pembanding utama (P1) dan 0552 dicatat sebagai selisih definisi (P2).
2. **`OBS_STATUS` disimpan sebagai kolom `status_obs` (K-005).** Kode B selalu disertai `NOTE_INDICATOR` "Break in
   series: Methodology revised" (4 baris), jadi dipakai sebagai penanda patahan. DSD di paket hanya
   merujuk codelist `CL_OBS_STATUS` tanpa daftar artinya; kode yang ditemukan dicatat di `reports/ilostat-status.csv`.
3. **ILO T552 2016 janggal (K-012).** 44,78, padahal 2015 22,38, 2017 27,46, dan BPS 2016 23,6; tidak bertanda B. Nilai
   disimpan apa adanya dan dilaporkan sebagai peringatan; Gold tidak memakainya untuk rekonsiliasi.
4. **Satuan `var2003` (K-007).** Kosong di katalog; ditetapkan persen dari judul, besaran, dan satuan ILO (PT).
5. **Dua provinsi baru hilang 2025 (K-013).** Papua Tengah dan Papua Pegunungan tidak ada di `var2003` 2025: `missing`
   (2 sel), tidak diisi.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Membuang nilai ILO T552 2016 dari Silver sebagai galat sumber, asalkan buktinya (2015, 2017, BPS) tercatat.
- Menyimpan status pengamatan ILO di tabel terpisah alih-alih kolom tambahan, asalkan bisa digabung kembali per kunci.
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
