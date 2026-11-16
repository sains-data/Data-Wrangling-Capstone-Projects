# Kunci Sprint 1 — Kasus 14 Produktivitas dan industri

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 14
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 24 / 24 |
| Baris mentah di berkas data | 4.030 |
| Baris Silver | 1.779 (9 seri, 1 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 11 lolos, 0 peringatan |
| Waktu `python pipeline.py` | ±2.4 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 24 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (5 JSON, 2 catatan unduhan, 5 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca ILOSTAT (3 CSV, 4 JSON) | `src/ekstraksi/ilostat.py` | CSV SDMX dibaca utuh; dimensi lewat `src/kamus_ilo.py`; `OBS_STATUS` ke kolom `status_obs`; DSD dan dataflow untuk definisi |
| Pembaca WDI (5 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 240 calon anomali dengan alasan |
| Profil seri pembanding (5 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 173 sel kosong: 154 belum_ada, 19 batas_lama, 0 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 165 outlier, 0 patahan seri, 7 patahan wilayah, 0 galat input; 2 kunci JSON BPS tak terbaca dilaporkan; snapshot ganda dibandingkan |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 5 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 4 pasangan selisih, 0 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Kunci JSON yang tidak terbaca (K-003).** JSON produktivitas memuat dua kunci `datacontent` sepanjang 10 karakter
   (`1116101150`, `1116101160`) yang kode wilayahnya tidak ada di daftar label; keduanya juga tidak ada di CSV.
   Pembaca tidak membuangnya diam-diam: 2 kunci dilaporkan di `reports/kunci-bps-tak-terbaca.csv`
   dan tidak masuk Silver.
2. **Laju bisa negatif (K-007).** `var1161` dan dua seri ILO 8.2.1 adalah laju pertumbuhan per tahun (`persen_per_tahun`,
   rentang -100 sampai 100), bukan persen 0–100. Uji patahan berbasis perubahan relatif tidak dijalankan untuk laju;
   WDI menerbitkan tingkat (USD PPP 2021), jadi lajunya dihitung di Gold sebelum dibandingkan (P2).
3. **Dua basis ILO bernilai sama, dan ada proyeksi (K-006, K-010).** `SDG_0821` (USD konstan 2015) dan `SDG_B821` (PPP
   2021) punya laju yang sama di semua tahun. Keduanya memuat 2026–2027, yang dicatat sebagai proyeksi dan tidak ikut
   rekonsiliasi.
4. **Provinsi Papua baru (K-005).** `var.note` `var1161`: laju 2024 provinsi pemekaran dihitung pada provinsi induk karena
   data tenaga kerja provinsi baru baru ada 2024; sel 2023–2024 provinsi baru `batas_lama`. 2024 dan 2025 angka sementara.
5. **Satu ukuran di `var1214` (K-008).** Judulnya hanya proporsi nilai tambah manufaktur terhadap PDB (bagian pertama 9.2.1);
   tidak ada ukuran kedua untuk dipisah. Dasar harga BPS dan WDI tidak disebut, jadi P3 menunggu pemeriksaan di Sprint 2.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik untuk kunci yang terbaca); yang penting hanya satu format masuk Silver.
- Menyimpan hanya satu dari dua basis ILO karena lajunya sama, asalkan kesamaannya dibuktikan dan dicatat.
- Satuan laju ditulis `persen` dengan rentang validasi khusus, asalkan nilai negatif tidak ditolak.
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
