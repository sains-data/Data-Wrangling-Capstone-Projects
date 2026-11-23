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
| satu_baris_per_provinsi_tahun | keras (kasus) | setiap seri BPS × wilayah × tahun muncul tepat satu kali | LOLOS |
| who_satu_total_per_tahun | keras (kasus) | setiap seri WHO × tahun punya paling banyak satu baris rincian total | LOLOS |
| tidak_ada_angka_sensor | keras (kasus) | tidak ada nilai SN.ITK.DEFC.ZS ≤ 2,5 yang terbaca sebagai angka pasti | LOLOS |
| bps_wdi_pou_berdekatan | peringatan (kasus) | PoU Indonesia BPS vs WDI berbeda > 2 poin (peringatan: periksa metode, bukan galat) | PERINGATAN (3 baris) |
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

### bps_wdi_pou_berdekatan

| periode | SN.ITK.DEFC.ZS | var1473 | selisih_poin |
|---|---|---|---|
| 2017 | 6.00 | 8.23 | 2.23 |
| 2022 | 6.60 | 10.21 | 3.61 |
| 2023 | 6.50 | 8.53 | 2.03 |
