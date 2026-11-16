# Kunci Sprint 1 — Kasus 15 Kemiskinan dan daerah tertinggal

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 15
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 11 / 11 |
| Baris mentah di berkas data | 7.804 |
| Baris Silver | 3.897 (4 seri, 5 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 10 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±2.2 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 11 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (3 JSON, 1 catatan unduhan, 3 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 227 calon anomali dengan alasan |
| Profil seri pembanding (1 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 153 sel kosong: 139 belum_ada, 8 batas_lama, 6 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 150 outlier, 23 patahan seri, 3 patahan wilayah, 0 galat input; 4 pergantian sumber Indeks Desa dari catatan penerbit |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 4 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 1 pasangan selisih, 1 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Semester tidak dirata-rata (K-006).** `var192` tahunan pada 2007–2011, lalu Maret (S1) dan September (S2) sejak
   2012; 2023 hanya Maret. `turtahun` dipetakan ke `periode` `AAAA` / `AAAA-S1` / `AAAA-S2` dengan `jenis_periode` yang
   sesuai, dan aturan validasi menjaga kecocokan keduanya.
2. **WDI = P0 Maret (K-014).** Angka tahunan `SI.POV.NAHC` sama dengan P0 BPS Semester 1 yang dibulatkan satu desimal
   (2020: 9,78 menjadi 9,8; rata-rata dua semester 9,98 tidak cocok). P1 memasangkan S1 dengan tahun WDI
   (19 tahun).
3. **Kode SDG (K-007).** P0 terhadap garis kemiskinan nasional adalah indikator 1.2.1; berkasnya diberi nama
   `sdg10_10_1_1_f` karena dipakai sebagai butir nasional 10.1.1(f). Seri desa butir (c) dan (d) sesuai nama berkas.
4. **Jakarta tanpa desa (K-005).** DKI Jakarta tidak ada di seri desa karena seluruh wilayahnya kelurahan:
   6 sel `tidak_diterbitkan`, bukan missing.
5. **Indeks Desa berganti sumber setiap tahun (K-012).** `var.note`: 2019 Podes 2018 + pemutakhiran, 2020 pemutakhiran
   2020 dengan daftar desa baru, 2021 Pendataan Podes 2021. Perubahan serentak 2019→2020 dan 2020→2021 dikategorikan
   patahan seri, bukan tren.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Periode semester ditulis `AAAA-03` / `AAAA-09` (bulan acuan) dengan `jenis_periode` bulan, asalkan konsisten.
- Menyimpan Jakarta sebagai `missing` dengan catatan "tidak berlaku", asalkan tidak diisi nol.
- Kode SDG katalog 10.1.1 untuk P0, asalkan dicatat bahwa indikatornya 1.2.1.
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
