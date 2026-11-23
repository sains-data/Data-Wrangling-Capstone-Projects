# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg8_produktivitas.json | bps_json | data | 524 | 5 halaman |
| bps/2026-10-17/json/sdg9_9_2_2_v2755.json | bps_json | data | 288 | 3 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg8_produktivitas.csv | bps_csv | data | 524 |  |
| bps/2026-10-17/sdg9_9_2_2_v2755.csv | bps_csv | data | 288 |  |
| bps/2026-10-20/json/sdg2_2_3_1_a_v1344.json | bps_json | data | 315 | 3 halaman |
| bps/2026-10-20/json/sdg9_9_2_1_v1214.json | bps_json | data | 494 | 5 halaman |
| bps/2026-10-20/json/sdg9_9_2_2_v2755.json | bps_json | data | 288 | 3 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg2_2_3_1_a_v1344.csv | bps_csv | data | 315 |  |
| bps/2026-10-20/sdg9_9_2_1_v1214.csv | bps_csv | data | 494 |  |
| bps/2026-10-20/sdg9_9_2_2_v2755.csv | bps_csv | data | 288 |  |
| ilostat/2026-10-20/data/DF_SDG_0821_NOC_RT.csv | ilo_csv | data | 28 | dimensi: (tanpa rincian); FREQ A |
| ilostat/2026-10-20/data/DF_SDG_0922_NOC_RT.csv | ilo_csv | data | 24 | dimensi: (tanpa rincian); FREQ A |
| ilostat/2026-10-20/data/DF_SDG_B821_NOC_RT.csv | ilo_csv | data | 28 | dimensi: (tanpa rincian); FREQ A |
| ilostat/2026-10-20/dsd/SDG_0821_NOC_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/SDG_0922_NOC_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/SDG_B821_NOC_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/metadata/dataflow.json | ilo_dataflow | meta | 3 | 1,215 dataflow ILOSTAT, 3 seri kasus disaring |
| wdi/2026-10-20/data/kelompok-02-hal-01.json | wdi_data | data | 66 | 3,960 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/data/kelompok-06-hal-01.json | wdi_data | data | 66 | 3,894 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |

Jumlah: 24 berkas dari 24 di MANIFEST, 4,030 baris mentah di berkas data.
