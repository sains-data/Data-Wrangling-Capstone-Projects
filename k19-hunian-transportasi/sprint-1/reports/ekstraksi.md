# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg11_11_1_1_a_v1241.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-17/json/sdg9_9_1_2_v2753.json | bps_json | data | 370 | 2 halaman |
| bps/2026-10-17/json/sdg9_9_1_2_v2754.json | bps_json | data | 390 | 2 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg11_11_1_1_a_v1241.csv | bps_csv | data | 393 |  |
| bps/2026-10-17/sdg9_9_1_2_v2753.csv | bps_csv | data | 370 |  |
| bps/2026-10-17/sdg9_9_1_2_v2754.csv | bps_csv | data | 390 |  |
| bps/2026-10-20/json/sdg11_11_1_1_a_v1241.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-20/json/sdg11_11_2_1_a_v2012.json | bps_json | data | 70 | 1 halaman |
| bps/2026-10-20/json/sdg11_11_2_1_b_v2013.json | bps_json | data | 70 | 1 halaman |
| bps/2026-10-20/json/sdg9_9_1_2_v2753.json | bps_json | data | 370 | 2 halaman |
| bps/2026-10-20/json/sdg9_9_1_2_v2754.json | bps_json | data | 390 | 2 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg11_11_1_1_a_v1241.csv | bps_csv | data | 393 |  |
| bps/2026-10-20/sdg11_11_2_1_a_v2012.csv | bps_csv | data | 70 |  |
| bps/2026-10-20/sdg11_11_2_1_b_v2013.csv | bps_csv | data | 70 |  |
| bps/2026-10-20/sdg9_9_1_2_v2753.csv | bps_csv | data | 370 |  |
| bps/2026-10-20/sdg9_9_1_2_v2754.csv | bps_csv | data | 390 |  |
| wdi/2026-10-20/data/kelompok-01-hal-01.json | wdi_data | data | 66 | 3,960 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |

Jumlah: 22 berkas dari 22 di MANIFEST, 4,958 baris mentah di berkas data.
