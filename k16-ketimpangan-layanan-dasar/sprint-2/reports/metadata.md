# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var2011 | Proporsi penduduk yang hidup di bawah 50 persen dari median pendapatan, menurut provinsi | Proporsi penduduk yang hidup di bawah 50 persen dari median pendapatan |
| var2016 | Proporsi rumah tangga dengan akses terhadap pelayanan dasar menurut provinsi | Proporsi rumah tangga dengan akses terhadap pelayanan dasar |
| var1254 | Total pendapatan pemerintah sebagai proporsi terhadap PDB menurut sumbernya | Total pendapatan pemerintah sebagai proporsi terhadap PDB |
| SI.DST.50MD | Proportion of people living below 50 percent of median income (%) | Proportion of people living below 50 percent of median income (%) |
| SI.POV.DDAY | Poverty headcount ratio at $3.00 a day (2021 PPP) (% of population) | Poverty headcount ratio at $3.00 a day (2021 PPP) (% of population) |
| SDG_0111_SEX_AGE_RT | SDG indicator 1.1.1: Working poverty rate by sex and age | Working poverty rate by sex and age (%) |
| SDG_0131_SEX_SOC_RT | SDG indicator 1.3.1: Proportion of population covered by social protection floors/systems by sex and function | Proportion of population covered by social protection floors/systems (%) |
| SDG_1041_NOC_RT | SDG indicator 10.4.1: Labour income share as a percent of GDP | Labour income share as a percent of GDP (%) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var2011 | tidak_ada | persen | judul 'Proporsi penduduk'; var.unit kosong; nilai 0–30 | 10.2.1 | 10.2.1 |
| var2016 | persen | persen | var.unit: 'Persen' | 1.4.1 | 1.4.1 |
| var1254 | tidak_ada | persen | judul 'sebagai proporsi terhadap PDB'; var.unit kosong | 17.1.1 | 17.1.1 |
| SI.DST.50MD | — | persen | name: '(%)' | — | 10.2.1 |
| SI.POV.DDAY | — | persen | name: '(% of population)' | — | 1.1.1 |
| SDG_0111_SEX_AGE_RT | — | persen | UNIT_MEASURE PT | 1.1.1 | 1.1.1 |
| SDG_0131_SEX_SOC_RT | — | persen | UNIT_MEASURE PT | 1.3.1 | 1.3.1 |
| SDG_1041_NOC_RT | — | persen | UNIT_MEASURE PT | 10.4.1 | 10.4.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var2011 | satuan tidak_ada -> persen |
| var1254 | satuan tidak_ada -> persen |
| SI.DST.50MD | kode SDG kosong -> 10.2.1 |
| SI.POV.DDAY | kode SDG kosong -> 1.1.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 2011 | Sumber Data: Susenas Data beberapa provinsi tidak dapat ditampilkan karena Relative Standard Error (RSE) hasil estimasi terlalu tinggi |
| 1254 | Sumber : BPS |
| 2016 | Komponen penyusun indikator air minum yang dikelola secara aman (air layak, terletak di dalam kawasan rumah, tersedia setiap dibutuhkan (tidak kekurangan air dalam 24 jam), dan memenuhi syarat kualitas kualitas air minum (tidak keruh, berwarna, berbusa, dll)). Sedangkan air minum layak mencakup: Rumah tangga memiliki sumber air minum utama yang berupa leding, air terlindungi, dan air hujan. Air terlindungi mencakup sumur bor/pompa, sumur terlindung dan mata air terlindung. Bagi rumah tangga yang menggunakan sumber air minum berupa air kemasan, maka rumah tangga dikategorikan memiliki akses air minum layak jika sumber air untuk mandi/cuci berasal dari leding, sumur bor/pompa, sumur terlindung, mata air terlindung, dan air hujan. Sanitasi layak: Rumah tangga memiliki fasilitas tempat Buang Air Besar (BAB) yang digunakan sendiri atau bersama rumah tangga tertentu (terbatas) ataupun di MCK Komunal, menggunakan jenis kloset leher angsa, dan tempat pembuangan akhir tinja di tangki septik atau IPAL atau bisa juga di lubang tanah jika wilayah tempat tinggalnya di perdesaan. Sumber Data: Susenas |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SI.DST.50MD | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SI.POV.DDAY | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
