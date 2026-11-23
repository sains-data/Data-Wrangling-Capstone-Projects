# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-20/json/sdg5_5_3_1_v1360.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-20/json/sdg5_5_5_2_v2003.json | bps_json | data | 391 | 4 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg5_5_3_1_v1360.csv | bps_csv | data | 393 |  |
| bps/2026-10-20/sdg5_5_5_2_v2003.csv | bps_csv | data | 391 |  |
| ilostat/2026-10-20/data/DF_SDG_0552_NOC_RT.csv | ilo_csv | data | 5 | dimensi: (tanpa rincian); FREQ A |
| ilostat/2026-10-20/data/DF_SDG_T552_NOC_RT.csv | ilo_csv | data | 15 | dimensi: (tanpa rincian); FREQ A |
| ilostat/2026-10-20/dsd/SDG_0552_NOC_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/SDG_T552_NOC_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/metadata/dataflow.json | ilo_dataflow | meta | 2 | 1,215 dataflow ILOSTAT, 2 seri kasus disaring |
| wdi/2026-10-20/data/kelompok-05-hal-01.json | wdi_data | data | 66 | 3,960 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/data/kelompok-07-hal-01.json | wdi_data | data | 66 | 2,112 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |

Jumlah: 15 berkas dari 15 di MANIFEST, 1,720 baris mentah di berkas data.
