# Kasus 21 — Keamanan dan pencatatan sipil

Klaster F. Lingkungan dan tata kelola, Tujuan SDG 16. Enam seri provinsi BPS (`var1311`, `var1312`, `var2738`,
`var2740`, `var1410`, `var1831`) dan dua pembanding nasional (WDI `SP.REG.BRTH.ZS`, `VC.IHR.PSRC.P5`). Paket
`k21-keamanan-pencatatan-sipil.zip`, 26 berkas, snapshot BPS 17 dan 20 Oktober 2026, WDI 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Empat seri ada di dua snapshot.
- Korban kejahatan dan pelaporan ke polisi kehilangan banyak provinsi sejak 2020, tanpa catatan.
- Periode korban kejahatan adalah tahun kejadian, bukan tahun survei.
- Dua seri akta kelahiran berbeda kelompok umur.
- Seri satu halaman dan banyak halaman harus sama-sama terbaca.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
