# Laporan tim — Kunci, kasus 01 Kerawanan pangan provinsi

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini menyatukan dua seri provinsi BPS dari Susenas (prevalensi ketidakcukupan konsumsi pangan, PoU, dan
kerawanan pangan sedang atau berat menurut FIES) dengan dua seri nasional FAO lewat WDI dan tiga seri gizi
balita WHO. Silver pertama berisi 1.414 baris dari 7 seri. Panel provinsi tahunan
2017–2025 cukup panjang, sehingga masalah utamanya bukan sel kosong, melainkan tiga hal: duplikat tersembunyi
di berkas WHO, pemekaran Papua di tengah panel, dan selisih BPS–FAO yang tidak bisa dijelaskan dari metadata paket.

## Data dan lineage

14 berkas mentah dari snapshot 20 Oktober 2026: BPS (2 CSV, 2 JSON, 1 catatan unduhan), WDI
(1 berkas data, 3 metadata), WHO GHO (3 CSV, 2 metadata). Semua berkas tertangani oleh `ekstraksi.jalankan()`
(2.184 baris mentah di berkas data). Setiap baris Silver membawa `_berkas_raw` dan `_sha256_raw`
dari `src.common.manifest`; pemeriksa skema mencocokkannya dengan `MANIFEST.csv`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| BPS dua format | nilai CSV = JSON | JSON sebagai sumber | 646 | K-002 |
| Total WHO ditulis tiga cara | baris semua `DIM_*` kosong, semua `TOTAL`, sebagian `TOTAL`, nilai sama | satu baris dipakai | 24 dibuang | K-011 |
| Sel WHO bertentangan | laki-laki 24–35 bulan 2008: 15,7 dan 16,3 | tidak masuk Silver | 2 | K-012 |
| Provinsi belum dibentuk | empat provinsi Papua baru sebelum 2023 | `belum_ada` | 48 sel | K-001 |
| Provinsi baru belum terbit | Papua dan Papua Barat 2023 masih batas lama | `batas_lama` | 8 sel | K-016 |
| Wilayah induk mengecil | Papua, Papua Barat 2023→2024 | `patahan_wilayah` | 4 | K-013 |
| Provinsi selalu di ujung sebaran | IQR antarprovinsi berulang | perbedaan struktural, nilai tidak diubah | 8 provinsi | K-004 |
| Calon anomali lain | IQR ke bawah, perubahan, ke samping | 63 outlier ditandai, nilai tidak diubah | 114 calon | K-004 |
| Kode SDG WDI kosong | `sumber46_indikator.json` | 2.1.1 dan 2.1.2 | 2 seri | K-007 |
| WDI tahun tanpa estimasi | `value: null` | tidak masuk Silver | 98 | K-009 |
| Batas sensor PoU FAO | sourceNote: 2.5 bisa berarti < 2,5% | aturan validasi; tidak ada nilai Indonesia yang terkena | 0 | K-010 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0). Uji
patahan seri tidak menemukan lompatan serentak; yang paling dekat adalah PoU 2021→2022, saat lebih dari separuh
provinsi naik lebih dari 20%, masih di bawah ambang 70%. Panel memakai susunan 38 provinsi; perbandingan Papua lintas 2024
tidak sah tanpa menyusun ulang wilayah lama.

## Integrasi dan rekonsiliasi

Panel Gold memuat 2 indikator provinsi (628 sel terisi, 56 sel kosong berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh seri utama dan pembanding berdampingan; tabel rekonsiliasi berisi 68 baris (`reports/rekonsiliasi.md`). Median selisih relatif mutlak pasangan berseri utama provinsi: 16.6%.

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | Ketidakcukupan konsumsi pangan: BPS (Susenas) vs WDI (FAO) | 31.3% | metode berbeda | metode (sumber data dan model berbeda); periode angka FAO belum terjawab dari paket |
| P2 | Kerawanan pangan sedang atau berat (FIES): BPS vs WDI (FAO) | 2.7% | metode berbeda | sumber data dan cara estimasi berbeda; definisi FIES sama |
| P3 | Gizi balita WHO (stunting, overweight, wasting): konteks, bukan pasangan BPS | — | definisi berbeda | definisi berbeda: status gizi balita, bukan kecukupan pangan penduduk |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak ditulis; semua periode seri utama tampil walau tanpa pasangan.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (20 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: satu baris per seri × provinsi × tahun, satu total WHO
per tahun, tidak ada angka sensor FAO. Setiap aturan diuji dengan baris yang sengaja dirusak (`tests/`). Silver
dimuat ke DuckDB dengan kunci primer dan CHECK (1.414 baris). `python pipeline.py` berjalan
±3.0 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Kelompok ini enam orang, jadi satu komponen dipegang dua orang dan dibagi
menurut sumber (panduan kelompok bagian 5): ekstraksi dan lineage; profil dan pembersihan; transformasi dan
panel; integrasi, penyimpanan, dan skala; validasi dan dokumentasi.

Sprint 2 menambah 10 aturan Gold (kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori baku, selisih yang dihitung ulang cocok), masing-masing diuji dengan Gold yang sengaja dirusak; Gold dimuat ke DuckDB (866 baris).
