# Kunci Sprint 1 — Kasus 08 Kesetaraan pendidikan

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 8
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 15 / 15 |
| Baris mentah di berkas data | 10.790 |
| Baris Silver | 5.418 (7 seri, 9 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 11 aturan: 11 lolos, 0 peringatan |
| Waktu `python pipeline.py` | ±4.0 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 15 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BPS (5 JSON, 1 catatan unduhan, 5 CSV) | `src/ekstraksi/bps.py` | kunci `datacontent` dipotong menurut panjang kode di daftar label; metadata `var` ikut dibaca |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 551 calon anomali dengan alasan |
| Profil seri pembanding (2 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 599 sel kosong: 527 belum_ada, 69 batas_lama, 0 tidak_diterbitkan, 3 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 342 outlier, 6 patahan seri, 30 patahan wilayah, 0 galat input |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 7 koreksi katalog dengan bukti dari berkas mentah |
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

1. **Jenjang dan jenis rasio dari judul (K-003).** Tiga seri berkode 4.5.1 di katalog. Judul JSON menunjukkan
   `var2595` = paritas *kuintil* APK SMA, `var2600` = paritas *jenis kelamin* APK perguruan tinggi, sedangkan
   `var304` adalah APM per jenjang (bukan indeks paritas), jadi kodenya dikoreksi ke target 4.1.
2. **Rasio BPS ditulis dikali 100 (K-007).** Nilai `var2595` dan `var2600` 32–260 (Indonesia ±77 dan ±115),
   sedangkan GPI WDI 0,77–1,02. Satuan BPS `rasio_x100`, WDI `rasio`; aturan validasi menilai keduanya setelah
   skala disamakan, dan penyeragaman untuk perbandingan dikerjakan di Gold.
3. **Satuan yang kosong di katalog (K-007).** APM, APS, dan tingkat penyelesaian = `persen` (tidak bisa melebihi 100);
   penyelesaian SD WDI = rasio masuk kasar yang bisa melebihi 100, jadi bersatuan `persen_apk`.
4. **Catatan APS salah tempel (K-009).** `var.note` APS berisi definisi ketimpangan partisipasi menurut disabilitas,
   bukan definisi APS menurut kelompok umur. Catatan itu tidak dipakai; definisi diambil dari judul.
5. **Penyelesaian SD BPS dan WDI berbeda definisi (K-014).** BPS: kohort umur 3–5 tahun di atas umur lulus; WDI:
   siswa baru kelas terakhir tanpa memandang umur. P1 dihitung selisihnya dengan kategori *definisi*.

## Pilihan lain yang juga sah

- CSV BPS sebagai sumber Silver (nilainya identik); yang penting hanya satu format masuk Silver.
- Membagi rasio BPS dengan 100 sudah di Silver, asalkan faktornya tercatat dan satuannya ditulis `rasio`.
- Tidak memakai APS sama sekali (tanpa kode SDG), asalkan alasannya tertulis.
- Menyimpan `var304` dengan kode katalog 4.5.1 dan catatan "bukan indeks paritas", asalkan tidak dipasangkan dengan GPI.
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
