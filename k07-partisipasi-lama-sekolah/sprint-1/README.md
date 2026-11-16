# Kunci Sprint 1 — Kasus 07 Partisipasi dan lama sekolah

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 7
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 15 / 15 |
| Baris mentah di berkas data | 24.726 |
| Baris Silver | 4.216 (6 seri, 8 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 12 aturan: 12 lolos, 0 peringatan |
| Waktu `python pipeline.py` | ±3.3 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 15 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (5 JSON, 1 catatan unduhan, 5 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 367 calon anomali dengan alasan |
| Profil seri pembanding (1 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 454 sel kosong: 402 belum_ada, 49 batas_lama, 0 tidak_diterbitkan, 3 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 262 outlier, 9 patahan seri, 27 patahan wilayah, 0 galat input; 8.167 baris kabupaten/kota dikeluarkan |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 4 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 1 pasangan selisih, 1 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 4 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Seri mana yang perguruan tinggi (K-003).** Katalog memberi `var303` dan `var1443` kode 4.3.1. `turvar` `var303`
   hanya SD, SMP, dan SM, jadi kodenya dikoreksi ke target 4.1. APK perguruan tinggi hanya dari `var1443`
   (kelompok umur acuan 19–23 tahun menurut `var.note`).
2. **Satuan APK sendiri (K-007).** APK menghitung siswa semua umur dibagi penduduk usia jenjang, sehingga bisa
   melebihi 100 (APK SD sampai di atas 120). Satuannya `persen_apk` dengan rentang sah 0–250, terpisah dari `persen`
   yang dibatasi 0–100.
3. **Kabupaten/kota dikeluarkan (K-005).** Berkas HLS memuat provinsi, kabupaten/kota, dan Indonesia sekaligus:
   8.167 baris kabupaten/kota tidak masuk Silver provinsi, dan aturan validasi menjaganya.
4. **Kelompok umur `var2685` tumpang tindih (K-006).** 15–64 mencakup tiga kelompok lain, jadi tidak ada total buatan;
   deret yang diprofilkan adalah 15–64.
5. **Pergantian definisi APK 2007 dan satu sel missing (K-012, K-013).** Mulai 2007 APK mencakup paket A/B/C
   (`var.note`). Aceh 2005 tidak ada di ketiga jenjang tanpa catatan penerbit: satu-satunya sel `missing`
   (3 sel), tidak diisi.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Menyimpan kabupaten/kota HLS di tabel terpisah (bukan Silver provinsi), asalkan jumlah barisnya dicatat.
- Satu satuan `persen` untuk semua dengan rentang validasi khusus APK, asalkan aturan rentang tidak menolak APK > 100.
- Memprofilkan kelompok umur 15–24 alih-alih 15–64 untuk `var2685`, asalkan alasannya tertulis.
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
