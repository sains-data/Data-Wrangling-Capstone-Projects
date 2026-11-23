# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-20/json/sdg10_10_2_1_v2011.json | bps_json | data | 205 | 2 halaman |
| bps/2026-10-20/json/sdg17_17_1_1_v1254.json | bps_json | data | 70 | 1 halaman |
| bps/2026-10-20/json/sdg1_1_4_1_v2016.json | bps_json | data | 525 | 2 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg10_10_2_1_v2011.csv | bps_csv | data | 205 |  |
| bps/2026-10-20/sdg17_17_1_1_v1254.csv | bps_csv | data | 70 |  |
| bps/2026-10-20/sdg1_1_4_1_v2016.csv | bps_csv | data | 525 |  |
| ilostat/2026-10-20/data/DF_SDG_0111_SEX_AGE_RT.csv | ilo_csv | data | 218 | dimensi: SEX, AGE; FREQ A |
| ilostat/2026-10-20/data/DF_SDG_0131_SEX_SOC_RT.csv | ilo_csv | data | 30 | dimensi: SEX, SOC; FREQ A |
| ilostat/2026-10-20/data/DF_SDG_1041_NOC_RT.csv | ilo_csv | data | 23 | dimensi: (tanpa rincian); FREQ A |
| ilostat/2026-10-20/dsd/SDG_0111_SEX_AGE_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/SDG_0131_SEX_SOC_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/SDG_1041_NOC_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/metadata/dataflow.json | ilo_dataflow | meta | 3 | 1,215 dataflow ILOSTAT, 3 seri kasus disaring |
| wdi/2026-10-20/data/kelompok-06-hal-01.json | wdi_data | data | 132 | 3,894 baris di berkas, 2 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |

Jumlah: 18 berkas dari 18 di MANIFEST, 2,003 baris mentah di berkas data.
