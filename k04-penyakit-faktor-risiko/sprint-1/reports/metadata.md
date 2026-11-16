# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1393 | Kejadian Malaria Per 1000 Orang | Kejadian malaria per 1.000 penduduk |
| var1480 | Prevalensi Tekanan Darah Tinggi Menurut Provinsi | Prevalensi tekanan darah tinggi (hasil pengukuran) |
| var1435 | Persentase Penduduk Berumur 15 Tahun ke Atas yang Merokok Tembakau selama Sebulan Terakhir Menurut Provinsi | Persentase penduduk umur 15 tahun ke atas yang merokok tembakau selama sebulan terakhir |
| SH.MLR.INCD.P3 | Incidence of malaria (per 1,000 population at risk) | Incidence of malaria (per 1,000 population at risk) |
| MALARIA_EST_INCIDENCE | Malaria cases | Estimated malaria incidence (per 1000 population at risk) |
| NCDMORT3070 | Non-communicable diseases deaths (age 30 to 70) | Probability of dying between age 30 and 70 from any of CVD, cancer, diabetes, or CRD (%) |
| M_Est_tob_curr_std | Tobacco use | Age-standardized prevalence of current tobacco use, 15+ (%) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1393 | tidak_ada | per_1000_penduduk | var.label: 'Kejadian Malaria Per 1000 Orang'; var.unit, kolom satuan CSV, dan satuan di manifest_asal kosong | 3.3.3 | 3.3.3 |
| var1480 | tidak_ada | persen | var.label: 'Prevalensi ...'; var.unit kosong; besaran angka 20–40 sesuai persen penduduk | 3.4.1 | 3.4.1(b) |
| var1435 | persen | persen | var.unit: 'Persen' | 3.a.1 | 3.a.1 |
| SH.MLR.INCD.P3 | — | per_1000_penduduk_berisiko | name: '(per 1,000 population at risk)' | — | 3.3.3 |
| MALARIA_EST_INCIDENCE | — | per_1000_penduduk_berisiko | kolom RATE_PER_1000_N; Denominator: 'Population living in areas where malaria transmission occurs' | 3.3.3 | 3.3.3 |
| NCDMORT3070 | — | persen | kolom RATE_PER_100_N; UnitOfMeasure: percentage of 30-year-old people | 3.4.1 | 3.4.1 |
| M_Est_tob_curr_std | — | persen | kolom PERCENT_POP_N | 3.a.1 | 3.a.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var1393 | satuan tidak_ada -> per_1000_penduduk |
| var1480 | satuan tidak_ada -> persen; kode SDG 3.4.1 -> 3.4.1(b) |
| SH.MLR.INCD.P3 | kode SDG kosong -> 3.3.3 |
| MALARIA_EST_INCIDENCE | IND_NAME 'Malaria cases' tidak menyebut estimasi dan penyebut |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1393 | Sumber : Kementerian Kesehatan RI, Profil Kesehatan Indonesia |
| 1480 | Sumber: Riskesdas 2007 dan 2013, Sirkesnas 2016, Integrasi Susenas dan Riskesdas 2018, Kementerian Kesehatan RI berdasarkan hasil pengukuran tekanan darah |
| 1435 | Sumber: Susenas Maret |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SH.MLR.INCD.P3 | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
