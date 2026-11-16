# Kasus 03 — Kesehatan reproduksi remaja

Klaster A. Pangan dan kesehatan, Tujuan SDG 3. Dua seri provinsi BPS (`var1394` KB metode modern, `var1353`
angka kelahiran remaja) dan tiga pembanding nasional (WDI `SP.ADO.TFRT`; WHO `MDG_0000000003`, `SDGFPALL`).
Paket `k03-kesehatan-reproduksi-remaja.zip`, 13 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | menyusul |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- `var1353` hanya umur 15–19 (judul JSON), walaupun katalog menyebut angka kelahiran remaja secara umum.
- Satuan `var1353` tidak ditulis BPS; buktinya harus dicari di metadata WHO dan WDI.
- WHO memuat dua kelompok umur dalam satu berkas; baris 10–14 tidak sebanding dengan BPS.
- Angka KB BPS jauh di bawah `SDGFPALL` karena penyebutnya berbeda, bukan karena salah.
- WHO tidak punya tahun 2012 dan 2017, jadi pasangan BPS–WHO tidak punya tahun bersama.
- Kalimantan Timur 2012 masih mencakup Kalimantan Utara.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
