# Kunci Sprint 1 — Kasus 12 Upah dan informalitas

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 12
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 10 / 10 |
| Baris mentah di berkas data | 2.265 |
| Baris Silver | 1.584 (4 seri, 117 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 11 lolos, 0 peringatan |
| Waktu `python pipeline.py` | ±1.9 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 10 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (2 JSON, 1 catatan unduhan, 2 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca ILOSTAT (2 CSV, 3 JSON) | `src/ekstraksi/ilostat.py` | CSV SDMX dibaca utuh; dimensi lewat `src/kamus_ilo.py`; `OBS_STATUS` ke kolom `status_obs`; DSD dan dataflow untuk definisi |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 83 calon anomali dengan alasan |
| Profil seri pembanding (2 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 60 sel kosong: 52 belum_ada, 8 batas_lama, 0 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 42 outlier, 0 patahan seri, 4 patahan wilayah, 0 galat input; total klasifikasi ILO lain diuji sama dengan total utama |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 1 koreksi katalog dengan bukti dari berkas mentah |
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

1. **Unit upah sama sebelum dibandingkan (K-007).** BPS: "Rupiah/Jam" (`var.unit`), nominal. ILO: `UNIT_MEASURE` LC
   dengan `NOTE_INDICATOR` "IDR: Indonesian rupiah", penghasilan per jam, nominal. Keduanya bersatuan `rupiah_per_jam`.
   Upah tidak disesuaikan inflasi di Sprint 1; upah riil hanya dihitung di Gold dengan indeks harga yang dicatat sumbernya.
2. **Satu total utama per klasifikasi ILO (K-006).** Berkas ILO memuat beberapa klasifikasi jabatan (ISCO-08, ISCO-88,
   tingkat keahlian) dan sektor (SECTOR, AGGREGATE), masing-masing dengan totalnya. Total utama = `OCU_SKILL_TOTAL` dan
   `ECO_SECTOR_TOTAL`; total klasifikasi lain tetap rincian, dan aturan validasi memastikan nilainya sama dengan total utama.
3. **Informalitas ILO jauh di atas BPS (K-014).** ILO ±80%, BPS ±58% pada tahun yang sama; keduanya mencakup semua sektor.
   Selisih dikategorikan definisi (kriteria informal), bukan galat; rincian ILO tanpa pertanian (`SECTOR_NAG`) disiapkan
   untuk diuji di Sprint 2.
4. **Satuan `var2153` (K-008).** Kosong di katalog; ditetapkan persen dari judul dan besaran.
5. **Revisi penimbang (K-012).** `var.note` upah: 2015–2019 angka revisi karena perubahan penimbang; dicatat di cakupan,
   tidak dianggap patahan. Distribusi upah menceng; provinsi ekstrem ditandai sebagai perbedaan struktural, tidak dihapus.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Membuang total klasifikasi lain dari Silver karena sama dengan total utama, asalkan kesamaannya diuji dulu.
- Memakai klasifikasi ISCO-08 sebagai total utama jabatan, asalkan dipakai konsisten.
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
