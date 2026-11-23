# Panel Gold provinsi x periode x indikator

Dihasilkan `python pipeline.py` (`src/gold/panel.py`) dari Silver, grid, dan kategori anomali Sprint 1.

## Aturan satu nilai per sel

1. **Snapshot**: seri yang ada di dua snapshot memakai snapshot terbaru; angka snapshot lain dibandingkan di `reports/snapshot-bps.csv` (bila ada).
2. **Rincian**: satu indikator = satu deret utama (`total`, atau rincian di `DERET`). Rincian lain tetap di Silver.
3. **Berkas**: bila satu sel punya beberapa berkas, `URUTAN_BERKAS` memilih satu (`reports/deret-berkas.csv`).
4. **Periode**: disimpan apa adanya; tidak dirata-rata ke tahunan.
5. **Penanda**: outlier, patahan, dan galat input dari Sprint 1 ikut sebagai kolom `penanda`; nilainya tidak diubah.

Baris Silver provinsi yang tidak masuk panel (rincian lain atau berkas lain): 0.

## Indikator

| indikator | satuan | periode | jumlah_periode | sel | terisi | ditandai |
|---|---|---|---|---|---|---|
| var1980 [jenjang=sd] | persen | 2015–2023 | 9 | 342 | 306 | 45 |
| var1980 [jenjang=sma] | persen | 2015–2023 | 9 | 342 | 306 | 39 |
| var1980 [jenjang=smp] | persen | 2015–2023 | 9 | 342 | 306 | 32 |
| var2211 [umur=13-15] | persen | 2015–2025 | 11 | 418 | 382 | 47 |
| var2211 [umur=16-18] | persen | 2015–2025 | 11 | 418 | 382 | 46 |
| var2211 [umur=19-23] | persen | 2015–2025 | 11 | 418 | 382 | 59 |
| var2211 [umur=7-12] | persen | 2015–2025 | 11 | 418 | 382 | 53 |
| var2595 | rasio_x100 | 2020–2025 | 6 | 228 | 212 | 26 |
| var2600 | rasio_x100 | 2020–2025 | 6 | 228 | 212 | 26 |
| var304 [jenjang=sd] | persen | 2003–2025 | 23 | 874 | 769 | 81 |
| var304 [jenjang=sm] | persen | 2003–2025 | 23 | 874 | 769 | 49 |
| var304 [jenjang=smp] | persen | 2003–2025 | 23 | 874 | 769 | 48 |

## Status sel

| indikator | batas_lama | belum_ada | missing | terisi |
|---|---|---|---|---|
| var1980 [jenjang=sd] | 4 | 32 | 0 | 306 |
| var1980 [jenjang=sma] | 4 | 32 | 0 | 306 |
| var1980 [jenjang=smp] | 4 | 32 | 0 | 306 |
| var2211 [umur=13-15] | 4 | 32 | 0 | 382 |
| var2211 [umur=16-18] | 4 | 32 | 0 | 382 |
| var2211 [umur=19-23] | 4 | 32 | 0 | 382 |
| var2211 [umur=7-12] | 4 | 32 | 0 | 382 |
| var2595 | 4 | 12 | 0 | 212 |
| var2600 | 4 | 12 | 0 | 212 |
| var304 [jenjang=sd] | 11 | 93 | 1 | 769 |
| var304 [jenjang=sm] | 11 | 93 | 1 | 769 |
| var304 [jenjang=smp] | 11 | 93 | 1 | 769 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 5,776 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 769 baris x 16 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
