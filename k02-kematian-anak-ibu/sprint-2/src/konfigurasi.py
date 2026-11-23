"""Keputusan wrangling Kasus 02 — Kematian anak dan ibu.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, cara menulis rincian, jendela rujukan survei, sel yang dinyatakan tidak terbit,
ambang anomali, dan pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 2
SLUG = "kematian-anak-ibu"
JUDUL = "Kematian anak dan ibu"

# K-002: JSON dipakai sebagai sumber Silver BPS (CSV identik nilainya, JSON membawa judul, satuan, catatan).
FORMAT_BPS = "json"

SERI = {
    "var1373": dict(
        sumber="bps", tingkat="provinsi",
        nama="Angka Kematian Balita (AKBa) per 1.000 kelahiran hidup",
        satuan="per_1000_kh", katalog_satuan="tidak_ada",
        bukti_satuan="var.label: 'Angka Kematian Balita Per 1000 Kelahiran Hidup'; var.unit kosong; CSV kolom satuan kosong",
        sdg="3.2.1", katalog_sdg="3.2.1",
        bukti_sdg="judul = kematian balita, sama dengan indikator global 3.2.1 (under-5 mortality)",
        cakupan="kematian sebelum umur 5 tahun; sumber SDKI; nasional rujukan 5 tahun, provinsi 10 tahun sebelum survei",
        koreksi="satuan tidak_ada -> per_1000_kh",
    ),
    "var1584": dict(
        sumber="bps", tingkat="provinsi",
        nama="Angka Kematian Bayi (AKB) per 1.000 kelahiran hidup",
        satuan="per_1000_kh", katalog_satuan="tidak_ada",
        bukti_satuan="var.label: 'Angka Kematian Bayi (AKB) Per 1000 Kelahiran Hidup'; var.unit kosong",
        sdg="3.2.1(b)", katalog_sdg="3.2.1",
        bukti_sdg="indikator global 3.2.1 hanya kematian balita; AKB adalah butir (b) 3.2.1 di metadata TPB nasional",
        cakupan="kematian sebelum umur 1 tahun; sumber SDKI; nasional rujukan 5 tahun, provinsi 10 tahun sebelum survei",
        koreksi="satuan tidak_ada -> per_1000_kh; kode SDG 3.2.1 -> 3.2.1(b) (bukan indikator global 3.2.1)",
    ),
    "var1541": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase perempuan pernah kawin 15–49 tahun yang kelahiran terakhirnya di fasilitas kesehatan, 40% pengeluaran terbawah",
        satuan="persen", katalog_satuan="persen",
        bukti_satuan="var.unit: 'Persen'",
        sdg="3.1.2(b)", katalog_sdg="3.1.2",
        bukti_sdg="indikator global 3.1.2 = persalinan ditolong tenaga kesehatan terlatih; judul var1541 = persalinan di "
                  "fasilitas kesehatan untuk 40% terbawah, yaitu butir (b) 3.1.2 nasional dengan disagregasi kelompok pengeluaran",
        cakupan="perempuan pernah kawin 15–49, kelahiran terakhir, kelompok 40% pengeluaran terbawah",
        koreksi="kode SDG 3.1.2 -> 3.1.2(b); bukan ukuran yang sama dengan indikator global 3.1.2",
    ),
    "SH.DYN.MORT": dict(
        sumber="wdi", tingkat="nasional", nama="Mortality rate, under-5 (per 1,000 live births)",
        satuan="per_1000_kh", katalog_satuan="—", bukti_satuan="name: '(per 1,000 live births)'",
        sdg="3.2.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json (Sustainable Development Goals)",
        cakupan="estimasi model UN IGME, tahunan", koreksi="kode SDG kosong -> 3.2.1",
    ),
    "SH.STA.MMRT": dict(
        sumber="wdi", tingkat="nasional", nama="Maternal mortality ratio (modeled estimate, per 100,000 live births)",
        satuan="per_100000_kh", katalog_satuan="—", bukti_satuan="name: '(modeled estimate, per 100,000 live births)'",
        sdg="3.1.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="estimasi model regresi (sourceNote)", koreksi="kode SDG kosong -> 3.1.1",
    ),
    "SH.STA.BRTC.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Births attended by skilled health staff (% of total)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of total)'",
        sdg="3.1.2", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="semua persalinan, ditolong tenaga kesehatan terlatih; dari survei (DHS dsb.), banyak tahun kosong",
        koreksi="kode SDG kosong -> 3.1.2",
    ),
    "MDG_0000000007": dict(
        sumber="who_gho", tingkat="nasional", nama="Under-five mortality rate (probability of dying by age 5 per 1000 live births)",
        satuan="per_1000_kh", katalog_satuan="—", bukti_satuan="kolom RATE_PER_1000_N",
        sdg="3.2.1", katalog_sdg="3.2.1", bukti_sdg="metadata WHO", cakupan="estimasi UN IGME, tahunan",
    ),
    "MDG_0000000026": dict(
        sumber="who_gho", tingkat="nasional", nama="Maternal mortality ratio (per 100 000 live births)",
        satuan="per_100000_kh", katalog_satuan="—", bukti_satuan="kolom RATE_PER_100000_N",
        sdg="3.1.1", katalog_sdg="3.1.1", bukti_sdg="metadata WHO", cakupan="estimasi model MMEIG, tahunan",
    ),
    "WHOSIS_000003": dict(
        sumber="who_gho", tingkat="nasional", nama="Neonatal mortality rate (per 1000 live births)",
        satuan="per_1000_kh", katalog_satuan="—", bukti_satuan="kolom RATE_PER_1000_N",
        sdg="3.2.2", katalog_sdg="3.2.2", bukti_sdg="metadata WHO", cakupan="kematian 0–27 hari, estimasi UN IGME",
        koreksi="IND_NAME di CSV tertulis 'Mortality rate (neonetal)'; nama baku dari odata/Indicator.json",
    ),
}

# Rincian (K-006)
RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {"DIM_SEX": "jenis_kelamin", "DIM_AGE": "umur", "DIM_POP_WEALTH_QUINTILE": "kuintil"}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"jenis_kelamin": {"FEMALE", "MALE"}, "kuintil": {"WQ1", "WQ2", "WQ3", "WQ4", "WQ5"}, "umur": None}

# Jendela rujukan survei (K-008), dari var.note: nasional 5 tahun, provinsi 10 tahun sebelum survei.
RUJUKAN_TAHUN = {("var1373", "nasional"): 5, ("var1373", "provinsi"): 10,
                 ("var1584", "nasional"): 5, ("var1584", "provinsi"): 10}

# Sel grid yang dinyatakan tidak ada oleh penerbit (K-005)
TIDAK_TERBIT = {
    ("var1373", "provinsi", "2017"): "var.note var1373: 'Angka provinsi tahun 2017 tidak ada'",
    ("var1584", "provinsi", "2017"): "var.note var1584: 'AKB untuk provinsi tahun 2017 tidak ada'",
}
TAHUN_TERBIT = {"var1373": {"2012", "2017"}, "var1584": {"2012", "2017"}, "var1541": {"2015", "2016", "2017", "2018", "2019"}}

# Rentang sah per satuan (galat input dan validasi)
RENTANG = {"persen": (0, 100), "per_1000_kh": (0, 1000), "per_100000_kh": (0, 100000)}

# Ambang anomali (K-004): IQR lebih tahan terhadap satu nilai ekstrem daripada z-score pada ±33 provinsi.
# Arah ke samping hanya bila satu provinsi punya >= 6 periode; dengan 5 titik, IQR per provinsi tidak stabil.
ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Kematian balita: titik survei BPS vs estimasi tahunan WHO dan WDI",
         utama="var1373", rincian_utama="total", pembanding=[("MDG_0000000007", "total"), ("SH.DYN.MORT", "total")],
         jenis="selisih", kategori="metode dan definisi periode (survei dengan rujukan 5 tahun vs estimasi model tahunan)",
         alasan_rincian="WHO rincian total (jenis kelamin dan kuintil TOTAL); BPS baris Indonesia",
         pertanyaan=[
             ("Seri BPS mana yang balita?", "var1373: var.label 'Angka Kematian Balita'."),
             ("Periode apa yang diwakili angka BPS?", "Angka Indonesia merujuk 5 tahun sebelum survei (var.note); WHO/WDI satu tahun kalender."),
             ("Dari mana estimasi WHO/WDI?", "Keduanya UN IGME (sourceOrganization WDI), dibuat dengan model dari banyak survei."),
         ]),
    dict(id="P2", judul="Kematian bayi BPS dan pembanding yang tersedia",
         utama="var1584", rincian_utama="total", pembanding=[],
         jenis="konteks", kategori="definisi berbeda: tidak ada seri kematian bayi (0–11 bulan) di paket pembanding",
         alasan_rincian="WHOSIS_000003 = neonatal 0–27 hari, MDG_0000000007 = balita; keduanya bukan bayi",
         pertanyaan=[
             ("Seri BPS mana yang bayi?", "var1584: var.label 'Angka Kematian Bayi (AKB)'."),
             ("Apakah WHOSIS_000003 setara?", "Tidak: neonatal (0–27 hari) adalah sebagian dari kematian bayi. Dipakai sebagai konteks."),
         ]),
    dict(id="P3", judul="Persalinan: di fasilitas (BPS, 40% terbawah) vs ditolong tenaga kesehatan (WDI, semua)",
         utama="var1541", rincian_utama="total", pembanding=[("SH.STA.BRTC.ZS", "total")],
         jenis="konteks", kategori="definisi dan cakupan berbeda; tidak dihitung sebagai selisih",
         alasan_rincian="tidak ada rincian yang menyamakan keduanya di paket",
         pertanyaan=[
             ("Apa yang diukur var1541?", "Kelahiran terakhir di fasilitas kesehatan (bukan ditolong tenaga kesehatan)."),
             ("Siapa yang dihitung?", "Perempuan pernah kawin 15–49 pada 40% pengeluaran terbawah; WDI: semua persalinan."),
         ]),
    dict(id="P4", judul="Kematian balita: WHO vs WDI (dua rilis estimasi yang sama)",
         utama="MDG_0000000007", rincian_utama="total", pembanding=[("SH.DYN.MORT", "total")],
         jenis="selisih", kategori="vintage (rilis estimasi UN IGME berbeda)",
         alasan_rincian="rincian total keduanya",
         pertanyaan=[("Apakah sumbernya sama?", "Ya, UN IGME; selisih menunjukkan perbedaan waktu rilis, diuji lagi di Sprint 3 dengan arsip WDI.")]),
    dict(id="P5", judul="Rasio kematian ibu: WHO vs WDI (konteks nasional)",
         utama="MDG_0000000026", rincian_utama="total", pembanding=[("SH.STA.MMRT", "total")],
         jenis="selisih", kategori="vintage; tidak ada padanan BPS di paket",
         alasan_rincian="rincian total keduanya",
         pertanyaan=[("Apakah ada padanan BPS?", "Tidak di paket ini; seri ini masuk Gold sebagai konteks nasional.")]),
]

# ------------------------------------------------------------------ Sprint 2: Gold dan rekonsiliasi
# Keputusan Sprint 2 ditambahkan di bawah keputusan Sprint 1 (lihat log K-016 dst.).

# K-016: kategori baku setiap pasangan ditetapkan dari bukti Sprint 1, tidak diturunkan dari teks.
KATEGORI_BAKU = {"P1": "metode berbeda", "P2": "definisi berbeda", "P3": "definisi berbeda",
                 "P4": "vintage berbeda", "P5": "vintage berbeda"}
for _p in PASANGAN:
    _p["kategori_baku"] = KATEGORI_BAKU[_p["id"]]

# K-017: angka Indonesia var1373 merujuk 5 tahun sebelum survei (K-008), sedangkan WHO/WDI satu tahun kalender.
# Pasangan P1J membandingkan angka survei dengan rata-rata 5 tahun pembanding sebelum tahun survei, supaya
# selisih yang tersisa tidak lagi berasal dari beda periode rujukan.
PASANGAN.append(dict(
    PASANGAN[0], id="P1J", judul="Kematian balita: BPS vs rata-rata WHO/WDI pada jendela rujukan 5 tahun",
    jendela_pembanding=5, kategori_baku="metode berbeda",
    kategori="metode (survei SDKI vs estimasi model UN IGME); periode rujukan sudah disamakan dengan merata-ratakan "
             "pembanding pada 5 tahun sebelum survei",
    pertanyaan=[("Mengapa dirata-rata?", "var.note: angka Indonesia merujuk 5 tahun sebelum survei (K-008)."),
                ("Tahun mana yang dirata-rata?", "t−5 sampai t−1 untuk survei tahun t (2007–2011 untuk 2012).")]))
