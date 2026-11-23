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
| var1254 | persen | 2015–2016 | 2 | 76 | 68 | 7 |
| var2011 | persen | 2018–2023 | 6 | 228 | 199 | 13 |
| var2016 [layanan=air_minum] | persen | 2019–2023 | 5 | 190 | 170 | 10 |
| var2016 [layanan=kesehatan] | persen | 2019–2023 | 5 | 190 | 170 | 15 |
| var2016 [layanan=sanitasi] | persen | 2019–2023 | 5 | 190 | 170 | 13 |

## Status sel

| indikator | batas_lama | belum_ada | terisi | tidak_diterbitkan |
|---|---|---|---|---|
| var1254 | 0 | 8 | 68 | 0 |
| var2011 | 0 | 20 | 199 | 9 |
| var2016 [layanan=air_minum] | 4 | 16 | 170 | 0 |
| var2016 [layanan=kesehatan] | 4 | 16 | 170 | 0 |
| var2016 [layanan=sanitasi] | 4 | 16 | 170 | 0 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 874 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 272 baris x 9 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
