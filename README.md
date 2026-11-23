# Kunci Capstone Data Wrangling 2026

Repo acuan untuk 23 kasus Capstone Data Wrangling (Indikator SDG Indonesia dari Banyak Sumber, Program
Studi Sains Data ITERA). Setiap folder kelompok berisi repo tim yang sudah dikerjakan, dipisah per sprint,
dalam bentuk yang sama dengan template `sains-data/capstone-dw-2026-starter`.

**Cara memakai.** Folder sprint dibuka setelah sprint itu ditutup dan demo semua kelompok dilihat dosen.
Pelajari dan bandingkan dengan repo timmu: berkas mana yang berbeda, keputusan mana yang kamu ambil
berbeda, dan apa alasannya. Setiap keputusan di sini adalah salah satu jawaban yang dapat dipertahankan;
alternatif yang ditolak ada di `log-keputusan.csv` setiap folder. Wawancara menanyakan alasan di balik
keputusan timmu, bukan apakah hasilnya sama dengan kunci.

## Menjalankan satu folder

```bash
cd k02-kematian-anak-ibu/sprint-1
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python unduh_data.py --kasus 2
python pipeline.py
python -m pytest -q
```

## Daftar kasus

| Kasus | Sprint 1 | Sprint 2 | Sprint 3 |
|---|---|---|---|
| [01 Kerawanan pangan provinsi](k01-kerawanan-pangan/) | [selesai](k01-kerawanan-pangan/sprint-1/) (1.414 baris Silver, ±2,0 detik) | [selesai](k01-kerawanan-pangan/sprint-2/) (2 indikator Gold, 628 sel terisi, 68 baris rekonsiliasi) | menyusul |
| [02 Kematian anak dan ibu](k02-kematian-anak-ibu/) | [selesai](k02-kematian-anak-ibu/sprint-1/) (867 baris Silver, ±1,9 detik) | [selesai](k02-kematian-anak-ibu/sprint-2/) (3 indikator Gold, 236 sel terisi, 135 baris rekonsiliasi) | menyusul |
| [03 Kesehatan reproduksi remaja](k03-kesehatan-reproduksi-remaja/) | [selesai](k03-kesehatan-reproduksi-remaja/sprint-1/) (235 baris Silver, ±1,8 detik) | [selesai](k03-kesehatan-reproduksi-remaja/sprint-2/) (2 indikator Gold, 134 sel terisi, 28 baris rekonsiliasi) | menyusul |
| [04 Penyakit dan faktor risiko](k04-penyakit-faktor-risiko/) | [selesai](k04-penyakit-faktor-risiko/sprint-1/) (1.058 baris Silver, ±2,1 detik) | [selesai](k04-penyakit-faktor-risiko/sprint-2/) (3 indikator Gold, 886 sel terisi, 71 baris rekonsiliasi) | menyusul |
| [05 Layanan dan tenaga kesehatan](k05-layanan-tenaga-kesehatan/) | [selesai](k05-layanan-tenaga-kesehatan/sprint-1/) (1.722 baris Silver, ±2,3 detik) | [selesai](k05-layanan-tenaga-kesehatan/sprint-2/) (5 indikator Gold, 836 sel terisi, 17 baris rekonsiliasi) | menyusul |
| [06 Melek aksara](k06-melek-aksara/) | [selesai](k06-melek-aksara/sprint-1/) (5.762 baris Silver, ±2,4 detik) | [selesai](k06-melek-aksara/sprint-2/) (2 indikator Gold, 995 sel terisi, 41 baris rekonsiliasi) | menyusul |
| [07 Partisipasi dan lama sekolah](k07-partisipasi-lama-sekolah/) | [selesai](k07-partisipasi-lama-sekolah/sprint-1/) (4.216 baris Silver, ±3,3 detik) | [selesai](k07-partisipasi-lama-sekolah/sprint-2/) (7 indikator Gold, 3.726 sel terisi, 27 baris rekonsiliasi) | menyusul |
| [08 Kesetaraan pendidikan](k08-kesetaraan-pendidikan/) | [selesai](k08-kesetaraan-pendidikan/sprint-1/) (5.418 baris Silver, ±4,0 detik) | [selesai](k08-kesetaraan-pendidikan/sprint-2/) (12 indikator Gold, 5.177 sel terisi, 21 baris rekonsiliasi) | menyusul |
| [09 Keterampilan TIK dan PAUD](k09-tik-paud/) | [selesai](k09-tik-paud/sprint-1/) (1.653 baris Silver, ±2,3 detik) | [selesai](k09-tik-paud/sprint-2/) (4 indikator Gold, 1.528 sel terisi, 33 baris rekonsiliasi) | menyusul |
| [10 Kesetaraan gender](k10-kesetaraan-gender/) | [selesai](k10-kesetaraan-gender/sprint-1/) (840 baris Silver, ±1,9 detik) | [selesai](k10-kesetaraan-gender/sprint-2/) (2 indikator Gold, 762 sel terisi, 33 baris rekonsiliasi) | menyusul |
| [11 Pengangguran](k11-pengangguran/) | [selesai](k11-pengangguran/sprint-1/) (7.572 baris Silver, ±2,9 detik) | [selesai](k11-pengangguran/sprint-2/) (1 indikator Gold, 1.939 sel terisi, 91 baris rekonsiliasi) | menyusul |
| [12 Upah dan informalitas](k12-upah-informalitas/) | [selesai](k12-upah-informalitas/sprint-1/) (1.584 baris Silver, ±1,9 detik) | [selesai](k12-upah-informalitas/sprint-2/) (2 indikator Gold, 662 sel terisi, 19 baris rekonsiliasi) | menyusul |
| [13 Pemuda dan pekerja anak](k13-pemuda-pekerja-anak/) | [selesai](k13-pemuda-pekerja-anak/sprint-1/) (720 baris Silver, ±1,9 detik) | [selesai](k13-pemuda-pekerja-anak/sprint-2/) (2 indikator Gold, 588 sel terisi, 31 baris rekonsiliasi) | menyusul |
| [14 Produktivitas dan industri](k14-produktivitas-industri/) | [selesai](k14-produktivitas-industri/sprint-1/) (1.779 baris Silver, ±2,4 detik) | [selesai](k14-produktivitas-industri/sprint-2/) (4 indikator Gold, 1.575 sel terisi, 67 baris rekonsiliasi) | menyusul |
| [15 Kemiskinan dan daerah tertinggal](k15-daerah-tertinggal/) | [selesai](k15-daerah-tertinggal/sprint-1/) (3.897 baris Silver, ±2,2 detik) | [selesai](k15-daerah-tertinggal/sprint-2/) (3 indikator Gold, 1.329 sel terisi, 23 baris rekonsiliasi) | menyusul |
| [16 Ketimpangan dan layanan dasar](k16-ketimpangan-layanan-dasar/) | [selesai](k16-ketimpangan-layanan-dasar/sprint-1/) (1.137 baris Silver, ±2,2 detik) | [selesai](k16-ketimpangan-layanan-dasar/sprint-2/) (5 indikator Gold, 777 sel terisi, 37 baris rekonsiliasi) | menyusul |
| [17 Air minum, sanitasi, dan kebersihan](k17-air-sanitasi/) | [selesai](k17-air-sanitasi/sprint-1/) (3.242 baris Silver, ±2,8 detik) | [selesai](k17-air-sanitasi/sprint-2/) (6 indikator Gold, 2.549 sel terisi, 92 baris rekonsiliasi) | menyusul |
| [18 Energi: listrik dan bahan bakar memasak](k18-energi/) | [selesai](k18-energi/sprint-1/) (4.889 baris Silver, ±2,9 detik) | [selesai](k18-energi/sprint-2/) (4 indikator Gold, 2.590 sel terisi, 54 baris rekonsiliasi) | menyusul |
| [19 Hunian dan transportasi](k19-hunian-transportasi/) | [selesai](k19-hunian-transportasi/sprint-1/) (1.305 baris Silver, ±2,5 detik) | [selesai](k19-hunian-transportasi/sprint-2/) (7 indikator Gold, 1.258 sel terisi, 16 baris rekonsiliasi) | menyusul |
| [20 Hutan, lahan, dan lingkungan](k20-hutan-lahan-lingkungan/) | [selesai](k20-hutan-lahan-lingkungan/sprint-1/) (4.045 baris Silver, ±2,9 detik) | [selesai](k20-hutan-lahan-lingkungan/sprint-2/) (7 indikator Gold, 1.641 sel terisi, 36 baris rekonsiliasi) | menyusul |
| [21 Keamanan dan pencatatan sipil](k21-keamanan-pencatatan-sipil/) | [selesai](k21-keamanan-pencatatan-sipil/sprint-1/) (1.370 baris Silver, ±2,5 detik) | [selesai](k21-keamanan-pencatatan-sipil/sprint-2/) (6 indikator Gold, 1.315 sel terisi, 32 baris rekonsiliasi) | menyusul |
| [22 Korban bencana](k22-korban-bencana/) | [selesai](k22-korban-bencana/sprint-1/) (14.193 baris Silver, ±5,4 detik) | [selesai](k22-korban-bencana/sprint-2/) (10 indikator Gold, 1.374 sel terisi, 19 baris rekonsiliasi) | menyusul |
| [23 Kerusakan dan kerugian bencana](k23-kerusakan-kerugian-bencana/) | [selesai](k23-kerusakan-kerugian-bencana/sprint-1/) (18.187 baris Silver, ±6,7 detik) | [selesai](k23-kerusakan-kerugian-bencana/sprint-2/) (12 indikator Gold, 1.688 sel terisi, 33 baris rekonsiliasi) | menyusul |

Data mentah tidak disimpan di repo ini; `unduh_data.py` mengunduhnya dari Release starter (snapshot 17–20
Oktober 2026) dan memeriksa sha256-nya. Lisensi data mengikuti `data/LISENSI.md` yang ikut terunduh.

## 6. Pertanyaan pancingan per tugas backlog Sprint 1

| Tugas | Tanyakan | Yang dicari di jawaban |
|---|---|---|
| Penjaga data | "Kalau satu berkas berubah besok, bagian mana yang menangkapnya?" | sha256 di MANIFEST, `data_hash` sama di laptop semua anggota |
| Pembaca per sumber | "Berapa baris per berkas, dan dari mana angka itu?" | jumlah dari kode, bukan dari Excel; pembaca tidak membersihkan apa pun |
| `ekstraksi.jalankan()` | "Bagaimana kalian tahu tidak ada berkas MANIFEST yang terlewat?" | assert atau tes yang membandingkan daftar berkas |
| Profil seri utama | "Calon anomali mana yang kalian pertahankan, dan kenapa?" | anomali sebagai calon dengan alasan, bukan daftar yang langsung dibuang |
| Profil pembanding | "Tahun berapa saja pembanding beririsan dengan seri provinsi?" | baris ada vs nilai ada (WDI `value: null`) |
| Grid 38 provinsi | "Sel kosong ini kategori apa? Buktinya di mana?" | provinsi belum dibentuk, tidak diterbitkan, batas lama, baru benar-benar missing |
| Outlier, patahan, galat, duplikat | "Bagaimana membedakan outlier dari patahan seri?" | uji berapa provinsi ikut melompat; catatan penerbit; dua snapshot dibandingkan |
| Satuan, periode, SDG | "Satuan seri ini dari mana? Tunjukkan di berkasnya." | `var.label`/`var.note`/`UNIT_MEASURE`/judul, bukan katalog saja |
| Silver pertama | "Keputusan mana yang paling banyak mengubah jumlah baris?" | merujuk baris log dengan `dampak_baris` |
| Tabel nasional + pasangan | "Selisih terbesar: galat atau beda definisi?" | pertanyaan keterbandingan (umur, cakupan, rujukan waktu) sebelum menghitung selisih |
| Skema SQL | "Apa kunci primer Silver, dan apakah data kalian sendiri melanggarnya?" | kunci memuat rincian (dan berkas bila satu sel punya beberapa berkas) |
| Aturan validasi | "Tunjukkan tes yang gagal kalau satu baris dirusak." | tes baris rusak, bukan hanya tes yang lolos pada data asli |
| Data dictionary | "Satu baris Silver: dari berkas mana, baris ke berapa?" | contoh penelusuran lewat `_berkas_raw` dan `_sha256_raw` |
| Integrator | "Urutan merge kalian, dan apa yang rusak di tengah?" | riwayat commit dan PR, bukan satu commit besar di akhir |
| Analis | "Angka ini di `reports/tim.md` datang dari mana?" | setiap angka bisa dirujuk ke Silver atau log |
| Koordinator | "Sprint Goal tercapai? Apa yang dipindah ke Sprint 2?" | Log Sprint jujur, termasuk yang tidak selesai |
| Reproduksi | "Silver hasil klon bersih sama persis dengan yang di-commit?" | dibandingkan dengan kode, waktu jalan dicatat |

## 7. Satu pertanyaan pembuka per kelompok

Diambil dari jebakan yang paling sering terlewat (`kNN-*/README.md`); jawabannya ada di log kunci.

| Kasus | Pertanyaan pembuka | Jawaban yang dicari |
|---|---|---|
| [01](k01-kerawanan-pangan/) | Kenapa ada kunci Silver kembar di `NUTRITION_WH_2`? | "total" ditulis tiga cara di kolom `DIM_*` |
| [02](k02-kematian-anak-ibu/) | `var1373` dan `var1584` berkode SDG sama; duplikat? | bukan: balita vs bayi, bukti `var.label` |
| [03](k03-kesehatan-reproduksi-remaja/) | Kelompok umur `var1353` apa, dan baris WHO mana yang sebanding? | 15–19 dari judul JSON; baris WHO 10–14 tidak sebanding |
| [04](k04-penyakit-faktor-risiko/) | Malaria BPS dan WHO sebanding? | per 1.000 penduduk vs per 1.000 penduduk berisiko |
| [05](k05-layanan-tenaga-kesehatan/) | Kenapa `var1477` hilang dari profil kalau menyaring total? | seri ini tidak punya baris total; satuan di `var.note` |
| [06](k06-melek-aksara/) | Bagaimana membaca tabel rinci HTML Excel? | tiga blok, header bertingkat, nama tanpa kode dipetakan |
| [07](k07-partisipasi-lama-sekolah/) | APK 104: galat? | tidak; aturan 0–100 salah untuk APK |
| [08](k08-kesetaraan-pendidikan/) | Rasio BPS dan GPI WDI satu skala? | BPS dikali 100, WDI tidak |
| [09](k09-tik-paud/) | `var1221` ada di dua snapshot; mana yang masuk Silver? | aturan pemilihan tercatat, bukan keduanya |
| [10](k10-kesetaraan-gender/) | Dua seri ILO 5.5.2 sama? | senior-menengah vs seluruh manajemen; `OBS_STATUS` B = patahan |
| [11](k11-pengangguran/) | TPT Februari dan Agustus dirata-rata? | tidak; periode dipisah, ILO rujukan Agustus |
| [12](k12-upah-informalitas/) | Satuan upah ILO dari mana? | `UNIT_MEASURE` dan `NOTE_INDICATOR`; klasifikasi dengan total masing-masing |
| [13](k13-pemuda-pekerja-anak/) | Umur pekerja anak BPS, ILO, WDI sama? | 5–17, 15–17 (kolom AGE), 7–14 |
| [14](k14-produktivitas-industri/) | Kenapa dua kunci JSON produktivitas tidak terbaca? | tidak cocok dengan daftar label; laju bisa negatif |
| [15](k15-daerah-tertinggal/) | Sel Jakarta kosong di seri desa: missing? | bukan; Jakarta tidak punya desa |
| [16](k16-ketimpangan-layanan-dasar/) | Provinsi kosong di `var2011`? | ditekan karena RSE (catatan penerbit) |
| [17](k17-air-sanitasi/) | Isi `var847` sesuai kode katalognya? | bukan; sanitasi layak, bukan 11.1.1 |
| [18](k18-energi/) | Koma desimal di tabel bahan bakar ditangani di mana? | pembaca HTML, kolom per kolom |
| [19](k19-hunian-transportasi/) | Hunian layak turun 2018→2019 di hampir semua provinsi: outlier? | patahan definisi, jangan di-*winsorize* |
| [20](k20-hutan-lahan-lingkungan/) | Kolom 2020 tutupan hutan sudah benar? | tergeser terhadap nama provinsi (kolom `cek`) |
| [21](k21-keamanan-pencatatan-sipil/) | Periode korban kejahatan tahun apa? | tahun kejadian, bukan tahun survei; empat seri di dua snapshot |
| [22](k22-korban-bencana/) | Rekap kab/kota 2021: berapa kab/kota terbaca untuk Aceh? | semua, setelah sel Provinsi tergabung diisi; kode Kemendagri Papua |
| [23](k23-kerusakan-kerugian-bencana/) | Luas lahan terbakar 2012 = 44 juta ha: dipakai? | mustahil, ditangani sebagai galat input dengan bukti |