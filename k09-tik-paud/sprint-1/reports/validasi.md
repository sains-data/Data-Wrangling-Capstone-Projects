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
| satu_snapshot_per_seri | keras (kasus) | setiap seri BPS dari satu berkas (snapshot terbaru) | LOLOS |
| unik_per_provinsi_tahun | keras (kasus) | seri x provinsi x tahun unik | LOLOS |
| tik_muda_tidak_lebih_rendah | peringatan (kasus) | TIK 15–24 < TIK 15–59 pada sel yang sama (peringatan) | PERINGATAN (3 baris) |
| rse_tinggi | peringatan (kasus) | sel APK PAUD dengan RSE 25–50% (peringatan: tandai di Gold) | PERINGATAN (2 baris) |

## Kegagalan aturan umum

Tidak ada.

## Baris yang memicu aturan kasus

### tik_muda_tidak_lebih_rendah

| wilayah_kode | periode | tik_15_24 | tik_15_59 |
|---|---|---|---|
| 9500 | 2024 | 56.08 | 58.01 |
| 9500 | 2025 | 57.49 | 59.14 |
| 9700 | 2025 | 15.79 | 18.67 |

### rse_tinggi

| seri_kode | nama_wilayah | periode | nilai |
|---|---|---|---|
| var1439 | Papua Pegunungan | 2024 | 3.08 |
| var1439 | Papua Pegunungan | 2025 | 3.10 |
