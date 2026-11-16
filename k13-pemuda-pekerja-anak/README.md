# Kasus 13 — Pemuda dan pekerja anak

Klaster C. Gender dan ketenagakerjaan, Tujuan SDG 8. Dua seri provinsi BPS (`var1186` NEET, `var2658` pekerja anak),
dua pembanding WDI (`SL.UEM.NEET.ZS`, `SL.TLF.0714.ZS`), dan tiga seri ILOSTAT (`SDG_0861_SEX_RT`,
`SDG_A871_SEX_AGE_RT`, `SDG_B871_SEX_AGE_RT`). Paket `k13-pemuda-pekerja-anak.zip`, 16 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Pekerja anak: BPS 5–17, ILO hanya 15–17 (lihat kolom AGE, bukan hanya DSD), WDI 7–14.
- B871 sama dengan A871 untuk umur 15–17.
- WDI anak bekerja tidak tumpang tindih tahun dengan BPS; itu bukan missing.
- Berkas ILO B871 hanya 3 baris.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
