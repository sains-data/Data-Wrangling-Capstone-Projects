# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg4_amh.json | bps_json | data | 427 | 4 halaman |
| bps/2026-10-17/json/sdg4_amh_rinci.json | bps_statis_html | data | 5973 | tabel statis: HTML diratakan, 3 blok x 3 tingkat header |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg4_amh.csv | bps_csv | data | 427 |  |
| bps/2026-10-17/sdg4_amh_rinci.csv | bps_statis | data | 5967 | tabel statis (nama wilayah, tanpa var_id) |
| wdi/2026-10-20/data/kelompok-03-hal-01.json | wdi_data | data | 66 | 3,432 baris di berkas, 1 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 1 | metadata seri kasus saja |

Jumlah: 9 berkas dari 9 di MANIFEST, 12,860 baris mentah di berkas data.
