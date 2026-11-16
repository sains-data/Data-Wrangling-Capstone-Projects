# Kunci Sprint 1 — Kasus 21 Keamanan dan pencatatan sipil

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 21
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 26 / 26 |
| Baris mentah di berkas data | 4.108 |
| Baris Silver | 1.370 (8 seri, 1 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 11 lolos, 0 peringatan |
| Waktu `python pipeline.py` | ±2.5 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 26 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (10 JSON, 2 catatan unduhan, 10 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 115 calon anomali dengan alasan |
| Profil seri pembanding (2 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 243 sel kosong: 116 belum_ada, 11 batas_lama, 0 tidak_diterbitkan, 116 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 38 outlier, 19 patahan seri, 11 patahan wilayah, 0 galat input; snapshot ganda dibandingkan (0 nilai berbeda) |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 6 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 1 pasangan selisih, 2 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Empat seri di dua snapshot (K-003).** `var1311`, `var1312`, `var2738`, `var2740` ada di snapshot 17 dan
   20 Oktober; dibandingkan per kunci (0 nilai berbeda), lalu snapshot terbaru dipakai.
   Aturan validasi memastikan satu nilai per kunci.
2. **Provinsi hilang sejak 2020 tanpa catatan (K-005).** Korban kejahatan kekerasan dan pelaporan ke polisi
   kehilangan 7–18 provinsi per tahun sejak 2020; penerbit tidak menjelaskannya. Sel itu `missing`
   (116 sel di semua seri), tidak diisi. Dugaan (angka ditekan karena terlalu kecil atau RSE tinggi)
   dicatat sebagai pertanyaan untuk Sprint 2.
3. **Periode = tahun kejadian (K-012).** `var.note` `var1311`: angka 2017 berasal dari Susenas 2018 dengan rujukan
   kejadian 1 Januari–31 Desember 2017. Periode disimpan seperti diterbitkan (tahun kejadian) dan 2017 didaftar
   sebagai pergantian definisi.
4. **Dua seri akta kelahiran (K-006).** `var1410` balita (16.9.1) dan `var1831` anak 0–17 tahun (butir nasional
   16.9.1(b)) tetap terpisah; hanya `var1410` yang dipasangkan dengan WDI (kelompok umur sama).
5. **Matriks ketersediaan (K-013).** Persen sel terisi per seri × tahun ada di `reports/kelengkapan-panel.md`;
   tidak ada tahun yang dimiliki keenam seri, jadi jendela analisis ditetapkan per pasangan, bukan satu jendela bersama.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Memakai snapshot 17 Oktober untuk seri yang ganda, asalkan aturannya sama untuk semua seri.
- Menggeser angka korban kejahatan ke tahun survei (2017 → 2018), asalkan dilakukan konsisten untuk semua tahun dan dicatat.
- Mengategorikan sel yang hilang sejak 2020 sebagai `tidak_diterbitkan` bila tim menemukan catatan penekanan angka dari BPS.
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
