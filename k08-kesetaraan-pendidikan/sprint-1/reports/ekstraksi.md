# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg4_4_5_1_v2595.json | bps_json | data | 218 | 2 halaman |
| bps/2026-10-17/json/sdg4_4_5_1_v2600.json | bps_json | data | 218 | 2 halaman |
| bps/2026-10-17/json/sdg4_apm.json | bps_json | data | 2376 | 8 halaman |
| bps/2026-10-17/json/sdg4_aps.json | bps_json | data | 1572 | 4 halaman |
| bps/2026-10-17/json/sdg4_completion.json | bps_json | data | 945 | 3 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg4_4_5_1_v2595.csv | bps_csv | data | 218 |  |
| bps/2026-10-17/sdg4_4_5_1_v2600.csv | bps_csv | data | 218 |  |
| bps/2026-10-17/sdg4_apm.csv | bps_csv | data | 2376 |  |
| bps/2026-10-17/sdg4_aps.csv | bps_csv | data | 1572 |  |
| bps/2026-10-17/sdg4_completion.csv | bps_csv | data | 945 |  |
| wdi/2026-10-20/data/kelompok-03-hal-01.json | wdi_data | data | 132 | 3,432 baris di berkas, 2 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |

Jumlah: 15 berkas dari 15 di MANIFEST, 10,790 baris mentah di berkas data.
