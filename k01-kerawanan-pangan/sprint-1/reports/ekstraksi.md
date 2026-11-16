# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-20/json/sdg2_2_1_1_v1473.json | bps_json | data | 323 | 3 halaman |
| bps/2026-10-20/json/sdg2_2_1_2_v1474.json | bps_json | data | 323 | 3 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg2_2_1_1_v1473.csv | bps_csv | data | 323 |  |
| bps/2026-10-20/sdg2_2_1_2_v1474.csv | bps_csv | data | 323 |  |
| wdi/2026-10-20/data/kelompok-07-hal-01.json | wdi_data | data | 132 | 2,112 baris di berkas, 2 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| who_gho/2026-10-20/datadot/5F8A486_NUTSTUNTINGPREV.csv | who_csv | data | 75 |  |
| who_gho/2026-10-20/datadot/64E2430_NUTOVERWEIGHTPREV.csv | who_csv | data | 75 |  |
| who_gho/2026-10-20/datadot/FC5231F_NUTRITION_WH_2.csv | who_csv | data | 610 |  |
| who_gho/2026-10-20/datadot/ddiindicators_skip0000.json | who_ddi | meta | 3 | definisi lengkap seri kasus |
| who_gho/2026-10-20/odata/Indicator.json | who_odata | meta | 3 |  |

Jumlah: 14 berkas dari 14 di MANIFEST, 2,184 baris mentah di berkas data.
