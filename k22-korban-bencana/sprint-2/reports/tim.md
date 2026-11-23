# Laporan tim — Kunci, kasus 22 Korban bencana

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini memakai sembilan seri provinsi BNPB (kejadian, korban meninggal, hilang, luka/sakit, mengungsi,
terdampak, terdampak-mengungsi, dua angka per 100.000) beserta penyebutnya (jumlah penduduk), dan satu seri WDI.
Silver pertama berisi 14.193 baris dari 11 seri. Tantangannya bentuk data: tidak ada kode
seri, enam tata letak dalam dua format, sel tergabung, angka provinsi yang sebagian harus dibentuk dari kab/kota,
dan observasi yang sama terbit di beberapa berkas.

## Data dan lineage

44 berkas mentah: katalog CKAN (1), DataStore JSON BNPB (26), XLSX unduhan tangan (13), WDI (1 data
+ 3 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()` (77.522 baris mentah di berkas data,
77.456 sel BNPB). Setiap baris Silver membawa `_berkas_raw` dan `_sha256_raw`; angka provinsi hasil jumlah
kab/kota dapat ditelusuri ke baris kab/kotanya lewat `reports/bnpb-agregasi.csv`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Tanpa kode seri, enam tata letak | judul resource katalog CKAN, kepala kolom | satu bentuk sel + kamus ukuran | 77.456 sel | K-002 |
| Sel Provinsi tergabung | rekap 2021/2022 XLSX | sel diisi sebelum dibaca | 4.494 angka jumlahan | K-003 |
| Kode Kemendagri ≠ BPS untuk Papua | lembar Keterangan | dipetakan, kode dan nama harus sepakat | — | K-001 |
| Kab/kota dijumlahkan | tabel kab/kota | jumlah + banyak kab/kota dicatat | 46.330 baris kab/kota | K-008 |
| Kab/kota vs provinsi | aturan hitung Keterangan | kejadian boleh lebih besar (164); DKI -> Jawa Barat 2024 peringatan | 6 korban | K-009 |
| Observasi sama di beberapa berkas | `reports/bnpb-lintas-berkas.csv` | semua disimpan; deret memilih satu | 172 kelompok berbeda | K-007 |
| INDONESIA tanah longsor 2024 = 27 | tiga tabel lain dan jumlah provinsi = 207 | peringatan, tidak diubah | 1 | K-014 |
| Galat titik mengambang Excel | `11.000000000000002` | dibulatkan | 33 | K-010 |
| Tahun tanpa tabel provinsi | katalog CKAN | `tidak_diterbitkan` | 1.772 sel | K-011 |
| Pemekaran Papua | rekap 2022 34 provinsi | `patahan_wilayah` | 6 | K-013 |
| Jumlah korban menceng | profil | IQR pada log(1 + nilai) | 119 calon (101 outlier) | K-004 |

Tidak ada galat input menurut rentang satuan (0).

## Integrasi dan rekonsiliasi

Panel Gold memuat 10 indikator provinsi (1.374 sel terisi, 2.008 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 19 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 0.0%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Mengungsi per 100.000: angka BNPB vs dihitung ulang dari pengungsi dan penduduk | 0.0% | tidak berselisih (angka sama) | pembulatan atau penduduk berbeda; berkas pengungsi dan berkas per 100.000 terbit terpisah |
| P2 | Meninggal dan hilang per 100.000: angka BNPB vs (meninggal + hilang) / penduduk | 0.0% | tidak berselisih (angka sama) | pembulatan; pembilang dari dua berkas terpisah |
| P3 | Kejadian banjir: baris INDONESIA vs jumlah 38 provinsi | 0.3% | definisi berbeda | definisi penghitungan: kejadian lintas provinsi dihitung sekali secara nasional |
| P4 | Penduduk terdampak kekeringan, banjir, suhu ekstrem (WDI): konteks | — | definisi berbeda | periode tidak beririsan: WDI rata-rata 1990–2009, BNPB 2010–2025 |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan. Keputusan khusus pasangan: P1 dan P2: angka per 100.000 yang diterbitkan dibandingkan dengan hitungan ulang (jumlah korban / jumlah penduduk x 100.000) dari berkas lain; P3: baris INDONESIA dibandingkan dengan jumlah baris provinsi di berkas yang sama (GOLD_AGREGAT); selisih = kejadian lintas provinsi.

## Validasi dan reproduksibilitas

23 aturan berjalan setiap `python pipeline.py` (20 lolos, 3
peringatan; `reports/validasi.md`). Aturan khas kasus: cacah bilangan bulat, jumlah jenis = Total, angka per 100.000
dapat dihitung ulang; peringatan untuk kab/kota vs provinsi dan baris Indonesia yang berbeda antarberkas. Silver
dimuat ke DuckDB (14.193 baris). `python pipeline.py` berjalan ±7.1 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (3.479 baris).
