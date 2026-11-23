# Panel Gold provinsi x periode x indikator

Dihasilkan `python pipeline.py` (`src/gold/panel.py`) dari Silver, grid, dan kategori anomali Sprint 1.

## Aturan satu nilai per sel

1. **Snapshot**: seri yang ada di dua snapshot memakai snapshot terbaru; angka snapshot lain dibandingkan di `reports/snapshot-bps.csv` (bila ada).
2. **Rincian**: satu indikator = satu deret utama (`total`, atau rincian di `DERET`). Rincian lain tetap di Silver.
3. **Berkas**: bila satu sel punya beberapa berkas, `URUTAN_BERKAS` memilih satu (`reports/deret-berkas.csv`).
4. **Periode**: disimpan apa adanya; tidak dirata-rata ke tahunan.
5. **Penanda**: outlier, patahan, dan galat input dari Sprint 1 ikut sebagai kolom `penanda`; nilainya tidak diubah.

Baris Silver provinsi yang tidak masuk panel (rincian lain atau berkas lain): 2,096.

## Indikator

| indikator | satuan | periode | jumlah_periode | sel | terisi | ditandai |
|---|---|---|---|---|---|---|
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | persen | 2001–2021 | 16 | 608 | 529 | 60 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | persen | 2001–2021 | 16 | 608 | 529 | 50 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | persen | 2001–2021 | 16 | 608 | 528 | 99 |
| var87 | persen | 1993–2025 | 32 | 1216 | 1004 | 128 |

## Status sel

| indikator | batas_lama | belum_ada | missing | terisi | tidak_diterbitkan |
|---|---|---|---|---|---|
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2 | 74 | 2 | 529 | 1 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2 | 74 | 2 | 529 | 1 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2 | 74 | 3 | 528 | 1 |
| var87 | 9 | 199 | 0 | 1004 | 4 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 3,040 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 1,004 baris x 8 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
