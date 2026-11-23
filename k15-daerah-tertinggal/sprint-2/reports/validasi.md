# Hasil validasi Silver dan Gold

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
| jumlah_desa_sama_rincian | keras (kasus) | desa: jumlah = sangat tertinggal + tertinggal | LOLOS |
| jumlah_desa_bilangan_bulat | keras (kasus) | jumlah desa bilangan bulat >= 0 | LOLOS |
| semester_hanya_untuk_s1_s2 | keras (kasus) | jenis_periode semester hanya AAAA-S1/S2, tahun hanya AAAA | LOLOS |
| kota_tidak_lebih_miskin | peringatan (kasus) | P0 perkotaan > perdesaan (peringatan) | PERINGATAN (106 baris) |
| gold: kunci panel unik | keras (Gold) | indikator + wilayah_kode + periode tidak kembar | LOLOS |
| gold: satu satuan per indikator | keras (Gold) | satu indikator panel hanya punya satu satuan | LOLOS |
| gold: status sel dan nilai | keras (Gold) | status sel baku; nilai ada jika dan hanya jika sel terisi | LOLOS |
| gold: sel tertelusur ke Silver | keras (Gold) | setiap sel terisi punya baris Silver asal (seri, wilayah, periode, berkas) | LOLOS |
| gold: nilai sama dengan Silver | keras (Gold) | nilai panel = nilai Silver asalnya (tidak ada nilai yang diubah di Gold) | LOLOS |
| gold: tabel nasional unik | keras (Gold) | seri + rincian + periode tidak kembar | LOLOS |
| rekonsiliasi: kategori baku | keras (Gold) | kategori dari daftar baku; penjelasan tidak kosong | LOLOS |
| rekonsiliasi: selisih = utama − pembanding | keras (Gold) | selisih dihitung ulang dan cocok | LOLOS |
| rekonsiliasi: baris berpasangan dihitung | keras (Gold) | pasangan selisih dengan dua nilai punya selisih, atau catatan mengapa tidak | LOLOS |
| rekonsiliasi: periode utama tidak dibuang | keras (Gold) | setiap tahun seri utama di tabel nasional muncul di rekonsiliasi | LOLOS |

## Kegagalan aturan umum

Tidak ada.

## Baris yang memicu aturan kasus dan Gold

### kota_tidak_lebih_miskin

| wilayah_kode | periode | daerah=RURAL | daerah=URBAN | total |
|---|---|---|---|---|
| 1200 | 2007 | 13.63 | 14.21 | 13.90 |
| 1200 | 2008 | 12.29 | 12.85 | 12.55 |
| 1200 | 2010 | 11.29 | 11.34 | 11.31 |
| 1200 | 2013-S2 | 10.33 | 10.45 | 10.39 |
| 1200 | 2020-S2 | 9.02 | 9.25 | 9.14 |
| 1200 | 2021-S1 | 8.84 | 9.15 | 9.01 |
| 1200 | 2021-S2 | 8.26 | 8.68 | 8.49 |
| 1200 | 2022-S1 | 7.98 | 8.76 | 8.42 |
| 1200 | 2022-S2 | 7.96 | 8.63 | 8.33 |
| 1200 | 2023-S1 | 8.03 | 8.23 | 8.15 |
| 1400 | 2023-S1 | 6.65 | 6.73 | 6.68 |
| 1400 | 2024-S1 | 6.61 | 6.76 | 6.67 |
| 1500 | 2007 | 7.81 | 15.42 | 10.27 |
| 1500 | 2008 | 7.43 | 13.28 | 9.32 |
| 1500 | 2009 | 6.88 | 12.71 | 8.77 |
| 1500 | 2010 | 6.67 | 11.80 | 8.34 |
| 1500 | 2011 | 7.53 | 11.19 | 8.65 |
| 1500 | 2012-S1 | 7.52 | 10.44 | 8.42 |
| 1500 | 2012-S2 | 7.29 | 10.53 | 8.28 |
| 1500 | 2013-S1 | 7.27 | 9.89 | 8.07 |
| 1500 | 2013-S2 | 7.54 | 10.41 | 8.42 |
| 1500 | 2014-S1 | 7.07 | 9.85 | 7.92 |
| 1500 | 2014-S2 | 7.39 | 10.67 | 8.39 |
| 1500 | 2015-S1 | 7.67 | 11.60 | 8.86 |
| 1500 | 2015-S2 | 7.82 | 12.11 | 9.12 |
| 1500 | 2016-S1 | 7.32 | 10.86 | 8.41 |
| 1500 | 2016-S2 | 7.30 | 10.73 | 8.37 |
| 1500 | 2017-S1 | 6.92 | 10.94 | 8.19 |
| 1500 | 2017-S2 | 6.66 | 10.53 | 7.90 |
| 1500 | 2018-S1 | 6.75 | 10.41 | 7.92 |
