# Laporan tim — Kunci, kasus 11 Pengangguran

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai TPT provinsi BPS (1986 sampai Februari 2026), dua seri WDI, dan tiga seri ILOSTAT. Silver pertama
berisi 7.572 baris dari 6 seri. Pekerjaan utamanya memetakan tiga jenis periode BPS dan
triwulan ILO, menangani 28 kode umur ILO, dan menjelaskan mengapa TPT BPS selalu di atas angka ILO.

## Data dan lineage

14 berkas mentah: BPS (1 JSON 14 halaman, 1 CSV, 1 catatan unduhan), WDI (1 data + 3 metadata),
ILOSTAT (3 CSV SDMX, 3 DSD, 1 daftar dataflow). Semua berkas tertangani oleh `ekstraksi.jalankan()` (9.853
baris mentah).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Tiga jenis periode BPS | Tahunan, Februari, Agustus | `AAAA`, `AAAA-02`, `AAAA-08` | 2.000 | K-006 |
| Triwulan ILO | `FREQ` Q | `AAAA-Qn` | 2.535 | K-003 |
| Empat klasifikasi umur ILO | 28 kode umur | klasifikasi ikut ditulis | 90 nilai rincian | K-007 |
| BPS di atas ILO | 1–3,3 poin, 18 tahun | selisih definisi | 24 tahun | K-014 |
| Status ILO B dan U | `OBS_STATUS` | `status_obs` | 569 / 276 | K-005 |
| Maluku 2000, Sakernas 1995 | `var.note` | `tidak_diterbitkan`; 1995 tidak ada | 2 sel | K-005, K-011 |
| Lonjakan serentak | 1994, 2001, Agustus 2020 | `patahan_seri` | 10 calon | K-012 |
| Pemekaran wilayah | sejak 1999 | `belum_ada` 356, `batas_lama` 21, `patahan_wilayah` 10 | sel | K-001, K-010 |
| Calon anomali | IQR | 168 outlier | 179 | K-004 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0).

## Integrasi dan rekonsiliasi

Panel Gold memuat 1 indikator provinsi (1.939 sel terisi, 379 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 91 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 37.2%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | TPT BPS Agustus vs ILO SDG 8.5.2 (total, rujukan Agustus) | 37.2% | definisi berbeda | definisi pengangguran (BPS lebih tinggi 1–3,3 poin pada 18 tahun; dugaan cakupan BPS lebih luas) dan pengolahan |
| P2 | WDI estimasi nasional vs estimasi model ILO | 0.0% | metode berbeda | metode: survei (= ILO SDG 8.5.2) vs model ILOEST yang mengisi dan menyesuaikan |
| P3 | Pengangguran menurut disabilitas (ILO): konteks | — | tanpa pasangan | tidak ada padanan BPS di paket |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (20 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: jenis periode sesuai bentuknya, bulan BPS hanya Februari dan
Agustus tanpa tahun buatan, status ILO terdaftar; peringatan untuk selisih BPS Agustus vs ILO. Silver dimuat ke
DuckDB (7.572 baris). `python pipeline.py` berjalan ±4.0 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (2.663 baris).
