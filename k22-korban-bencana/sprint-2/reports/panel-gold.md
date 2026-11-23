# Panel Gold provinsi x periode x indikator

Dihasilkan `python pipeline.py` (`src/gold/panel.py`) dari Silver, grid, dan kategori anomali Sprint 1.

## Aturan satu nilai per sel

1. **Snapshot**: seri yang ada di dua snapshot memakai snapshot terbaru; angka snapshot lain dibandingkan di `reports/snapshot-bps.csv` (bila ada).
2. **Rincian**: satu indikator = satu deret utama (`total`, atau rincian di `DERET`). Rincian lain tetap di Silver.
3. **Berkas**: bila satu sel punya beberapa berkas, `URUTAN_BERKAS` memilih satu (`reports/deret-berkas.csv`).
4. **Periode**: disimpan apa adanya; tidak dirata-rata ke tahunan.
5. **Penanda**: outlier, patahan, dan galat input dari Sprint 1 ikut sebagai kolom `penanda`; nilainya tidak diubah.

Baris Silver provinsi yang tidak masuk panel (rincian lain atau berkas lain): 11,852.

## Indikator

| indikator | satuan | periode | jumlah_periode | sel | terisi | ditandai |
|---|---|---|---|---|---|---|
| jumlah_penduduk | jiwa | 2025 | 1 | 38 | 38 | 0 |
| kejadian [jumlah] | kejadian | 2010–2025 | 16 | 608 | 608 | 62 |
| korban_hilang [jumlah] | jiwa | 2010–2025 | 16 | 608 | 144 | 21 |
| korban_luka_sakit [jumlah] | jiwa | 2010–2025 | 16 | 608 | 144 | 10 |
| korban_mengungsi [jumlah] | jiwa | 2010–2025 | 16 | 608 | 76 | 3 |
| korban_mengungsi_per_100rb [jumlah] | per_100000_penduduk | 2025 | 1 | 38 | 38 | 1 |
| korban_meninggal [jumlah] | jiwa | 2021–2025 | 4 | 152 | 144 | 10 |
| korban_meninggal_hilang_per_100rb [jumlah] | per_100000_penduduk | 2025 | 1 | 38 | 38 | 5 |
| korban_terdampak [jumlah] | jiwa | 2010–2025 | 16 | 608 | 76 | 3 |
| korban_terdampak_mengungsi [jumlah] | jiwa | 2021–2022 | 2 | 76 | 68 | 4 |

## Status sel

| indikator | belum_ada | terisi | tidak_diterbitkan |
|---|---|---|---|
| jumlah_penduduk | 0 | 38 | 0 |
| kejadian [jumlah] | 0 | 608 | 0 |
| korban_hilang [jumlah] | 55 | 144 | 409 |
| korban_luka_sakit [jumlah] | 55 | 144 | 409 |
| korban_mengungsi [jumlah] | 55 | 76 | 477 |
| korban_mengungsi_per_100rb [jumlah] | 0 | 38 | 0 |
| korban_meninggal [jumlah] | 8 | 144 | 0 |
| korban_meninggal_hilang_per_100rb [jumlah] | 0 | 38 | 0 |
| korban_terdampak [jumlah] | 55 | 76 | 477 |
| korban_terdampak_mengungsi [jumlah] | 8 | 68 | 0 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 3,382 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 608 baris x 14 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
