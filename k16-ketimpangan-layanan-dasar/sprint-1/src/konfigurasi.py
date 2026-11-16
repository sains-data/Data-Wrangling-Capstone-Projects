"""Keputusan wrangling Kasus 16 — Ketimpangan dan layanan dasar.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, sel yang tidak ditampilkan karena RSE tinggi, rincian layanan dasar, status dan
proyeksi ILO, ambang anomali, dan pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 16
SLUG = "ketimpangan-layanan-dasar"
JUDUL = "Ketimpangan dan layanan dasar"

FORMAT_BPS = "json"

_MODEL = "ILO modelled estimates (SOURCE); kode OBS_STATUS A, R, M tidak dijelaskan di paket"
SERI = {
    "var2011": dict(
        sumber="bps", tingkat="provinsi", nama="Proporsi penduduk yang hidup di bawah 50 persen dari median pendapatan",
        satuan="persen", katalog_satuan="tidak_ada", bukti_satuan="judul 'Proporsi penduduk'; var.unit kosong; nilai 0–30",
        sdg="10.2.1", katalog_sdg="10.2.1", bukti_sdg="judul = indikator 10.2.1",
        cakupan="Susenas; 2018–2023; provinsi dengan RSE terlalu tinggi tidak ditampilkan (var.note); judul menyebut pendapatan",
        koreksi="satuan tidak_ada -> persen",
    ),
    "var2016": dict(
        sumber="bps", tingkat="provinsi", nama="Proporsi rumah tangga dengan akses terhadap pelayanan dasar",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="1.4.1", katalog_sdg="1.4.1", bukti_sdg="judul = akses layanan dasar, indikator 1.4.1",
        cakupan="rumah tangga; turvar menyebut empat layanan, tetapi hanya air minum, sanitasi, dan fasilitas kesehatan yang berisi "
                "angka (mobilitas kosong); tanpa total; 2019–2023",
    ),
    "var1254": dict(
        sumber="bps", tingkat="provinsi", nama="Total pendapatan pemerintah sebagai proporsi terhadap PDB",
        satuan="persen", katalog_satuan="tidak_ada", bukti_satuan="judul 'sebagai proporsi terhadap PDB'; var.unit kosong",
        sdg="17.1.1", katalog_sdg="17.1.1", bukti_sdg="judul = indikator 17.1.1",
        cakupan="hanya 2015 dan 2016; judul menyebut 'menurut sumbernya' tetapi berkas tanpa rincian sumber",
        koreksi="satuan tidak_ada -> persen",
    ),
    "SI.DST.50MD": dict(
        sumber="wdi", tingkat="nasional", nama="Proportion of people living below 50 percent of median income (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(%)'",
        sdg="10.2.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="pendapatan atau konsumsi per kapita (sourceNote); median diukur dalam PPP 2021; Bank Dunia PIP",
        koreksi="kode SDG kosong -> 10.2.1",
    ),
    "SI.POV.DDAY": dict(
        sumber="wdi", tingkat="nasional", nama="Poverty headcount ratio at $3.00 a day (2021 PPP) (% of population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of population)'",
        sdg="1.1.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="seluruh penduduk; garis US$3 per hari PPP 2021", koreksi="kode SDG kosong -> 1.1.1",
    ),
    "SDG_0111_SEX_AGE_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Working poverty rate by sex and age (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT", sdg="1.1.1", katalog_sdg="1.1.1",
        bukti_sdg="nama dataflow 'SDG indicator 1.1.1'",
        cakupan="pekerja (bukan seluruh penduduk); garis US$3 per hari PPP (deskripsi dataflow); " + _MODEL,
    ),
    "SDG_0131_SEX_SOC_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Proportion of population covered by social protection floors/systems (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT", sdg="1.3.1", katalog_sdg="1.3.1",
        bukti_sdg="nama dataflow 'SDG indicator 1.3.1'", cakupan="rincian fungsi perlindungan sosial; tahun tidak berurutan",
    ),
    "SDG_1041_NOC_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Labour income share as a percent of GDP (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT", sdg="10.4.1", katalog_sdg="10.4.1",
        bukti_sdg="nama dataflow 'SDG indicator 10.4.1'", cakupan="2004–2026; 2026 proyeksi; " + _MODEL,
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
LAYANAN = {"Akses pada layanan air minum": "air_minum", "Akses pada layanan sanitasi dasar": "sanitasi",
           "Akses pada mobilitas dasar": "mobilitas", "Akses pada fasilitas kesehatan dasar": "kesehatan"}
RINCIAN_BPS = {"var2016": ("layanan", LAYANAN)}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"layanan": set(LAYANAN.values()), "jenis_kelamin": {"MALE", "FEMALE"}, "umur": None, "perlindungan_sosial": None}

# K-006: label mobilitas ada di turvar tetapi berkas tidak memuat satu pun angkanya; tiga layanan diprofilkan
DERET = {"var2016": ["layanan=air_minum", "layanan=sanitasi", "layanan=kesehatan"]}

RUJUKAN_TAHUN = {}
# K-005: var.note var2011: provinsi dengan RSE terlalu tinggi tidak ditampilkan
TIDAK_TERBIT = {("var2011", "provinsi", str(t)): "var.note: data beberapa provinsi tidak ditampilkan karena RSE hasil estimasi "
                                                 "terlalu tinggi" for t in range(2018, 2024)}
TAHUN_TERBIT = {}

PROYEKSI = {"SDG_1041_NOC_RT": {"2026"}}
TAHUN_UNDUH = 2026
STATUS_ILO = {"A", "R", "M"}

RENTANG = {"persen": (0, 100)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Di bawah 50% median: BPS vs WDI",
         utama="var2011", rincian_utama="total", pembanding=[("SI.DST.50MD", "total")],
         jenis="selisih", kategori="definisi dan metode: BPS menyebut pendapatan; WDI pendapatan atau konsumsi per kapita dengan median PPP",
         alasan_rincian="tanpa rincian",
         pertanyaan=[("Pendapatan atau pengeluaran?", "Judul BPS menyebut pendapatan; sourceNote WDI menyebut pendapatan atau konsumsi. "
                      "Untuk Indonesia keduanya perlu dipastikan dari dokumentasi Susenas dan PIP di Sprint 2.")]),
    dict(id="P2", judul="Kemiskinan pekerja (ILO) vs kemiskinan ekstrem penduduk (WDI)",
         utama="SDG_0111_SEX_AGE_RT", rincian_utama="total", pembanding=[("SI.POV.DDAY", "total")],
         jenis="selisih", kategori="populasi berbeda (pekerja vs seluruh penduduk); garis kemiskinan sama (US$3 PPP 2021)",
         alasan_rincian="ILO total jenis kelamin dan umur 15+",
         pertanyaan=[("Garis kemiskinannya?", "Keduanya US$3 per hari PPP (deskripsi dataflow ILO, name WDI)."),
                     ("Populasinya?", "ILO: orang bekerja; WDI: seluruh penduduk.")]),
    dict(id="P3", judul="Layanan dasar, pendapatan pemerintah (BPS) dan perlindungan sosial, porsi upah (ILO): konteks",
         utama="var2016", rincian_utama="layanan=air_minum", pembanding=[],
         jenis="konteks", kategori="tidak ada padanan langsung di paket", alasan_rincian="layanan air minum sebagai contoh",
         pertanyaan=[("Ada padanan?", "Tidak; SDG_0131 dan SDG_1041 dipakai sebagai konteks nasional.")]),
]
