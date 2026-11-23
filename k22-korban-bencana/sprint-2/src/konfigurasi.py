"""Keputusan wrangling Kasus 22 — Korban bencana.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, cara menulis rincian, berkas mana yang dipakai deret profil, sel yang dinyatakan
tidak terbit, ambang anomali, dan pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.

Nama ukuran BNPB (judul resource dan kepala kolom -> seri) ada di src/kamus_bnpb.py karena sama untuk semua
kasus BNPB; di sini hanya dipilih seri mana yang masuk kasus ini.
"""

KASUS = 22
SLUG = "korban-bencana"
JUDUL = "Korban bencana"

FORMAT_BPS = "json"     # tidak dipakai (tidak ada seri BPS)

_CKAN = "judul resource di ckan/package_search-pusdatinkom-01.json"
_K = dict(sumber="bnpb", tingkat="provinsi", satuan="jiwa", katalog_satuan="jiwa",
          bukti_satuan="baris satuan '(jiwa)' di bawah kepala 'Korban' pada rekap 2021/2022 (XLSX tangan)",
          sdg="13.1.1|1.5.1|11.5.1", katalog_sdg="13.1.1|1.5.1|11.5.1",
          bukti_sdg="indikator global 13.1.1 = 1.5.1 = 11.5.1 (meninggal, hilang, dan terdampak langsung per 100.000 "
                    "penduduk); seri ini komponen pembilangnya, bukan indikatornya")
SERI = {
    "kejadian": dict(sumber="bnpb", tingkat="provinsi", nama="Jumlah kejadian bencana", satuan="kejadian",
                     katalog_satuan="kejadian",
                     bukti_satuan="Keterangan: 'Jumlah Kejadian: Jumlah Total Kejadian Bencana Menurut Klasifikasi Penyajian'",
                     sdg="—", katalog_sdg="—", bukti_sdg="tidak ada indikator global untuk jumlah kejadian",
                     cakupan="satu kejadian satu jenis utama; kejadian lintas provinsi dihitung di setiap provinsi terdampak "
                             "tetapi sekali secara nasional (Keterangan); ambang batas kejadian (Keterangan)"),
    "korban_meninggal": dict(**_K, nama="Jumlah korban meninggal dunia akibat bencana",
                             cakupan=f"provinsi per jenis 2021, 2022, 2024, 2025; nasional 2010–2024 ada di katalog tetapi "
                                     f"tidak di paket (resource b2fa5c46, {_CKAN})"),
    "korban_hilang": dict(**_K, nama="Jumlah korban hilang akibat bencana",
                          cakupan="provinsi per jenis 2021, 2022, 2024, 2025; nasional per jenis 2010–2024"),
    "korban_luka_sakit": dict(**_K, nama="Jumlah korban luka/sakit akibat bencana",
                              cakupan="provinsi per jenis 2021, 2022, 2024, 2025; nasional per jenis 2010–2024; "
                                      "judul 2025 'Korban Luka', kepala rekap 'Luka-Luka'"),
    "korban_mengungsi": dict(**_K, nama="Jumlah korban mengungsi akibat bencana",
                             cakupan="provinsi per jenis 2024, 2025; nasional per jenis 2010–2024; tabel 2024 banyak sel kosong"),
    "korban_terdampak": dict(**_K, nama="Jumlah korban terdampak akibat bencana",
                             cakupan="provinsi per jenis 2024, 2025; nasional per jenis 2010–2024"),
    "korban_terdampak_mengungsi": dict(**_K, nama="Jumlah korban terdampak dan mengungsi (satu kolom di rekap 2021/2022)",
                                       cakupan="hanya rekap 2021/2022; kepala 'Terdampak - Mengungsi' tidak memisahkan "
                                               "keduanya, jadi tidak digabung dengan korban_terdampak atau korban_mengungsi"),
    "korban_mengungsi_per_100rb": dict(
        sumber="bnpb", tingkat="provinsi", nama="Jumlah korban mengungsi per 100.000 orang", satuan="per_100000_penduduk",
        katalog_satuan="per_100000_penduduk", bukti_satuan=f"{_CKAN}: 'Jumlah Korban Mengungsi per 100.000 Orang ...'",
        sdg="13.1.1|1.5.1|11.5.1", katalog_sdg="13.1.1|1.5.1|11.5.1",
        bukti_sdg="per 100.000 penduduk seperti indikator global, tetapi hanya pengungsi (indikator global: terdampak langsung)",
        cakupan="2025; penyebut = kolom Jumlah Penduduk di berkas yang sama (Keterangan: publikasi BPS)"),
    "korban_meninggal_hilang_per_100rb": dict(
        sumber="bnpb", tingkat="provinsi", nama="Jumlah korban meninggal dan hilang per 100.000 orang",
        satuan="per_100000_penduduk", katalog_satuan="per_100000_penduduk",
        bukti_satuan=f"{_CKAN}: 'Jumlah Korban Meninggal dan Hilang per 100.000 Orang ...'",
        sdg="13.1.1|1.5.1|11.5.1", katalog_sdg="13.1.1|1.5.1|11.5.1",
        bukti_sdg="bagian meninggal + hilang dari indikator global 13.1.1 (tanpa terdampak langsung)",
        cakupan="2025; penyebut = kolom Jumlah Penduduk di berkas yang sama"),
    "jumlah_penduduk": dict(
        sumber="bnpb", tingkat="provinsi", nama="Jumlah penduduk (penyebut angka per 100.000)", satuan="jiwa",
        katalog_satuan="jiwa", bukti_satuan="Keterangan: 'Jumlah Penduduk Berdasarkan Publikasi Badan Pusat Statistik'",
        sdg="—", katalog_sdg="—", bukti_sdg="penyebut, bukan indikator",
        cakupan="2025; muncul di dua berkas per 100.000 (nilai sama, lihat reports/bnpb-lintas-berkas.csv)"),
    "EN.CLC.MDAT.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Droughts, floods, extreme temperatures (% of population, average 1990-2009)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of population, average 1990-2009)'",
        sdg="—", katalog_sdg="—", bukti_sdg="tercantum di sumber46_indikator.json tanpa kode indikator SDG",
        cakupan="satu angka rata-rata 1990–2009 yang ditulis sebagai date 2009; hanya kekeringan, banjir, suhu ekstrem"),
}

# Rincian (K-006): jenis bencana memakai slug kolom tabel per jenis; ejaan lain di rekap 2021/2022 disamakan
# (src/kamus_bnpb.py JENIS_SAMA). Baris 'Total' rekap nasional = total.
RINCIAN_TOTAL_BPS = set()
RINCIAN_TOTAL_WHO = set()
RINCIAN_DIMENSI = {"jenis_bencana": "jenis_bencana", "tingkat_kerusakan": "tingkat_kerusakan"}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"jenis_bencana": {"banjir", "cuaca_ekstrem", "erupsi_gunung_api", "gelombang_pasang_dan_abrasi",
                                  "gempabumi", "kebakaran_hutan_dan_lahan", "kekeringan", "tanah_longsor", "tsunami"},
                "tingkat_kerusakan": {"berat", "sedang", "ringan"}}

RUJUKAN_TAHUN = {}

# Deret profil = jumlah semua jenis bencana dalam satu berkas (K-005). Jenis membagi habis kejadian: "Jika satu
# kejadian melibatkan lebih dari satu tipe kejadian bencana, ditentukan satu tipe kejadian utama" (Keterangan).
DERET = {s: ["jumlah"] for s in ("kejadian", "korban_meninggal", "korban_hilang", "korban_luka_sakit", "korban_mengungsi",
                                 "korban_terdampak", "korban_terdampak_mengungsi", "korban_mengungsi_per_100rb",
                                 "korban_meninggal_hilang_per_100rb")}

# Satu sel provinsi x tahun bisa punya angka dari beberapa berkas (K-007). Deret profil memakai satu berkas:
# tabel provinsi diterbitkan langsung lebih dulu, salinan kompilasi sesudahnya, angka jumlahan kab/kota terakhir.
URUTAN_BERKAS = [
    ("*/5dfcae7e-*", "Jumlah Kejadian Bencana Menurut Provinsi Tahun 2010-2024: angka provinsi yang diterbitkan, satu tabel"),
    ("*/tangan/*per-provinsi*", "rekap provinsi 2021/2022"),
    ("*/tangan/*menurut-provinsi*", "tabel provinsi 2025"),
    ("*/datastore/data-bencana-indonesia/*", "tabel provinsi 2024 dataset data-bencana-indonesia"),
    ("*/datastore/kompilasi-*/*", "salinan tabel 2024 dataset kompilasi (nilai sama, reports/bnpb-lintas-berkas.csv)"),
    ("*/tangan/*kabup*", "rekap kab/kota 2021/2022 yang dijumlahkan ke provinsi: cadangan"),
]

_TAUTAN = ("katalog CKAN (ckan/package_search-pusdatinkom-01.json): untuk tahun ini hanya ada resource tautan "
           "'Jumlah Kejadian Bencana Tahun {t}' tanpa format dan tanpa DataStore; angka provinsi tidak diterbitkan sebagai tabel")
_NASIONAL = ("katalog CKAN: tahun ini hanya terbit di tabel nasional per jenis '... Akibat Bencana Tahun 2010-2024'; "
             "tabel provinsi hanya 2021, 2022 (rekap), 2024, 2025")
TIDAK_TERBIT = {}
for _s, _tahun in {"korban_hilang": range(2010, 2024), "korban_luka_sakit": range(2010, 2024),
                   "korban_mengungsi": range(2010, 2024), "korban_terdampak": range(2010, 2024)}.items():
    for _t in _tahun:
        if _t not in (2021, 2022):
            TIDAK_TERBIT[(_s, "provinsi", str(_t))] = _NASIONAL
for _s in ("korban_mengungsi", "korban_terdampak"):
    for _t in ("2021", "2022"):
        TIDAK_TERBIT[(_s, "provinsi", _t)] = ("rekap 2021/2022 hanya punya kolom gabungan 'Terdampak - Mengungsi' "
                                              "(seri korban_terdampak_mengungsi)")
for _s in ("korban_hilang", "korban_luka_sakit", "korban_mengungsi", "korban_terdampak"):
    TIDAK_TERBIT[(_s, "provinsi", "2023")] = _TAUTAN.format(t=2023)
TAHUN_TERBIT = {}

RENTANG = {"kejadian": (0, 100_000), "jiwa": (0, 300_000_000), "per_100000_penduduk": (0, 100_000), "persen": (0, 100)}

# Ambang anomali (K-004). Jumlah korban sangat menceng (beberapa kejadian besar mendominasi): IQR dihitung pada
# log(1 + nilai), sehingga provinsi besar tidak otomatis outlier dan nol tetap terdefinisi.
ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70, "skala": "log1p"}

PASANGAN = [
    dict(id="P1", judul="Mengungsi per 100.000: angka BNPB vs dihitung ulang dari pengungsi dan penduduk",
         utama="korban_mengungsi_per_100rb", rincian_utama="jenis_bencana=banjir",
         pembanding=[("korban_mengungsi", "jenis_bencana=banjir"), ("jumlah_penduduk", "total")],
         jenis="selisih", kategori="pembulatan atau penduduk berbeda; berkas pengungsi dan berkas per 100.000 terbit terpisah",
         alasan_rincian="banjir: jenis dengan pengungsi terbanyak 2025; jenis lain dihitung sama di Sprint 2",
         pertanyaan=[
             ("Penyebutnya apa?", "Kolom Jumlah Penduduk di berkas per 100.000 itu sendiri (Keterangan: publikasi BPS)."),
             ("Pembilangnya dari berkas mana?", "Tabel 'Jumlah Korban Mengungsi Akibat Bencana Menurut Provinsi 2025'; "
                                                "baris dan jenis yang sama."),
             ("Apa yang diharapkan?", "pengungsi / penduduk x 100.000 sama dengan angka terbit sampai pembulatan."),
         ]),
    dict(id="P2", judul="Meninggal dan hilang per 100.000: angka BNPB vs (meninggal + hilang) / penduduk",
         utama="korban_meninggal_hilang_per_100rb", rincian_utama="jenis_bencana=banjir",
         pembanding=[("korban_meninggal", "jenis_bencana=banjir"), ("korban_hilang", "jenis_bencana=banjir"),
                     ("jumlah_penduduk", "total")],
         jenis="selisih", kategori="pembulatan; pembilang dari dua berkas terpisah",
         alasan_rincian="banjir, sama dengan P1",
         pertanyaan=[
             ("Apakah pembilang = meninggal + hilang?", "Judul resource: 'Meninggal dan Hilang per 100.000 Orang'."),
             ("Apakah sama dengan indikator 13.1.1?", "Tidak sepenuhnya: 13.1.1 juga memasukkan terdampak langsung."),
         ]),
    dict(id="P3", judul="Kejadian banjir: baris INDONESIA vs jumlah 38 provinsi",
         utama="kejadian", rincian_utama="jenis_bencana=banjir", pembanding=[("kejadian", "jenis_bencana=banjir")],
         jenis="selisih", kategori="definisi penghitungan: kejadian lintas provinsi dihitung sekali secara nasional",
         alasan_rincian="baris INDONESIA di tabel per jenis dibandingkan dengan jumlah baris provinsi di berkas yang sama",
         pertanyaan=[
             ("Mengapa jumlah provinsi boleh lebih besar?", "Keterangan: kejadian yang berdampak lebih dari satu provinsi "
                                                            "dihitung satu kali secara nasional dan di setiap provinsi terdampak."),
             ("Bolehkah sebaliknya (jumlah provinsi < INDONESIA)?", "Tidak; bila terjadi, itu temuan yang dicatat."),
         ]),
    dict(id="P4", judul="Penduduk terdampak kekeringan, banjir, suhu ekstrem (WDI): konteks",
         utama="EN.CLC.MDAT.ZS", rincian_utama="total", pembanding=[("korban_terdampak", "jenis_bencana=banjir")],
         jenis="konteks", kategori="periode tidak beririsan: WDI rata-rata 1990–2009, BNPB 2010–2025",
         alasan_rincian="WDI tanpa rincian; BNPB banjir sebagai contoh jenis yang tercakup",
         pertanyaan=[
             ("Mengapa tidak dihitung selisihnya?", "WDI satu angka rata-rata 1990–2009 (name), tidak ada tahun yang sama."),
             ("Satuannya sama?", "Tidak: WDI persen penduduk, BNPB jiwa."),
         ]),
]

# ------------------------------------------------------------------ Sprint 2: Gold dan rekonsiliasi
# Keputusan Sprint 2 ditambahkan di bawah keputusan Sprint 1 (lihat log-keputusan.csv).

# Kategori baku setiap pasangan ditetapkan dari bukti Sprint 1 (pertanyaan keterbandingan di atas),
# tidak diturunkan dari teks.
KATEGORI_BAKU = {"P1": "metode berbeda", "P2": "metode berbeda", "P3": "definisi berbeda", "P4": "definisi berbeda"}

# P1/P2: angka per 100.000 yang diterbitkan dibandingkan dengan hitungan ulang dari jumlah korban dan jumlah penduduk.
_PER = dict(cara="per", skala=100000)
UBAH_PASANGAN = {
    "P1": dict(hitung_pembanding=dict(_PER, label="korban_mengungsi / jumlah_penduduk x 100.000",
                                      keterangan="pembanding = hitungan ulang dari pengungsi dan jumlah penduduk")),
    "P2": dict(hitung_pembanding=dict(_PER, label="(korban_meninggal + korban_hilang) / jumlah_penduduk x 100.000",
                                      keterangan="pembanding = hitungan ulang dari meninggal + hilang dan jumlah penduduk")),
    # P3: baris INDONESIA dibandingkan dengan jumlah baris provinsi di berkas yang sama.
    "P3": dict(pembanding_agregat=True),
}
GOLD_AGREGAT = {"kejadian": dict(rincian="jenis_bencana=banjir", berkas_sama=True,
                                 alasan="jumlah baris provinsi di tabel yang sama dengan baris INDONESIA")}
for _p in PASANGAN:
    _p["kategori_baku"] = KATEGORI_BAKU[_p["id"]]
    _p.update(UBAH_PASANGAN.get(_p["id"], {}))
