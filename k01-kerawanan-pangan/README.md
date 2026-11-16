# Kasus 01 — Kerawanan pangan provinsi

Klaster A. Pangan dan kesehatan, Tujuan SDG 2. Dua seri provinsi BPS (`var1473` PoU, `var1474` FIES) dan lima
pembanding nasional (WDI `SN.ITK.DEFC.ZS`, `SN.ITK.MSFI.ZS`; WHO `NUTSTUNTINGPREV`, `NUTOVERWEIGHTPREV`,
`NUTRITION_WH_2`). Paket `k01-kerawanan-pangan.zip`, 14 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- `NUTRITION_WH_2` menulis "total" dengan tiga cara (semua `DIM_*` kosong, semua `TOTAL`, sebagian `TOTAL`).
  Tanpa penanganan, kunci Silver kembar. Satu sel 2008 bahkan punya dua nilai berbeda.
- Empat provinsi Papua baru terbit mulai 2024, bukan 2023. Sel 2023 mereka bukan missing: angkanya masih di
  dalam Papua dan Papua Barat.
- Papua dan Papua Barat 2023→2024 berubah karena wilayahnya mengecil, bukan karena keadaan membaik.
- sourceNote PoU WDI: angka 2.5 dapat berarti kurang dari 2,5%.
- Metadata WDI tidak menyebut apakah angka FAO tahunan atau rata-rata; selisih BPS–FAO tidak boleh dianggap galat.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
