# Kunci Sprint 1 — Kasus 04 Penyakit dan faktor risiko

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 4
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 16 / 16 |
| Baris mentah di berkas data | 2.012 |
| Baris Silver | 1.058 (7 seri, 3 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 10 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±2.1 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 16 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (3 JSON, 1 catatan unduhan, 3 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| Pembaca WHO GHO (3 CSV, 2 JSON) | `src/ekstraksi/who_gho.py` | kolom nilai dikenali dari akhiran `_N/_NL/_NU`; kolom `DIM_*` utuh |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 154 calon anomali dengan alasan |
| Profil seri pembanding (4 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 140 sel kosong: 100 belum_ada, 6 batas_lama, 34 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 105 outlier, 2 patahan seri, 4 patahan wilayah, 0 galat input |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 4 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 3 pasangan selisih, 1 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Satuan malaria dan penyebutnya (K-007, K-014).** BPS: "Per 1000 Orang" (seluruh penduduk, kasus yang
   dilaporkan). WHO dan WDI: per 1.000 *penduduk berisiko*, yaitu penduduk di daerah penularan (Denominator WHO).
   Satuannya dibedakan di Silver (`per_1000_penduduk` vs `per_1000_penduduk_berisiko`) supaya tidak tergabung,
   dan P1 dikategorikan selisih definisi dan metode.
2. **Hipertensi: butir nasional dan sumber campuran (K-008, K-005).** Nama tabel BPS `sdg3_3_4_1_b` menunjukkan butir
   3.4.1(b); indikator global 3.4.1 adalah kematian PTM. Tahun 2016 hanya berisi baris Indonesia (Sirkesnas), jadi
   34 sel provinsi 2016 `tidak_diterbitkan`. Sumber berganti tiap putaran (Riskesdas, Sirkesnas, Susenas+Riskesdas),
   sehingga perubahan antarputaran tidak dibaca sebagai tren tanpa catatan.
3. **Proyeksi WHO (K-010).** `M_Est_tob_curr_std` memuat 2025 dan 2030. 2030 jelas sesudah tanggal unduh; 2025
   mengikuti lompatan lima tahunan yang sama sesudah 2022. Keduanya tetap di Silver seperti diterbitkan, terdaftar
   di `PROYEKSI`, dan tidak ikut tahun beririsan P2 (4 tahun dipakai).
4. **Malaria tidak di-*winsorize* (K-004).** Papua, Papua Barat, Maluku, dan NTT selalu di ujung sebaran: ditandai
   perbedaan struktural (4 provinsi), nilai tidak diubah. Penurunan serentak 2013→2014 ditandai
   patahan seri karena lebih dari 70% provinsi turun lebih dari 20%; belum ada catatan metode yang menjelaskannya.
5. **Jendela analisis bersama (K-015).** Malaria 2010–2021, hipertensi 2007–2018 (empat putaran), merokok 2015–2025.
   Tidak ada tahun yang dimiliki ketiganya dengan cakupan provinsi lengkap selain 2018; jendela per seri dinyatakan
   di `reports/kelengkapan-panel.md`, bukan dipaksa sama.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Membuang baris proyeksi WHO dari Silver, asalkan jumlahnya dan alasannya tercatat; atau menyimpannya dengan kolom
  penanda tambahan (`status_angka = proyeksi`).
- Sel provinsi hipertensi 2016 sebagai `missing` dengan catatan, asalkan tidak diisi dari 2013 atau 2018.
- Penurunan malaria 2013→2014 dikategorikan perubahan nyata bila tim menemukan rujukan program, asalkan rujukannya
  dicatat.
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
