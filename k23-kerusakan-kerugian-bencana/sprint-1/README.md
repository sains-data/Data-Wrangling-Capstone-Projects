# Kunci Sprint 1 — Kasus 23 Kerusakan dan kerugian bencana

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 23
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 58 / 58 |
| Baris mentah di berkas data | 90.269 |
| Baris Silver | 18.187 (15 seri, 40 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 14 aturan: 10 lolos, 4 peringatan |
| Waktu `python pipeline.py` | ±6.7 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 58 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BNPB (39 JSON, 15 XLSX) | `src/ekstraksi/bnpb.py` | DataStore dan XLSX ke satu bentuk sel; tata letak dikenali dari kepala kolom; sel tergabung diisi; judul resource dari katalog CKAN = nama ukuran (`src/kamus_bnpb.py`) |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 158 calon anomali dengan alasan |
| Profil seri pembanding (3 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 3.556 sel kosong: 398 belum_ada, 0 batas_lama, 3.158 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 130 outlier, 10 patahan seri, 16 patahan wilayah, 1 galat input; observasi yang sama di beberapa berkas dibandingkan (172 dari 7.060 berbeda) |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 2 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 2 pasangan selisih, 1 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 4 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Satu bentuk sel untuk dua format dan tujuh tata letak (K-002, K-003).** DataStore JSON dan XLSX unduhan tangan
   diubah ke satu tabel sel (90.203 sel); nama ukuran dari judul resource katalog CKAN atau kepala kolom rekap.
   Sel Provinsi rekap yang tergabung diisi dulu; tanpa itu rekap kab/kota hanya membawa satu kab/kota per provinsi.
2. **Rumah rusak: tingkat kerusakan sebagai rincian (K-006).** Rekap 2021/2022 dan rekap nasional 2025 memecah rumah
   rusak menjadi berat, sedang, ringan; tabel 2024/2025 tidak. Keduanya satu seri `rumah_rusak` dengan rincian
   `tingkat_kerusakan`; aturan keras memastikan berat + sedang + ringan 2025 = tabel per jenis.
3. **Nilai kerusakan dan kerugian adalah usulan, dijumlah ke provinsi (K-012).** Tabel memuat kab/kota yang mengajukan
   rencana rehabilitasi-rekonstruksi. Usulan yang mencakup beberapa tahun kejadian ("2013 - 2015") tidak dipakai
   (168 sel). Kab/kota yang mengajukan lebih dari sekali untuk tahun kejadian yang sama
   (10 kasus, misalnya Donggala dan Kota Palu 2018) tetap dijumlahkan dan didaftar di
   `reports/bnpb-usulan-berulang.csv`; Sprint 2 memutuskan usulan mana yang mewakili kerusakan.
4. **Galat input yang tidak bisa dikoreksi tidak masuk Silver (K-014).** Luas lahan, kebun, dan hutan terbakar 2012
   tertulis 44.041.216,5 ha, lebih dari seperlima daratan Indonesia; tahun lain di bawah 120 ribu ha. Tidak ada berkas
   lain untuk sel itu, jadi baris itu dibuang lewat `GALAT_INPUT` di konfigurasi (1 galat input).
5. **Luas sawah dan lahan hanya terbit nasional; satuannya dugaan (K-013).** Kedua seri jadi tingkat nasional dan
   satuan `hektar` diambil dari ambang batas di lembar Keterangan ("1 hektar lahan terdampak/rusak"), bukan dari
   tabelnya (2 koreksi katalog).
6. **Kab/kota vs provinsi dan antarberkas (K-008, K-009).** Dari 6.708 pasangan, 6.541
   sama; kejadian kab/kota lebih besar pada 164 pasangan (aturan hitung Keterangan). Rumah
   rusak 2024: 50 unit masuk DKI Jakarta di tabel provinsi tetapi Jawa Barat di tabel kab/kota. Rekapitulasi nilai
   2015–2024 berbeda dari tabel per tahun di dua provinsi 2017: Ogan Ilir tercatat dua kali di tabel per tahun, dan
   Sulawesi Tengah memuat Toli Toli di tabel per tahun tetapi Buol di rekapitulasi.
7. **Tahun tanpa tabel provinsi dan provinsi tanpa usulan = `tidak_diterbitkan` dengan bukti (K-011).**
   3.158 sel; sisa `missing` 0.

## Pilihan lain yang juga sah

- Memakai hanya usulan dengan Tahun Proposal terakhir per kab/kota dan tahun kejadian, asalkan aturannya sama untuk
  semua tahun dan nilai nol pada usulan ulang dibahas.
- Membagi rata usulan beberapa tahun kejadian ke setiap tahun, asalkan aturan pembagiannya tertulis.
- Menyimpan luas 2012 apa adanya dan menandainya outlier dengan rentang yang lebih longgar; kunci membuangnya karena
  angkanya mustahil secara fisik.
- Satuan luas `tidak_ada` seperti katalog sampai Juklak Standar Data dibaca.
- Rumah rusak per tingkat sebagai tiga seri terpisah; kunci memilih satu seri dengan rincian agar sejalan dengan
  tabel per jenis.
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
