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
| var1186 | persen | 2015–2025 | 11 | 418 | 382 | 41 |
| var2658 | persen | 2020–2025 | 6 | 228 | 206 | 31 |

## Status sel

| indikator | batas_lama | belum_ada | missing | terisi |
|---|---|---|---|---|
| var1186 | 4 | 32 | 0 | 382 |
| var2658 | 4 | 12 | 6 | 206 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 646 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 382 baris x 6 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
