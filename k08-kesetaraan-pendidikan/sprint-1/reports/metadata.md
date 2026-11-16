# Metadata seri: nama, satuan, kode SDG

Dihasilkan `python pipeline.py` dari berkas mentah dan `src/konfigurasi.py`. Tabel lengkap ada di `docs/seri.csv`. Bila katalog dan berkas mentah berbeda, berkas mentah yang dipakai dan koreksinya dicatat di `log-keputusan.csv`.

## Nama di berkas mentah dan nama baku

| seri_kode | nama_di_berkas | nama_baku |
|---|---|---|
| var304 | Angka Partisipasi Murni (APM) Menurut Provinsi dan Jenjang Pendidikan | Angka Partisipasi Murni (APM) menurut jenjang SD, SMP, SM |
| var2595 | 4.5.1* Rasio Angka Partisipasi Kasar (APK) pada jenjang SMA/sederajat untuk kuintil terendah/kuintil tertinggi menurut provinsi | Rasio APK SMA/sederajat kuintil pengeluaran terendah terhadap kuintil tertinggi |
| var2600 | 4.5.1* Rasio Angka Partisipasi Kasar (APK) pada jenjang PT/sederajat untuk perempuan/laki-laki menurut provinsi | Rasio APK perguruan tinggi perempuan terhadap laki-laki |
| var1980 | Tingkat Penyelesaian Pendidikan Menurut Jenjang Pendidikan dan Provinsi | Tingkat penyelesaian pendidikan menurut jenjang |
| var2211 | Angka Partisipasi Sekolah (APS) Menurut Provinsi dan Kelompok Umur | Angka Partisipasi Sekolah (APS) menurut kelompok umur |
| SE.ENR.PRSC.FM.ZS | School enrollment, primary and secondary (gross), gender parity index (GPI) | School enrollment, primary and secondary (gross), gender parity index (GPI) |
| SE.PRM.CMPT.ZS | Primary completion rate, total (% of relevant age group) | Primary completion rate, total (% of relevant age group) |

## Satuan dan kode SDG

| seri_kode | katalog_satuan | satuan | bukti_satuan | katalog_sdg | sdg_kode |
|---|---|---|---|---|---|
| var304 | tidak_ada | persen | judul 'Angka Partisipasi Murni'; var.unit kosong; APM hanya siswa usia jenjang, jadi <= 100 | 4.5.1 | 4.1 |
| var2595 | tidak_ada | rasio_x100 | judul 'Rasio APK ... kuintil terendah/kuintil tertinggi'; var.unit kosong; nilai 32–124, Indonesia ±77: rasio dikali 100 | 4.5.1 | 4.5.1 |
| var2600 | tidak_ada | rasio_x100 | judul 'Rasio APK ... perempuan/laki-laki'; var.unit kosong; nilai 62–260, Indonesia ±115: rasio dikali 100 | 4.5.1 | 4.5.1 |
| var1980 | tidak_ada | persen | var.note: 'persentase anak dan remaja yang berhasil menyelesaikan' | 4.1.2 | 4.1.2 |
| var2211 | tidak_ada | persen | judul 'Angka Partisipasi Sekolah'; var.unit kosong; nilai <= 100 | — | — |
| SE.ENR.PRSC.FM.ZS | — | rasio | name: 'gender parity index' | — | 4.5.1 |
| SE.PRM.CMPT.ZS | — | persen_apk | sourceNote: gross intake ratio to the last grade, tanpa memandang umur (bisa > 100) | — | 4.1.2 |

## Koreksi katalog

| seri_kode | koreksi_katalog |
|---|---|
| var304 | satuan tidak_ada -> persen; kode SDG 4.5.1 -> 4.1 |
| var2595 | satuan tidak_ada -> rasio_x100 |
| var2600 | satuan tidak_ada -> rasio_x100 |
| var1980 | satuan tidak_ada -> persen |
| var2211 | satuan tidak_ada -> persen; var.note tidak dipakai (salah tempel) |
| SE.ENR.PRSC.FM.ZS | kode SDG kosong -> 4.5.1 |
| SE.PRM.CMPT.ZS | kode SDG kosong -> 4.1.2 |

## Catatan BPS (var.note)

| var_id | catatan (tanpa tag HTML) |
|---|---|
| 2595 |  |
| 2600 |  |
| 304 | Sumber: BPS, Susenas Catatan: Mulai tahun 2007, APM mencakup pendidikan non-formal (paket A setara SD sederajat, paket B setara SMP sederajat dan paket C setara SMA/SMK sederajat) |
| 2211 | Sumber : BPS, Susenas Definisi : Angka yang menggambarkan ketimpangan partisipasi sekolah antara penduduk berusia 7-17 tahun dengan disabilitas dan tanpa disabilitas |
| 1980 | Definisi Indikator: Indikator ini mengukur persentase anak dan remaja yang berhasil menyelesaikan jenjang pendidikan yang sesuai dengan rentang usianya. Rentang usia yang termasuk dalam perhitungan ini adalah antara 1 sampai dengan 3 tahun sejak usia kelulusan jenjang pendidikan pada umumnya. Berdasarkan usia wajib belajar yang dimulai sejak 7 tahun, maka dengan asumsi siswa belajar penuh waktu dan tidak tinggal kelas, mereka lulus SD/sederajat pada usia sekitar 12 tahun. Oleh karena itu rentang usia yang digunakan untuk penghitungan tingkat ketuntasan SD/sederajat adalah anak atau remaja usia 13 tahun (12 + 1 tahun) sampai dengan 15 tahun (12 + 3 tahun). Tingkat penyelesaian yang mencapai atau mendekati 100% menunjukkan bahwa hampir seluruh anak-anak dan remaja telah menyelesaikan jenjang pendidikan yang seharusnya atau sesuai usia mereka, tanpa keterlambatan yang signifikan atau berarti. Sumber Data: Susenas KOR |

## Metadata WDI yang muncul di lebih dari satu berkas

| seri | jumlah_entri | berkas | isi_sama |
|---|---|---|---|
| SE.ENR.PRSC.FM.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |
| SE.PRM.CMPT.ZS | 2 | sumber2_indikator.json, sumber46_indikator.json | ya |

## Judul dengan spasi di awal/akhir

Tidak ada.
