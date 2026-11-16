# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1360 | Proporsi Perempuan Umur 20-24 Tahun Yang Berstatus Kawin Atau Berstatus Hidup Bersama Sebelum Umur 18 Tahun Menurut Provinsi | Proporsi perempuan umur 20–24 tahun yang berstatus kawin atau hidup bersama sebelum umur 18 tahun |
| var2003 | Proporsi perempuan yang berada di posisi managerial menurut provinsi | Proporsi perempuan yang berada di posisi manajerial |
| SG.GEN.PARL.ZS | Proportion of seats held by women in national parliaments (%) | Proportion of seats held by women in national parliaments (%) |
| SP.M18.2024.FE.ZS | Women who were first married by age 18 (% of women ages 20-24) | Women who were first married by age 18 (% of women ages 20-24) |
| SDG_0552_NOC_RT | SDG indicator 5.5.2: Proportion of women in senior and middle management positions | Proportion of women in senior and middle management positions (%) |
| SDG_T552_NOC_RT | SDG indicator 5.5.2: Proportion of women in managerial positions | Proportion of women in managerial positions, total management (%) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1360 | persen | persen | var.unit: 'Persen' | 5.3.1 | 5.3.1 |
| var2003 | tidak_ada | persen | judul 'Proporsi'; var.unit kosong; nilai 10–50 dan dekat dengan ILO (UNIT_MEASURE PT = persen) | 5.5.2 | 5.5.2 |
| SG.GEN.PARL.ZS | — | persen | name: '(%)' | — | 5.5.1 |
| SP.M18.2024.FE.ZS | — | persen | name: '(% of women ages 20-24)' | — | 5.3.1 |
| SDG_0552_NOC_RT | — | persen | UNIT_MEASURE PT | 5.5.2 | 5.5.2 |
| SDG_T552_NOC_RT | — | persen | UNIT_MEASURE PT | 5.5.2 | 5.5.2 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var2003 | satuan tidak_ada -> persen |
| SG.GEN.PARL.ZS | kode SDG kosong -> 5.5.1 |
| SP.M18.2024.FE.ZS | kode SDG kosong -> 5.3.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1360 | Sumber : Susenas, Badan Pusat Statistik Definisi : bagian dari seluruh perempuan berumur 20—24 tahun yang usia saat kawin pertama atau hidup bersama pertama kali sebelum berumur 18 tahun |
| 2003 | Sumber Data: Sakernas Catatan: Mencakup seluruh lapangan usaha yang ada pada KBLI 2015 |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SG.GEN.PARL.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SP.M18.2024.FE.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
