# Laporan tim — Kunci, kasus 17 Air minum, sanitasi, dan kebersihan

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini menyatukan enam seri provinsi BPS untuk lima konsep (air layak, air aman, sanitasi layak, sanitasi aman,
cuci tangan) dengan dua seri WDI dan tiga seri WHO. Silver pertama berisi 3.242 baris dari
11 seri. Panel terpanjang mencakup 1993–2025, sehingga masalahnya berlapis: kode SDG katalog yang
tertukar, definisi yang berganti di tengah seri, provinsi yang tidak dicacah atau hanya dicacah di ibu kota,
pemekaran wilayah sejak 1999, dan dua tabel BPS yang berisi angka yang sama.

## Data dan lineage

22 berkas mentah: BPS snapshot 17 Oktober 2026 (6 CSV, 6 JSON berhalaman, 1 catatan unduhan), WDI
dan WHO snapshot 20 Oktober 2026 (WDI 1 data + 3 metadata, WHO 3 CSV + 2 metadata). Semua berkas tertangani oleh
`ekstraksi.jalankan()` (6.382 baris mentah di berkas data). Setiap baris Silver membawa `_berkas_raw`
dan `_sha256_raw`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Kode SDG katalog tertukar | `var847`: judul sanitasi layak, katalog 11.1.1 | 6.2.1; aturan tujuan SDG vs nama berkas | 1.036 | K-007 |
| Kode tahun beda panjang | daftar `tahun`: 93–99 dan 100+ | pemotong kunci mencoba semua panjang | 6.382 mentah | K-003 |
| Provinsi tidak dicacah | `var.def` a, b | `tidak_diterbitkan` per provinsi | 8 sel | K-005 |
| Hanya ibu kota (2002) | `var.def` c | `cakupan_parsial` | 6 calon | K-012 |
| Definisi berganti | `var.def` d (air 2011, sanitasi 2019), `var.note` cuci tangan | `patahan_seri` | 52 calon | K-013 |
| Dua tabel sanitasi aman | `var2749` = `var2179` gabungan | keduanya di Silver, dijaga aturan | 0 | K-011 |
| Satu-satunya missing | Papua Pegunungan di `var2749` | tidak diisi; Gold memakai `var2179` | 2 sel | K-011 |
| Pemekaran sejak 1999 | Babel, Banten, Gorontalo, Maluku Utara, Kepri, Papua Barat, Sulbar, Kaltara, Papua 2024 | `belum_ada` 413, `batas_lama` 30, `patahan_wilayah` 26 | sel | K-001 |
| Provinsi selalu di ujung | IQR berulang | perbedaan struktural | 7 provinsi | K-004 |
| Calon anomali lain | IQR ke bawah, perubahan, ke samping | 266 outlier ditandai | 403 calon | K-004 |
| Satuan bantuan WHO | odata: juta USD konstan 2024 | satuan `juta_usd_konstan_2024` | 14 | K-009 |
| BPS dua format | nilai CSV = JSON | JSON sebagai sumber | 3.058 | K-002 |

Tidak ada galat input (0). Perkotaan lebih rendah dari perdesaan pada beberapa sel sanitasi aman
(peringatan validasi) dibiarkan sebagai temuan.

## Integrasi dan rekonsiliasi

Disiapkan di Sprint 1, dihitung di Sprint 2 (`reports/pasangan-rekonsiliasi.md`):

- P1 air aman BPS vs WHO dan WDI: 3 tahun; rumah tangga vs penduduk.
- P2 air layak BPS vs WDI basic: 15 tahun, dipisah sebelum dan sesudah pergantian rumus BPS.
- P3 cuci tangan BPS vs WHO: 7 tahun; 2016 dari modul MKP.
- P4 air aman WHO vs WDI: 23 tahun; vintage.
- P5 bantuan pembangunan WHO: konteks.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (10 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: tujuan SDG sesuai nama berkas, dua tabel sanitasi aman sama,
angka gabungan di antara perkotaan dan perdesaan; satu peringatan untuk perkotaan lebih rendah dari perdesaan.
Setiap aturan diuji dengan baris yang sengaja dirusak (`tests/`). Silver dimuat ke DuckDB dengan kunci primer dan
CHECK (3.242 baris). `python pipeline.py` berjalan ±2.8 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
