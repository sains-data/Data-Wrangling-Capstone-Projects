# Kunci Sprint 1 — Kasus 18 Energi: listrik dan bahan bakar memasak

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 18
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 9 / 9 |
| Baris mentah di berkas data | 10.041 |
| Baris Silver | 4.889 (4 seri, 7 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 11 lolos, 0 peringatan |
| Waktu `python pipeline.py` | ±2.9 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 9 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (2 JSON, 1 catatan unduhan, 2 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 337 calon anomali dengan alasan |
| Profil seri pembanding (2 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 450 sel kosong: 421 belum_ada, 15 batas_lama, 7 tidak_diterbitkan, 7 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 307 outlier, 7 patahan seri, 22 patahan wilayah, 0 galat input; uji silang HTML vs CSV 0 beda; 385 sel berkoma desimal |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 2 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 2 pasangan selisih, 0 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Tabel bahan bakar dibaca dari HTML (K-002).** JSON tabel statis berisi HTML Excel dengan header tahun × jenis
   bahan bakar; tahunnya tidak rapat (2001, lalu 2007–2021) dan dibaca dari header. Uji silang dengan CSV
   pratampil: 0 beda.
2. **Dua pemisah desimal dalam satu tabel (K-003).** 385 sel (antara lain seluruh
   kolom 2016) memakai koma desimal (`77,94`), sisanya titik. Ribuan di tabel statis dipisah spasi, jadi koma tanpa
   titik dibaca sebagai desimal. Tanpa uji silang, kolom itu hilang tanpa galat.
3. **Kategori bersih untuk Gold (K-008).** Listrik dan gas/elpiji = bersih; minyak tanah, arang/briket, kayu = tidak
   bersih (minyak tanah dikecualikan menurut sourceNote WDI, pedoman WHO); "lainnya" (termasuk rumah tangga yang
   tidak memasak) = tidak ditentukan. Pemetaan ini ada di `KATEGORI_BAHAN_BAKAR` dan diuji aturan validasi.
4. **Listrik PLN bukan semua listrik (K-014).** `var87` hanya penerangan utama dari PLN dan menghitung rumah tangga;
   WDI menghitung penduduk dengan semua sumber listrik. Selisih P1 dikategorikan definisi.
5. **Susenas 2000–2002 dan sel "-" (K-005, K-012, K-013).** Provinsi yang tidak dicacah (Aceh 2000–2001, Maluku 2000)
   `tidak_diterbitkan`; 2002 hanya ibu kota `cakupan_parsial`. Sel "-" di tabel bahan bakar tidak diisi nol; Maluku
   dan Maluku Utara 2001 serta minyak tanah Jakarta 2021 tetap `missing` (7 sel).

## Pilihan lain yang juga sah

- CSV pratampil sebagai sumber Silver tabel bahan bakar, asalkan HTML tetap dibaca untuk uji silang.
- Mengisi "-" Jakarta 2021 dengan 0 bila ada rujukan bahwa "-" di tabel itu berarti nihil, dan mencatat rujukannya.
- Memasukkan "lainnya" ke tidak bersih, asalkan pengaruhnya terhadap angka bersih dilaporkan.
- Tidak menyimpan baris "Jumlah" (selalu ±100), asalkan aturan jumlah tetap dihitung dari rincian.
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
