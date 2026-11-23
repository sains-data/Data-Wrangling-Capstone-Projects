# Panel Gold provinsi x periode x indikator

Dihasilkan `python pipeline.py` (`src/gold/panel.py`) dari Silver, grid, dan kategori anomali Sprint 1.

## Aturan satu nilai per sel

1. **Snapshot**: seri yang ada di dua snapshot memakai snapshot terbaru; angka snapshot lain dibandingkan di `reports/snapshot-bps.csv` (bila ada).
2. **Rincian**: satu indikator = satu deret utama (`total`, atau rincian di `DERET`). Rincian lain tetap di Silver.
3. **Berkas**: bila satu sel punya beberapa berkas, `URUTAN_BERKAS` memilih satu (`reports/deret-berkas.csv`).
4. **Periode**: disimpan apa adanya; tidak dirata-rata ke tahunan.
5. **Penanda**: outlier, patahan, dan galat input dari Sprint 1 ikut sebagai kolom `penanda`; nilainya tidak diubah.

Baris Silver provinsi yang tidak masuk panel (rincian lain atau berkas lain): 2,184.

## Indikator

| indikator | satuan | periode | jumlah_periode | sel | terisi | ditandai |
|---|---|---|---|---|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | ribu_hektar | 2014–2023 | 10 | 380 | 337 | 56 |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | persen | 2014–2023 | 10 | 380 | 337 | 57 |
| var1304 | ribu_hektar | 2014–2023 | 6 | 228 | 203 | 54 |
| var2532 [komponen=ika] | indeks | 2019–2024 | 6 | 228 | 212 | 32 |
| var2532 [komponen=iktl] | indeks | 2019–2024 | 6 | 228 | 211 | 45 |
| var2532 [komponen=iku] | indeks | 2019–2024 | 6 | 228 | 212 | 48 |
| var588 | hektar | 2006–2018 | 4 | 152 | 129 | 21 |

## Status sel

| indikator | batas_lama | belum_ada | terisi | tidak_diterbitkan |
|---|---|---|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | 7 | 36 | 337 | 0 |
| tabel:sdg15_tutupan_hutan:persen [tutupan=hutan] | 7 | 36 | 337 | 0 |
| var1304 | 5 | 20 | 203 | 0 |
| var2532 [komponen=ika] | 0 | 16 | 212 | 0 |
| var2532 [komponen=iktl] | 1 | 16 | 211 | 0 |
| var2532 [komponen=iku] | 0 | 16 | 212 | 0 |
| var588 | 1 | 18 | 129 | 4 |

`terisi` = ada angka; kategori lain berasal dari grid Sprint 1 (`reports/kelengkapan-panel.md`). Sel kosong tidak diisi: tidak ada interpolasi di Gold.

## Berkas

- `data/gold/panel.parquet`: 1,824 baris (panjang, termasuk sel kosong).
- `data/gold/panel_lebar.parquet`: 474 baris x 11 kolom (hanya sel terisi; satu kolom per indikator, satuan per indikator di `docs/data-dictionary.md`).
