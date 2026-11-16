# Tabel nasional dan pasangan rekonsiliasi

Dihasilkan `python pipeline.py` (`src/gold/nasional.py`) dari Silver dan `src/konfigurasi.py`. Selisih dihitung di Sprint 2; Sprint 1 memastikan setiap pasangan memang sebanding dan mencatat tahun yang beririsan.

Tabel nasional (periode x seri, rincian total, tampilan lebar): `reports/tabel-nasional.csv`. Kolom BPS hanya terisi pada tahun survei; itu bentuk datanya, tidak diisi.

## Ringkasan pasangan

| id | seri_utama | pembanding | jenis | periode_beririsan | tahun | dugaan_kategori |
|---|---|---|---|---|---|---|
| P1 | korban_mengungsi_per_100rb | korban_mengungsi [jenis_bencana=banjir], jumlah_penduduk [total] | selisih | 1 | 2025 | pembulatan atau penduduk berbeda; berkas pengungsi dan berkas per 100.000 terbit terpisah |
| P2 | korban_meninggal_hilang_per_100rb | korban_meninggal [jenis_bencana=banjir], korban_hilang [jenis_bencana=banjir], jumlah_penduduk [total] | selisih | 1 | 2025 | pembulatan; pembilang dari dua berkas terpisah |
| P3 | kejadian | kejadian [jenis_bencana=banjir] | selisih | 16 | 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | definisi penghitungan: kejadian lintas provinsi dihitung sekali secara nasional |
| P4 | EN.CLC.MDAT.ZS | korban_terdampak [jenis_bencana=banjir] | konteks | 0 | — | periode tidak beririsan: WDI rata-rata 1990–2009, BNPB 2010–2025 |

## Rincian per pasangan

### P1: Mengungsi per 100.000: angka BNPB vs dihitung ulang dari pengungsi dan penduduk
- Seri utama: `korban_mengungsi_per_100rb` (rincian `jenis_bencana=banjir`)
- Pembanding: `korban_mengungsi` (rincian `jenis_bencana=banjir`), `jumlah_penduduk` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2025
- Dugaan kategori selisih (diuji di Sprint 2): pembulatan atau penduduk berbeda; berkas pengungsi dan berkas per 100.000 terbit terpisah

Pertanyaan keterbandingan dan jawabannya:

1. **Penyebutnya apa?** Kolom Jumlah Penduduk di berkas per 100.000 itu sendiri (Keterangan: publikasi BPS).
2. **Pembilangnya dari berkas mana?** Tabel 'Jumlah Korban Mengungsi Akibat Bencana Menurut Provinsi 2025'; baris dan jenis yang sama.
3. **Apa yang diharapkan?** pengungsi / penduduk x 100.000 sama dengan angka terbit sampai pembulatan.

### P2: Meninggal dan hilang per 100.000: angka BNPB vs (meninggal + hilang) / penduduk
- Seri utama: `korban_meninggal_hilang_per_100rb` (rincian `jenis_bencana=banjir`)
- Pembanding: `korban_meninggal` (rincian `jenis_bencana=banjir`), `korban_hilang` (rincian `jenis_bencana=banjir`), `jumlah_penduduk` (rincian `total`)
- Jenis: **selisih**; tahun beririsan: 2025
- Dugaan kategori selisih (diuji di Sprint 2): pembulatan; pembilang dari dua berkas terpisah

Pertanyaan keterbandingan dan jawabannya:

1. **Apakah pembilang = meninggal + hilang?** Judul resource: 'Meninggal dan Hilang per 100.000 Orang'.
2. **Apakah sama dengan indikator 13.1.1?** Tidak sepenuhnya: 13.1.1 juga memasukkan terdampak langsung.

### P3: Kejadian banjir: baris INDONESIA vs jumlah 38 provinsi
- Seri utama: `kejadian` (rincian `jenis_bencana=banjir`)
- Pembanding: `kejadian` (rincian `jenis_bencana=banjir`)
- Jenis: **selisih**; tahun beririsan: 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025
- Dugaan kategori selisih (diuji di Sprint 2): definisi penghitungan: kejadian lintas provinsi dihitung sekali secara nasional

Pertanyaan keterbandingan dan jawabannya:

1. **Mengapa jumlah provinsi boleh lebih besar?** Keterangan: kejadian yang berdampak lebih dari satu provinsi dihitung satu kali secara nasional dan di setiap provinsi terdampak.
2. **Bolehkah sebaliknya (jumlah provinsi < INDONESIA)?** Tidak; bila terjadi, itu temuan yang dicatat.

### P4: Penduduk terdampak kekeringan, banjir, suhu ekstrem (WDI): konteks
- Seri utama: `EN.CLC.MDAT.ZS` (rincian `total`)
- Pembanding: `korban_terdampak` (rincian `jenis_bencana=banjir`)
- Jenis: **konteks**; tahun beririsan: —
- Dugaan kategori selisih (diuji di Sprint 2): periode tidak beririsan: WDI rata-rata 1990–2009, BNPB 2010–2025

Pertanyaan keterbandingan dan jawabannya:

1. **Mengapa tidak dihitung selisihnya?** WDI satu angka rata-rata 1990–2009 (name), tidak ada tahun yang sama.
2. **Satuannya sama?** Tidak: WDI persen penduduk, BNPB jiwa.
