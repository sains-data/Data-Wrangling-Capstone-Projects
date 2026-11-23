# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg15_iklh.json | bps_json | data | 1179 | 2 halaman |
| bps/2026-10-17/json/sdg15_lahan_kritis.json | bps_json | data | 399 | 2 halaman |
| bps/2026-10-17/json/sdg15_tutupan_hutan.json | bps_statis_html | data | 1735 | tabel statis: HTML diratakan, 2 blok x 4 tingkat header |
| bps/2026-10-17/json/sdg15_tutupan_kawasan.json | bps_json | data | 627 | 2 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg15_iklh.csv | bps_csv | data | 1179 |  |
| bps/2026-10-17/sdg15_lahan_kritis.csv | bps_csv | data | 399 |  |
| bps/2026-10-17/sdg15_tutupan_hutan.csv | bps_statis | data | 1770 | tabel statis (nama wilayah, tanpa var_id) |
| bps/2026-10-17/sdg15_tutupan_kawasan.csv | bps_csv | data | 627 |  |
| wdi/2026-10-20/data/kelompok-01-hal-01.json | wdi_data | data | 198 | 3,960 baris di berkas, 3 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 3 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 3 | metadata seri kasus saja |

Jumlah: 13 berkas dari 13 di MANIFEST, 8,113 baris mentah di berkas data.
