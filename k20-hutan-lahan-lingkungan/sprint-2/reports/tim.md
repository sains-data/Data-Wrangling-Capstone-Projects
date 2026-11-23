# Laporan tim — Kunci, kasus 20 Hutan, lahan, dan lingkungan

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai tabel statis tutupan hutan (luas dan persen), tiga seri BPS (penutupan lahan menurut kawasan,
lahan kritis, komponen IKLH), dan tiga seri WDI. Silver pertama berisi 4.045 baris dari 8
seri. Temuan terpenting adalah galat di sumber: kolom 2020 tabel tutupan hutan tergeser terhadap nama provinsi.

## Data dan lineage

13 berkas mentah: BPS snapshot 17 Oktober 2026 (3 JSON dinamis, 1 JSON tabel statis, 4 CSV, 1 catatan
unduhan), WDI (1 data + 3 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (8.113 baris
mentah di berkas data).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Tabel statis HTML, dua satuan | header luas dan % | dua seri; uji silang CSV | 0 beda | K-002, K-006 |
| Kolom 2020 tergeser | 2020 menyimpang > 50%; kolom `cek` CSV | disimpan, peringatan, tidak dipakai di Gold | — | K-013 |
| Jumlah ≠ rincian | DIY 2016 di dua tabel | dilaporkan | 1 | K-012 |
| Kode SDG keliru | judul `var1304`, berkas `sdg15_iklh` | 15.1.1, 15 | 1.806 | K-007 |
| Tiga satuan luas | ribu ha, ha, km2 | disimpan apa adanya | — | K-008 |
| Kalimantan Utara digabung | keterangan tabel | `batas_lama` | 21 sel | K-001 |
| Jakarta tanpa lahan kritis | tidak ada di 4 review | `tidak_diterbitkan` | 4 sel | K-005 |
| Calon anomali | IQR | 194 outlier, 11 provinsi struktural | 313 | K-004 |

Tidak ada sel yang benar-benar missing (0). Galat input tidak ditemukan oleh aturan rentang; galat
kolom 2020 ditemukan oleh aturan konsistensi, bukan rentang.

## Integrasi dan rekonsiliasi

Panel Gold memuat 7 indikator provinsi (1.641 sel terisi, 183 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 36 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 0.3%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Luas hutan nasional: BPS (ribu ha) vs WDI (km persegi) | 0.4% | definisi berbeda | definisi (tutupan lahan berhutan KLHK vs definisi FAO) setelah satuan diseragamkan (1 ribu ha = 10 km2) |
| P2 | Persentase hutan: BPS (terhadap penutupan lahan) vs WDI (terhadap luas daratan) | 0.8% | definisi berbeda | definisi (penyebut: luas penutupan lahan vs luas daratan) |
| P3 | Indeks kualitas udara (BPS) vs PM2.5 (WDI): konteks | — | definisi berbeda | arah berlawanan: indeks tinggi = baik, PM2.5 tinggi = buruk |
| P4 | Kawasan hutan (var1304) vs tutupan hutan (tabel statis): dua tabel KLHK | 0.0% | tidak berselisih (angka sama) | sumber sama (rekalkulasi KLHK); jumlah luas seharusnya sama |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan. Keputusan khusus pasangan: P1: WDI km2 dikali 0,1 menjadi ribu hektar (1 km2 = 100 ha) sebelum selisih dihitung.

## Validasi dan reproduksibilitas

22 aturan berjalan setiap `python pipeline.py` (19 lolos, 3
peringatan; `reports/validasi.md`). Aturan khas kasus: luas ≥ 0 dengan satu satuan per seri, komponen IKLH dari
kamus; peringatan untuk jumlah ≠ rincian, kolom 2020 tergeser, dan hutan + non hutan ≠ jumlah. Silver dimuat ke
DuckDB (4.045 baris). `python pipeline.py` berjalan ±3.9 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (2.011 baris).
