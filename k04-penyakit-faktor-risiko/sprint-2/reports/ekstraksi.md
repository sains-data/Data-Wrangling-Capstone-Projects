# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-20/json/sdg3_3_3_3_v1393.json | bps_json | data | 416 | 4 halaman |
| bps/2026-10-20/json/sdg3_3_4_1_b_v1480.json | bps_json | data | 104 | 2 halaman |
| bps/2026-10-20/json/sdg3_3_a_1_v1435.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg3_3_3_3_v1393.csv | bps_csv | data | 416 |  |
| bps/2026-10-20/sdg3_3_4_1_b_v1480.csv | bps_csv | data | 104 |  |
| bps/2026-10-20/sdg3_3_a_1_v1435.csv | bps_csv | data | 393 |  |
| wdi/2026-10-20/data/kelompok-05-hal-01.json | wdi_data | data | 66 | 3,960 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |
| who_gho/2026-10-20/datadot/1F96863_NCDMORT3070.csv | who_csv | data | 66 |  |
| who_gho/2026-10-20/datadot/442CEA8_MALARIA_EST_INCIDENCE.csv | who_csv | data | 24 |  |
| who_gho/2026-10-20/datadot/75DDA77_M_Est_tob_curr_std.csv | who_csv | data | 30 |  |
| who_gho/2026-10-20/datadot/ddiindicators_skip0000.json | who_ddi | meta | 3 | definisi lengkap seri kasus |
| who_gho/2026-10-20/odata/Indicator.json | who_odata | meta | 3 |  |

Jumlah: 16 berkas dari 16 di MANIFEST, 2,012 baris mentah di berkas data.
