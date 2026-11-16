# Kunci Sprint 1 — Kasus 20 Hutan, lahan, dan lingkungan

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 20
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 13 / 13 |
| Baris mentah di berkas data | 8.113 |
| Baris Silver | 4.045 (8 seri, 13 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 12 aturan: 9 lolos, 3 peringatan |
| Waktu `python pipeline.py` | ±2.9 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 13 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (4 JSON, 1 catatan unduhan, 4 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 313 calon anomali dengan alasan |
| Profil seri pembanding (3 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 183 sel kosong: 158 belum_ada, 21 batas_lama, 4 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 194 outlier, 0 patahan seri, 18 patahan wilayah, 0 galat input; uji silang HTML vs CSV 0 beda; kolom 2020 tabel tutupan tergeser (peringatan) |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 5 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 3 pasangan selisih, 1 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 2 aturan khas kasus, 3 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Tabel tutupan hutan dari HTML, luas dan persen dipisah (K-002, K-006).** Header bertingkat tahun × tutupan ×
   ukuran (luas ribu ha, %, jumlah). Karena satuannya berbeda, luas dan persen menjadi dua seri
   (`...:luas_ribu_ha`, `...:persen`). Uji silang dengan CSV pratampil: 0 beda.
2. **Kolom 2020 tergeser (K-013).** Pada 2020 banyak provinsi memuat angka provinsi lain (Bengkulu 191,9 mirip Bangka
   Belitung, Bali 5.656,6 padahal luasnya 566,9). Kolom `cek` CSV pratampil menandai hal yang sama ("luas hutan +
   non hutan tidak sama dengan jumlah"). Nilai disimpan apa adanya dan diberi dua peringatan; Gold tidak memakai luas
   2020 sampai disejajarkan ulang.
3. **Identitas dan kode SDG dari judul (K-007).** `var1304` adalah luas penutupan lahan menurut status kawasan
   (15.1.1, bukan 15.3.1); `var588` lahan kritis (15.3.1); `var2532` adalah enam komponen IKLH (berkas `sdg15_iklh`),
   bukan 11.6.2, dan disimpan sebagai rincian `komponen`.
4. **Satuan luas tidak diseragamkan di Silver (K-008).** Ribu hektar (tabel statis, `var1304`), hektar (`var588`),
   km persegi (WDI) disimpan seperti diterbitkan; konversi (1 ribu ha = 10 km2) dikerjakan di Gold.
5. **Jumlah vs rincian (K-012).** DI Yogyakarta 2016 tidak cocok di `var1304` maupun tabel statis (selisih
   -2.874,6 ribu ha), tanda galat di sumber yang sama. Dilaporkan sebagai peringatan, tidak diperbaiki.

## Pilihan lain yang juga sah

- CSV pratampil sebagai sumber Silver tabel tutupan hutan, asalkan HTML tetap dibaca untuk uji silang.
- Menyejajarkan ulang kolom 2020 di Silver bila tim bisa membuktikan urutan baris aslinya, dengan catatan di log.
- Menyeragamkan semua luas ke hektar di Silver, asalkan nilai asli dan faktornya tercatat.
- Menyimpan komponen IKLH sebagai enam seri terpisah alih-alih rincian.
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
