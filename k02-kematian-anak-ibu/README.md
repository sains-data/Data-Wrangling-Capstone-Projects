# Kasus 02 — Kematian anak dan ibu

Klaster A. Pangan dan kesehatan, Tujuan SDG 3. Tiga seri provinsi BPS (`var1373`, `var1584`, `var1541`) dan
enam pembanding nasional (WDI `SH.DYN.MORT`, `SH.STA.MMRT`, `SH.STA.BRTC.ZS`; WHO `MDG_0000000007`,
`MDG_0000000026`, `WHOSIS_000003`). Paket `k02-kematian-anak-ibu.zip`, 16 berkas, snapshot 20 Oktober 2026.

| Sprint | Isi | Status |
|---|---|---|
| [sprint-1](sprint-1/) | ekstraksi, profil, pembersihan, Silver pertama, persiapan integrasi dan SQL | selesai |
| [sprint-2](sprint-2/) | panel Gold, Silver dan Gold di SQL, tabel rekonsiliasi | selesai |
| [sprint-3](sprint-3/) | arsip WDI, pandas vs DuckDB/Dask, validasi lengkap, laporan | menyusul |

## Hal yang paling sering terlewat di kasus ini

- `var1373` dan `var1584` berkode SDG sama di katalog, tetapi yang satu kematian balita, yang lain kematian
  bayi. Bukti: `var.label` di JSON.
- `var.note` kedua seri kematian berisi tiga butir: sumbernya SDKI, jendela rujukan nasional dan provinsi
  berbeda (5 dan 10 tahun), dan angka provinsi 2017 tidak ada.
- Judul `var1541` menyebut persalinan *di fasilitas kesehatan* pada *40% pengeluaran terbawah*; itu bukan
  ukuran yang sama dengan `SH.STA.BRTC.ZS` (ditolong tenaga kesehatan, semua persalinan).
- Satu CSV WHO memakai `RATE_PER_100000_*`, dua lainnya `RATE_PER_1000_*`; `IND_NAME` neonatal salah ketik.
- Seri WDI punya banyak tahun dengan `value: null`, terutama seri persalinan.

Mulai dari [sprint-1/README.md](sprint-1/README.md).
