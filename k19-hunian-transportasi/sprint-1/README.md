# Kunci Sprint 1 — Kasus 19 Hunian dan transportasi

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 19
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 22 / 22 |
| Baris mentah di berkas data | 4.958 |
| Baris Silver | 1.305 (6 seri, 3 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 11 lolos, 0 peringatan |
| Waktu `python pipeline.py` | ±2.5 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 22 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (8 JSON, 2 catatan unduhan, 8 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 202 calon anomali dengan alasan |
| Profil seri pembanding (1 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 72 sel kosong: 52 belum_ada, 4 batas_lama, 16 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 103 outlier, 3 patahan seri, 2 patahan wilayah, 0 galat input; snapshot ganda dibandingkan (0 nilai berbeda) |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 4 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 0 pasangan selisih, 2 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Hunian layak berganti definisi 2019 (K-012).** `var.note`: sejak 2019 dipakai empat kriteria (luas per kapita,
   air minum layak, sanitasi layak, ketahanan bangunan). Hampir semua provinsi turun lebih dari 20% pada 2018→2019
   (uji patahan: 97% provinsi). Itu patahan definisi, bukan outlier; nilai tidak di-*winsorize* atau dihapus.
2. **Moda dari judul, bukan katalog (K-003).** `var2753` = kapal, `var2754` = pesawat terbang (judul JSON). Bongkar dan
   muat menjadi rincian `arus`, tanpa total buatan; satuannya kilogram (`var.unit` KG).
3. **Cakupan wilayah moda berbeda (K-005).** Statistik kapal tidak memuat DI Yogyakarta (kelima tahun) dan Papua
   Pegunungan (tidak berbatasan laut): 16 sel `tidak_diterbitkan`. Statistik pesawat memuat
   semua provinsi.
4. **Tiga seri di dua snapshot (K-004).** Hunian layak dan kedua seri bongkar muat ada di snapshot 17 dan 20 Oktober;
   nilainya sama (0 beda), snapshot terbaru dipakai.
5. **Hunian layak vs kumuh perkotaan (K-014).** Arah berlawanan dan populasi berbeda (rumah tangga vs penduduk
   perkotaan): P1 konteks, dibandingkan arah perubahannya, bukan selisih.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Mengubah kilogram ke ton di Silver, asalkan satuan ditulis `ton` dan faktornya tercatat.
- Menulis sel kapal DI Yogyakarta dan Papua Pegunungan sebagai `missing` dengan catatan "tidak berlaku".
- Memisahkan seri hunian layak menjadi dua seri (sebelum dan sesudah 2019), asalkan titik sambungnya ditandai.
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
