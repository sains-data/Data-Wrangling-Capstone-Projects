# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1402 | Persentase Unmet Need Pelayanan Kesehatan Menurut Provinsi | Persentase unmet need pelayanan kesehatan |
| var2279 | Persentase Penduduk yang Memiliki Jaminan Kesehatan Nasional (JKN) Menurut Provinsi | Persentase penduduk yang memiliki Jaminan Kesehatan Nasional (JKN) |
| var1477 | Kepadatan Dan Distribusi Tenaga Kesehatan | Kepadatan tenaga kesehatan menurut profesi (per 100.000 penduduk) |
| HWF_0001 | Density of doctors | Medical doctors (per 10 000 population) |
| HWF_0006 | Density of nurses and midwives | Nursing and midwifery personnel (per 10 000 population) |
| UHC_INDEX_REPORTED | UHC Service coverage index | UHC service coverage index |
| FINPROTECTION_CATA_TOT_10_POP | Household health expenditure greater than 10% of household budget | Population with household health spending > 10% of budget (%) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1402 | persen | persen | var.unit: 'Persen' | 3.8.1 | 3.8.1(a) |
| var2279 | persen | persen | var.unit: 'Persen' | 3.8.2 | 3.8.2(a) |
| var1477 | tidak_ada | per_100000_penduduk | var.note: '(per 100.000 penduduk)'; var.unit dan kolom satuan CSV kosong | — | 3.c.1 |
| HWF_0001 | — | per_10000_penduduk | kolom RATE_PER_10000_N; UnitOfMeasure | 3.c.1 | 3.c.1 |
| HWF_0006 | — | per_10000_penduduk | kolom RATE_PER_10000_N; UnitOfMeasure | 3.c.1 | 3.c.1 |
| UHC_INDEX_REPORTED | — | indeks | kolom INDEX_N; UnitOfMeasure: rata-rata skor 14 indikator penanda | 3.8.1 | 3.8.1 |
| FINPROTECTION_CATA_TOT_10_POP | — | persen | kolom PERCENT_POP_N | 3.8.2 | 3.8.2 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var1402 | kode SDG 3.8.1 -> 3.8.1(a) |
| var2279 | kode SDG 3.8.2 -> 3.8.2(a) |
| var1477 | satuan tidak_ada -> per_100000_penduduk; kode SDG kosong -> 3.c.1 |
| HWF_0001 | IND_NAME 'Density of doctors' |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1402 | Sumber: Susenas Maret |
| 2279 | Kepemilikan JKN adalah jika memiliki BPJS PBI, BPJS Non PBI, atau Jamkesda Sumber: Susenas Maret |
| 1477 | Sumber : Informasi SDM Kesehatan Badan PPSDM Kesehatan, Kementerian Kesehatan RI (per 100.000 penduduk) |

## Metadata WDI yang muncul di lebih dari satu berkas

Tidak ada.

## Judul dengan spasi di awal/akhir

Tidak ada.
