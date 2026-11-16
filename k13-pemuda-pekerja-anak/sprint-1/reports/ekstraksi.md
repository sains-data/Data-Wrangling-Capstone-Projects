# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg8_8_7_1_v2658.json | bps_json | data | 212 | 2 halaman |
| bps/2026-10-17/json/sdg8_neet.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg8_8_7_1_v2658.csv | bps_csv | data | 212 |  |
| bps/2026-10-17/sdg8_neet.csv | bps_csv | data | 393 |  |
| ilostat/2026-10-20/data/DF_SDG_0861_SEX_RT.csv | ilo_csv | data | 72 | dimensi: SEX; FREQ A |
| ilostat/2026-10-20/data/DF_SDG_A871_SEX_AGE_RT.csv | ilo_csv | data | 9 | dimensi: SEX, AGE; FREQ A |
| ilostat/2026-10-20/data/DF_SDG_B871_SEX_AGE_RT.csv | ilo_csv | data | 3 | dimensi: SEX, AGE; FREQ A |
| ilostat/2026-10-20/dsd/SDG_0861_SEX_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/SDG_A871_SEX_AGE_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/SDG_B871_SEX_AGE_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/metadata/dataflow.json | ilo_dataflow | meta | 3 | 1,215 dataflow ILOSTAT, 3 seri kasus disaring |
| wdi/2026-10-20/data/kelompok-06-hal-01.json | wdi_data | data | 132 | 3,894 baris di berkas, 2 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |

Jumlah: 16 berkas dari 16 di MANIFEST, 1,426 baris mentah di berkas data.
