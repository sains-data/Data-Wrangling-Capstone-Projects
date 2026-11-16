# Kunci Sprint 1 — Kasus 01 Kerawanan pangan provinsi

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 1
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 14 / 14 |
| Baris mentah di berkas data | 2.184 |
| Baris Silver | 1.414 (7 seri, 69 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 10 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±2.0 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 14 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (2 JSON, 1 catatan unduhan, 2 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| Pembaca WHO GHO (3 CSV, 2 JSON) | `src/ekstraksi/who_gho.py` | kolom nilai dikenali dari akhiran `_N/_NL/_NU`; kolom `DIM_*` utuh |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 114 calon anomali dengan alasan |
| Profil seri pembanding (5 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 56 sel kosong: 48 belum_ada, 8 batas_lama, 0 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 63 outlier, 0 patahan seri, 4 patahan wilayah, 0 galat input; 24 kembar setara dan 2 kembar bertentangan WHO (`reports/kembar-who.csv`) |
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

1. **Format kanonik BPS (K-002).** CSV dan JSON memuat pasangan wilayah-tahun dan nilai yang identik
   (`reports/anomali.md`, bagian dua format). JSON dipakai karena membawa `var.unit` dan `var.note`; hanya satu
   format yang masuk Silver.
2. **Duplikat di berkas WHO wasting (K-011).** Satu tahun bisa punya tiga baris "total": semua `DIM_*` kosong,
   semua `TOTAL`, atau sebagian `TOTAL`. Setelah dienkode ketiganya `total` dengan nilai sama, jadi satu dipakai
   (24 baris dibuang). Satu sel (laki-laki 24–35 bulan, 2008) muncul dua kali dengan nilai
   berbeda (15,7 dan 16,3); berkas tidak memberi cara memilih, jadi keduanya tidak masuk Silver
   (`reports/kembar-who.csv`).
3. **Pemekaran Papua (K-001, K-016).** Empat provinsi baru baru terbit mulai 2024, sedangkan Papua dan Papua Barat
   tetap terbit pada 2023 dengan batas lama. Sel 2023 keempat provinsi baru dikategorikan `batas_lama`
   (8 sel), bukan missing, dan perubahan Papua 2023→2024 ditandai `patahan_wilayah`, bukan tren.
4. **Perbedaan struktural vs outlier (K-004).** Maluku, Maluku Utara, dan provinsi Papua selalu di ujung atas
   sebaran PoU. Provinsi yang di luar batas IQR pada sebagian besar periodenya ditandai sekali sebagai perbedaan
   struktural (8 provinsi); outlier dipakai untuk kejadian satu tahun, misalnya Kalimantan Utara 2022.
5. **Selisih BPS–WDI bukan galat (K-014).** PoU Indonesia BPS dan FAO berbeda lebih dari 2 poin pada beberapa tahun
   (peringatan validasi). Selisih dicatat sebagai pertanyaan metode; apakah angka FAO rata-rata beberapa tahun
   tidak bisa dijawab dari metadata paket, jadi dijawab di Sprint 2.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Untuk kembar bertentangan WHO: menyimpan keduanya dengan penanda di kolom tambahan, atau memilih salah satu
  dengan aturan tertulis (misalnya baris yang punya batas bawah/atas). Yang tidak sah: memilih diam-diam.
- Menulis sel Papua 2023 sebagai `missing` dengan catatan, asalkan tidak diisi dari angka induk.
- Tanpa kategori perbedaan struktural, asalkan outlier yang berulang setiap tahun dijelaskan sekali, bukan
  dibahas satu per satu.
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
