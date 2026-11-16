# Kunci Sprint 1 — Kasus 11 Pengangguran

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 11
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 14 / 14 |
| Baris mentah di berkas data | 9.853 |
| Baris Silver | 7.572 (6 seri, 90 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 10 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±2.9 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 14 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (1 JSON, 1 catatan unduhan, 1 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca ILOSTAT (3 CSV, 4 JSON) | `src/ekstraksi/ilostat.py` | CSV SDMX dibaca utuh; dimensi lewat `src/kamus_ilo.py`; `OBS_STATUS` ke kolom `status_obs`; DSD dan dataflow untuk definisi |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 179 calon anomali dengan alasan |
| Profil seri pembanding (5 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 379 sel kosong: 356 belum_ada, 21 batas_lama, 2 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 168 outlier, 10 patahan seri, 10 patahan wilayah, 0 galat input; status ILO B 569 dan U 276 baris di `status_obs` |
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

1. **Tiga jenis periode BPS (K-006).** `turtahun` berisi Tahunan (1986–2004, tanpa 1995), Februari, dan Agustus (sejak
   2005). Dipetakan ke `AAAA` (tahun) dan `AAAA-02` / `AAAA-08` (bulan); Februari dan Agustus tidak dirata-rata di Silver.
   Triwulan ILO (`FREQ` Q) menjadi `AAAA-Q1` / `AAAA-Q3` (triwulan).
2. **BPS lebih tinggi daripada ILO (K-014).** TPT BPS Agustus 1–3,3 poin di atas ILO SDG 8.5.2 pada 18 tahun
   (peringatan validasi). ILO memakai rujukan Agustus (`NOTE_SOURCE`), jadi P1 memasangkan BPS Agustus; selisihnya
   dikategorikan definisi pengangguran, bukan galat. WDI estimasi nasional sama dengan ILO SDG 8.5.2; WDI estimasi
   model (ILOEST) berbeda pada tahun tertentu.
3. **Status ILO (K-005).** `status_obs` B (569 baris, disertai "Break in series") dan U (276
   baris, artinya tidak dijelaskan di paket) disimpan apa adanya; 226 baris ILO tanpa nilai tidak
   masuk Silver.
4. **Kode umur ILO menyimpan klasifikasinya (K-007).** `UNE_DEAP_SEX_AGE_RT` punya 28 kode umur dari empat klasifikasi
   (YTHADULT, AGGREGATE, 10YRBANDS, 5YRBANDS); total 15+ muncul di beberapa klasifikasi. Rincian ditulis dengan
   klasifikasinya (`umur=10YRBANDS_Y15-24`) supaya tidak kembar, dan penjumlahan umur di Gold hanya dalam satu klasifikasi.
5. **Patahan dan sel tidak dicacah (K-005, K-012).** Maluku dan Maluku Utara 2000 `tidak_diterbitkan` (`var.note`).
   Lonjakan serentak 1993→1994, 2000→2001, dan Februari→Agustus 2020 ditandai patahan seri; yang terakhir diduga
   pandemi, dua yang pertama diduga perubahan definisi Sakernas, dicari buktinya di Sprint 2.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Periode Februari/Agustus ditulis `AAAA-S1` / `AAAA-S2`, asalkan bulan acuannya dicatat di data dictionary.
- Memasangkan BPS Februari dengan ILO bila tim menemukan bahwa angka ILO tahun tertentu memakai Februari.
- Menyaring `UNE_DEAP_SEX_AGE_RT` ke satu klasifikasi umur sejak Silver, asalkan jumlah baris yang dibuang dicatat.
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
