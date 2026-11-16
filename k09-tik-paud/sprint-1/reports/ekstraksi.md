# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg4_4_4_1_a_v1451.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-17/json/sdg4_4_4_1_b_v1447.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-17/json/sdg4_apk_paud.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-17/json/sdg5_5_b_1_v1221.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg4_4_4_1_a_v1451.csv | bps_csv | data | 393 |  |
| bps/2026-10-17/sdg4_4_4_1_b_v1447.csv | bps_csv | data | 393 |  |
| bps/2026-10-17/sdg4_apk_paud.csv | bps_csv | data | 393 |  |
| bps/2026-10-17/sdg5_5_b_1_v1221.csv | bps_csv | data | 393 |  |
| bps/2026-10-20/json/sdg5_5_b_1_v1221.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg5_5_b_1_v1221.csv | bps_csv | data | 393 |  |
| wdi/2026-10-20/data/kelompok-02-hal-01.json | wdi_data | data | 66 | 3,960 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/data/kelompok-03-hal-01.json | wdi_data | data | 66 | 3,432 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |

Jumlah: 17 berkas dari 17 di MANIFEST, 4,062 baris mentah di berkas data.
