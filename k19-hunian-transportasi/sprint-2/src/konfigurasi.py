"""Keputusan wrangling Kasus 19 — Hunian dan transportasi.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri (moda transportasi
dari judul), satuan dan kode SDG beserta buktinya, rincian bongkar/muat, pergantian definisi, ambang
anomali, dan pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 19
SLUG = "hunian-transportasi"
JUDUL = "Hunian dan transportasi"

FORMAT_BPS = "json"

_ARUS = "rincian bongkar dan muat (turvar), tanpa jumlah; 2021–2025"
SERI = {
    "var1241": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga yang memiliki akses terhadap hunian yang layak",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="11.1.1(a)", katalog_sdg="11.1.1", bukti_sdg="var.label diawali '11.1.1.(a)'",
        cakupan="rumah tangga; Susenas; empat kriteria hunian layak sejak 2019 (var.note)", koreksi="kode SDG 11.1.1 -> 11.1.1(a)",
    ),
    "var2012": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga dengan akses nyaman (jarak 0,5 km) ke transportasi umum",
        satuan="persen", katalog_satuan="tidak_ada", bukti_satuan="judul 'Persentase rumah tangga'; var.unit kosong",
        sdg="11.2.1(a)", katalog_sdg="11.2.1", bukti_sdg="nama berkas sdg11_11_2_1_a_v2012: butir nasional (a)",
        cakupan="Susenas Modul Ketahanan Sosial; hanya 2017 dan 2020", koreksi="satuan tidak_ada -> persen; kode SDG -> 11.2.1(a)",
    ),
    "var2013": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase penduduk 10 tahun ke atas yang menggunakan kendaraan bermotor umum dengan rute tertentu",
        satuan="persen", katalog_satuan="tidak_ada", bukti_satuan="judul 'Persentase penduduk'; var.unit kosong",
        sdg="11.2.1(b)", katalog_sdg="11.2.1", bukti_sdg="nama berkas sdg11_11_2_1_b_v2013: butir nasional (b)",
        cakupan="penduduk 10+; Susenas Modul Ketahanan Sosial; hanya 2017 dan 2020", koreksi="satuan tidak_ada -> persen; kode SDG -> 11.2.1(b)",
    ),
    "var2753": dict(
        sumber="bps", tingkat="provinsi", nama="Jumlah bongkar muat barang moda transportasi kapal",
        satuan="kilogram", katalog_satuan="kilogram", bukti_satuan="var.unit: 'KG'",
        sdg="9.1.2", katalog_sdg="9.1.2", bukti_sdg="var.label diawali '9.1.2*'; moda kapal dari judul", cakupan=_ARUS,
    ),
    "var2754": dict(
        sumber="bps", tingkat="provinsi", nama="Jumlah bongkar muat barang moda transportasi pesawat terbang",
        satuan="kilogram", katalog_satuan="kilogram", bukti_satuan="var.unit: 'KG'",
        sdg="9.1.2", katalog_sdg="9.1.2", bukti_sdg="var.label diawali '9.1.2*.'; moda pesawat dari judul", cakupan=_ARUS,
    ),
    "EN.POP.SLUM.UR.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Population living in slums (% of urban population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of urban population)'",
        sdg="11.1.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="penduduk perkotaan; arah berlawanan dengan hunian layak; UN-Habitat", koreksi="kode SDG kosong -> 11.1.1",
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_BPS = {s: ("arus", {"Bongkar": "bongkar", "Muat": "muat"}) for s in ("var2753", "var2754")}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"arus": {"bongkar", "muat"}}

DERET = {s: ["arus=bongkar", "arus=muat"] for s in ("var2753", "var2754")}

RUJUKAN_TAHUN = {}
# K-005: provinsi yang tidak pernah ada di statistik bongkar muat kapal (2021–2025)
TIDAK_TERBIT = {("var2753", 3400, str(th)): "DI Yogyakarta tidak ada di kelima tahun statistik kapal (dugaan: tanpa pelabuhan yang dicakup)"
                for th in range(2021, 2026)}
TIDAK_TERBIT |= {("var2753", 9700, str(th)): "Papua Pegunungan tidak berbatasan laut; tidak ada di statistik kapal sejak terbentuk"
                 for th in range(2023, 2026)}
TAHUN_TERBIT = {}
PATAHAN_DEFINISI = {"var1241": {"2019": "var.note: sejak 2019 hunian layak memakai empat kriteria (luas per kapita >= 7,2 m2, "
                                        "air minum layak, sanitasi layak, ketahanan bangunan)"}}

RENTANG = {"persen": (0, 100), "kilogram": (0, 1e13)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Hunian layak (BPS, rumah tangga) vs penduduk kumuh perkotaan (WDI): konteks",
         utama="var1241", rincian_utama="total", pembanding=[("EN.POP.SLUM.UR.ZS", "total")],
         jenis="konteks", kategori="definisi berbeda: arah berlawanan dan populasi berbeda; dibandingkan arah perubahannya",
         alasan_rincian="tanpa rincian",
         pertanyaan=[("Arah?", "Hunian layak naik = baik; penduduk kumuh naik = buruk."),
                     ("Populasi?", "BPS semua rumah tangga; WDI penduduk perkotaan.")]),
    dict(id="P2", judul="Bongkar muat kapal vs pesawat (BPS): jumlah provinsi vs Indonesia",
         utama="var2753", rincian_utama="arus=bongkar", pembanding=[("var2754", "arus=bongkar")],
         jenis="konteks", kategori="moda berbeda; rekonsiliasi internal: jumlah provinsi vs baris Indonesia di Gold",
         alasan_rincian="arus bongkar; muat diperlakukan sama",
         pertanyaan=[("Moda?", "var2753 kapal, var2754 pesawat terbang (judul JSON)."),
                     ("Cakupan wilayah?", "Kapal dan pesawat tidak memuat provinsi yang sama; lihat grid.")]),
]

# ------------------------------------------------------------------ Sprint 2: Gold dan rekonsiliasi
# Keputusan Sprint 2 ditambahkan di bawah keputusan Sprint 1 (lihat log-keputusan.csv).

# Kategori baku setiap pasangan ditetapkan dari bukti Sprint 1 (pertanyaan keterbandingan di atas),
# tidak diturunkan dari teks.
KATEGORI_BAKU = {"P1": "definisi berbeda", "P2": "definisi berbeda"}

for _p in PASANGAN:
    _p["kategori_baku"] = KATEGORI_BAKU[_p["id"]]
