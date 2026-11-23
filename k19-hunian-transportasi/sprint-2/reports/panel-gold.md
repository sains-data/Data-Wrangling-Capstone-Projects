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
| var1241 | persen | 2015–2025 | 11 | 418 | 382 | 38 |
| var2012 | persen | 2017–2020 | 2 | 76 | 68 | 5 |
| var2013 | persen | 2017–2020 | 2 | 76 | 68 | 7 |
| var2753 [arus=bongkar] | kilogram | 2021–2025 | 5 | 190 | 180 | 34 |
| var2753 [arus=muat] | kilogram | 2021–2025 | 5 | 190 | 180 | 36 |
| var2754 [arus=bongkar] | kilogram | 2021–2025 | 5 | 190 | 190 | 35 |
| var2754 [arus=muat] | kilogram | 2021–2025 | 5 | 190 | 190 | 47 |

## Status sel

| indikator | batas_lama | belum_ada | terisi | tidak_diterbitkan |
|---|---|---|---|---|
| var1241 | 4 | 32 | 382 | 0 |
| var2012 | 0 | 8 | 68 | 0 |
| var2013 | 0 | 8 | 68 | 0 |
| var2753 [arus=bongkar] | 0 | 2 | 180 | 8 |
| var2753 [arus=muat] | 0 | 2 | 180 | 8 |
| var2754 [arus=bongkar] | 0 | 0 | 190 | 0 |
| var2754 [arus=muat] | 0 | 0 | 190 | 0 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 1,330 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 394 baris x 11 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
