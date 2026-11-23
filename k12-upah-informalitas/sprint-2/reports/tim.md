# Laporan tim — Kunci, kasus 12 Upah dan informalitas

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai dua seri provinsi BPS (upah rata-rata per jam, proporsi lapangan kerja informal) dan dua seri ILOSTAT
yang dirinci menurut jenis kelamin dan jabatan atau sektor. Tidak ada WDI. Silver pertama berisi 1.584
baris dari 4 seri. Pekerjaan utamanya menyamakan unit upah, menangani beberapa klasifikasi ILO dalam satu
berkas, dan menjelaskan selisih besar informalitas.

## Data dan lineage

10 berkas mentah: BPS (2 JSON, 2 CSV, 1 catatan unduhan), ILOSTAT (2 CSV SDMX, 2 DSD, 1 daftar
dataflow). Semua berkas tertangani oleh `ekstraksi.jalankan()` (2.265 baris mentah).

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Unit upah | Rupiah/Jam; LC + IDR | `rupiah_per_jam` nominal | — | K-007 |
| Beberapa total dalam satu berkas | ISCO-08, ISCO-88, keahlian; SECTOR, AGGREGATE | satu total utama; lainnya diuji sama | 0 | K-006 |
| Informalitas ILO vs BPS | ±80% vs ±58% | selisih definisi | 4 tahun | K-014 |
| Satuan informal kosong | judul | persen | 288 | K-008 |
| Status ILO B | `OBS_STATUS` | `status_obs` | 144 | K-003 |
| Pemekaran wilayah | Papua 2024 | `belum_ada` 52, `batas_lama` 8, `patahan_wilayah` 4 | sel | K-001, K-009 |
| Upah menceng | IQR | 42 outlier, 5 provinsi struktural | 83 | K-004 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0).

## Integrasi dan rekonsiliasi

Panel Gold memuat 2 indikator provinsi (662 sel terisi, 60 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 19 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 13.9%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Upah per jam: BPS (pekerja) vs ILO (rata-rata penghasilan per jam pekerja) | 9.3% | metode berbeda | metode (pengolahan Sakernas; nominal keduanya, rupiah per jam) |
| P2 | Informalitas: BPS vs ILO | 28.7% | definisi berbeda | definisi (ILO jauh lebih tinggi, ±80% vs ±58%: kriteria informal berbeda) |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (21 lolos, 0
peringatan; `reports/validasi.md`). Aturan khas kasus: upah positif berunit rupiah per jam, total klasifikasi lain sama
dengan total utama, status ILO terdaftar; peringatan bila upah BPS dan ILO berbeda lebih dari 20%. Silver dimuat ke
DuckDB (1.584 baris). `python pipeline.py` berjalan ±3.0 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (781 baris).
