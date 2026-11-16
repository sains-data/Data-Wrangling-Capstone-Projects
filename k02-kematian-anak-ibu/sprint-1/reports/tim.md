# Laporan tim — Kunci, kasus 02 Kematian anak dan ibu

Status: draf akhir Sprint 1. Angka dapat ditarik ulang dari `data/silver/silver.parquet`, `reports/`, dan
`log-keputusan.csv` (id K-xxx).

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

Disiapkan di Sprint 1, dihitung di Sprint 2 (`reports/pasangan-rekonsiliasi.md`):

- P1 kematian balita BPS (Indonesia) vs WHO dan WDI: 2 tahun beririsan; dugaan selisih karena
  metode dan jendela rujukan.
- P2 kematian bayi BPS: tidak ada pembanding setara di paket; WHO neonatal hanya konteks.
- P3 persalinan di fasilitas (BPS) vs ditolong tenaga kesehatan (WDI): konteks, bukan pasangan selisih.
- P4 dan P5 WHO vs WDI (balita, kematian ibu): sumber estimasi sama; selisih diduga *vintage*. Validasi
  sudah memberi peringatan untuk tahun-tahun dengan selisih balita > 10%.

## Validasi dan reproduksibilitas

11 aturan berjalan setiap `python pipeline.py` (10 lolos, 1
peringatan; `reports/validasi.md`). Aturan khas kasus: AKBa ≥ AKB pada wilayah, periode, dan jendela yang
sama; tidak ada tahun BPS di luar tahun terbit; setiap baris kematian BPS punya jendela rujukan. Setiap
aturan diuji dengan baris yang sengaja dirusak (`tests/`). Silver dimuat ke DuckDB dengan kunci primer dan
CHECK (867 baris). `python pipeline.py` berjalan ±1.9 detik.

## Pembagian kerja

Kunci tidak memuat nama atau NIM. Pembagian komponen mengikuti panduan kelompok bagian 5: ekstraksi dan
lineage; profil dan pembersihan; transformasi dan panel; integrasi, penyimpanan, dan skala; validasi dan
dokumentasi.
