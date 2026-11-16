# Kasus 18 — Energi: listrik dan bahan bakar memasak

Klaster E. Infrastruktur dan permukiman, Tujuan SDG 7. Seri BPS `var87` (listrik PLN) dan tabel statis
`tabel:sdg7_bahan_bakar`, dengan dua pembanding nasional (WDI `EG.ELC.ACCS.ZS`, `EG.CFT.ACCS.ZS`). Paket
`k18-energi.zip`, 9 berkas, snapshot BPS 17 Oktober 2026, WDI 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, kategori bersih, Silver dan Gold di SQL, rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Tabel bahan bakar adalah HTML; sebagian kolomnya memakai koma desimal.
- Tahun tabel bahan bakar tidak rapat (2001, 2007–2021).
- Listrik BPS hanya PLN dan menghitung rumah tangga.
- Minyak tanah tidak termasuk bahan bakar bersih menurut WDI.
- Catatan Susenas 2000–2002: provinsi tidak dicacah atau hanya ibu kota.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
