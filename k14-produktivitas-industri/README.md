# Kasus 14 — Produktivitas dan industri

Klaster C. Gender dan ketenagakerjaan, Tujuan SDG 2, 8, dan 9. Empat seri provinsi BPS (`var1161`, `var1344`, `var1214`,
`var2755`), dua pembanding WDI (`SL.GDP.PCAP.EM.KD`, `NV.IND.MANF.ZS`), dan tiga seri ILOSTAT (`SDG_0821_NOC_RT`,
`SDG_B821_NOC_RT`, `SDG_0922_NOC_RT`). Paket `k14-produktivitas-industri.zip`, 24 berkas, snapshot BPS 17 dan
20 Oktober 2026, WDI dan ILOSTAT 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, laju dari WDI, Silver dan Gold di SQL, rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Dua kunci JSON produktivitas tidak cocok dengan daftar label.
- Laju produktivitas bisa negatif; satuan persen 0–100 menolaknya.
- Dua seri ILO 8.2.1 beda basis harga, lajunya sama; keduanya memuat proyeksi 2026–2027.
- WDI menerbitkan tingkat PDB per pekerja, bukan laju.
- `var2755` ada di dua snapshot.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
