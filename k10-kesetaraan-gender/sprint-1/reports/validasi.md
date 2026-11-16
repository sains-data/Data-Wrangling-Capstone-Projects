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
| status_ilo_terdaftar | keras (kasus) | status_obs ILO terdaftar (B) atau kosong | LOLOS |
| dua_definisi_ilo_terpisah | keras (kasus) | dua definisi ILO dari berkas masing-masing | LOLOS |
| senior_tidak_melebihi_total | keras (kasus) | 0552 tidak melebihi T552 lebih dari 1 poin | LOLOS |
| ilo_dekat_bps | peringatan (kasus) | ILO T552 vs BPS > 5 poin (peringatan) | PERINGATAN (1 baris) |

## Kegagalan aturan umum

Tidak ada.

## Baris yang memicu aturan kasus

### ilo_dekat_bps

| periode | bps | ilo_t552 |
|---|---|---|
| 2016 | 23.60 | 44.78 |
