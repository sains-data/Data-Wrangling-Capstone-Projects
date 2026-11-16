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
| balita_tidak_kurang_dari_bayi | keras (kasus) | AKBa (var1373) ≥ AKB (var1584) pada wilayah, periode, dan rujukan yang sama | LOLOS |
| bps_hanya_tahun_terbit | keras (kasus) | tidak ada tahun BPS di luar tahun terbit (tidak ada interpolasi tanpa penanda) | LOLOS |
| survei_kematian_punya_rujukan | keras (kasus) | baris var1373/var1584 punya rujukan_tahun | LOLOS |
| who_wdi_balita_berdekatan | peringatan (kasus) | WHO vs WDI kematian balita berbeda > 10% (peringatan: selisih vintage yang besar) | PERINGATAN (3 baris) |

## Kegagalan aturan umum

Tidak ada.

## Baris yang memicu aturan kasus

### who_wdi_balita_berdekatan

| periode | MDG_0000000007 | SH.DYN.MORT | selisih_relatif |
|---|---|---|---|
| 2021 | 22.02 | 19.90 | 0.11 |
| 2022 | 21.29 | 19.10 | 0.12 |
| 2023 | 20.62 | 18.40 | 0.12 |
