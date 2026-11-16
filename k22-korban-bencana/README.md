# Kasus 22 — Korban bencana

Klaster G. Bencana (BNPB), Tujuan SDG 1, 11, 13. Sembilan seri provinsi BNPB (`kejadian`, `korban_meninggal`,
`korban_hilang`, `korban_luka_sakit`, `korban_mengungsi`, `korban_terdampak`, `korban_terdampak_mengungsi`,
`korban_mengungsi_per_100rb`, `korban_meninggal_hilang_per_100rb`) dengan penyebut `jumlah_penduduk`, dan satu
pembanding nasional (WDI `EN.CLC.MDAT.ZS`). Paket `k22-korban-bencana.zip`, 44 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- Sel Provinsi tergabung di rekap XLSX: tanpa diisi, rekap kab/kota hanya membawa satu kab/kota per provinsi.
- Kode Kemendagri enam provinsi Papua berbeda dari kode BPS.
- Kejadian hasil jumlah kab/kota boleh lebih besar dari angka provinsi; korban tidak.
- Observasi yang sama terbit di beberapa berkas, dan tidak selalu sama (INDONESIA tanah longsor 2024: 27 vs 207).
- Korban provinsi hanya terbit per jenis bencana; totalnya adalah jumlah semua jenis.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
