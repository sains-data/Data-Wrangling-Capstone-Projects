# Panel Gold provinsi x periode x indikator

Dihasilkan `python pipeline.py` (`src/gold/panel.py`) dari Silver, grid, dan kategori anomali Sprint 1.

## Aturan satu nilai per sel

1. **Snapshot**: seri yang ada di dua snapshot memakai snapshot terbaru; angka snapshot lain dibandingkan di `reports/snapshot-bps.csv` (bila ada).
2. **Rincian**: satu indikator = satu deret utama (`total`, atau rincian di `DERET`). Rincian lain tetap di Silver.
3. **Berkas**: bila satu sel punya beberapa berkas, `URUTAN_BERKAS` memilih satu (`reports/deret-berkas.csv`).
4. **Periode**: disimpan apa adanya; tidak dirata-rata ke tahunan.
5. **Penanda**: outlier, patahan, dan galat input dari Sprint 1 ikut sebagai kolom `penanda`; nilainya tidak diubah.

Baris Silver provinsi yang tidak masuk panel (rincian lain atau berkas lain): 612.

## Indikator

| indikator | satuan | periode | jumlah_periode | sel | terisi | ditandai |
|---|---|---|---|---|---|---|
| var1402 | persen | 2015–2025 | 11 | 418 | 382 | 40 |
| var1477 [profesi=bidan] | per_100000_penduduk | 2016–2018 | 3 | 114 | 102 | 7 |
| var1477 [profesi=dokter_umum] | per_100000_penduduk | 2016–2018 | 3 | 114 | 102 | 10 |
| var1477 [profesi=perawat] | per_100000_penduduk | 2016–2018 | 3 | 114 | 102 | 4 |
| var2279 | persen | 2022–2025 | 4 | 152 | 148 | 1 |

## Status sel

| indikator | batas_lama | belum_ada | terisi |
|---|---|---|---|
| var1402 | 4 | 32 | 382 |
| var1477 [profesi=bidan] | 0 | 12 | 102 |
| var1477 [profesi=dokter_umum] | 0 | 12 | 102 |
| var1477 [profesi=perawat] | 0 | 12 | 102 |
| var2279 | 0 | 4 | 148 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 912 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 386 baris x 9 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
