# Kasus 20 — Hutan, lahan, dan lingkungan

Klaster F. Lingkungan dan tata kelola, Tujuan SDG 15. Tabel statis tutupan hutan (dua seri: luas dan persen), tiga
seri BPS (`var1304` penutupan lahan menurut kawasan, `var588` lahan kritis, `var2532` komponen IKLH) dan tiga
pembanding nasional (WDI `AG.LND.FRST.K2`, `AG.LND.FRST.ZS`, `EN.ATM.PM25.MC.M3`). Paket
`k20-hutan-lahan-lingkungan.zip`, 13 berkas, snapshot BPS 17 Oktober 2026, WDI 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, konversi satuan luas, Silver dan Gold di SQL, rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Kolom 2020 tabel tutupan hutan tergeser terhadap nama provinsi (kolom `cek` CSV menandainya).
- Luas dan persen dalam satu tabel statis; satu seri hanya boleh satu satuan.
- `var2532` adalah komponen IKLH (berkas `sdg15_iklh`), bukan 11.6.2.
- Tiga satuan luas: ribu hektar, hektar, km persegi.
- Indeks kualitas udara dan PM2.5 berlawanan arah.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
