# Kunci Sprint 2 — Kasus 23 Kerusakan dan kerugian bencana

Folder ini adalah repo tim sesudah semua backlog Sprint 2 dikerjakan: isi `sprint-1/` ditambah panel Gold,
tabel nasional, tabel rekonsiliasi, Silver dan Gold di SQL, serta validasi Gold. Bandingkan dengan repo timmu
berkas demi berkas. Seperti Sprint 1, setiap keputusan di sini adalah **salah satu jawaban yang dapat
dipertahankan**; alternatif yang ditolak ada di `log-keputusan.csv` (K-016 dan seterusnya untuk Sprint 2).

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
| Baris Silver | 18.187 (sama dengan Sprint 1) |
| Panel Gold | 12 indikator, 5.244 sel: 1.688 terisi, 3.556 kosong berkategori |
| Tabel nasional Gold | 28 baris, 9 seri |
| Tabel rekonsiliasi | 33 baris, 3 selisih dihitung |
| Median selisih relatif mutlak | 0.0% (seri utama provinsi); 0.0% semua pasangan |
| DuckDB | Silver 18.187 baris + Gold 5.305 baris + 43 dokumen JSON (9.4 MB, tidak di-commit) |
| Aturan validasi | 24 aturan (10 di antaranya Gold): 20 lolos, 4 peringatan |
| Waktu `python pipeline.py` | ±8.7 detik |

## Peta backlog Sprint 2 → bukti

| Backlog (Papan Tim) | Di mana | Yang ditunjukkan |
|---|---|---|
| Aturan satu nilai per sel Gold (pembersihan) | `src/gold/panel.py`, `reports/panel-gold.md` bagian *Aturan* | snapshot, rincian, berkas, periode; 14.988 baris Silver provinsi tidak masuk panel |
| Panel Gold provinsi × periode × indikator (transformasi) | `data/gold/panel.parquet`, `data/gold/panel_lebar.parquet` | 12 indikator; sel kosong tetap tampil dengan kategorinya; 158 sel bertanda anomali, nilai tidak diubah |
| Tabel nasional Gold (ekstraksi) | `src/gold/nasional_gold.py`, `data/gold/nasional.parquet` | seri utama dan pembanding berdampingan; kolom `asal` |
| Silver dan Gold di SQL (integrasi) | `src/gold/silver.sql`, `src/gold/gold.sql`, `src/gold/muat_sql.py`, `reports/basis-data.md` | kunci primer, CHECK, jumlah baris dicocokkan, uji sel ganda ditolak, banding dengan dokumen JSON |
| Tabel rekonsiliasi berkategori (integrasi) | `src/gold/rekonsiliasi.py`, `data/gold/rekonsiliasi.parquet`, `reports/rekonsiliasi.md` | 33 baris; kategori baku dan penjelasan setiap pasangan |
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

1. **Aturan sel diwarisi dari deret Sprint 1.** Panel memuat 12 indikator; seri berincian memakai rincian di `DERET`: `kejadian` (`jumlah`), `rumah_rusak` (`jumlah`), `rumah_terendam` (`jumlah`), `fasyankes_rusak` (`jumlah`), `satuan_pendidikan_rusak` (`jumlah`), `jembatan_rusak` (`jumlah`), `kantor_rusak` (`jumlah`), `rumah_ibadat_rusak` (`jumlah`), `kios_toko_rusak` (`jumlah`), `pabrik_rusak` (`jumlah`), `nilai_kerusakan` (`jumlah`), `nilai_kerugian` (`jumlah`). Snapshot terbaru dan satu berkas per sel; 14.988 baris Silver provinsi tidak masuk panel (rincian lain tetap di Silver).
2. **Sel kosong ikut Gold.** 3.556 sel kosong tampil dengan kategorinya (3.158 `tidak_diterbitkan`, 398 `belum_ada`); tidak ada interpolasi. 158 sel membawa penanda anomali Sprint 1; nilainya tidak diubah.
3. **Kategori baku ditetapkan per pasangan.** P1 *belum terjelaskan*; P2 *belum terjelaskan*; P3 *definisi berbeda*.
4. **P1.** Baris INDONESIA dibandingkan dengan jumlah baris provinsi di berkas yang sama (GOLD_AGREGAT).
5. **P2.** Rumah rusak berat + sedang + ringan di rekap nasional dijumlahkan dulu sebelum dibandingkan dengan tabel per jenis.
6. **Selisih terbesar: P1** (0.0%, tidak berselisih (angka sama)). Seharusnya sama: satu rumah tidak dihitung di dua provinsi (berbeda dengan kejadian).
7. **Tidak berselisih: P1, P2.** Angka kedua sisi sama; selisih nol dicatat sebagai kategori *tidak berselisih*, bukan dihapus.
8. **Basis data.** Silver dan Gold di DuckDB dengan kunci primer dan CHECK kategori; JSON mentah disimpan sebagai dokumen hanya untuk perbandingan (`reports/basis-data.md`).

## Pilihan lain yang juga sah

- Membandingkan dengan tabel nasional 2010–2024 alih-alih baris INDONESIA tabel per jenis.
- Membandingkan per tingkat bila tabel per jenis kelak memecah tingkat kerusakan.
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
