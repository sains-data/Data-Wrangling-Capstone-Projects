# Kategori anomali dan duplikat

Dihasilkan `python pipeline.py` (`src/silver/anomali.py`). Nilai di Silver tidak diubah kecuali galat input yang koreksinya jelas.

## Galat input (semua baris Silver diperiksa terhadap rentang satuan): 0

Tidak ada nilai di luar rentang satuannya.

## Uji patahan seri

| seri_kode | pergantian | provinsi | porsi_naik | porsi_turun | patahan | keterangan |
|---|---|---|---|---|---|---|
| var543 | 1986→1987 | 26 | 0.12 | 0.35 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1987→1988 | 26 | 0.46 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1988→1989 | 26 | 0.27 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1989→1990 | 26 | 0.12 | 0.27 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1990→1991 | 26 | 0.31 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1991→1992 | 26 | 0.35 | 0.04 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1992→1993 | 26 | 0.04 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1993→1994 | 26 | 1.00 | 0.00 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1994→1996 | 26 | 0.31 | 0.04 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1996→1997 | 26 | 0.04 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1997→1998 | 26 | 0.31 | 0.19 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1998→1999 | 26 | 0.54 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 1999→2000 | 25 | 0.12 | 0.20 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2000→2001 | 25 | 0.72 | 0.04 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2001→2002 | 30 | 0.33 | 0.07 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2002→2003 | 30 | 0.17 | 0.13 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2003→2004 | 30 | 0.20 | 0.07 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2004→2005-02 | 30 | 0.17 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2005-02→2005-08 | 30 | 0.37 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2005-08→2006-02 | 30 | 0.03 | 0.23 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2006-02→2006-08 | 33 | 0.18 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2006-08→2007-02 | 33 | 0.03 | 0.15 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2007-02→2007-08 | 33 | 0.03 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2007-08→2008-02 | 33 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2008-02→2008-08 | 33 | 0.03 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2008-08→2009-02 | 33 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2009-02→2009-08 | 33 | 0.06 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2009-08→2010-02 | 33 | 0.00 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2010-02→2010-08 | 33 | 0.09 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2010-08→2011-02 | 33 | 0.00 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2011-02→2011-08 | 33 | 0.18 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2011-08→2012-02 | 33 | 0.00 | 0.48 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2012-02→2012-08 | 33 | 0.15 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2012-08→2013-02 | 33 | 0.00 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2013-02→2013-08 | 33 | 0.30 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2013-08→2014-02 | 33 | 0.03 | 0.42 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2014-02→2014-08 | 33 | 0.52 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2014-08→2015-02 | 33 | 0.09 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2015-02→2015-08 | 34 | 0.44 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2015-08→2016-02 | 34 | 0.03 | 0.38 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2016-02→2016-08 | 34 | 0.18 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2016-08→2017-02 | 34 | 0.09 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2017-02→2017-08 | 34 | 0.15 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2017-08→2018-02 | 34 | 0.00 | 0.24 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2018-02→2018-08 | 34 | 0.12 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2018-08→2019-02 | 34 | 0.00 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2019-02→2019-08 | 34 | 0.18 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2019-08→2020-02 | 34 | 0.06 | 0.09 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2020-02→2020-08 | 34 | 0.82 | 0.00 | ya | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2020-08→2021-02 | 34 | 0.00 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2021-02→2021-08 | 34 | 0.00 | 0.03 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2021-08→2022-02 | 34 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2022-02→2022-08 | 34 | 0.00 | 0.18 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2022-08→2023-02 | 34 | 0.09 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2023-02→2023-08 | 34 | 0.00 | 0.12 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2023-08→2024-02 | 34 | 0.06 | 0.06 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2024-02→2024-08 | 38 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2024-08→2025-02 | 38 | 0.08 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2025-02→2025-08 | 38 | 0.00 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |
| var543 | 2025-08→2026-02 | 38 | 0.03 | 0.00 | tidak | ambang lompat 20%, porsi serentak ≥ 70% |

## Pergantian definisi yang dinyatakan penerbit

Tidak ada.

## Cakupan parsial yang dinyatakan penerbit

Tidak ada.

## Perubahan batas wilayah di tengah panel: 10

| seri_kode | induk | wilayah_kode | periode | anak | nilai_sebelum | nilai_sesudah |
|---|---|---|---|---|---|---|
| var543 | Riau | 1400 | 2006-02 | Kepulauan Riau | 12.16 | 11.46 |
| var543 | Sumatera Selatan | 1600 | 2001 | Kepulauan Bangka Belitung | 5.73 | 6.32 |
| var543 | Jawa Barat | 3200 | 2001 | Banten | 8.99 | 11.77 |
| var543 | Kalimantan Timur | 6400 | 2015-02 | Kalimantan Utara | 7.38 | 7.17 |
| var543 | Sulawesi Utara | 7100 | 2001 | Gorontalo | 8.66 | 10.21 |
| var543 | Sulawesi Selatan | 7300 | 2006-02 | Sulawesi Barat | 15.93 | 12.32 |
| var543 | Maluku | 8100 | 2001 | Maluku Utara | 4.70 | 11.28 |
| var543 | Papua Barat | 9100 | 2024-02 | Papua Barat Daya | 5.38 | 4.31 |
| var543 | Papua | 9400 | 2006-02 | Papua Barat | 7.31 | 4.50 |
| var543 | Papua | 9400 | 2024-02 | Papua Selatan, Papua Tengah, Papua Pegunungan | 2.67 | 5.81 |

Nilai induk sebelum periode ini mencakup wilayah provinsi pemekaran; sesudahnya tidak. Perubahannya bukan tren dan tidak diratakan.

## Calon anomali dan kategorinya (179)

| seri_kode | nama_wilayah | periode | nilai | arah | kategori | tindakan |
|---|---|---|---|---|---|---|
| var543 | DKI Jakarta | 1986 | 10.35 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Timur | 1986 | 0.99 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Timur | 1986 | 4.80 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Barat | 1987 | 1.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1987 | 9.66 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Timur | 1987 | 0.80 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Tengah | 1987 | 0.63 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tengah | 1987 | 2.32 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 1987 | 4.09 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Jambi | 1988 | 2.57 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Lampung | 1988 | 1.03 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1988 | 10.01 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Timur | 1988 | 0.85 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 1988 | 2.94 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Lampung | 1989 | 1.24 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1989 | 8.47 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Timur | 1989 | 0.88 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Timur | 1989 | 3.11 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Lampung | 1990 | 0.86 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1990 | 7.30 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Timur | 1990 | 0.65 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Utara | 1990 | 3.27 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Lampung | 1991 | 0.89 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1991 | 6.35 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Timur | 1991 | 0.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Tengah | 1991 | 0.88 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Lampung | 1992 | 1.21 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1992 | 6.35 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Aceh | 1993 | 4.01 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1993 | 5.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1994 | 9.10 | ke bawah + perubahan | patahan_seri | tandai; cari catatan metode |
| var543 | Kalimantan Tengah | 1996 | 3.00 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1997 | 10.94 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Utara | 1997 | 8.02 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1998 | 12.32 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Utara | 1998 | 5.48 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 1999 | 15.01 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 2000 | 12.08 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 2001 | 15.07 | ke bawah | patahan_seri | tandai; cari catatan metode |
| var543 | Kalimantan Timur | 2001 | 6.81 | perubahan | patahan_seri | tandai; cari catatan metode |
| var543 | Sulawesi Tengah | 2001 | 8.25 | ke samping | patahan_seri | tandai; cari catatan metode |
| var543 | Sulawesi Tenggara | 2001 | 7.51 | ke samping | patahan_seri | tandai; cari catatan metode |
| var543 | Kalimantan Barat | 2002 | 8.57 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Timur | 2002 | 11.76 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tengah | 2002 | 8.06 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tenggara | 2002 | 8.33 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Gorontalo | 2002 | 13.17 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2002 | 8.08 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku Utara | 2002 | 15.25 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Bengkulu | 2003 | 7.48 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Lampung | 2003 | 9.14 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Jawa Timur | 2003 | 8.79 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Tengah | 2003 | 7.59 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tengah | 2003 | 4.64 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Selatan | 2003 | 17.32 | ke bawah + perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tenggara | 2003 | 10.30 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Gorontalo | 2003 | 10.17 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2003 | 12.63 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku Utara | 2003 | 7.50 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Barat | 2004 | 12.74 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Riau | 2004 | 15.25 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Selatan | 2004 | 15.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tenggara | 2004 | 9.35 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Gorontalo | 2004 | 12.29 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Papua | 2004 | 8.00 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Barat | 2005-02 | 11.50 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Riau | 2005-02 | 13.91 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Jambi | 2005-02 | 8.59 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Jawa Timur | 2005-02 | 8.45 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Timur | 2005-02 | 5.46 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Barat | 2005-02 | 8.61 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Selatan | 2005-02 | 13.58 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tenggara | 2005-02 | 8.92 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Barat | 2005-08 | 13.34 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Jambi | 2005-08 | 10.74 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Selatan | 2005-08 | 12.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Bengkulu | 2005-08 | 8.91 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Jawa Timur | 2005-08 | 8.51 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Barat | 2005-08 | 10.29 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Selatan | 2005-08 | 15.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tenggara | 2005-08 | 10.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Gorontalo | 2005-08 | 14.04 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Maluku Utara | 2005-08 | 13.09 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Utara | 2006-02 | 14.82 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Barat | 2006-02 | 12.93 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Jambi | 2006-02 | 7.77 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Selatan | 2006-02 | 12.10 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Lampung | 2006-02 | 9.76 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tengah | 2006-02 | 8.90 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tenggara | 2006-02 | 7.42 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Papua Barat | 2006-02 | 11.17 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Barat | 2006-08 | 11.87 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Lampung | 2006-08 | 9.13 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2006-08 | 12.24 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Jawa Timur | 2006-08 | 8.19 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Banten | 2006-08 | 18.91 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Barat | 2006-08 | 8.53 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Tengah | 2006-08 | 6.68 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tengah | 2006-08 | 10.31 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tenggara | 2006-08 | 9.67 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Barat | 2006-08 | 6.45 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sumatera Barat | 2007-02 | 11.02 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Jawa Barat | 2007-08 | 13.08 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Selatan | 2007-08 | 7.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tengah | 2007-08 | 8.39 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Barat | 2007-08 | 5.45 | perubahan + ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2007-08 | 12.20 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku Utara | 2007-08 | 6.05 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Bali | 2008-02 | 4.56 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Barat | 2008-02 | 5.68 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Maluku Utara | 2008-02 | 7.03 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Banten | 2008-08 | 15.18 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Riau | 2009-02 | 8.96 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Lampung | 2009-02 | 6.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Bangka Belitung | 2009-02 | 4.82 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Banten | 2009-02 | 14.90 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Barat | 2009-02 | 4.92 | ke samping | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Bangka Belitung | 2009-08 | 6.14 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Banten | 2009-08 | 14.97 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Timur | 2009-08 | 3.97 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Bangka Belitung | 2010-02 | 4.24 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Banten | 2010-02 | 14.13 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Riau | 2010-08 | 8.72 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Bangka Belitung | 2010-08 | 5.63 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Jambi | 2011-02 | 3.98 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Bangka Belitung | 2011-02 | 3.31 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Banten | 2011-02 | 13.62 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Selatan | 2011-02 | 6.89 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2011-02 | 8.18 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Riau | 2011-08 | 6.09 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2011-08 | 5.38 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Banten | 2011-08 | 13.74 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tengah | 2011-08 | 6.78 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2011-08 | 10.81 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Banten | 2012-02 | 10.68 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Tengah | 2012-02 | 3.75 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2012-02 | 7.59 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Bengkulu | 2012-08 | 3.62 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2013-02 | 6.05 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2013-08 | 9.91 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Aceh | 2014-02 | 6.75 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2014-02 | 6.59 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2014-08 | 10.51 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Jambi | 2015-02 | 2.73 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2015-02 | 9.05 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2015-02 | 6.72 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2015-08 | 6.20 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2016-02 | 9.03 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Bangka Belitung | 2016-08 | 2.60 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Bangka Belitung | 2017-02 | 4.46 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Selatan | 2017-02 | 3.53 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Maluku | 2018-02 | 7.07 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Barat | 2019-02 | 1.29 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Timur | 2019-08 | 5.94 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Utara | 2019-08 | 4.49 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Barat | 2019-08 | 2.98 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kalimantan Utara | 2020-02 | 5.71 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Selatan | 2020-02 | 5.70 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2020-08 | 10.34 | ke bawah + perubahan | patahan_seri | tandai; cari catatan metode |
| var543 | DKI Jakarta | 2020-08 | 10.95 | ke bawah + perubahan | patahan_seri | tandai; cari catatan metode |
| var543 | Jawa Barat | 2020-08 | 10.46 | ke bawah | patahan_seri | tandai; cari catatan metode |
| var543 | Banten | 2020-08 | 10.64 | ke bawah | patahan_seri | tandai; cari catatan metode |
| var543 | Bali | 2020-08 | 5.63 | perubahan | patahan_seri | tandai; cari catatan metode |
| var543 | Riau | 2021-02 | 4.96 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2021-02 | 10.12 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | DKI Jakarta | 2021-02 | 8.51 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Jawa Barat | 2021-02 | 8.92 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Banten | 2021-02 | 9.01 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2021-08 | 9.91 | ke bawah | outlier | tandai, nilai tidak diubah |
| var543 | Jawa Barat | 2021-08 | 9.82 | ke bawah + perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Barat | 2021-08 | 3.01 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Kepulauan Riau | 2022-02 | 8.02 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Jawa Barat | 2022-02 | 8.35 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Nusa Tenggara Barat | 2022-02 | 3.92 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Papua | 2024-02 | 5.81 | perubahan | patahan_wilayah | tandai; jangan bandingkan induk sebelum dan sesudah pemekaran |
| var543 | Sulawesi Selatan | 2025-08 | 4.21 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Papua Selatan | 2025-08 | 4.04 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Sulawesi Selatan | 2026-02 | 4.95 | perubahan | outlier | tandai, nilai tidak diubah |
| var543 | Papua Selatan | 2026-02 | 5.25 | perubahan | outlier | tandai, nilai tidak diubah |

Outlier di sini adalah outlier statistik. Menyebutnya *outlier asli* butuh penjelasan dunia nyata (kebijakan, bencana, cakupan survei); kolom itu diisi tim saat Sprint 2 bila buktinya ditemukan.

## Duplikat dua format BPS (CSV vs JSON)

| seri | baris_json | baris_csv | pasangan_sama | hanya_json | hanya_csv | nilai_berbeda | satuan_csv |
|---|---|---|---|---|---|---|---|
| var543 | 2000 | 2000 | 2000 | 0 | 0 | 0 | Persen |

## Kunci Silver kembar: 0
