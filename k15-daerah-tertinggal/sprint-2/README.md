# Kunci Sprint 2 — Kasus 15 Kemiskinan dan daerah tertinggal

Folder ini adalah repo tim sesudah semua backlog Sprint 2 dikerjakan: isi `sprint-1/` ditambah panel Gold,
tabel nasional, tabel rekonsiliasi, Silver dan Gold di SQL, serta validasi Gold. Bandingkan dengan repo timmu
berkas demi berkas. Seperti Sprint 1, setiap keputusan di sini adalah **salah satu jawaban yang dapat
dipertahankan**; alternatif yang ditolak ada di `log-keputusan.csv` (K-016 dan seterusnya untuk Sprint 2).

## Menjalankan

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 15
python pipeline.py
python -m src.common.skema data/silver/silver.parquet
python -m pytest -q
```

Hasil yang diharapkan (diukur saat kunci dibangun, starter commit `71e0ee1`):

| Ukuran | Nilai |
|---|---|
| Baris Silver | 3.897 (sama dengan Sprint 1) |
| Panel Gold | 3 indikator, 1.482 sel: 1.329 terisi, 153 kosong berkategori |
| Tabel nasional Gold | 67 baris, 4 seri |
| Tabel rekonsiliasi | 23 baris, 19 selisih dihitung |
| Median selisih relatif mutlak | 0.3% (seri utama provinsi); 0.3% semua pasangan |
| DuckDB | Silver 3.897 baris + Gold 1.572 baris + 8 dokumen JSON (4.7 MB, tidak di-commit) |
| Aturan validasi | 21 aturan (10 di antaranya Gold): 20 lolos, 1 peringatan |
| Waktu `python pipeline.py` | ±3.3 detik |

## Peta backlog Sprint 2 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Aturan satu nilai per sel Gold (pembersihan) | `src/gold/panel.py`, `reports/panel-gold.md` bagian *Aturan* | snapshot, rincian, berkas, periode; 2.429 baris Silver provinsi tidak masuk panel |
| Panel Gold provinsi × periode × indikator (transformasi) | `data/gold/panel.parquet`, `data/gold/panel_lebar.parquet` | 3 indikator; sel kosong tetap tampil dengan kategorinya; 227 sel bertanda anomali, nilai tidak diubah |
| Tabel nasional Gold (ekstraksi) | `src/gold/nasional_gold.py`, `data/gold/nasional.parquet` | seri utama dan pembanding berdampingan; kolom `asal` |
| Silver dan Gold di SQL (integrasi) | `src/gold/silver.sql`, `src/gold/gold.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | kunci primer, CHECK, jumlah baris dicocokkan, uji sel ganda ditolak, banding dengan dokumen JSON |
| Tabel rekonsiliasi berkategori (integrasi) | `src/gold/rekonsiliasi.py`, `data/gold/rekonsiliasi.parquet`, `reports/rekonsiliasi.md` | 23 baris; kategori baku dan penjelasan setiap pasangan |
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

1. **Aturan sel diwarisi dari deret Sprint 1.** Panel memuat 3 indikator (baris `total`). Snapshot terbaru dan satu berkas per sel; 2.429 baris Silver provinsi tidak masuk panel (rincian lain tetap di Silver).
2. **Sel kosong ikut Gold.** 153 sel kosong tampil dengan kategorinya (139 `belum_ada`, 8 `batas_lama`, 6 `tidak_diterbitkan`); tidak ada interpolasi. 227 sel membawa penanda anomali Sprint 1; nilainya tidak diubah.
3. **Kategori baku ditetapkan per pasangan.** P1 *metode berbeda*; P2 *definisi berbeda*.
4. **Selisih terbesar: P1** (0.3%, metode berbeda). Pembulatan: WDI = P0 Maret BPS dibulatkan satu desimal; tahun 2007–2011 BPS tahunan.
5. **Basis data.** Silver dan Gold di DuckDB dengan kunci primer dan CHECK kategori; JSON mentah disimpan sebagai dokumen hanya untuk perbandingan (`reports/basis-data.md`).

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
