# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-20/json/sdg3_3_8_1_a_v1402.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-20/json/sdg3_3_8_2_a_v2279.json | bps_json | data | 152 | 2 halaman |
| bps/2026-10-20/json/sdg3_3_c_1_v1477.json | bps_json | data | 926 | 1 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg3_3_8_1_a_v1402.csv | bps_csv | data | 393 |  |
| bps/2026-10-20/sdg3_3_8_2_a_v2279.csv | bps_csv | data | 152 |  |
| bps/2026-10-20/sdg3_3_c_1_v1477.csv | bps_csv | data | 926 |  |
| who_gho/2026-10-20/datadot/217795A_HWF_0001.csv | who_csv | data | 13 |  |
| who_gho/2026-10-20/datadot/5C8435F_HWF_0006.csv | who_csv | data | 13 |  |
| who_gho/2026-10-20/datadot/9A706FD_UHC_INDEX_REPORTED.csv | who_csv | data | 24 |  |
| who_gho/2026-10-20/datadot/A65146D_FINPROTECTION_CATA_TOT_10_POP.csv | who_csv | data | 201 |  |
| who_gho/2026-10-20/datadot/ddiindicators_skip0000.json | who_ddi | meta | 4 | definisi lengkap seri kasus |
| who_gho/2026-10-20/odata/Indicator.json | who_odata | meta | 4 |  |

Jumlah: 13 berkas dari 13 di MANIFEST, 3,193 baris mentah di berkas data.
