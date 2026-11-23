# Laporan tim — Kunci, kasus 02 Kematian anak dan ibu

Status: draf akhir Sprint 2. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `data/gold/`, `reports/`,
dan `log-keputusan.csv` (id K-xxx).

## Ringkasan

Kasus ini menyatukan tiga seri provinsi BPS (kematian balita, kematian bayi, persalinan di fasilitas
kesehatan untuk 40% pengeluaran terbawah) dengan enam seri nasional WHO dan WDI. Silver pertama berisi
867 baris dari 9 seri. Temuan utama kualitas data ada di metadata, bukan di angka:
dua seri BPS berbagi kode SDG yang sama tetapi mengukur hal berbeda, satuan tidak tercatat di katalog, dan
angka survei merujuk jendela waktu yang berbeda untuk tingkat nasional dan provinsi.

## Data dan lineage

16 berkas mentah dari snapshot 20 Oktober 2026: BPS (3 CSV, 3 JSON, 1 catatan unduhan), WDI
(1 berkas data, 3 metadata), WHO GHO (3 CSV, 2 metadata). Semua berkas tertangani oleh
`ekstraksi.jalankan()` (1.185 baris mentah di berkas data). Setiap baris Silver membawa
`_berkas_raw` dan `_sha256_raw` dari `src.common.manifest`; pemeriksa skema mencocokkannya dengan
`MANIFEST.csv`. Contoh penelusuran satu baris ada di `docs/data-dictionary.md`.

## Masalah data dan penanganannya

| Masalah | Bukti | Keputusan | Baris terdampak | Log |
|---|---|---|---|---|
| Dua seri BPS berkode SDG sama | `var.label` berbeda (balita, bayi) | dua seri terpisah, bukan duplikat | 0 | K-003 |
| Satuan katalog `tidak_ada` | `var.label` memuat "Per 1000 Kelahiran Hidup" | `per_1000_kh` | 70 | K-007 |
| Kode SDG tidak persis | judul `var1584` (bayi), `var1541` (di fasilitas, 40% terbawah) | 3.2.1(b), 3.1.2(b) | 210 | K-009 |
| Jendela rujukan berbeda | `var.note`: nasional 5 tahun, provinsi 10 tahun | kolom `rujukan_tahun` | 70 | K-008 |
| Sel provinsi 2017 kosong | `var.note`: angka provinsi 2017 tidak ada | `tidak_diterbitkan` | 68 sel | K-005 |
| Provinsi belum dibentuk | Kalimantan Utara (2012), empat provinsi Papua baru | `belum_ada` | 38 sel | K-001 |
| WDI tahun tanpa estimasi | `value: null` | tidak masuk Silver | 73 | K-010 |
| BPS dua format | nilai CSV = JSON | JSON sebagai sumber | 245 | K-002 |
| Nama WHO salah ketik | `IND_NAME` "neonetal" | nama dari `odata/Indicator.json` | — | K-012 |
| Calon anomali | IQR antarprovinsi dan perubahan antarperiode | 5 ditandai sebagai outlier, nilai tidak diubah | 5 | K-004 |

Tidak ada sel yang benar-benar missing (0) dan tidak ada galat input (0). Uji
patahan hanya mungkin untuk `var1541` (lima periode) dan tidak menemukan lompatan serentak. Panel provinsi
kematian hanya berisi tahun 2012; panel persalinan 2015–2019. Panel tidak boleh dibaca sebagai keadaan
tahun sesudahnya.

## Integrasi dan rekonsiliasi

Panel Gold memuat 3 indikator provinsi (236 sel terisi, 106 sel kosong
berkategori; `reports/panel-gold.md`). Tabel nasional Gold menaruh angka Indonesia BPS dan enam seri WHO/WDI
berdampingan; tabel rekonsiliasi berisi 135 baris (`reports/rekonsiliasi.md`).

| Pasangan | Yang dibandingkan | Median selisih relatif | Kategori | Penjelasan |
|---|---|---|---|---|
| P1 | AKBa BPS vs WHO dan WDI, tahun yang sama | 31.5% | metode berbeda | BPS selalu lebih tinggi; sebagian karena angka survei merujuk 5 tahun sebelum survei |
| P1J | AKBa BPS vs rata-rata WHO/WDI 5 tahun sebelum survei | 15.5% | metode berbeda | sesudah periode rujukan disamakan, sisa selisih = survei SDKI vs model UN IGME (K-017) |
| P2 | AKB BPS | — | definisi berbeda | tidak ada seri kematian bayi di paket pembanding; WHO neonatal hanya konteks |
| P3 | persalinan di fasilitas (BPS) vs ditolong tenaga kesehatan (WDI) | — | definisi berbeda | ukuran dan populasi berbeda; ditampilkan berdampingan, tidak dihitung selisihnya |
| P4 | AKBa WHO vs WDI | 0.8% | vintage berbeda | sumber estimasi sama (UN IGME), rilis berbeda; diuji dengan arsip WDI di Sprint 3 |
| P5 | AKI WHO vs WDI | 0.1% | vintage berbeda | sama dengan P4; tidak ada padanan BPS di paket |

Tidak ada selisih yang dihapus atau disamakan paksa. Tahun pembanding di luar rentang seri utama tidak
ditulis; semua tahun BPS tampil walau tanpa pasangan.

## Validasi dan reproduksibilitas

21 aturan berjalan setiap `python pipeline.py` (20 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: AKBa ≥ AKB pada wilayah, periode, dan jendela yang
sama; tidak ada tahun BPS di luar tahun terbit; setiap baris kematian BPS punya jendela rujukan. Setiap
aturan diuji dengan baris yang sengaja dirusak (`tests/`). Silver dimuat ke DuckDB dengan kunci primer dan
CHECK (867 baris), begitu pula Gold (794 baris; `reports/basis-data.md`). Sprint 2 menambah
10 aturan Gold: kunci panel unik, sel tertelusur ke Silver, nilai Gold sama dengan Silver, kategori
baku, dan selisih yang dihitung ulang cocok. `python pipeline.py` berjalan ±2.8 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5: ekstraksi dan
lineage; profil dan pembersihan; transformasi dan panel; integrasi, penyimpanan, dan skala; validasi dan
dokumentasi.
