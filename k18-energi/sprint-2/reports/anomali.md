# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var87 | 1993→1994 | 26 | 0.12 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 1994→1995 | 26 | 0.12 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 1995→1996 | 26 | 0.04 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 1996→1997 | 26 | 0.15 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 1997→1998 | 26 | 0.08 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 1998→1999 | 26 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 1999→2000 | 24 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2000→2001 | 24 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2001→2002 | 29 | 0.10 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2002→2003 | 30 | 0.00 | 0.10 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2003→2004 | 30 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2004→2006 | 30 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2006→2007 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2007→2008 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2008→2009 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2009→2010 | 33 | 0.03 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2010→2011 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2011→2012 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2012→2013 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2013→2014 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2014→2015 | 33 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2015→2016 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2016→2017 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2017→2018 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2018→2019 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2019→2020 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2020→2021 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2021→2022 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2022→2023 | 34 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2023→2024 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var87 | 2024→2025 | 38 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2001→2007 | 27 | 0.74 | 0.07 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2007→2008 | 33 | 0.76 | 0.03 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2008→2009 | 33 | 0.33 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2009→2010 | 33 | 0.36 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2010→2011 | 33 | 0.45 | 0.21 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2011→2012 | 33 | 0.52 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2012→2013 | 33 | 0.21 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2013→2014 | 33 | 0.33 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2014→2015 | 33 | 0.39 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2015→2016 | 34 | 0.24 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2016→2017 | 34 | 0.12 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2017→2018 | 34 | 0.15 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2018→2019 | 34 | 0.03 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2019→2020 | 34 | 0.06 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | 2020→2021 | 34 | 0.12 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2001→2007 | 27 | 0.00 | 0.33 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2007→2008 | 33 | 0.00 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2008→2009 | 33 | 0.00 | 0.24 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2009→2010 | 33 | 0.09 | 0.33 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2010→2011 | 33 | 0.00 | 0.52 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2011→2012 | 33 | 0.00 | 0.67 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2012→2013 | 33 | 0.03 | 0.33 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2013→2014 | 33 | 0.00 | 0.52 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2014→2015 | 33 | 0.00 | 0.55 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2015→2016 | 34 | 0.00 | 0.38 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2016→2017 | 34 | 0.06 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2017→2018 | 34 | 0.00 | 0.38 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2018→2019 | 34 | 0.21 | 0.38 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2019→2020 | 34 | 0.06 | 0.47 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | 2020→2021 | 33 | 0.06 | 0.45 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2001→2007 | 27 | 0.15 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2007→2008 | 33 | 0.06 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2008→2009 | 33 | 0.00 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2009→2010 | 33 | 0.00 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2010→2011 | 33 | 0.00 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2011→2012 | 33 | 0.00 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2012→2013 | 33 | 0.03 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2013→2014 | 33 | 0.00 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2014→2015 | 33 | 0.00 | 0.39 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2015→2016 | 34 | 0.00 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2016→2017 | 34 | 0.00 | 0.53 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2017→2018 | 34 | 0.03 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2018→2019 | 34 | 0.03 | 0.24 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2019→2020 | 34 | 0.09 | 0.24 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | 2020→2021 | 34 | 0.03 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

- `var87` 2002: Aceh, Maluku, Maluku Utara, Papua

## Perubahan batas wilayah di tengah panel: 22

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var87 | Riau | 1400 | 2006 | Kepulauan Riau | 60.24 | 57.95 |
| var87 | Sumatera Selatan | 1600 | 2001 | Kepulauan Bangka Belitung | 64.08 | 59.34 |
| var87 | Jawa Barat | 3200 | 2001 | Banten | 93.09 | 93.22 |
| var87 | Kalimantan Timur | 6400 | 2015 | Kalimantan Utara | 85.20 | 87.55 |
| var87 | Sulawesi Utara | 7100 | 2001 | Gorontalo | 83.86 | 92.50 |
| var87 | Sulawesi Selatan | 7300 | 2006 | Sulawesi Barat | 74.75 | 81.63 |
| var87 | Maluku | 8100 | 2001 | Maluku Utara | 66.11 | 76.81 |
| var87 | Papua Barat | 9100 | 2024 | Papua Barat Daya | 83.20 | 82.31 |
| var87 | Papua | 9400 | 2006 | Papua Barat | 41.55 | 36.55 |
| var87 | Papua | 9400 | 2024 | Papua Selatan, Papua Tengah, Papua Pegunungan | 47.07 | 90.24 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Riau | 1400 | 2007 | Kepulauan Riau | 6.09 | 12.07 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Kalimantan Timur | 6400 | 2015 | Kalimantan Utara | 79.94 | 91.55 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Sulawesi Selatan | 7300 | 2007 | Sulawesi Barat | 18.92 | 14.21 |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua | 9400 | 2007 | Papua Barat | 0.87 | 0.83 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Riau | 1400 | 2007 | Kepulauan Riau | 50.08 | 44.63 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Timur | 6400 | 2015 | Kalimantan Utara | 8.80 | 1.73 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Selatan | 7300 | 2007 | Sulawesi Barat | 26.57 | 27.82 |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua | 9400 | 2007 | Papua Barat | 32.60 | 32.44 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Riau | 1400 | 2007 | Kepulauan Riau | 37.58 | 34.68 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Kalimantan Timur | 6400 | 2015 | Kalimantan Utara | 9.04 | 4.89 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Sulawesi Selatan | 7300 | 2007 | Sulawesi Barat | 50.04 | 52.67 |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua | 9400 | 2007 | Papua Barat | 63.34 | 65.08 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (337)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | DKI Jakarta | 2001 | 28.71 | ke bawah + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Jawa Barat | 2001 | 7.83 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Banten | 2001 | 14.53 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Bali | 2001 | 22.43 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Sulawesi Selatan | 2001 | 18.92 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Kepulauan Bangka Belitung | 2007 | 24.36 | perubahan | patahan_seri | tandai; cari catatan metode |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | DKI Jakarta | 2007 | 34.20 | ke bawah + ke samping | patahan_seri | tandai; cari catatan metode |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Jawa Barat | 2007 | 11.56 | ke samping | patahan_seri | tandai; cari catatan metode |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Banten | 2007 | 16.52 | ke samping | patahan_seri | tandai; cari catatan metode |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | DKI Jakarta | 2008 | 75.86 | ke bawah + perubahan | patahan_seri | tandai; cari catatan metode |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Jawa Barat | 2008 | 25.04 | perubahan + ke samping | patahan_seri | tandai; cari catatan metode |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Banten | 2008 | 38.88 | ke bawah + perubahan | patahan_seri | tandai; cari catatan metode |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Sumatera Selatan | 2009 | 39.90 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | DKI Jakarta | 2009 | 83.75 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Jawa Barat | 2009 | 66.69 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Jawa Tengah | 2009 | 35.39 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | DI Yogyakarta | 2009 | 43.06 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Jawa Timur | 2009 | 32.94 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Banten | 2009 | 62.00 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Kepulauan Riau | 2010 | 33.32 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Kalimantan Timur | 2010 | 52.81 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Kepulauan Riau | 2011 | 53.44 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Nusa Tenggara Timur | 2016 | 0.57 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Kalimantan Tengah | 2016 | 51.07 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Sulawesi Tengah | 2016 | 29.45 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku | 2016 | 0.65 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku Utara | 2016 | 0.65 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua Barat | 2016 | 1.59 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua | 2016 | 0.80 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Nusa Tenggara Timur | 2017 | 0.52 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Kalimantan Tengah | 2017 | 69.27 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Sulawesi Tengah | 2017 | 47.88 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku | 2017 | 0.44 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku Utara | 2017 | 0.89 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua Barat | 2017 | 3.42 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua | 2017 | 0.88 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Nusa Tenggara Timur | 2018 | 1.04 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku | 2018 | 0.75 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku Utara | 2018 | 1.70 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua Barat | 2018 | 4.50 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua | 2018 | 1.13 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Nusa Tenggara Timur | 2019 | 1.20 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Sulawesi Tengah | 2019 | 49.57 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku | 2019 | 0.89 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku Utara | 2019 | 1.23 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua Barat | 2019 | 4.31 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua | 2019 | 1.39 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Nusa Tenggara Timur | 2020 | 1.01 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Sulawesi Tengah | 2020 | 59.55 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku | 2020 | 0.80 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku Utara | 2020 | 0.97 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua Barat | 2020 | 4.35 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua | 2020 | 1.73 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Nusa Tenggara Barat | 2021 | 79.53 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Nusa Tenggara Timur | 2021 | 1.41 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Sulawesi Tengah | 2021 | 68.97 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku | 2021 | 1.76 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Maluku Utara | 2021 | 1.48 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua Barat | 2021 | 5.21 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=gas_elpiji] | Papua | 2021 | 1.92 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | DKI Jakarta | 2001 | 0.28 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Timur | 2001 | 81.51 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Kepulauan Riau | 2007 | 12.29 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | DKI Jakarta | 2007 | 0.27 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Kalimantan Timur | 2007 | 24.10 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Riau | 2008 | 24.53 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Kepulauan Riau | 2008 | 20.83 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | DKI Jakarta | 2008 | 0.68 | ke bawah + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | DKI Jakarta | 2009 | 0.52 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Jawa Tengah | 2009 | 51.31 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Kepulauan Riau | 2010 | 8.91 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | DKI Jakarta | 2010 | 0.30 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Sulawesi Barat | 2010 | 73.71 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Maluku | 2010 | 55.51 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua Barat | 2010 | 42.85 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | DKI Jakarta | 2011 | 0.16 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Kalimantan Barat | 2012 | 39.30 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Sulawesi Barat | 2012 | 61.15 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Timur | 2014 | 79.60 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Gorontalo | 2014 | 43.96 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Timur | 2015 | 78.17 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Kalimantan Utara | 2015 | 20.57 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua | 2015 | 67.74 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Timur | 2016 | 77.58 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua | 2016 | 67.04 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Timur | 2017 | 75.25 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Sulawesi Tengah | 2017 | 37.68 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Maluku Utara | 2017 | 53.85 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua | 2017 | 63.49 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Timur | 2018 | 74.81 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Maluku Utara | 2018 | 49.87 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua | 2018 | 64.37 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Timur | 2019 | 70.94 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Kalimantan Utara | 2019 | 13.21 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Sulawesi Tengah | 2019 | 42.04 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Maluku Utara | 2019 | 48.63 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua | 2019 | 62.76 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Barat | 2020 | 26.65 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Timur | 2020 | 70.83 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Sulawesi Tengah | 2020 | 33.36 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Maluku Utara | 2020 | 46.47 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua | 2020 | 63.15 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Barat | 2021 | 11.02 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Nusa Tenggara Timur | 2021 | 69.28 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Kalimantan Utara | 2021 | 13.14 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Sulawesi Tengah | 2021 | 23.79 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Maluku | 2021 | 30.20 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Maluku Utara | 2021 | 45.03 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua Barat | 2021 | 27.34 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=kayu] | Papua | 2021 | 64.67 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sumatera Selatan | 2001 | 35.79 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Lampung | 2001 | 21.34 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | DKI Jakarta | 2001 | 60.92 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Barat | 2001 | 61.12 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Tengah | 2001 | 35.04 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | DI Yogyakarta | 2001 | 31.27 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Timur | 2001 | 43.18 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Banten | 2001 | 57.49 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Bali | 2001 | 27.67 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sumatera Selatan | 2007 | 35.14 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kepulauan Riau | 2007 | 70.02 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | DKI Jakarta | 2007 | 57.90 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Barat | 2007 | 48.74 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Tengah | 2007 | 26.25 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | DI Yogyakarta | 2007 | 23.25 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Timur | 2007 | 34.08 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Banten | 2007 | 45.46 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Bali | 2007 | 23.68 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sumatera Selatan | 2008 | 31.87 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kepulauan Riau | 2008 | 63.98 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | DKI Jakarta | 2008 | 16.70 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Barat | 2008 | 38.99 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Tengah | 2008 | 24.14 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | DI Yogyakarta | 2008 | 15.70 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Timur | 2008 | 27.23 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Banten | 2008 | 26.67 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Bali | 2008 | 22.23 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sumatera Selatan | 2009 | 13.64 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Barat | 2009 | 2.83 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Jawa Tengah | 2009 | 11.25 | ke samping | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Banten | 2009 | 4.05 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sumatera Utara | 2010 | 27.42 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Timur | 2010 | 24.62 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Riau | 2011 | 33.29 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Bengkulu | 2011 | 10.05 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kepulauan Riau | 2011 | 33.29 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Riau | 2012 | 16.27 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Utara | 2012 | 26.73 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Gorontalo | 2012 | 15.00 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Utara | 2013 | 18.47 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Tenggara | 2013 | 32.27 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku | 2013 | 44.65 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sumatera Barat | 2015 | 16.08 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kepulauan Bangka Belitung | 2015 | 16.89 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Selatan | 2015 | 18.58 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Timur | 2015 | 1.73 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku | 2015 | 51.62 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku Utara | 2015 | 39.02 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua Barat | 2015 | 59.80 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sumatera Barat | 2016 | 8.01 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Tengah | 2016 | 23.02 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Selatan | 2016 | 12.31 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Tengah | 2016 | 14.33 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku | 2016 | 55.07 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua Barat | 2016 | 58.05 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kepulauan Riau | 2017 | 16.15 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Nusa Tenggara Barat | 2017 | 18.45 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Nusa Tenggara Timur | 2017 | 23.51 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Tengah | 2017 | 12.68 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Selatan | 2017 | 7.55 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Utara | 2017 | 17.69 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Tengah | 2017 | 10.92 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Tenggara | 2017 | 19.17 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku | 2017 | 61.55 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku Utara | 2017 | 44.12 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua Barat | 2017 | 63.66 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua | 2017 | 34.44 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Nusa Tenggara Barat | 2018 | 15.68 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Tengah | 2018 | 7.13 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Utara | 2018 | 13.30 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Tenggara | 2018 | 16.59 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku | 2018 | 62.41 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku Utara | 2018 | 46.36 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua Barat | 2018 | 66.94 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kepulauan Bangka Belitung | 2019 | 11.04 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kepulauan Riau | 2019 | 13.17 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Nusa Tenggara Barat | 2019 | 18.97 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Nusa Tenggara Timur | 2019 | 26.98 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kalimantan Utara | 2019 | 6.41 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Tengah | 2019 | 6.42 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Tenggara | 2019 | 19.38 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku | 2019 | 65.82 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku Utara | 2019 | 47.50 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua Barat | 2019 | 69.59 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua | 2019 | 34.35 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kepulauan Bangka Belitung | 2020 | 3.59 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Kepulauan Riau | 2020 | 8.42 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Nusa Tenggara Barat | 2020 | 9.20 | perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Nusa Tenggara Timur | 2020 | 27.08 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Sulawesi Tenggara | 2020 | 19.37 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku | 2020 | 65.84 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku Utara | 2020 | 50.34 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua Barat | 2020 | 70.47 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua | 2020 | 33.90 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Nusa Tenggara Timur | 2021 | 28.40 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku | 2021 | 66.56 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Maluku Utara | 2021 | 51.58 | ke bawah | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua Barat | 2021 | 65.88 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| tabel:sdg7_bahan_bakar [bahan_bakar=minyak_tanah] | Papua | 2021 | 32.47 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Aceh | 1993 | 36.48 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Sumatera Utara | 1993 | 50.55 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | DKI Jakarta | 1993 | 97.14 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Barat | 1993 | 61.56 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Tengah | 1993 | 54.96 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | DI Yogyakarta | 1993 | 68.21 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Timur | 1993 | 51.75 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Bali | 1993 | 76.49 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Barat | 1993 | 28.54 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Timur | 1993 | 53.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Utara | 1993 | 62.70 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Aceh | 1994 | 39.23 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Sumatera Utara | 1994 | 57.47 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Barat | 1994 | 68.67 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Tengah | 1994 | 61.64 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | DI Yogyakarta | 1994 | 75.86 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Timur | 1994 | 60.04 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Bali | 1994 | 79.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Timur | 1994 | 62.39 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Utara | 1994 | 64.67 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Aceh | 1995 | 45.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Sumatera Utara | 1995 | 59.08 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Barat | 1995 | 74.37 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Tengah | 1995 | 70.97 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | DI Yogyakarta | 1995 | 81.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Timur | 1995 | 66.69 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Bali | 1995 | 86.13 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Utara | 1995 | 70.23 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Aceh | 1996 | 50.52 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Barat | 1996 | 79.68 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Tengah | 1996 | 78.17 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | DI Yogyakarta | 1996 | 85.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Timur | 1996 | 74.32 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Utara | 1996 | 71.94 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | DKI Jakarta | 1997 | 98.47 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Tengah | 1997 | 83.59 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | DI Yogyakarta | 1997 | 90.48 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Jawa Timur | 1997 | 79.04 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Barat | 1997 | 56.89 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Tenggara | 1998 | 49.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 1998 | 34.56 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Lampung | 2000 | 43.06 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Timur | 2000 | 76.47 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Selatan | 2000 | 77.02 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Utara | 2001 | 92.50 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var87 | Gorontalo | 2002 | 60.42 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Maluku | 2002 | 100.00 | perubahan | cakupan_parsial | tandai; jangan bandingkan dengan periode lain |
| var87 | Maluku Utara | 2002 | 91.65 | perubahan | cakupan_parsial | tandai; jangan bandingkan dengan periode lain |
| var87 | Papua | 2002 | 100.00 | perubahan + ke samping | cakupan_parsial | tandai; jangan bandingkan dengan periode lain |
| var87 | Aceh | 2003 | 84.31 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | DKI Jakarta | 2003 | 96.27 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Maluku | 2003 | 63.79 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Maluku Utara | 2003 | 49.26 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2003 | 37.89 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Aceh | 2006 | 81.57 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Lampung | 2006 | 64.10 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Gorontalo | 2006 | 64.54 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2006 | 36.55 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var87 | Riau | 2008 | 67.44 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kepulauan Riau | 2008 | 68.65 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2008 | 37.36 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Barat | 2008 | 55.14 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2008 | 37.07 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Sumatera Selatan | 2009 | 76.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Bengkulu | 2009 | 77.07 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kepulauan Riau | 2009 | 57.69 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Maluku Utara | 2009 | 57.99 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua Barat | 2009 | 57.67 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Riau | 2010 | 56.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kepulauan Riau | 2010 | 86.14 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Barat | 2010 | 81.52 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Barat | 2010 | 45.97 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua Barat | 2010 | 66.11 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2010 | 32.83 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2011 | 31.79 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2012 | 32.33 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2013 | 59.45 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2013 | 35.68 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2014 | 35.90 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua Barat | 2015 | 75.95 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2015 | 39.16 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Barat | 2016 | 75.58 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2016 | 39.79 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2017 | 66.02 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Tengah | 2017 | 81.75 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Utara | 2017 | 91.54 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Maluku Utara | 2017 | 84.33 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2017 | 41.61 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2018 | 69.37 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Barat | 2018 | 83.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2018 | 43.51 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2019 | 70.07 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2019 | 44.49 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2020 | 74.05 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2020 | 43.14 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Kepulauan Riau | 2021 | 98.46 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2021 | 81.12 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Tengah | 2021 | 83.52 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Utara | 2021 | 91.63 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Barat | 2021 | 91.75 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua Barat | 2021 | 81.08 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2021 | 43.92 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2022 | 85.58 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Tengah | 2022 | 85.36 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua Barat | 2022 | 83.49 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2022 | 43.04 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2023 | 87.81 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Tengah | 2023 | 87.81 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Utara | 2023 | 95.72 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Sulawesi Barat | 2023 | 94.67 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua Barat | 2023 | 83.20 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2023 | 47.07 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Nusa Tenggara Timur | 2024 | 91.01 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Kalimantan Barat | 2024 | 92.95 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Maluku | 2024 | 95.37 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Maluku Utara | 2024 | 94.27 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua Barat | 2024 | 82.31 | ke bawah | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var87 | Papua | 2024 | 90.24 | perubahan + ke samping | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var87 | Papua Selatan | 2024 | 67.05 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var87 | Papua Tengah | 2024 | 35.27 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var87 | Papua Pegunungan | 2024 | 14.53 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var87 | Kalimantan Tengah | 2025 | 90.69 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua Barat | 2025 | 84.16 | ke bawah | outlier | tandai, nilai tidak diubah |
| var87 | Papua Barat Daya | 2025 | 94.09 | perubahan | outlier | tandai, nilai tidak diubah |
| var87 | Papua | 2025 | 91.78 | ke samping | outlier | tandai, nilai tidak diubah |
| var87 | Papua Selatan | 2025 | 73.62 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var87 | Papua Tengah | 2025 | 35.67 | ke bawah | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |
| var87 | Papua Pegunungan | 2025 | 20.78 | ke bawah + perubahan | perbedaan_struktural | tandai sekali per provinsi; bukan kejadian satu tahun |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var87 | 1036 | 1036 | 1036 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
