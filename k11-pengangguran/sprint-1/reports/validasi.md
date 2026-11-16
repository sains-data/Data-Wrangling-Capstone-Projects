# Hasil validasi Silver

Dihasilkan `python pipeline.py` (`src/validasi/`). Aturan keras menghentikan pipeline bila gagal; peringatan dilaporkan untuk diperiksa manusia. Aturan juga diuji dengan baris yang sengaja dirusak (`pytest`, berkas `tests/test_validasi.py`).

| aturan | jenis | keterangan | hasil |
|---|---|---|---|
| kolom dan tipe | keras (umum) | setiap kolom ada dengan tipe yang benar; nilai tidak kosong | LOLOS |
| rincian_dari_kamus | keras (umum) | rincian 'total' atau 'dimensi=kode' dengan dimensi/kode dari kamus konfigurasi | LOLOS |
| satu_satuan_per_seri | keras (umum) | satu seri hanya punya satu satuan | LOLOS |
| nilai_dalam_rentang_satuan | keras (umum) | nilai berada di rentang sah satuannya (persen 0–100, per 1.000 0–1.000, ...) | LOLOS |
| batas_bawah_le_nilai_le_batas_atas | keras (umum) | untuk baris yang punya batas: batas bawah ≤ nilai ≤ batas atas | LOLOS |
| kunci unik | keras (umum) | kombinasi sumber + seri_kode + wilayah_kode + periode + rincian + _berkas_raw tidak kembar | LOLOS |
| wilayah dan periode | keras (umum) | wilayah_kode dari kamus 38 provinsi + 9999; periode berbentuk baku | LOLOS |
| jenis_periode_sesuai_bentuk | keras (kasus) | jenis_periode sesuai bentuk periode (termasuk triwulan ILO) | LOLOS |
| bps_hanya_feb_agu_atau_tahun | keras (kasus) | bulan BPS hanya 02/08; tidak ada tahun buatan sesudah 2004 | LOLOS |
| status_ilo_terdaftar | keras (kasus) | status_obs ILO terdaftar (B, U) atau kosong | LOLOS |
| bps_agustus_dekat_ilo | peringatan (kasus) | TPT BPS Agustus vs ILO > 1 poin (peringatan: definisi) | PERINGATAN (18 baris) |

## Kegagalan aturan umum

Tidak ada.

## Baris yang memicu aturan kasus

### bps_agustus_dekat_ilo

| periode | bps_agustus | ilo | selisih |
|---|---|---|---|
| 2005 | 11.24 | 7.95 | 3.30 |
| 2006 | 10.28 | 7.55 | 2.73 |
| 2007 | 9.11 | 8.06 | 1.05 |
| 2008 | 8.39 | 7.21 | 1.18 |
| 2009 | 7.87 | 6.11 | 1.76 |
| 2010 | 7.14 | 5.61 | 1.53 |
| 2011 | 7.48 | 5.15 | 2.33 |
| 2012 | 6.13 | 4.47 | 1.66 |
| 2013 | 6.17 | 4.34 | 1.83 |
| 2014 | 5.94 | 4.05 | 1.89 |
| 2015 | 6.18 | 4.51 | 1.67 |
| 2016 | 5.61 | 4.30 | 1.31 |
| 2017 | 5.50 | 3.78 | 1.72 |
| 2019 | 5.23 | 3.59 | 1.64 |
| 2020 | 7.07 | 4.25 | 2.82 |
| 2021 | 6.49 | 3.83 | 2.66 |
| 2022 | 5.86 | 3.46 | 2.40 |
| 2023 | 5.32 | 3.42 | 1.90 |
