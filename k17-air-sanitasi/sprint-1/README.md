# Kunci Sprint 1 — Kasus 17 Air minum, sanitasi, dan kebersihan

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 17
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 22 / 22 |
| Baris mentah di berkas data | 6.382 |
| Baris Silver | 3.242 (11 seri, 3 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 10 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±2.8 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 22 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (6 JSON, 1 catatan unduhan, 6 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| Pembaca WHO GHO (3 CSV, 2 JSON) | `src/ekstraksi/who_gho.py` | kolom nilai dikenali dari akhiran `_N/_NL/_NU`; kolom `DIM_*` utuh |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 403 calon anomali dengan alasan |
| Profil seri pembanding (5 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 453 sel kosong: 413 belum_ada, 30 batas_lama, 8 tidak_diterbitkan, 2 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 266 outlier, 52 patahan seri, 26 patahan wilayah, 0 galat input; 6 cakupan parsial; 3 pergantian definisi dari catatan penerbit |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 3 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 4 pasangan selisih, 1 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Judul berkas menentukan identitas seri (K-007).** Katalog memberi `var847` kode 11.1.1 (hunian layak), padahal
   `var.label` dan nama berkasnya sanitasi layak. Kodenya dikoreksi ke 6.2.1, dan aturan validasi memeriksa
   tujuan SDG setiap seri BPS terhadap angka `sdgN_` di nama berkasnya.
2. **Enam seri, empat konsep (K-014).** Air layak (`var845`), air aman (`var2741`), sanitasi layak (`var847`),
   sanitasi aman (`var2179`, `var2749`), cuci tangan (`var1273`). Garis waktu konsep ada di
   `reports/kelengkapan-panel.md`; Silver menyimpan semua seri, seri kanonik per tahun dipilih di Gold.
3. **Pergantian definisi dari catatan penerbit (K-013).** Air layak berganti rumus mulai 2011 (tabel melompat
   2010→2021), sanitasi layak mengikuti metadata SDGs sejak 2019, cuci tangan 2016 dari modul MKP. Ketiganya
   didaftar di `PATAHAN_DEFINISI` dan calon anomali pada periode itu dikategorikan patahan seri, bukan outlier.
4. **Susenas 2000–2002 (K-005, K-012).** Aceh dan Maluku tidak dicacah pada 2000, Aceh tidak dicacah pada 2001:
   8 sel `tidak_diterbitkan` per provinsi. Pada 2002 Aceh, Maluku, Maluku Utara, dan Papua
   hanya dicacah di ibu kota, sehingga lonjakannya dikategorikan `cakupan_parsial` (6 calon).
5. **Dua tabel sanitasi aman (K-011).** `var2749` sama persis dengan `var2179` rincian gabungan pada 2024–2025, kecuali
   Papua Pegunungan yang tidak ada di `var2749`. Itu satu-satunya sel `missing` (2); tidak diisi di
   Silver, karena Gold memakai `var2179` sebagai seri kanonik.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Tidak memasukkan `var2749` ke Silver karena isinya sama dengan `var2179`, asalkan pemeriksaan kesamaannya tertulis.
- Mengubah SDGODAWS ke USD (dikalikan sejuta) di Silver, asalkan satuannya ditulis `usd_konstan_2024`.
- Menulis rincian daerah `perkotaan`/`perdesaan` alih-alih kode WHO `URBAN`/`RURAL`, asalkan satu kamus dipakai untuk BPS dan WHO.
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
