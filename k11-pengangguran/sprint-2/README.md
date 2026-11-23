# Kunci Sprint 2 — Kasus 11 Pengangguran

Folder ini adalah repo tim sesudah semua backlog Sprint 2 dikerjakan: isi `sprint-1/` ditambah panel Gold,
tabel nasional, tabel rekonsiliasi, Silver dan Gold di SQL, serta validasi Gold. Bandingkan dengan repo timmu
berkas demi berkas. Seperti Sprint 1, setiap keputusan di sini adalah **salah satu jawaban yang dapat
dipertahankan**; alternatif yang ditolak ada di `log-keputusan.csv` (K-016 dan seterusnya untuk Sprint 2).

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 11
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Baris Silver | 7.572 (sama dengan Sprint 1) |
| Panel Gold | 1 indikator, 2.318 sel: 1.939 terisi, 379 kosong berkategori |
| Tabel nasional Gold | 254 baris, 6 seri |
| Tabel rekonsiliasi | 91 baris, 56 selisih dihitung |
| Median selisih relatif mutlak | 37.2% (seri utama provinsi); 0.0% semua pasangan |
| DuckDB | Silver 7.572 baris + Gold 2.663 baris + 10 dokumen JSON (5.8 MB, tidak di-commit) |
| Aturan validasi | 21 aturan (10 di antaranya Gold): 20 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±4.0 detik |

## Peta backlog Sprint 2 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Aturan satu nilai per sel Gold (pembersihan) | `src/gold/panel.py`, `reports/panel-gold.md` bagian *Aturan* | snapshot, rincian, berkas, periode; 0 baris Silver provinsi tidak masuk panel |
| Panel Gold provinsi × periode × indikator (transformasi) | `data/gold/panel.parquet`, `data/gold/panel_lebar.parquet` | 1 indikator; sel kosong tetap tampil dengan kategorinya; 179 sel bertanda anomali, nilai tidak diubah |
| Tabel nasional Gold (ekstraksi) | `src/gold/nasional_gold.py`, `data/gold/nasional.parquet` | seri utama dan pembanding berdampingan; kolom `asal` |
| Silver dan Gold di SQL (integrasi) | `src/gold/silver.sql`, `src/gold/gold.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | kunci primer, CHECK, jumlah baris dicocokkan, uji sel ganda ditolak, banding dengan dokumen JSON |
| Tabel rekonsiliasi berkategori (integrasi) | `src/gold/rekonsiliasi.py`, `data/gold/rekonsiliasi.parquet`, `reports/rekonsiliasi.md` | 91 baris; kategori baku dan penjelasan setiap pasangan |
| Aturan validasi Gold dan rekonsiliasi (validasi) | `src/validasi/gold.py`, `tests/test_gold.py`, `reports/validasi.md` | 10 aturan Gold, masing-masing diuji dengan Gold yang sengaja dirusak |
| Sprint Goal, Log Sprint, Demo (koordinator) | `sprint/sprint-2/`, `DEMO.md` | contoh Sprint Goal, Log Sprint, naskah demo |
| Merge sampai Gold, SQL, rekonsiliasi (integrator) | bagian *Urutan merge* di bawah | `python pipeline.py` dari klon bersih |
| Draf bagian *Integrasi dan rekonsiliasi* (analis) | `reports/tim.md` | setiap angka dapat ditarik dari `data/gold/` |
| Uji klon bersih + rekaman demo (reproduksi) | `DEMO.md` | Silver, Gold, rekonsiliasi hasil jalan ulang = yang di-commit |

Tugas pendamping (hanya bila komponen dipegang dua orang):

| Pendamping | Di mana |
|---|---|
| Kelengkapan panel Gold dan penanda | `reports/panel-gold.md` bagian *Status sel*; kolom `status_sel`, `penanda` |
| Kolom turunan Gold | `GOLD_TURUNAN` di `src/konfigurasi.py` (nilai asli tetap); kosong bila kasus tidak membutuhkannya |
| Pembanding siap dipasangkan | `PASANGAN` (rincian pembanding) dan `GOLD_KONVERSI` di `src/konfigurasi.py` |
| Data dictionary kolom Gold | `docs/data-dictionary.md` bagian Gold (43 kolom) |

## Keputusan Sprint 2 yang paling menentukan

1. **Aturan sel diwarisi dari deret Sprint 1.** Panel memuat 1 indikator (baris `total`). Snapshot terbaru dan satu berkas per sel; 0 baris Silver provinsi tidak masuk panel (rincian lain tetap di Silver).
2. **Sel kosong ikut Gold.** 379 sel kosong tampil dengan kategorinya (356 `belum_ada`, 21 `batas_lama`, 2 `tidak_diterbitkan`); tidak ada interpolasi. 179 sel membawa penanda anomali Sprint 1; nilainya tidak diubah.
3. **Kategori baku ditetapkan per pasangan.** P1 *definisi berbeda*; P2 *metode berbeda*; P3 *tanpa pasangan*.
4. **Selisih terbesar: P1** (37.2%, definisi berbeda). Definisi pengangguran (BPS lebih tinggi 1–3,3 poin pada 18 tahun; dugaan cakupan BPS lebih luas) dan pengolahan.
5. **Tidak berselisih: P2.** Angka kedua sisi sama; selisih nol dicatat sebagai kategori *tidak berselisih*, bukan dihapus.
6. **Basis data.** Silver dan Gold di DuckDB dengan kunci primer dan CHECK kategori; JSON mentah disimpan sebagai dokumen hanya untuk perbandingan (`reports/basis-data.md`).

## Pilihan lain yang juga sah

- Menghitung selisih relatif terhadap seri utama (bukan pembanding); pilihannya ditulis di laporan.
- Memasukkan rincian lain ke panel sebagai indikator tambahan, selama satu sel tetap satu nilai.
- Panel lebar saja (tanpa versi panjang), selama sel kosong dan kategorinya tetap terlihat di tempat lain.
- Kategori selisih yang lebih rinci daripada daftar baku, selama setiap kategori punya bukti.
- SQLite atau PostgreSQL alih-alih DuckDB; menyimpan Gold sebagai Parquet saja tanpa SQL **tidak** memenuhi DoD.

## Yang berubah dari sprint-1

- Baru: `src/gold/panel.py`, `nasional_gold.py`, `rekonsiliasi.py`, `gold.sql`; `src/validasi/gold.py`;
  `src/dokumen_gold.py`; `tests/test_gold.py`; `data/gold/*.parquet`; `reports/panel-gold.md`, `rekonsiliasi.md`.
- Diubah: `src/gold/__init__.py`, `src/gold/muat_sql.py`, `src/validasi/__init__.py`, `src/konfigurasi.py`
  (bagian Sprint 2 di akhir berkas), `reports/basis-data.md`, `reports/tim.md`, `log-keputusan.csv`.
- Tidak berubah: ekstraksi dan Silver (Silver identik dengan sprint-1).

## Urutan merge yang disarankan (integrator)

1. `src/gold/panel.py` (pembersihan + transformasi) — panel lolos aturan *gold: kunci panel unik*.
2. `src/gold/nasional_gold.py` (ekstraksi) — tabel nasional.
3. `src/gold/rekonsiliasi.py` dan `PASANGAN` di konfigurasi (integrasi).
4. `src/gold/gold.sql`, `muat_sql.py` (integrasi) — jumlah baris SQL = Parquet.
5. `src/validasi/gold.py`, `tests/test_gold.py`, `src/dokumen_gold.py` (validasi).

Setelah setiap merge: `python pipeline.py && python -m pytest -q` di `main`.

## Belum dikerjakan di Sprint 2

Analisis revisi pembanding dari arsip WDI dan perbandingan pandas vs DuckDB/Dask (tahap 7), skema validasi
lengkap, reproduksi akhir, dan laporan tim/individu final (Sprint 3).
