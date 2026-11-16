# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-20/json/sdg3_3_1_2_v1541.json | bps_json | data | 175 | 2 halaman |
| bps/2026-10-20/json/sdg3_3_2_1_v1373.json | bps_json | data | 35 | 1 halaman |
| bps/2026-10-20/json/sdg3_3_2_1_v1584.json | bps_json | data | 35 | 1 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg3_3_1_2_v1541.csv | bps_csv | data | 175 |  |
| bps/2026-10-20/sdg3_3_2_1_v1373.csv | bps_csv | data | 35 |  |
| bps/2026-10-20/sdg3_3_2_1_v1584.csv | bps_csv | data | 35 |  |
| wdi/2026-10-20/data/kelompok-05-hal-01.json | wdi_data | data | 198 | 3,960 baris di berkas, 3 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 3 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 3 | metadata seri kasus saja |
| who_gho/2026-10-20/datadot/2322814_MDG_0000000007.csv | who_csv | data | 387 |  |
| who_gho/2026-10-20/datadot/A4C49D3_WHOSIS_000003.csv | who_csv | data | 71 |  |
| who_gho/2026-10-20/datadot/AC597B1_MDG_0000000026.csv | who_csv | data | 39 |  |
| who_gho/2026-10-20/datadot/ddiindicators_skip0000.json | who_ddi | meta | 3 | definisi lengkap seri kasus |
| who_gho/2026-10-20/odata/Indicator.json | who_odata | meta | 3 |  |

Jumlah: 16 berkas dari 16 di MANIFEST, 1,185 baris mentah di berkas data.
