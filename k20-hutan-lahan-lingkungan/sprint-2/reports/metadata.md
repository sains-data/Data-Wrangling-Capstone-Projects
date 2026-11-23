# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | Rekapitulasi Luas Penutupan Lahan Hutan dan Non Hutan Menurut Provinsi Tahun 2014-2023 (Ribu Ha) | Luas penutupan lahan hutan dan non hutan (ribu ha) |
| tabel:sdg15_tutupan_hutan:persen | Rekapitulasi Luas Penutupan Lahan Hutan dan Non Hutan Menurut Provinsi Tahun 2014-2023 (Ribu Ha) | Persentase penutupan lahan hutan dan non hutan |
| var1304 | Luas Penutupan Lahan Indonesa di Dalam dan di Luar Kawasan Hutan Menurut Provinsi | Luas penutupan lahan di dalam dan di luar kawasan hutan (ribu ha) |
| var588 | Luas dan Penyebaran Lahan Kritis Menurut Provinsi | Luas lahan kritis dan sangat kritis (hektar) |
| var2532 | Komponen Penyusun Indeks Kualitas Lingkungan Hidup Menurut Provinsi | Komponen penyusun Indeks Kualitas Lingkungan Hidup (IKLH) |
| AG.LND.FRST.K2 | Forest area (sq. km) | Forest area (sq. km) |
| AG.LND.FRST.ZS | Forest area (% of land area) | Forest area (% of land area) |
| EN.ATM.PM25.MC.M3 | PM2.5 air pollution, mean annual exposure (micrograms per cubic meter) | PM2.5 air pollution, mean annual exposure (micrograms per cubic meter) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| tabel:sdg15_tutupan_hutan:luas_ribu_ha | ribu_hektar | ribu_hektar | judul tabel '(Ribu Ha)'; header 'Luas Penutupan Lahan (Ribu Ha)' | 15.1.1 | 15.1.1 |
| tabel:sdg15_tutupan_hutan:persen | persen | persen | header '%' | 15.1.1 | 15.1.1 |
| var1304 | ribu_hektar | ribu_hektar | var.unit: 'Ribu Hektar' | 15.3.1 | 15.1.1 |
| var588 | hektar | hektar | var.unit: 'Hektar' | 15.3.1 | 15.3.1 |
| var2532 | tidak_ada | indeks | judul 'Indeks'; nilai 0–100 | 11.6.2 | 15 |
| AG.LND.FRST.K2 | — | km2 | name: '(sq. km)' | — | 15.1.1 |
| AG.LND.FRST.ZS | — | persen | name: '(% of land area)' | — | 15.1.1 |
| EN.ATM.PM25.MC.M3 | — | mikrogram_per_m3 | name: '(micrograms per cubic meter)' | — | 11.6.2 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var1304 | kode SDG 15.3.1 -> 15.1.1 (luas tutupan, bukan degradasi) |
| var2532 | satuan tidak_ada -> indeks; kode SDG 11.6.2 -> 15 |
| AG.LND.FRST.K2 | kode SDG kosong -> 15.1.1 |
| AG.LND.FRST.ZS | kode SDG kosong -> 15.1.1 |
| EN.ATM.PM25.MC.M3 | kode SDG kosong -> 11.6.2 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 2532 | Sumber: Kementerian Lingkungan Hidup/ Badan Pengendalian Lingkungan Hidup |
| 588 | - Sumber : Statistik Kementerian Lingkungan Hidup dan Kehutanan, 2018 - Berdasarkan Peraturan Direktur Jenderal Bina Pengelolaan Daerah Aliran Sungai (DAS) Dan Perhutanan Sosial NOMOR : P. 4/V-SET/2013 menyebutkan bahwa Review lahan kritis dilakukan setiap 5 tahun sesuai dengan periode review rencana pengelolaan DAS. Dalam keadaan tertentu, apabila diperlukan maka periode review lahan kritis dapat dilakukan sebelum 5 tahun. |
| 1304 | Sumber : Rekalkulasi Penutupan Lahan Indonesia 2014-2023, Kementerian Lingkungan Hidup dan Kehutanan Definisi : Kenampakan biofisik di permukaan bumi yang terdiri dari areal bervegetasi, lahan terbuka, lahan terbangun, serta tubuh air dan lahan basah. |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| AG.LND.FRST.K2 | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| AG.LND.FRST.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| EN.ATM.PM25.MC.M3 | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
