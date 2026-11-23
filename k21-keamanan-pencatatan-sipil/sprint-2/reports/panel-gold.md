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
| var1311 | persen | 2015–2024 | 10 | 380 | 275 | 32 |
| var1312 | persen | 2014–2025 | 4 | 152 | 139 | 9 |
| var1410 | persen | 2015–2025 | 11 | 418 | 382 | 32 |
| var1831 | persen | 2015–2023 | 9 | 342 | 322 | 41 |
| var2738 | persen | 2014–2020 | 2 | 76 | 67 | 1 |
| var2740 | persen | 2020–2024 | 5 | 190 | 130 | 0 |

## Status sel

| indikator | batas_lama | belum_ada | missing | terisi |
|---|---|---|---|---|
| var1311 | 4 | 32 | 69 | 275 |
| var1312 | 1 | 12 | 0 | 139 |
| var1410 | 4 | 32 | 0 | 382 |
| var1831 | 0 | 20 | 0 | 322 |
| var2738 | 1 | 8 | 0 | 67 |
| var2740 | 1 | 12 | 47 | 130 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 1,558 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 431 baris x 10 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
