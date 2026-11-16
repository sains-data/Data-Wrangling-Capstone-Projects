# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg7_bahan_bakar.json | bps_statis_html | data | 3917 | tabel statis: HTML diratakan, 1 blok x 2 tingkat header, 385 sel berkoma desimal |
| bps/2026-10-17/json/sdg7_listrik_pln.json | bps_json | data | 1036 | 11 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg7_bahan_bakar.csv | bps_statis | data | 3920 | tabel statis (nama wilayah, tanpa var_id) |
| bps/2026-10-17/sdg7_listrik_pln.csv | bps_csv | data | 1036 |  |
| wdi/2026-10-20/data/kelompok-01-hal-01.json | wdi_data | data | 132 | 3,960 baris di berkas, 2 seri kasus disaring |
| wdi/2026-10-20/metadata/sumber.json | wdi_sumber | meta | 71 |  |
| wdi/2026-10-20/metadata/sumber2_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |
| wdi/2026-10-20/metadata/sumber46_indikator.json | wdi_meta | meta | 2 | metadata seri kasus saja |

Jumlah: 9 berkas dari 9 di MANIFEST, 10,041 baris mentah di berkas data.
