# Kasus 09 — Keterampilan TIK dan PAUD

Klaster B. Pendidikan, Tujuan SDG 4 dan 5. Empat seri provinsi BPS (`var1451` TIK 15–24, `var1447` TIK 15–59,
`var1439` APK PAUD, `var1221` telepon genggam) dan dua pembanding nasional (WDI `SE.PRE.ENRR`, `IT.NET.USER.ZS`).
Paket `k09-tik-paud.zip`, 17 berkas, snapshot BPS 17 dan 20 Oktober 2026, WDI 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- `var1221` ada di dua snapshot; tanpa aturan pemilihan, setiap angka masuk Silver dua kali.
- Dua seri TIK berbeda kelompok umur dan tumpang tindih; jangan digabung.
- APK PAUD bisa melebihi 100; Papua Pegunungan 2024–2025 ber-RSE tinggi.
- Telepon genggam (perangkat) bukan pengguna internet.
- Data WDI ada di dua berkas.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
