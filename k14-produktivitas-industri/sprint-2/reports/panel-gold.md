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
| var1161 | persen_per_tahun | 2011–2025 | 15 | 570 | 509 | 61 |
| var1214 | persen | 2010–2023 | 14 | 532 | 480 | 71 |
| var1344 | rupiah_per_tenaga_kerja | 2015–2023 | 9 | 342 | 306 | 50 |
| var2755 | persen | 2018–2025 | 8 | 304 | 280 | 58 |

## Status sel

| indikator | batas_lama | belum_ada | terisi |
|---|---|---|---|
| var1161 | 11 | 50 | 509 |
| var1214 | 0 | 52 | 480 |
| var1344 | 4 | 32 | 306 |
| var2755 | 4 | 20 | 280 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 1,748 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 556 baris x 8 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
