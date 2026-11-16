# Kasus 10 — Kesetaraan gender

Klaster C. Gender dan ketenagakerjaan, Tujuan SDG 5. Dua seri provinsi BPS (`var1360` perkawinan anak, `var2003`
perempuan manajer), dua pembanding WDI (`SG.GEN.PARL.ZS`, `SP.M18.2024.FE.ZS`), dan dua seri ILOSTAT
(`SDG_0552_NOC_RT`, `SDG_T552_NOC_RT`). Paket `k10-kesetaraan-gender.zip`, 15 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Dua seri ILO 5.5.2 berbeda definisi (senior dan menengah vs seluruh manajemen); BPS dekat dengan seluruh manajemen.
- `OBS_STATUS` B menandai patahan seri; arti kode lain tidak ada di DSD paket.
- ILO T552 2016 melonjak dua kali lipat tanpa tanda patahan.
- Satuan `var2003` kosong di katalog.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
