# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg16_16_1_3_a_v1311.json | bps_json | data | 285 | 4 halaman |
| bps/2026-10-17/json/sdg16_16_1_4_v1312.json | bps_json | data | 143 | 2 halaman |
| bps/2026-10-17/json/sdg16_16_2_1_a_v2738.json | bps_json | data | 69 | 1 halaman |
| bps/2026-10-17/json/sdg16_16_3_1_a_v2740.json | bps_json | data | 135 | 2 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg16_16_1_3_a_v1311.csv | bps_csv | data | 285 |  |
| bps/2026-10-17/sdg16_16_1_4_v1312.csv | bps_csv | data | 143 |  |
| bps/2026-10-17/sdg16_16_2_1_a_v2738.csv | bps_csv | data | 69 |  |
| bps/2026-10-17/sdg16_16_3_1_a_v2740.csv | bps_csv | data | 135 |  |
| bps/2026-10-20/json/sdg16_16_1_3_a_v1311.json | bps_json | data | 285 | 4 halaman |
| bps/2026-10-20/json/sdg16_16_1_4_v1312.json | bps_json | data | 143 | 2 halaman |
| bps/2026-10-20/json/sdg16_16_2_1_a_v2738.json | bps_json | data | 69 | 1 halaman |
| bps/2026-10-20/json/sdg16_16_3_1_a_v2740.json | bps_json | data | 135 | 2 halaman |
| bps/2026-10-20/json/sdg16_16_9_1_b_v1831.json | bps_json | data | 331 | 3 halaman |
| bps/2026-10-20/json/sdg16_16_9_1_v1410.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg16_16_1_3_a_v1311.csv | bps_csv | data | 285 |  |
| bps/2026-10-20/sdg16_16_1_4_v1312.csv | bps_csv | data | 143 |  |
| bps/2026-10-20/sdg16_16_2_1_a_v2738.csv | bps_csv | data | 69 |  |
| bps/2026-10-20/sdg16_16_3_1_a_v2740.csv | bps_csv | data | 135 |  |
| bps/2026-10-20/sdg16_16_9_1_b_v1831.csv | bps_csv | data | 331 |  |
| bps/2026-10-20/sdg16_16_9_1_v1410.csv | bps_csv | data | 393 |  |
| wdi/2026-10-20/data/kelompok-07-hal-01.json | wdi_data | data | 132 | 2,112 baris di berkas, 2 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |

Jumlah: 26 berkas dari 26 di MANIFEST, 4,108 baris mentah di berkas data.
