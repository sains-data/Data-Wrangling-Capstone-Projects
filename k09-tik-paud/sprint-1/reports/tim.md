# Laporan tim — Kunci, kasus 09 Keterampilan TIK dan PAUD

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai empat seri provinsi BPS (keterampilan TIK dua kelompok umur, APK PAUD, kepemilikan telepon
genggam) dan dua seri WDI. Silver pertama berisi 1.653 baris dari 6 seri. Kasusnya relatif
ringan; pekerjaan utamanya aturan pemilihan snapshot, memisahkan dua kelompok umur TIK, dan menandai sel dengan
galat sampling tinggi.

## Data dan lineage

17 berkas mentah: BPS snapshot 17 Oktober 2026 (4 JSON, 4 CSV, 1 catatan unduhan) dan 20 Oktober
2026 (`var1221` lagi: 1 JSON, 1 CSV, 1 catatan), WDI snapshot 20 Oktober 2026 (2 berkas data + 3 metadata). Semua
berkas tertangani oleh `ekstraksi.jalankan()` (4.062 baris mentah di berkas data).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Seri di dua snapshot | `var1221` 17 dan 20 Oktober | snapshot terbaru; 0 nilai berbeda | 1 seri | K-003 |
| Kode SDG kurang rinci | `var.label` 4.4.1.(a), 4.4.1.(b) | butir (a) dan (b) | 786 | K-006 |
| APK PAUD satuan kosong | judul APK | `persen_apk` | 393 | K-007 |
| RSE tinggi | `var.note`: Papua Pegunungan 2024–2025 | peringatan, ditandai di Gold | 2 | K-011 |
| TIK 15–59 melompat | > 70% provinsi naik > 20% (2016–2018) | `patahan_seri` | 1 | K-012 |
| Pemekaran wilayah | Kalimantan Utara, Papua 2024 | `belum_ada` 128, `batas_lama` 16, `patahan_wilayah` 8 | sel | K-001, K-010 |
| Calon anomali | IQR | 79 outlier, 9 provinsi struktural | 186 | K-004 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0).

## Integrasi dan rekonsiliasi

- P1 APK PAUD BPS vs WDI: 4 tahun (WDI berakhir 2018); kelompok umur acuan berbeda.
- P2 telepon genggam vs internet: konteks.
- P3 TIK 15–24 vs 15–59: konteks, tidak digabung.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (9 lolos, 2
peringatan; `reports/validasi.md`). Aturan khas kasus: satu snapshot per seri, seri × provinsi × tahun unik;
peringatan untuk TIK muda lebih rendah dan sel ber-RSE tinggi. Silver dimuat ke DuckDB (1.653 baris).
`python pipeline.py` berjalan ±2.3 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.
