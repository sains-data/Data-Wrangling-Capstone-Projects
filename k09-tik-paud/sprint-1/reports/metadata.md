# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var1451 | 4.4.1.(a) Proporsi Remaja Dan Dewasa Usia 15-24 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Provinsi | Proporsi remaja dan dewasa usia 15–24 tahun dengan keterampilan TIK |
| var1447 | 4.4.1.(b) Proporsi Remaja Dan Dewasa Usia 15-59 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Provinsi | Proporsi remaja dan dewasa usia 15–59 tahun dengan keterampilan TIK |
| var1439 | Angka Partisipasi Kasar (APK) Anak Yang Mengikuti Pendidikan Anak Usia Dini (PAUD) Menurut Provinsi | Angka Partisipasi Kasar (APK) PAUD |
| var1221 | 5.b.1* Proporsi Individu yang Menguasai/Memiliki Telepon Genggam Menurut Provinsi | Proporsi individu yang menguasai/memiliki telepon genggam |
| SE.PRE.ENRR | School enrollment, preprimary (% gross) | School enrollment, preprimary (% gross) |
| IT.NET.USER.ZS | Individuals using the Internet (% of population) | Individuals using the Internet (% of population) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var1451 | persen | persen | var.unit: 'Persen' | 4.4.1 | 4.4.1(a) |
| var1447 | persen | persen | var.unit: 'Persen' | 4.4.1 | 4.4.1(b) |
| var1439 | tidak_ada | persen_apk | judul 'Angka Partisipasi Kasar'; var.unit kosong; APK bisa > 100 | 4.2.2 | 4.2.2 |
| var1221 | persen | persen | var.unit: 'Persen' | 5.b.1 | 5.b.1 |
| SE.PRE.ENRR | — | persen_apk | name: '(% gross)' | — | 4.2.2 |
| IT.NET.USER.ZS | — | persen | name: '(% of population)' | — | 17.8.1 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var1451 | kode SDG 4.4.1 -> 4.4.1(a) |
| var1447 | kode SDG 4.4.1 -> 4.4.1(b) |
| var1439 | satuan tidak_ada -> persen_apk |
| SE.PRE.ENRR | kode SDG kosong -> 4.2.2 |
| IT.NET.USER.ZS | kode SDG kosong -> 17.8.1 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 1451 | Sumber: SUSENAS KOR, BPS |
| 1447 | Sumber : BPS |
| 1439 | Sumber: BPS, Susenas Catatan: APK PAUD 3-6 Tahun Provinsi Papua Pegunungan Tahun 2024-2025 memiliki Relative Standard Error (RSE) antara 25-50 persen, sehingga perlu kehati-hatian dalam penggunaan hasil estimasi |
| 1221 | Sumber: Susenas Kor, BPS Proporsi individu umur 5 tahun ke atas |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| IT.NET.USER.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SE.PRE.ENRR | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
