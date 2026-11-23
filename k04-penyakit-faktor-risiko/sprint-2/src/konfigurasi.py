"""Keputusan wrangling Kasus 04 — Penyakit dan faktor risiko.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, sel yang dinyatakan tidak terbit, tahun proyeksi, ambang anomali, dan pasangan
rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 4
SLUG = "penyakit-faktor-risiko"
JUDUL = "Penyakit dan faktor risiko"

FORMAT_BPS = "json"

SERI = {
    "var1393": dict(
        sumber="bps", tingkat="provinsi",
        nama="Kejadian malaria per 1.000 penduduk",
        satuan="per_1000_penduduk", katalog_satuan="tidak_ada",
        bukti_satuan="var.label: 'Kejadian Malaria Per 1000 Orang'; var.unit, kolom satuan CSV, dan satuan di manifest_asal kosong",
        sdg="3.3.3", katalog_sdg="3.3.3",
        bukti_sdg="judul = kejadian malaria per 1.000, indikator 3.3.3",
        cakupan="kasus yang dilaporkan; sumber Kementerian Kesehatan, Profil Kesehatan Indonesia (var.note); "
                "penyebut seluruh penduduk ('per 1000 orang'), tahunan 2010–2021",
        koreksi="satuan tidak_ada -> per_1000_penduduk",
    ),
    "var1480": dict(
        sumber="bps", tingkat="provinsi",
        nama="Prevalensi tekanan darah tinggi (hasil pengukuran)",
        satuan="persen", katalog_satuan="tidak_ada",
        bukti_satuan="var.label: 'Prevalensi ...'; var.unit kosong; besaran angka 20–40 sesuai persen penduduk",
        sdg="3.4.1(b)", katalog_sdg="3.4.1",
        bukti_sdg="nama tabel BPS 'sdg3_3_4_1_b_v1480' (manifest_asal.json): butir (b) 3.4.1 nasional; indikator global "
                  "3.4.1 adalah kematian akibat penyakit tidak menular (NCDMORT3070), bukan prevalensi",
        cakupan="survei: Riskesdas 2007 dan 2013, Sirkesnas 2016 (hanya Indonesia), Susenas+Riskesdas 2018 (var.note)",
        koreksi="satuan tidak_ada -> persen; kode SDG 3.4.1 -> 3.4.1(b)",
    ),
    "var1435": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase penduduk umur 15 tahun ke atas yang merokok tembakau selama sebulan terakhir",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="3.a.1", katalog_sdg="3.a.1",
        bukti_sdg="judul TPB nasional 3.a.1; ukuran kasar (tidak distandarkan umur), hanya rokok",
        cakupan="penduduk 15+; Susenas Maret; var.def: data sebelum 2015 tidak tersedia (variabel belum dikumpulkan)",
    ),
    "SH.MLR.INCD.P3": dict(
        sumber="wdi", tingkat="nasional", nama="Incidence of malaria (per 1,000 population at risk)",
        satuan="per_1000_penduduk_berisiko", katalog_satuan="—", bukti_satuan="name: '(per 1,000 population at risk)'",
        sdg="3.3.3", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="estimasi WHO (sourceOrganization: Global Health Observatory)", koreksi="kode SDG kosong -> 3.3.3",
    ),
    "MALARIA_EST_INCIDENCE": dict(
        sumber="who_gho", tingkat="nasional", nama="Estimated malaria incidence (per 1000 population at risk)",
        satuan="per_1000_penduduk_berisiko", katalog_satuan="—",
        bukti_satuan="kolom RATE_PER_1000_N; Denominator: 'Population living in areas where malaria transmission occurs'",
        sdg="3.3.3", katalog_sdg="3.3.3", bukti_sdg="metadata WHO",
        cakupan="estimasi model; penyebut penduduk di daerah penularan", koreksi="IND_NAME 'Malaria cases' tidak menyebut estimasi dan penyebut",
    ),
    "NCDMORT3070": dict(
        sumber="who_gho", tingkat="nasional", nama="Probability of dying between age 30 and 70 from any of CVD, cancer, diabetes, or CRD (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="kolom RATE_PER_100_N; UnitOfMeasure: percentage of 30-year-old people",
        sdg="3.4.1", katalog_sdg="3.4.1", bukti_sdg="metadata WHO",
        cakupan="umur 30–69 (DIM_AGE tunggal); estimasi WHO Global Health Estimates",
    ),
    "M_Est_tob_curr_std": dict(
        sumber="who_gho", tingkat="nasional", nama="Age-standardized prevalence of current tobacco use, 15+ (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="kolom PERCENT_POP_N",
        sdg="3.a.1", katalog_sdg="3.a.1", bukti_sdg="metadata WHO",
        cakupan="penduduk 15+; semua produk tembakau (diisap dan tidak diisap); distandarkan umur; model Bayesian; "
                "2025 dan 2030 proyeksi",
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {"DIM_SEX": "jenis_kelamin", "DIM_AGE": "umur"}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"jenis_kelamin": {"FEMALE", "MALE"}, "umur": None}

RUJUKAN_TAHUN = {}

# K-005: 2016 hanya baris Indonesia (Sirkesnas); tidak ada satu pun provinsi di JSON.
TIDAK_TERBIT = {("var1480", "provinsi", "2016"): "JSON var1480 tahun 2016 hanya memuat baris Indonesia (0 dari 34 provinsi); "
                                                   "var.note: sumber 2016 Sirkesnas, berbeda dari Riskesdas"}
TAHUN_TERBIT = {"var1393": {str(t) for t in range(2010, 2022)}, "var1480": {"2007", "2013", "2016", "2018"},
                "var1435": {str(t) for t in range(2015, 2026)}}

# K-010: tahun proyeksi WHO (bukan estimasi atas data survei); tidak ikut rekonsiliasi.
PROYEKSI = {"M_Est_tob_curr_std": {"2025", "2030"}}
TAHUN_UNDUH = 2026

RENTANG = {"persen": (0, 100), "per_1000_penduduk": (0, 1000), "per_1000_penduduk_berisiko": (0, 1000)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Malaria: kasus dilaporkan per 1.000 penduduk (BPS) vs estimasi per 1.000 penduduk berisiko (WHO, WDI)",
         utama="var1393", rincian_utama="total", pembanding=[("MALARIA_EST_INCIDENCE", "total"), ("SH.MLR.INCD.P3", "total")],
         jenis="selisih", kategori="definisi (penyebut: seluruh penduduk vs penduduk di daerah penularan) dan metode (dilaporkan vs estimasi)",
         alasan_rincian="tanpa rincian di ketiganya",
         pertanyaan=[
             ("Penyebut WHO?", "Penduduk di daerah penularan malaria (Denominator), bukan seluruh penduduk."),
             ("Penyebut BPS?", "'Per 1000 Orang' (judul), seluruh penduduk; angka dari laporan Kemenkes."),
             ("WHO vs WDI?", "WDI meneruskan WHO GHO (sourceOrganization); selisih keduanya vintage."),
         ]),
    dict(id="P2", judul="Merokok (BPS, kasar, rokok) vs penggunaan tembakau (WHO, distandarkan umur)",
         utama="var1435", rincian_utama="total", pembanding=[("M_Est_tob_curr_std", "total")],
         jenis="selisih", kategori="definisi (produk tembakau, standardisasi umur) dan metode (survei vs model); proyeksi dikeluarkan",
         alasan_rincian="WHO rincian total jenis kelamin",
         pertanyaan=[
             ("Apa yang dihitung WHO?", "Semua produk tembakau, harian atau tidak, distandarkan umur (DefinitionText, kode _std)."),
             ("Tahun mana yang sah?", "2025 dan 2030 proyeksi; hanya tahun estimasi yang beririsan dengan BPS yang dibandingkan."),
         ]),
    dict(id="P3", judul="Hipertensi (BPS) vs kematian PTM 30–70 (WHO): konteks",
         utama="var1480", rincian_utama="total", pembanding=[("NCDMORT3070", "total")],
         jenis="konteks", kategori="definisi berbeda: prevalensi faktor risiko vs probabilitas kematian",
         alasan_rincian="WHO rincian total jenis kelamin",
         pertanyaan=[("Kode SDG sama?", "Di katalog ya (3.4.1), tetapi var1480 adalah butir nasional 3.4.1(b).")]),
    dict(id="P4", judul="Malaria WHO vs WDI (estimasi yang sama, rilis berbeda)",
         utama="MALARIA_EST_INCIDENCE", rincian_utama="total", pembanding=[("SH.MLR.INCD.P3", "total")],
         jenis="selisih", kategori="vintage",
         alasan_rincian="tanpa rincian",
         pertanyaan=[("Sumbernya sama?", "Ya, WDI mengutip WHO GHO; diuji lagi di Sprint 3 dengan arsip WDI.")]),
]

# ------------------------------------------------------------------ Sprint 2: Gold dan rekonsiliasi
# Keputusan Sprint 2 ditambahkan di bawah keputusan Sprint 1 (lihat log-keputusan.csv).

# Kategori baku setiap pasangan ditetapkan dari bukti Sprint 1 (pertanyaan keterbandingan di atas),
# tidak diturunkan dari teks.
KATEGORI_BAKU = {"P1": "definisi berbeda", "P2": "definisi berbeda", "P3": "definisi berbeda", "P4": "vintage berbeda"}

# P1: penyebut berbeda (seluruh penduduk vs penduduk di daerah penularan), skala sama (per 1.000). Selisih tetap dihitung
# supaya besarnya beda definisi terlihat; kategorinya definisi berbeda, bukan galat.
GOLD_KONVERSI = {("per_1000_penduduk_berisiko", "per_1000_penduduk"): 1.0}
for _p in PASANGAN:
    _p["kategori_baku"] = KATEGORI_BAKU[_p["id"]]
