# Kasus 23 — Kerusakan dan kerugian bencana

Klaster G. Bencana (BNPB), Tujuan SDG 1, 11. Sebelas seri provinsi BNPB (`kejadian`, `rumah_rusak`,
`rumah_terendam`, `fasyankes_rusak`, `satuan_pendidikan_rusak`, `jembatan_rusak`, `kantor_rusak`,
`rumah_ibadat_rusak`, `kios_toko_rusak`, `pabrik_rusak`, `nilai_kerusakan`, `nilai_kerugian`), dua seri luas yang
hanya terbit nasional, dan satu pembanding WDI (`EN.CLC.MDAT.ZS`). Paket `k23-kerusakan-kerugian-bencana.zip`,
58 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Sel Provinsi tergabung di rekap XLSX: tanpa diisi, rekap kab/kota hanya membawa satu kab/kota per provinsi.
- Tabel nilai adalah daftar usulan rehabilitasi-rekonstruksi: ada usulan beberapa tahun kejadian dan usulan berulang.
- Luas lahan terbakar 2012 = 44 juta ha (mustahil).
- Rumah rusak kadang per tingkat (berat, sedang, ringan), kadang tidak.
- Luas sawah dan lahan hanya terbit nasional dan tidak menyatakan satuan.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
