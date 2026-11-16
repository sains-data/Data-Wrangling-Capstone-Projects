# Kunci Sprint 1 — Kasus 05 Layanan dan tenaga kesehatan

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 5
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 13 / 13 |
| Baris mentah di berkas data | 3.193 |
| Baris Silver | 1.722 (7 seri, 24 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 11 lolos, 0 peringatan |
| Waktu `python pipeline.py` | ±2.3 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 13 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (3 JSON, 1 catatan unduhan, 3 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WHO GHO (4 CSV, 2 JSON) | `src/ekstraksi/who_gho.py` | kolom nilai dikenali dari akhiran `_N/_NL/_NU`; kolom `DIM_*` utuh |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 62 calon anomali dengan alasan |
| Profil seri pembanding (4 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 76 sel kosong: 72 belum_ada, 4 batas_lama, 0 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 47 outlier, 11 patahan seri, 4 patahan wilayah, 0 galat input |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 4 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 2 pasangan selisih, 2 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Satuan dan profesi `var1477` (K-006, K-007).** `var.note` menulis "(per 100.000 penduduk)"; WHO memakai per
   10.000. Satuan disimpan seperti diterbitkan di Silver dan diseragamkan di Gold (faktor 0,1). Sepuluh profesi di
   `turvar` menjadi rincian `profesi=<kode>` dengan kamus di `src/konfigurasi.py` (`PROFESI`); tidak ada baris total.
2. **Deret yang diprofilkan (K-004).** Karena `var1477` tidak punya total, profil, grid, dan uji patahan dijalankan
   untuk tiga profesi yang punya pembanding WHO: dokter umum, perawat, dan bidan (label `var1477 [profesi=...]`).
3. **Kode SDG butir nasional (K-008).** Nama tabel BPS `sdg3_3_8_1_a` dan `sdg3_3_8_2_a` menunjukkan butir (a):
   unmet need dan kepemilikan JKN bukan indikator global 3.8.1 (indeks UHC) dan 3.8.2 (pengeluaran katastrofik).
   Pasangan P3 dan P4 karena itu konteks.
4. **JKN baru terbit 2022 (K-005).** Tahun sebelum 2022 tidak masuk grid dan tidak diimputasi ke belakang; aturan
   validasi menolak baris JKN sebelum 2022. Sel 2022 empat provinsi Papua baru `belum_ada`.
5. **Dua patahan seri (K-012).** Unmet need 2021→2022 (lebih dari 70% provinsi naik lebih dari 20%) dan kepadatan
   bidan 2016→2017 ditandai patahan seri, nilai tidak diubah; catatan metodenya dicari di Sprint 2.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Menyeragamkan kepadatan ke per 10.000 sudah di Silver, asalkan nilai asli dan faktornya tercatat (kolom tambahan
  atau log) dan aturan validasi menjaga satu satuan.
- Memprofilkan semua sepuluh profesi, atau hanya dokter umum, asalkan pilihannya tertulis.
- Kode profesi berbeda (misalnya `DOKTER_UMUM`) asalkan kamusnya ada di data dictionary.
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
