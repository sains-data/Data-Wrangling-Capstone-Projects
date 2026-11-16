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
| bps_hanya_tahun_terbit | keras (kasus) | tidak ada tahun BPS di luar tahun terbit (tidak ada interpolasi) | LOLOS |
| tahun_depan_terdaftar_proyeksi | keras (kasus) | baris dengan tahun > 2026 terdaftar di PROYEKSI | LOLOS |
| satuan_malaria_dibedakan | keras (kasus) | malaria BPS per 1.000 penduduk, WHO/WDI per 1.000 penduduk berisiko | LOLOS |
| lonjakan_malaria | peringatan (kasus) | kejadian malaria provinsi berubah > 10 kali lipat antartahun (peringatan: galat atau nyata?) | PERINGATAN (33 baris) |

## Kegagalan aturan umum

Tidak ada.

## Baris yang memicu aturan kasus

### lonjakan_malaria

| nama_wilayah | dari | ke | nilai_dari | nilai_ke | rasio |
|---|---|---|---|---|---|
| Jawa Barat | 2010 | 2011 | 0.430 | 0.012 | 0.03 |
| Jawa Tengah | 2010 | 2011 | 0.100 | 0.006 | 0.06 |
| Jawa Timur | 2010 | 2011 | 0.100 | 0.001 | 0.01 |
| Bali | 2010 | 2011 | 0.030 | 0.002 | 0.07 |
| DI Yogyakarta | 2011 | 2012 | 0.004 | 0.059 | 14.75 |
| Jawa Timur | 2011 | 2012 | 0.001 | 0.025 | 25.00 |
| Bali | 2011 | 2012 | 0.002 | 0.000 | 0.00 |
| Jawa Barat | 2012 | 2013 | 0.015 | 0.000 | 0.00 |
| Jawa Timur | 2012 | 2013 | 0.025 | 0.000 | 0.00 |
| Jawa Barat | 2013 | 2014 | 0.000 | 0.010 | inf |
| Jawa Timur | 2013 | 2014 | 0.000 | 0.010 | inf |
| Banten | 2013 | 2014 | 0.010 | 0.000 | 0.00 |
| Jawa Barat | 2014 | 2015 | 0.010 | 0.000 | 0.00 |
| Jawa Timur | 2014 | 2015 | 0.010 | 0.000 | 0.00 |
| DKI Jakarta | 2015 | 2016 | 0.000 | 0.010 | inf |
| Jawa Barat | 2015 | 2016 | 0.000 | 0.010 | inf |
| Jawa Timur | 2015 | 2016 | 0.000 | 0.010 | inf |
| Jawa Timur | 2016 | 2017 | 0.010 | 0.000 | 0.00 |
| Bali | 2016 | 2017 | 0.000 | 0.010 | inf |
| Jawa Barat | 2017 | 2018 | 0.010 | 0.000 | 0.00 |
| Jawa Timur | 2017 | 2018 | 0.000 | 0.010 | inf |
| Jawa Barat | 2018 | 2019 | 0.000 | 0.010 | inf |
| DI Yogyakarta | 2018 | 2019 | 0.010 | 0.000 | 0.00 |
| Kalimantan Barat | 2018 | 2019 | 0.020 | 0.000 | 0.00 |
| Riau | 2019 | 2020 | 0.020 | 0.240 | 12.00 |
| Bali | 2019 | 2020 | 0.010 | 0.000 | 0.00 |
| Kalimantan Barat | 2019 | 2020 | 0.000 | 0.010 | inf |
| Sumatera Selatan | 2020 | 2021 | 0.010 | 0.000 | 0.00 |
| Bengkulu | 2020 | 2021 | 0.050 | 0.000 | 0.00 |
| Jawa Barat | 2020 | 2021 | 0.010 | 0.000 | 0.00 |
