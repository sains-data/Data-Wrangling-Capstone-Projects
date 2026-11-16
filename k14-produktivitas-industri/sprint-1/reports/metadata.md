# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1161 | Laju Pertumbuhan PDB Per Tenaga Kerja/Tingkat Pertumbuhan PDB Riil Per Orang Bekerja Per Tahun | Laju pertumbuhan PDB riil per tenaga kerja (per orang bekerja) per tahun |
| var1344 | Nilai Tambah Pertanian Dibagi Jumlah Tenaga Kerja Di Sektor Pertanian | Nilai tambah pertanian dibagi jumlah tenaga kerja sektor pertanian |
| var1214 | Proporsi Nilai Tambah Sektor Industri Manufaktur Terhadap PDB | Proporsi nilai tambah sektor industri manufaktur terhadap PDB |
| var2755 | 9.2.2* Proporsi Tenaga Kerja Pada Sektor Industri Manufaktur Menurut Provinsi | Proporsi tenaga kerja pada sektor industri manufaktur |
| SL.GDP.PCAP.EM.KD | GDP per person employed (constant 2021 PPP $) | GDP per person employed (constant 2021 PPP $) |
| NV.IND.MANF.ZS | Manufacturing, value added (% of GDP) | Manufacturing, value added (% of GDP) |
| SDG_0821_NOC_RT | SDG indicator 8.2.1: Annual growth rate of output per worker, GDP constant 2015 US dollars | Annual growth rate of output per worker (GDP constant 2015 US$) (%) |
| SDG_B821_NOC_RT | SDG indicator 8.2.1: Annual growth rate of output per worker, GDP constant 2021 international dollars at PPP | Annual growth rate of output per worker (GDP constant 2021 PPP $) (%) |
| SDG_0922_NOC_RT | SDG indicator 9.2.2: Manufacturing employment as a proportion of total employment | Manufacturing employment as a proportion of total employment (%) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1161 | tidak_ada | persen_per_tahun | judul 'Laju Pertumbuhan ... Per Tahun'; var.unit kosong; nilai bisa negatif | 8.2.1 | 8.2.1 |
| var1344 | rupiah_per_tenaga_kerja | rupiah_per_tenaga_kerja | var.unit: 'Rupiah/Tenaga Kerja' | 2.3.1 | 2.3.1(a) |
| var1214 | tidak_ada | persen | judul 'Proporsi ... Terhadap PDB'; var.unit kosong; nilai 0–50 | 9.2.1 | 9.2.1 |
| var2755 | persen | persen | var.unit: 'Persen' | 9.2.2 | 9.2.2 |
| SL.GDP.PCAP.EM.KD | — | usd_ppp_2021 | name: '(constant 2021 PPP $)' | — | 8.2.1 |
| NV.IND.MANF.ZS | — | persen | name: '(% of GDP)' | — | 9.2.1 |
| SDG_0821_NOC_RT | — | persen_per_tahun | UNIT_MEASURE PT; judul DSD 'Annual growth rate' | 8.2.1 | 8.2.1 |
| SDG_B821_NOC_RT | — | persen_per_tahun | UNIT_MEASURE PT; judul DSD 'Annual growth rate' | 8.2.1 | 8.2.1 |
| SDG_0922_NOC_RT | — | persen | UNIT_MEASURE PT | 9.2.2 | 9.2.2 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var1161 | satuan tidak_ada -> persen_per_tahun |
| var1344 | kode SDG 2.3.1 -> 2.3.1(a) |
| var1214 | satuan tidak_ada -> persen |
| SL.GDP.PCAP.EM.KD | kode SDG kosong -> 8.2.1 |
| NV.IND.MANF.ZS | kode SDG kosong -> 9.2.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1161 | Sumber : Badan Pusat Statistik (diolah) 2024: Menggunakan angka sementara PDB/PDRB 2025: Menggunakan angka sangat sementara PDB/PDRB Catatan: Data laju pertumbuhan PDB/TK 2024 dihitung berdasarkan data pada provinsi induk (Provinsi Papua dan Papua Barat) karena Data tenaga kerja untuk DOB tersedia di 2024, sehingga data laju pertumbuhan untuk DOB tersedia di 2025 |
| 2755 | Sumber: BPS (Sakernas) |
| 1344 | Sumber: BPS 2022: Angka Sementara 2023: Angka Sangat Sementara |
| 1214 | Sumber : BPS 2022: Angka sementara 2023: Angka sangat sementara |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| NV.IND.MANF.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SL.GDP.PCAP.EM.KD | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
