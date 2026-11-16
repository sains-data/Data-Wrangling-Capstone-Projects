# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var192 | 2007→2008 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2008→2009 | 33 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2009→2010 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2010→2011 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2011→2012-S1 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2012-S1→2012-S2 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2012-S2→2013-S1 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2013-S1→2013-S2 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2013-S2→2014-S1 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2014-S1→2014-S2 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2014-S2→2015-S1 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2015-S1→2015-S2 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2015-S2→2016-S1 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2016-S1→2016-S2 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2016-S2→2017-S1 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2017-S1→2017-S2 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2017-S2→2018-S1 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2018-S1→2018-S2 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2018-S2→2019-S1 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2019-S1→2019-S2 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2019-S2→2020-S1 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2020-S1→2020-S2 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2020-S2→2021-S1 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2021-S1→2021-S2 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2021-S2→2022-S1 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2022-S1→2022-S2 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2022-S2→2023-S1 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2023-S1→2024-S1 | 34 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2024-S1→2024-S2 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2024-S2→2025-S1 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2025-S1→2025-S2 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var192 | 2025-S2→2026-S1 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2190 | 2019→2020 | 29 | 0.76 | 0.03 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var2190 | 2020→2021 | 29 | 0.41 | 0.14 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var2191 | 2019→2020 | 32 | 0.00 | 0.78 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var2191 | 2020→2021 | 30 | 0.00 | 0.70 | ya | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

- `var2190` mulai 2020: var.note: Indeks Desa 2020 dari Updating Podes 2020 dan daftar desa Kepmendagri 146/2020 (2019: Podes 2018 + Updating 2019, Kepmendagri 414/2019)
- `var2190` mulai 2021: var.note: Indeks Desa 2021 dari Pendataan Podes 2021 (2020: Updating Podes 2020)
- `var2191` mulai 2020: var.note: Indeks Desa 2020 dari Updating Podes 2020 dan daftar desa Kepmendagri 146/2020 (2019: Podes 2018 + Updating 2019, Kepmendagri 414/2019)
- `var2191` mulai 2021: var.note: Indeks Desa 2021 dari Pendataan Podes 2021 (2020: Updating Podes 2020)

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 3

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var192 | Kalimantan Timur | 6400 | 2015-S1 | Kalimantan Utara | 6.31 | 6.23 |
| var192 | Papua Barat | 9100 | 2024-S1 | Papua Barat Daya | 20.49 | 21.66 |
| var192 | Papua | 9400 | 2024-S1 | Papua Selatan, Papua Tengah, Papua Pegunungan | 26.03 | 17.26 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (227)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var192 | Aceh | 2007 | 26.65 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sumatera Utara | 2007 | 13.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sumatera Barat | 2007 | 11.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Riau | 2007 | 11.20 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Jambi | 2007 | 10.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sumatera Selatan | 2007 | 19.15 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Bengkulu | 2007 | 22.13 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Lampung | 2007 | 22.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Bangka Belitung | 2007 | 9.54 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Riau | 2007 | 10.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Jawa Barat | 2007 | 13.55 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Jawa Tengah | 2007 | 20.43 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Jawa Timur | 2007 | 19.98 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Banten | 2007 | 9.07 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Bali | 2007 | 6.63 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Nusa Tenggara Barat | 2007 | 24.99 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Nusa Tenggara Timur | 2007 | 27.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Barat | 2007 | 12.91 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Tengah | 2007 | 9.38 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Selatan | 2007 | 7.01 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Timur | 2007 | 11.04 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Utara | 2007 | 11.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Tengah | 2007 | 22.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Selatan | 2007 | 14.11 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Tenggara | 2007 | 21.33 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Gorontalo | 2007 | 27.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Barat | 2007 | 19.03 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Maluku | 2007 | 31.14 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Maluku Utara | 2007 | 11.97 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2007 | 39.31 | ke bawah + ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2007 | 40.78 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Aceh | 2008 | 23.53 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sumatera Barat | 2008 | 10.67 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Riau | 2008 | 10.63 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sumatera Selatan | 2008 | 17.73 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Lampung | 2008 | 20.98 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Bangka Belitung | 2008 | 8.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Riau | 2008 | 9.18 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Jawa Barat | 2008 | 13.01 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Jawa Timur | 2008 | 18.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Banten | 2008 | 8.15 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Bali | 2008 | 6.17 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Nusa Tenggara Barat | 2008 | 23.81 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Nusa Tenggara Timur | 2008 | 25.65 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Barat | 2008 | 11.07 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Tengah | 2008 | 8.71 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Selatan | 2008 | 6.48 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Timur | 2008 | 9.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Tengah | 2008 | 20.75 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Selatan | 2008 | 13.34 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Tenggara | 2008 | 19.53 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Gorontalo | 2008 | 24.88 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Barat | 2008 | 16.73 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Maluku | 2008 | 29.66 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Maluku Utara | 2008 | 11.28 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2008 | 35.12 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2008 | 37.08 | perubahan + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Sumatera Selatan | 2009 | 16.28 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Lampung | 2009 | 20.22 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Bangka Belitung | 2009 | 7.46 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Riau | 2009 | 8.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Jawa Timur | 2009 | 16.68 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Banten | 2009 | 7.64 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Nusa Tenggara Barat | 2009 | 22.78 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Timur | 2009 | 7.73 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Tengah | 2009 | 18.98 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Selatan | 2009 | 12.31 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Tenggara | 2009 | 18.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Gorontalo | 2009 | 25.01 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Barat | 2009 | 15.29 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Maluku | 2009 | 28.23 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Maluku Utara | 2009 | 10.36 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2009 | 35.71 | ke bawah + perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2009 | 37.53 | ke bawah + perubahan + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Lampung | 2010 | 18.94 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Bangka Belitung | 2010 | 6.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Riau | 2010 | 8.05 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Timur | 2010 | 7.66 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Sulawesi Tengah | 2010 | 18.07 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Gorontalo | 2010 | 23.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Maluku | 2010 | 27.74 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Maluku Utara | 2010 | 9.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2010 | 34.88 | ke bawah | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2010 | 36.80 | ke bawah + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Gorontalo | 2011 | 18.75 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Maluku | 2011 | 23.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2011 | 31.92 | ke bawah | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2011 | 31.98 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Barat | 2012-S1 | 28.20 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2012-S1 | 31.11 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Aceh | 2012-S2 | 18.58 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Maluku | 2012-S2 | 20.76 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2012-S2 | 27.04 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2012-S2 | 30.66 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Aceh | 2013-S1 | 17.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Sumatera Selatan | 2013-S1 | 14.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Bengkulu | 2013-S1 | 18.34 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Maluku | 2013-S1 | 19.49 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2013-S1 | 31.13 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Barat | 2013-S2 | 27.14 | ke bawah | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2013-S2 | 31.53 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Sumatera Utara | 2014-S1 | 9.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2014-S1 | 27.13 | ke bawah | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2014-S1 | 30.05 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Sulawesi Tenggara | 2014-S2 | 12.77 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2014-S2 | 26.26 | ke bawah | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2014-S2 | 27.80 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Nusa Tenggara Timur | 2015-S1 | 22.61 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2015-S1 | 28.17 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | DI Yogyakarta | 2015-S2 | 13.16 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2015-S2 | 25.73 | ke bawah | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2015-S2 | 28.40 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua | 2016-S1 | 28.54 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Kalimantan Utara | 2016-S2 | 6.99 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2016-S2 | 28.40 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Bengkulu | 2017-S1 | 16.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Maluku | 2017-S1 | 18.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2017-S1 | 27.62 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Barat | 2017-S2 | 23.12 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2017-S2 | 27.76 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Jawa Tengah | 2018-S1 | 11.32 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2018-S1 | 27.74 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Gorontalo | 2018-S2 | 15.83 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2018-S2 | 27.43 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Jawa Timur | 2019-S1 | 10.37 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Maluku Utara | 2019-S1 | 6.77 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2019-S1 | 22.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2019-S1 | 27.53 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Nusa Tenggara Barat | 2019-S2 | 13.88 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Nusa Tenggara Timur | 2019-S2 | 20.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Maluku Utara | 2019-S2 | 6.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2019-S2 | 21.51 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2019-S2 | 26.55 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | DKI Jakarta | 2020-S1 | 4.53 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Jawa Barat | 2020-S1 | 7.88 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Jawa Tengah | 2020-S1 | 11.41 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | DI Yogyakarta | 2020-S1 | 12.28 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Jawa Timur | 2020-S1 | 11.09 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Banten | 2020-S1 | 5.92 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2020-S1 | 26.64 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua | 2020-S2 | 26.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua | 2021-S1 | 26.86 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Maluku | 2021-S2 | 16.30 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2021-S2 | 27.38 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Aceh | 2022-S1 | 14.64 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Sumatera Selatan | 2022-S1 | 11.90 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Riau | 2022-S1 | 6.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2022-S1 | 21.33 | ke bawah | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2022-S1 | 26.56 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Bengkulu | 2022-S2 | 14.34 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2022-S2 | 21.43 | ke bawah | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2022-S2 | 26.80 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Barat | 2023-S1 | 20.49 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2023-S1 | 26.03 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Barat | 2024-S1 | 21.66 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var192 | Papua | 2024-S1 | 17.26 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var192 | Papua Tengah | 2024-S1 | 29.76 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Pegunungan | 2024-S1 | 32.97 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Aceh | 2024-S2 | 12.64 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Sumatera Selatan | 2024-S2 | 10.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Riau | 2024-S2 | 4.78 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2024-S2 | 18.09 | perubahan + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Selatan | 2024-S2 | 19.35 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Tengah | 2024-S2 | 27.60 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Pegunungan | 2024-S2 | 29.66 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Sumatera Selatan | 2025-S1 | 10.15 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Riau | 2025-S1 | 4.44 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Selatan | 2025-S1 | 3.84 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Timur | 2025-S1 | 5.17 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat Daya | 2025-S1 | 17.95 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2025-S1 | 19.16 | perubahan + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Selatan | 2025-S1 | 19.71 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Tengah | 2025-S1 | 28.90 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Pegunungan | 2025-S1 | 30.03 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Sumatera Selatan | 2025-S2 | 9.85 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Riau | 2025-S2 | 4.26 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Nusa Tenggara Timur | 2025-S2 | 17.50 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Selatan | 2025-S2 | 3.73 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Timur | 2025-S2 | 5.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2025-S2 | 19.58 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2025-S2 | 17.82 | perubahan + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Tengah | 2025-S2 | 29.45 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Pegunungan | 2025-S2 | 27.21 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Sumatera Selatan | 2026-S1 | 9.50 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kepulauan Riau | 2026-S1 | 4.09 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Selatan | 2026-S1 | 3.63 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Timur | 2026-S1 | 5.14 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Kalimantan Utara | 2026-S1 | 5.18 | ke samping | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat | 2026-S1 | 18.68 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Barat Daya | 2026-S1 | 16.49 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua | 2026-S1 | 18.39 | perubahan + ke samping | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Selatan | 2026-S1 | 18.54 | perubahan | outlier | tandai, nilai tidak diubah |
| var192 | Papua Tengah | 2026-S1 | 30.41 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var192 | Papua Pegunungan | 2026-S1 | 26.34 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2190 | Jawa Barat | 2019 | 341.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2190 | Jawa Tengah | 2019 | 296.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2190 | DI Yogyakarta | 2019 | 127.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2190 | Jawa Timur | 2019 | 345.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2190 | Bali | 2019 | 88.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2190 | Jawa Barat | 2020 | 518.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | Jawa Tengah | 2020 | 510.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | DI Yogyakarta | 2020 | 151.00 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | Jawa Timur | 2020 | 589.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | Bali | 2020 | 154.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | Nusa Tenggara Barat | 2020 | 67.00 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | Jawa Barat | 2021 | 636.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | Jawa Tengah | 2021 | 685.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | DI Yogyakarta | 2021 | 179.00 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | Jawa Timur | 2021 | 697.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | Bali | 2021 | 181.00 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2190 | Nusa Tenggara Barat | 2021 | 105.00 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Aceh | 2019 | 1,710.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2191 | Sumatera Utara | 2019 | 2,535.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2191 | Nusa Tenggara Timur | 2019 | 1,563.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2191 | Papua Barat | 2019 | 1,587.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2191 | Papua | 2019 | 5,094.00 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var2191 | Aceh | 2020 | 915.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Sumatera Utara | 2020 | 2,166.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Nusa Tenggara Timur | 2020 | 1,127.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Papua Barat | 2020 | 1,558.00 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Papua | 2020 | 5,015.00 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Aceh | 2021 | 708.00 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Sumatera Utara | 2021 | 1,848.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Nusa Tenggara Timur | 2021 | 955.00 | ke bawah + perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Kalimantan Barat | 2021 | 613.00 | perubahan | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Papua Barat | 2021 | 1,505.00 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |
| var2191 | Papua | 2021 | 4,970.00 | ke bawah | patahan_seri | tandai; definisi berganti menurut penerbit |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var192 | 3461 | 3461 | 3461 | 0 | 0 | 0 | Persen |
| var2190 | 102 | 102 | 102 | 0 | 0 | 0 | Desa |
| var2191 | 306 | 306 | 306 | 0 | 0 | 0 | Desa |

## Kunci Silver kembar: 0
