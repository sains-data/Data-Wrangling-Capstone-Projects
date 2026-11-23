# Kasus 19 — Hunian dan transportasi

Klaster E. Infrastruktur dan permukiman, Tujuan SDG 9 dan 11. Lima seri provinsi BPS (`var1241` hunian layak,
`var2012` akses transportasi umum, `var2013` pengguna kendaraan umum, `var2753` bongkar muat kapal, `var2754`
bongkar muat pesawat) dan satu pembanding nasional (WDI `EN.POP.SLUM.UR.ZS`). Paket `k19-hunian-transportasi.zip`,
22 berkas, snapshot BPS 17 dan 20 Oktober 2026, WDI 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Hunian layak turun di hampir semua provinsi 2018→2019 karena definisinya berganti; jangan di-*winsorize*.
- Moda bongkar muat hanya terbaca di judul JSON.
- Statistik kapal tidak memuat DIY dan Papua Pegunungan.
- Tiga seri ada di dua snapshot.
- Hunian layak dan penduduk kumuh berlawanan arah.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
