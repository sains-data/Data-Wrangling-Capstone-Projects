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
| upah_positif_satu_satuan | keras (kasus) | upah > 0 dan bersatuan rupiah_per_jam | LOLOS |
| total_klasifikasi_lain_sama | keras (kasus) | total klasifikasi lain = total utama | LOLOS |
| status_ilo_terdaftar | keras (kasus) | status_obs ILO terdaftar (B) atau kosong | LOLOS |
| upah_bps_dekat_ilo | peringatan (kasus) | upah BPS vs ILO berbeda > 20% (peringatan) | LOLOS |
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

Tidak ada.
