# Kasus 16 — Ketimpangan dan layanan dasar

Klaster D. Kemiskinan dan ketimpangan, Tujuan SDG 1, 10, dan 17. Tiga seri provinsi BPS (`var2011`, `var2016`,
`var1254`), dua pembanding WDI (`SI.DST.50MD`, `SI.POV.DDAY`), dan tiga seri ILOSTAT (`SDG_0111_SEX_AGE_RT`,
`SDG_0131_SEX_SOC_RT`, `SDG_1041_NOC_RT`). Paket `k16-ketimpangan-layanan-dasar.zip`, 18 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Provinsi kosong di `var2011` ditekan karena RSE (catatan penerbit), bukan missing.
- Layanan mobilitas ada di daftar turvar tetapi tanpa angka.
- Pendapatan pemerintah hanya dua tahun; jangan diimputasi di Silver.
- Kode status ILO A, R, M tidak dijelaskan di DSD paket.
- Kemiskinan pekerja (ILO) bukan kemiskinan penduduk (WDI).

Mulai dari [sprint-1/README.md](sprint-1/README.md).
