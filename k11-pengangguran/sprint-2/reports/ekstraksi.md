# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg8_tpt.json | bps_json | data | 2000 | 14 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg8_tpt.csv | bps_csv | data | 2000 |  |
| ilostat/2026-10-20/data/DF_SDG_0852_SEX_AGE_RT.csv | ilo_csv | data | 216 | dimensi: SEX, AGE; FREQ A |
| ilostat/2026-10-20/data/DF_SDG_0852_SEX_DSB_RT.csv | ilo_csv | data | 81 | dimensi: SEX, DSB; FREQ A |
| ilostat/2026-10-20/data/DF_UNE_DEAP_SEX_AGE_RT.csv | ilo_csv | data | 5424 | dimensi: SEX, AGE; FREQ A/Q |
| ilostat/2026-10-20/dsd/SDG_0852_SEX_AGE_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/SDG_0852_SEX_DSB_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/UNE_DEAP_SEX_AGE_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/metadata/dataflow.json | ilo_dataflow | meta | 3 | 1,215 dataflow ILOSTAT, 3 seri kasus disaring |
| wdi/2026-10-20/data/kelompok-07-hal-01.json | wdi_data | data | 132 | 2,112 baris di berkas, 2 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |

Jumlah: 14 berkas dari 14 di MANIFEST, 9,853 baris mentah di berkas data.
