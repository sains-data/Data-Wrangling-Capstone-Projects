# Kasus 15 — Kemiskinan dan daerah tertinggal

Klaster D. Kemiskinan dan ketimpangan, Tujuan SDG 1 dan 10. Tiga seri provinsi BPS (`var192` persentase penduduk
miskin, `var2190` desa mandiri, `var2191` desa tertinggal) dan satu pembanding nasional (WDI `SI.POV.NAHC`). Paket
`k15-daerah-tertinggal.zip`, 11 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- `var192` tahunan sampai 2011, lalu Maret dan September; September 2023 tidak ada.
- WDI memakai P0 Maret, dibulatkan satu desimal; jangan merata-ratakan semester.
- Jakarta tidak punya desa; sel kosongnya bukan missing.
- Indeks Desa berganti sumber dan daftar desa setiap tahun.
- Seri desa tidak punya baris Indonesia.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
