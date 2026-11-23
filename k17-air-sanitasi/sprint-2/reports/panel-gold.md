# Panel Gold provinsi x periode x indikator

Dihasilkan `python pipeline.py` (`src/gold/panel.py`) dari Silver, grid, dan kategori anomali Sprint 1.

## Aturan satu nilai per sel

1. **Snapshot**: seri yang ada di dua snapshot memakai snapshot terbaru; angka snapshot lain dibandingkan di `reports/snapshot-bps.csv` (bila ada).
2. **Rincian**: satu indikator = satu deret utama (`total`, atau rincian di `DERET`). Rincian lain tetap di Silver.
3. **Berkas**: bila satu sel punya beberapa berkas, `URUTAN_BERKAS` memilih satu (`reports/deret-berkas.csv`).
4. **Periode**: disimpan apa adanya; tidak dirata-rata ke tahunan.
5. **Penanda**: outlier, patahan, dan galat input dari Sprint 1 ikut sebagai kolom `penanda`; nilainya tidak diubah.

Baris Silver provinsi yang tidak masuk panel (rincian lain atau berkas lain): 418.

## Indikator

| indikator | satuan | periode | jumlah_periode | sel | terisi | ditandai |
|---|---|---|---|---|---|---|
| var1273 | persen | 2016–2025 | 10 | 380 | 348 | 78 |
| var2179 | persen | 2020–2025 | 6 | 228 | 212 | 32 |
| var2741 | persen | 2020–2025 | 6 | 228 | 212 | 23 |
| var2749 | persen | 2024–2025 | 2 | 76 | 74 | 4 |
| var845 | persen | 1993–2025 | 23 | 874 | 699 | 157 |
| var847 | persen | 1993–2025 | 32 | 1216 | 1004 | 109 |

## Status sel

| indikator | batas_lama | belum_ada | missing | terisi | tidak_diterbitkan |
|---|---|---|---|---|---|
| var1273 | 4 | 28 | 0 | 348 | 0 |
| var2179 | 4 | 12 | 0 | 212 | 0 |
| var2741 | 4 | 12 | 0 | 212 | 0 |
| var2749 | 0 | 0 | 2 | 74 | 0 |
| var845 | 9 | 162 | 0 | 699 | 4 |
| var847 | 9 | 199 | 0 | 1004 | 4 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 3,002 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 1,035 baris x 10 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
