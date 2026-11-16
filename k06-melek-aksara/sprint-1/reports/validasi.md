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
| satu_total_kanonik | keras (kasus) | setiap provinsi x tahun tepat satu angka total kanonik (var1458) | LOLOS |
| rincian_konsisten_per_provinsi | keras (kasus) | tabel rinci: susunan rincian sama di semua tahun satu provinsi (9, atau 6 tanpa perdesaan) | LOLOS |
| total_di_antara_kota_desa | keras (kasus) | total tabel rinci di antara perkotaan dan perdesaan | LOLOS |
| total_rinci_sama_ringkas | peringatan (kasus) | total tabel rinci ≠ var1458 pada sel yang sama (peringatan: dilaporkan, tidak disamakan) | PERINGATAN (34 baris) |

## Kegagalan aturan umum

Tidak ada.

## Baris yang memicu aturan kasus

### total_rinci_sama_ringkas

| wilayah_kode | periode | ringkas | rinci | selisih |
|---|---|---|---|---|
| 1100 | 2017 | 97.94 | 98.15 | 0.21 |
| 1200 | 2017 | 98.89 | 98.96 | 0.07 |
| 1300 | 2017 | 98.85 | 98.93 | 0.08 |
| 1400 | 2017 | 99.17 | 99.21 | 0.04 |
| 1500 | 2017 | 98.09 | 98.28 | 0.19 |
| 1600 | 2017 | 98.54 | 98.65 | 0.11 |
| 1700 | 2017 | 97.90 | 98.04 | 0.14 |
| 1800 | 2017 | 96.89 | 97.21 | 0.32 |
| 1900 | 2017 | 97.79 | 97.97 | 0.18 |
| 2100 | 2017 | 98.83 | 98.88 | 0.05 |
| 3100 | 2017 | 99.67 | 99.68 | 0.01 |
| 3200 | 2017 | 98.23 | 98.38 | 0.15 |
| 3300 | 2017 | 93.39 | 93.99 | 0.60 |
| 3400 | 2017 | 94.64 | 95.09 | 0.45 |
| 3500 | 2017 | 91.82 | 92.53 | 0.71 |
| 3600 | 2017 | 97.57 | 97.79 | 0.22 |
| 5100 | 2017 | 92.90 | 93.59 | 0.69 |
| 5200 | 2017 | 87.14 | 88.53 | 1.39 |
| 5300 | 2017 | 91.68 | 92.75 | 1.07 |
| 6100 | 2017 | 92.48 | 93.25 | 0.77 |
| 6300 | 2017 | 98.40 | 98.52 | 0.12 |
| 6400 | 2017 | 98.96 | 99.04 | 0.08 |
| 6500 | 2017 | 95.14 | 95.63 | 0.49 |
| 7100 | 2017 | 99.76 | 99.73 | -0.03 |
| 7200 | 2017 | 97.69 | 97.83 | 0.14 |
| 7300 | 2017 | 91.65 | 92.53 | 0.88 |
| 7400 | 2017 | 94.32 | 95.05 | 0.73 |
| 7500 | 2017 | 98.44 | 98.47 | 0.03 |
| 7600 | 2017 | 92.79 | 93.71 | 0.92 |
| 8100 | 2017 | 99.13 | 99.19 | 0.06 |
