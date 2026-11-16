# Kunci Sprint 1 — Kasus 02 Kematian anak dan ibu

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 2
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 16 / 16 |
| Baris mentah di berkas data | 1.185 |
| Baris Silver | 867 (9 seri, 8 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 10 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±1.9 detik |

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
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 5 calon anomali dengan alasan |
| Profil seri pembanding (6 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 106 sel kosong: 38 belum_ada, 0 batas_lama, 68 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 5 outlier, 0 patahan seri, 0 patahan wilayah, 0 galat input; CSV vs JSON identik |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 7 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 3 pasangan selisih, 2 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 1 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Identitas dua seri kematian (K-003).** `var1373` dan `var1584` sama-sama berkode 3.2.1 di katalog,
   tetapi `var.label` menunjukkan `var1373` = kematian balita dan `var1584` = kematian bayi. Keduanya seri
   sendiri, bukan duplikat.
2. **Jendela rujukan (K-008).** `var.note` menyebut angka Indonesia merujuk 5 tahun dan angka provinsi
   10 tahun sebelum survei. Disimpan di kolom `rujukan_tahun` supaya aturan validasi dan rekonsiliasi bisa
   membedakannya.
3. **Sel provinsi 2017 (K-005).** Penerbit sendiri menyatakan angka provinsi 2017 tidak ada; sel itu
   `tidak_diterbitkan`, bukan missing. Panel provinsi kematian hanya punya satu periode (2012).
4. **Satuan dan SDG (K-007, K-009).** Satuan `tidak_ada` diganti `per_1000_kh`; `var1541` ternyata persalinan
   *di fasilitas kesehatan* untuk *40% pengeluaran terbawah*, jadi kodenya 3.1.2(b) dan tidak dipasangkan
   sebagai selisih dengan `SH.STA.BRTC.ZS` (K-014).
5. **Tidak ada interpolasi di Silver (K-013).** Tahun di antara survei tidak diisi.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Menulis umur (`umur=Y_LT5`) di kolom `rincian` alih-alih mencatatnya sebagai cakupan seri.
- Jendela rujukan dicatat di data dictionary saja, asalkan aturan balita ≥ bayi tetap membandingkan angka
  dengan jendela yang sama.
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
