# Kunci Sprint 1 — Kasus 22 Korban bencana

Folder ini adalah repo tim yang sudah mengerjakan semua backlog Sprint 1, dalam bentuk yang sama dengan
template `capstone-dw-2026-starter`. Bandingkan berkas demi berkas dengan repo timmu. Setiap keputusan di
sini adalah **salah satu jawaban yang dapat dipertahankan**, bukan satu-satunya jawaban; alternatif yang
ditolak dan alasannya ada di `log-keputusan.csv`. Saat wawancara yang ditanyakan adalah alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan folder ini.

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 22
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Berkas di MANIFEST / dibaca | 44 / 44 |
| Baris mentah di berkas data | 77.522 |
| Baris Silver | 14.193 (11 seri, 10 nilai rincian) |
| Pemeriksa skema | LOLOS |
| Aturan validasi | 13 aturan: 10 lolos, 3 peringatan |
| Waktu `python pipeline.py` | ±5.4 detik |

Semua laporan di `reports/` dan `docs/data-dictionary.md` ditulis ulang oleh `python pipeline.py`, jadi
angkanya selalu sesuai dengan data.

## Peta backlog Sprint 1 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Penjaga data: `data/raw` cocok MANIFEST | `unduh_data.py`, `results/kunci/metrics.json` (`data_hash`) | sha256 44 berkas lolos; semua anggota harus punya `data_hash` yang sama |
| Pembaca BNPB (27 JSON, 13 XLSX) | `src/ekstraksi/bnpb.py` | DataStore dan XLSX ke satu bentuk sel; tata letak dikenali dari kepala kolom; sel tergabung diisi; judul resource dari katalog CKAN = nama ukuran (`src/kamus_bnpb.py`) |
| Pembaca WDI (4 JSON) | `src/ekstraksi/wdi.py` | penyaringan kode persis (bukan awalan); `value: null` dibawa apa adanya |
| `ekstraksi.jalankan()` | `src/ekstraksi/__init__.py`, `reports/ekstraksi.md` | tidak ada berkas MANIFEST yang terlewat; jumlah baris per berkas |
| Profil dan calon anomali seri utama | `src/silver/profil.py`, `reports/profil-seri-utama.md`, `reports/gambar/` | 119 calon anomali dengan alasan |
| Profil seri pembanding (1 seri) | `src/silver/pembanding.py`, `reports/ketersediaan-pembanding.md` | periode, rincian, irisan dengan seri utama; WDI baris ada vs nilai ada |
| Grid 38 provinsi × periode | `src/silver/grid.py`, `reports/kelengkapan-panel.md` | 2.008 sel kosong: 236 belum_ada, 0 batas_lama, 1.772 tidak_diterbitkan, 0 missing |
| Outlier, patahan, galat, duplikat | `src/silver/anomali.py`, `reports/anomali.md`, `reports/anomali.csv` | 101 outlier, 0 patahan seri, 6 patahan wilayah, 0 galat input; observasi yang sama di beberapa berkas dibandingkan (172 dari 4.157 berbeda) |
| Satuan, periode, kode SDG dari metadata | `src/silver/metadata.py`, `docs/seri.csv`, `reports/metadata.md` | 0 koreksi katalog dengan bukti dari berkas mentah |
| Silver pertama | `src/silver/bangun.py`, `data/silver/silver.parquet` | lolos `python -m src.common.skema` |
| Tabel nasional + pasangan rekonsiliasi | `src/gold/nasional.py`, `reports/tabel-nasional.csv`, `reports/pasangan-rekonsiliasi.md` | 3 pasangan selisih, 1 konteks |
| Rancangan skema SQL | `src/gold/silver.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | Silver dimuat ke DuckDB dengan kunci primer dan CHECK |
| Aturan validasi dasar | `src/validasi/aturan.py`, `src/validasi/khusus.py`, `reports/validasi.md` | 7 aturan umum, 3 aturan khas kasus, 3 peringatan |
| Data dictionary | `docs/data-dictionary.md` | semua kolom, kamus rincian, contoh penelusuran satu baris |
| Integrator: merge, pipeline sampai Silver | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Analis: ringkasan temuan | `reports/tim.md` | bagian *Masalah data dan penanganannya* |
| Koordinator: Sprint Goal, Log Sprint, demo | `sprint/sprint-1/`, `DEMO.md` | contoh Sprint Goal, Log Sprint tiga baris, naskah demo |
| Reproduksi: klon bersih + rekaman | `DEMO.md` | perintah dan waktu jalan |

## Keputusan yang paling menentukan

1. **Satu bentuk sel untuk dua format dan enam tata letak (K-002).** DataStore JSON dan XLSX unduhan tangan
   diubah ke satu tabel "satu sel = satu baris" (77.456 sel). Tata letak dikenali dari kepala kolom
   (per jenis, per tahun, rekap, rekap nasional); nama ukuran diambil dari judul resource di katalog CKAN karena
   tabel BNPB tidak membawa kode seri (21.428 sel milik ukuran kasus lain tidak dipakai).
2. **Sel tergabung diisi dulu (K-003).** Di rekap 2021/2022, sel Provinsi tergabung beberapa baris ke bawah;
   openpyxl hanya memberi nilai di baris pertama. Tanpa mengisinya, setiap provinsi di rekap kab/kota hanya
   membawa satu kab/kota. Sesudah diisi, jumlah kab/kota Aceh banjir 2021 = 100, sama dengan rekap provinsi.
3. **Kab/kota dijumlahkan ke provinsi, jumlahnya dicatat (K-008).** Kode kab/kota Kemendagri empat digit -> dua
   digit provinsi -> kode kunci (4.494 angka provinsi dari 46.330 baris kab/kota,
   `reports/bnpb-agregasi.csv`). Kode Kemendagri enam provinsi Papua berbeda dari BPS (91 = Papua, bukan Papua
   Barat); kode dan nama harus sepakat, kalau tidak pipeline berhenti.
4. **Kab/kota vs provinsi diuji, bukan diasumsikan (K-009).** Dari 4.010 pasangan,
   3.839 sama. Kejadian hasil jumlah kab/kota lebih besar pada 164 pasangan:
   sesuai aturan hitung di lembar Keterangan (kejadian lintas kab/kota dihitung di setiap kab/kota). Yang tidak
   sesuai aturan: 1 kejadian lebih kecil dan 6 angka korban
   berbeda, semuanya perpindahan DKI Jakarta -> Jawa Barat tahun 2024 (tanah longsor: 1 kejadian, 65 pengungsi,
   187 terdampak; banjir: 2.506 terdampak). Di tabel provinsi angka itu masuk DKI Jakarta, di tabel kab/kota masuk
   kab/kota Jawa Barat; jumlah kedua provinsi sama. Dicatat sebagai peringatan; tidak dipindahkan.
5. **Semua berkas dipertahankan; deret profil memilih satu (K-007).** Silver menyimpan observasi yang sama dari
   beberapa berkas (4.157 kelompok, 172 berbeda; salinan 2024 di dua dataset
   identik). Satu-satunya beda di luar angka jumlahan kab/kota: baris INDONESIA tanah longsor 2024 di tabel provinsi
   tertulis 27, padahal jumlah 38 provinsinya dan dua tabel lain 207. Nilai tidak diubah di Silver.
6. **Deret profil = jumlah semua jenis bencana (K-005); IQR pada log(1 + nilai) (K-004).** Korban provinsi hanya
   terbit per jenis; jenis membagi habis kejadian (satu kejadian satu jenis utama), jadi jumlahnya adalah total.
   Jumlah korban sangat menceng; IQR pada skala log menghasilkan 119 calon anomali.
7. **Tahun tanpa tabel provinsi = `tidak_diterbitkan` dengan bukti katalog (K-011).** 1.772 sel:
   korban 2010–2020 dan 2023 hanya terbit nasional, atau hanya sebagai tautan dasbor tanpa tabel.

## Pilihan lain yang juga sah

- Membaca setiap tata letak dengan fungsi terpisah, asalkan semua berakhir di skema Silver yang sama dan tidak ada
  berkas yang terlewat.
- Memakai hanya satu berkas per tahun di Silver (misalnya tabel provinsi, tanpa jumlahan kab/kota dan salinan
  kompilasi), asalkan berkas yang dibuang dan alasannya dicatat; kunci menyimpan semuanya agar perbedaannya terlihat.
- Mengoreksi baris INDONESIA tanah longsor 2024 menjadi 207 di Silver sebagai galat input, karena koreksinya jelas
  (jumlah provinsi dan dua tabel lain), asalkan lewat kode dan dicatat di log.
- Memprofilkan setiap jenis bencana sebagai deret sendiri; lebih rinci, tetapi banyak sel nol.
- z-score pada log(1 + nilai), atau IQR biasa per tahun dengan alasan tertulis mengapa provinsi besar memang besar.
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
