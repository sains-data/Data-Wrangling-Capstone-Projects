# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1473 | Prevalensi Ketidakcukupan Konsumsi Pangan | Prevalensi Ketidakcukupan Konsumsi Pangan (Prevalence of Undernourishment) |
| var1474 | Prevalensi Penduduk Dengan Kerawanan Pangan Sedang Atau Berat, Berdasarkan Pada Skala Pengalaman Kerawanan Pangan | Prevalensi penduduk dengan kerawanan pangan sedang atau berat (Skala Pengalaman Kerawanan Pangan, FIES) |
| SN.ITK.DEFC.ZS | Prevalence of undernourishment (% of population) | Prevalence of undernourishment (% of population) |
| SN.ITK.MSFI.ZS | Prevalence of moderate or severe food insecurity in the population (%) | Prevalence of moderate or severe food insecurity in the population (%) |
| NUTSTUNTINGPREV | Stunting in children (under 5) | Stunting in children (under 5) |
| NUTOVERWEIGHTPREV | Overweight in children (under 5) | Overweight in children (under 5) |
| NUTRITION_WH_2 | Wasting in children (under 5) | Wasting in children (under 5) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1473 | persen | persen | var.unit: 'Persen'; kolom satuan CSV 'Persen' | 2.1.1 | 2.1.1 |
| var1474 | persen | persen | var.unit: 'Persen' | 2.1.2 | 2.1.2 |
| SN.ITK.DEFC.ZS | — | persen | name: '(% of population)' | — | 2.1.1 |
| SN.ITK.MSFI.ZS | — | persen | name: '(%)' | — | 2.1.2 |
| NUTSTUNTINGPREV | — | persen | kolom RATE_PER_100_N | 2.2.1 | 2.2.1 |
| NUTOVERWEIGHTPREV | — | persen | kolom RATE_PER_100_N | 2.2.2 | 2.2.2 |
| NUTRITION_WH_2 | — | persen | kolom RATE_PER_100_N | 2.2.2 | 2.2.2 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| SN.ITK.DEFC.ZS | kode SDG kosong -> 2.1.1 |
| SN.ITK.MSFI.ZS | kode SDG kosong -> 2.1.2 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1473 | Sumber : Susenas |
| 1474 | Sumber : Susenas Definisi : Bagian dari populasi penduduk yang pernah atau sedang mengalami kerawanan pangan tingkat sedang atau parah berdasarkan skala pengalaman kerawanan pangan / food insecurity experience scale (FIES) setidaknya sekali dalam 12 bulan terakhir. |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SN.ITK.DEFC.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SN.ITK.MSFI.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
