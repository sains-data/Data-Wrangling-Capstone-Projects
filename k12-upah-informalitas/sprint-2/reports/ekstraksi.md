# Ekstraksi: jumlah baris per berkas

Dihasilkan `python pipeline.py`. Peran *data* berisi angka; *meta* berisi judul, definisi, atau catatan unduhan. Semua baris `data/raw/MANIFEST.csv` tertangani.

| berkas | pembaca | peran | baris | catatan |
|---|---|---|---|---|
| bps/2026-10-17/json/sdg8_informal.json | bps_json | data | 288 | 3 halaman |
| bps/2026-10-17/json/sdg8_upah.json | bps_json | data | 393 | 4 halaman |
| bps/2026-10-17/manifest_asal.json | bps_manifest_asal | meta | 42 | semua tabel unduhan BPS, bukan hanya kasus ini |
| bps/2026-10-17/sdg8_informal.csv | bps_csv | data | 288 |  |
| bps/2026-10-17/sdg8_upah.csv | bps_csv | data | 393 |  |
| ilostat/2026-10-20/data/DF_SDG_0831_SEX_ECO_RT.csv | ilo_csv | data | 216 | dimensi: SEX, ECO; FREQ A |
| ilostat/2026-10-20/data/DF_SDG_0851_SEX_OCU_NB.csv | ilo_csv | data | 687 | dimensi: SEX, OCU; FREQ A |
| ilostat/2026-10-20/dsd/SDG_0831_SEX_ECO_RT.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/dsd/SDG_0851_SEX_OCU_NB.json | ilo_dsd | meta | 1 |  |
| ilostat/2026-10-20/metadata/dataflow.json | ilo_dataflow | meta | 2 | 1,215 dataflow ILOSTAT, 2 seri kasus disaring |

Jumlah: 10 berkas dari 10 di MANIFEST, 2,265 baris mentah di berkas data.
