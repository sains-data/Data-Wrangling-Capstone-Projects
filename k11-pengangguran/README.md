# Kasus 11 — Pengangguran

Klaster C. Gender dan ketenagakerjaan, Tujuan SDG 8. Satu seri provinsi BPS (`var543` TPT), dua pembanding WDI
(`SL.UEM.TOTL.ZS`, `SL.UEM.TOTL.NE.ZS`), dan tiga seri ILOSTAT (`SDG_0852_SEX_AGE_RT`, `SDG_0852_SEX_DSB_RT`,
`UNE_DEAP_SEX_AGE_RT`). Paket `k11-pengangguran.zip`, 14 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- TPT BPS tahunan sampai 2004, lalu Februari dan Agustus; jangan dirata-rata.
- ILO memakai rujukan Agustus; BPS Agustus tetap 1–3 poin di atas ILO karena definisinya.
- Satu berkas ILO berisi data tahunan dan triwulanan.
- 28 kode umur ILO dari empat klasifikasi; total 15+ muncul berkali-kali.
- 1995 tanpa Sakernas; 2000 tanpa Maluku.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
