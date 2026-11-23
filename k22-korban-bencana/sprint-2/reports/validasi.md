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
| cacah_bilangan_bulat | keras (kasus) | kejadian dan jiwa bilangan bulat | LOLOS |
| jenis_menjumlah_ke_total | keras (kasus) | jumlah per jenis = baris Total di berkas yang sama | LOLOS |
| per_100rb_dihitung_ulang | keras (kasus) | angka per 100.000 = pembilang / penduduk x 100.000 | LOLOS |
| kejadian_kabkota_tidak_kurang | peringatan (kasus) | kejadian jumlah kab/kota < provinsi (peringatan) | PERINGATAN (1 baris) |
| korban_kabkota_sama_provinsi | peringatan (kasus) | korban jumlah kab/kota ≠ provinsi (peringatan) | PERINGATAN (6 baris) |
| indonesia_sama_lintas_berkas | peringatan (kasus) | baris Indonesia berbeda antarberkas (peringatan) | PERINGATAN (1 baris) |
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

### kejadian_kabkota_tidak_kurang

| seri_kode | wilayah_kode | periode | rincian | nilai_kabkota | nilai_provinsi | selisih | _berkas_raw_kabkota | _berkas_raw_provinsi |
|---|---|---|---|---|---|---|---|---|
| kejadian | 3100 | 2024 | jenis_bencana=tanah_longsor | 0.00 | 1.00 | -1.00 | bnpb/2026-10-20/datastore/data-bencana-indonesia/a4daec53-1119-43ef-b05e-00ec3a4c42a4.json | bnpb/2026-10-20/datastore/data-bencana-indonesia/faeb2406-b800-4b8e-9e09-37d4b2aa5879.json |

### korban_kabkota_sama_provinsi

| seri_kode | wilayah_kode | periode | rincian | nilai_kabkota | nilai_provinsi | selisih | _berkas_raw_kabkota | _berkas_raw_provinsi |
|---|---|---|---|---|---|---|---|---|
| korban_mengungsi | 3100 | 2024 | jenis_bencana=tanah_longsor | 0.00 | 65.00 | -65.00 | bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/68c4448c-3de9-42e3-987d-31f5c05c37ba.json | bnpb/2026-10-20/datastore/data-bencana-indonesia/d1fd9f08-26e1-453a-9be0-422538f01b5e.json |
| korban_mengungsi | 3200 | 2024 | jenis_bencana=tanah_longsor | 5,801.00 | 5,736.00 | 65.00 | bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/68c4448c-3de9-42e3-987d-31f5c05c37ba.json | bnpb/2026-10-20/datastore/data-bencana-indonesia/d1fd9f08-26e1-453a-9be0-422538f01b5e.json |
| korban_terdampak | 3100 | 2024 | jenis_bencana=banjir | 9,133.00 | 11,639.00 | -2,506.00 | bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/89eb9dac-a891-477e-b264-2265f72f4e56.json | bnpb/2026-10-20/datastore/data-bencana-indonesia/5b9f7853-e69b-4d3a-917c-3fa3e473ed60.json |
| korban_terdampak | 3100 | 2024 | jenis_bencana=tanah_longsor | 0.00 | 187.00 | -187.00 | bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/89eb9dac-a891-477e-b264-2265f72f4e56.json | bnpb/2026-10-20/datastore/data-bencana-indonesia/5b9f7853-e69b-4d3a-917c-3fa3e473ed60.json |
| korban_terdampak | 3200 | 2024 | jenis_bencana=banjir | 468,909.00 | 466,403.00 | 2,506.00 | bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/89eb9dac-a891-477e-b264-2265f72f4e56.json | bnpb/2026-10-20/datastore/data-bencana-indonesia/5b9f7853-e69b-4d3a-917c-3fa3e473ed60.json |
| korban_terdampak | 3200 | 2024 | jenis_bencana=tanah_longsor | 23,443.00 | 23,256.00 | 187.00 | bnpb/2026-10-20/datastore/kompilasi-data-jumlah-dan-dampak-kejadian-bencana-2024/89eb9dac-a891-477e-b264-2265f72f4e56.json | bnpb/2026-10-20/datastore/data-bencana-indonesia/5b9f7853-e69b-4d3a-917c-3fa3e473ed60.json |

### indonesia_sama_lintas_berkas

| seri_kode | wilayah_kode | periode | rincian | nunique | min | max | size |
|---|---|---|---|---|---|---|---|
| kejadian | 9999 | 2024 | jenis_bencana=tanah_longsor | 2 | 27.00 | 207.00 | 3 |
