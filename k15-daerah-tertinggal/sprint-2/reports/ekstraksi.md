# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-20/json/sdg10_10_1_1_c_v2191.json | bps_json | data | 306 | 1 halaman |
| bps/2026-10-20/json/sdg10_10_1_1_d_v2190.json | bps_json | data | 102 | 1 halaman |
| bps/2026-10-20/json/sdg10_10_1_1_f_v192.json | bps_json | data | 3461 | 7 halaman |
| bps/2026-10-20/manifest_asal.json | bps_manifest_asal | meta | 36 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-20/sdg10_10_1_1_c_v2191.csv | bps_csv | data | 306 |  |
| bps/2026-10-20/sdg10_10_1_1_d_v2190.csv | bps_csv | data | 102 |  |
| bps/2026-10-20/sdg10_10_1_1_f_v192.csv | bps_csv | data | 3461 |  |
| wdi/2026-10-20/data/kelompok-06-hal-01.json | wdi_data | data | 66 | 3,894 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |

Jumlah: 11 berkas dari 11 di MANIFEST, 7,804 baris mentah di berkas data.
