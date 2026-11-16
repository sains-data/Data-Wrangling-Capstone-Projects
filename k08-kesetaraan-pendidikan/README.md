# Kasus 08 — Kesetaraan pendidikan

Klaster B. Pendidikan, Tujuan SDG 4. Lima seri provinsi BPS (`var304` APM, `var2595` paritas kuintil APK SMA,
`var2600` paritas jenis kelamin APK PT, `var1980` tingkat penyelesaian, `var2211` APS) dan dua pembanding nasional
(WDI `SE.ENR.PRSC.FM.ZS`, `SE.PRM.CMPT.ZS`). Paket `k08-kesetaraan-pendidikan.zip`, 15 berkas, snapshot BPS
17 Oktober 2026, WDI 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Tiga seri berkode 4.5.1; jenis rasio (kuintil atau jenis kelamin) dan jenjangnya hanya ada di judul JSON.
- Rasio BPS ditulis dikali 100; GPI WDI tidak.
- `var.note` APS berisi definisi indikator lain.
- Penyelesaian SD BPS dan WDI berbeda definisi.
- APM mencakup paket A/B/C mulai 2007; Aceh 2005 kosong.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
