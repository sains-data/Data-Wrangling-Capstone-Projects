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
| luas_tidak_negatif_satu_satuan | keras (kasus) | luas >= 0 dan satu satuan per seri | LOLOS |
| komponen_dari_kamus | keras (kasus) | rincian IKLH hanya enam komponen dari kamus | LOLOS |
| jumlah_rincian_lahan | peringatan (kasus) | lahan kritis dan kawasan hutan: jumlah rincian = rincian jumlah (peringatan) | PERINGATAN (1 baris) |
| kolom_2020_tergeser | peringatan (kasus) | luas hutan 2020 menyimpang > 50% dari 2019–2021 (peringatan: baris sumber tergeser) | PERINGATAN (20 baris) |
| hutan_plus_non_hutan | peringatan (kasus) | luas hutan + non hutan ≠ jumlah (peringatan; ditandai 'cek' di CSV) | PERINGATAN (27 baris) |
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

### jumlah_rincian_lahan

| wilayah_kode | periode | selisih | seri_kode |
|---|---|---|---|
| 3400 | 2016 | -2,874.60 | var1304 |

### kolom_2020_tergeser

| wilayah_kode | 2019 | 2020 | 2021 | simpangan |
|---|---|---|---|---|
| 1700 | 674.60 | 191.90 | 654.20 | -0.71 |
| 1800 | 335.90 | 665.00 | 322.30 | 1.02 |
| 1900 | 192.10 | 344.20 | 205.00 | 0.73 |
| 3100 | 0.30 | 152.90 | 1.10 | 217.43 |
| 3200 | 797.20 | 0.90 | 686.50 | -1.00 |
| 3400 | 32.60 | 634.50 | 18.90 | 23.64 |
| 3500 | 1,207.30 | 20.30 | 1,248.00 | -0.98 |
| 3600 | 147.10 | 1,192.60 | 157.80 | 6.82 |
| 5100 | 99.80 | 5,656.60 | 96.00 | 56.78 |
| 5300 | 1,719.20 | 7,459.30 | 1,717.70 | 3.34 |
| 6100 | 5,587.00 | 13,289.50 | 5,637.80 | 1.37 |
| 6200 | 7,396.60 | 560.00 | 7,342.20 | -0.92 |
| 6400 | 12,806.40 | 3,802.40 | 7,758.00 | -0.63 |
| 7100 | 555.40 | 1,891.20 | 549.50 | 2.42 |
| 7200 | 3,816.30 | 837.60 | 3,760.20 | -0.78 |
| 7400 | 1,861.40 | 97.50 | 1,883.00 | -0.95 |
| 7600 | 823.30 | 1,725.40 | 811.50 | 1.11 |
| 8200 | 2,014.10 | 3,075.50 | 2,033.20 | 0.52 |
| 9100 | 8,874.90 | 25,396.60 | 9,087.00 | 1.83 |
| 9400 | 25,168.70 | 8,967.30 | 25,241.30 | -0.64 |

### hutan_plus_non_hutan

| wilayah_kode | periode | selisih |
|---|---|---|
| 1700 | 2020 | -343.20 |
| 1800 | 2020 | -1,432.50 |
| 1900 | 2020 | 1,775.70 |
| 3100 | 2020 | 873.90 |
| 3200 | 2020 | -3,633.30 |
| 3300 | 2020 | 242.00 |
| 3400 | 2016 | -2,874.60 |
| 3400 | 2020 | 3,137.20 |
| 3500 | 2020 | -4,518.30 |
| 3600 | 2020 | 3,898.50 |
| 5100 | 2018 | 0.30 |
| 5100 | 2020 | 14,005.90 |
| 5200 | 2020 | 1,733.70 |
| 5300 | 2020 | 10,543.70 |
| 6100 | 2020 | 4,932.00 |
| 6200 | 2020 | -13,826.70 |
| 6300 | 2020 | -2,515.40 |
| 6400 | 2020 | -13,470.10 |
| 7100 | 2020 | 2,172.10 |
| 7200 | 2020 | -4,354.50 |
| 7400 | 2020 | -3,044.70 |
| 7500 | 2020 | 781.70 |
| 7600 | 2020 | 3,042.30 |
| 8100 | 2020 | -1,491.50 |
| 8200 | 2020 | 1,491.50 |
| 9100 | 2020 | 21,452.00 |
| 9400 | 2020 | -21,452.00 |
