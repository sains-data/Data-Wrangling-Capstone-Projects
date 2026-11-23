"""Keputusan wrangling Kasus 13 — Pemuda dan pekerja anak.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri (dua definisi ILO
pekerja anak), kelompok umur, satuan dan kode SDG beserta buktinya, status ILO, ambang anomali, dan
pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 13
SLUG = "pemuda-pekerja-anak"
JUDUL = "Pemuda dan pekerja anak"

FORMAT_BPS = "json"

SERI = {
    "var1186": dict(
        sumber="bps", tingkat="provinsi", nama="Persentase usia muda (15–24 tahun) yang tidak sekolah, bekerja, atau mengikuti pelatihan (NEET)",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="8.6.1", katalog_sdg="8.6.1", bukti_sdg="NEET 15–24 = indikator 8.6.1", cakupan="umur 15–24; Sakernas; 2015–2025",
    ),
    "var2658": dict(
        sumber="bps", tingkat="provinsi", nama="Persentase pekerja anak usia 5–17 tahun sesuai metadata SDGs global",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen' (judul menyebut 'Persentase dan Jumlah', berkas hanya persentase)",
        sdg="8.7.1", katalog_sdg="8.7.1", bukti_sdg="var.label diawali '8.7.1*'",
        cakupan="umur 5–17; 2020–2025; DKI dan DIY tidak ada 2024–2025",
    ),
    "SL.UEM.NEET.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Share of youth not in education, employment or training, total (% of youth population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of youth population)'",
        sdg="8.6.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="ILO Labour Force Statistics; kelompok umur pemuda", koreksi="kode SDG kosong -> 8.6.1",
    ),
    "SL.TLF.0714.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Children in employment, total (% of children ages 7-14)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of children ages 7-14)'",
        sdg="8.7.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="umur 7–14; bekerja minimal satu jam seminggu; 2000–2010", koreksi="kode SDG kosong -> 8.7.1",
    ),
    "SDG_0861_SEX_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Proportion of youth aged 15 to 24 years not in education, employment or training (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT", sdg="8.6.1", katalog_sdg="8.6.1",
        bukti_sdg="nama DSD 'SDG indicator 8.6.1'", cakupan="umur 15–24; rincian jenis kelamin; OBS_STATUS B = patahan",
    ),
    "SDG_A871_SEX_AGE_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Proportion of children engaged in economic activity (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT", sdg="8.7.1", katalog_sdg="8.7.1",
        bukti_sdg="nama DSD 'SDG indicator 8.7.1'",
        cakupan="kegiatan ekonomi saja; berkas hanya umur 15–17 (AGE_CLDVERSION_Y15-17); 2009 (survei pekerja anak), 2019, 2023 (Sakernas)",
    ),
    "SDG_B871_SEX_AGE_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Proportion of children engaged in economic activity and household chores (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT", sdg="8.7.1", katalog_sdg="8.7.1",
        bukti_sdg="nama DSD 'SDG indicator 8.7.1'",
        cakupan="kegiatan ekonomi dan pekerjaan rumah tangga; hanya umur 15–17 dan 2009",
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"jenis_kelamin": {"MALE", "FEMALE"}, "umur": {"CLDVERSION_Y15-17"}}

RUJUKAN_TAHUN = {}
TIDAK_TERBIT = {}
TAHUN_TERBIT = {}

STATUS_ILO = {"B"}

RENTANG = {"persen": (0, 100)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="NEET 15–24: BPS vs ILO vs WDI",
         utama="var1186", rincian_utama="total", pembanding=[("SDG_0861_SEX_RT", "total"), ("SL.UEM.NEET.ZS", "total")],
         jenis="selisih", kategori="metode (olahan Sakernas yang sama); kelompok umur sama (15–24)",
         alasan_rincian="total jenis kelamin",
         pertanyaan=[("Kelompok umur?", "15–24 di ketiganya (judul BPS, nama DSD ILO, sourceNote WDI)."),
                     ("Sumber WDI?", "ILO Labour Force Statistics (sourceOrganization).")]),
    dict(id="P2", judul="Pekerja anak: BPS (5–17) vs ILO kegiatan ekonomi (15–17)",
         utama="var2658", rincian_utama="total", pembanding=[("SDG_A871_SEX_AGE_RT", "umur=CLDVERSION_Y15-17")],
         jenis="selisih", kategori="definisi (kelompok umur ILO hanya 15–17); tidak ada tahun beririsan kecuali 2023",
         alasan_rincian="ILO umur CLDVERSION_Y15-17, total jenis kelamin",
         pertanyaan=[("Kelompok umur ILO?", "Hanya 15–17 di berkas, walaupun definisi DSD mencakup 5–17."),
                     ("Beda A871 dan B871?", "B871 menambah pekerjaan rumah tangga >= 21 jam untuk umur 5–14; untuk 15–17 sama, "
                      "sehingga B871 2009 = A871 2009.")]),
    dict(id="P3", judul="Anak bekerja 7–14 (WDI): konteks",
         utama="SL.TLF.0714.ZS", rincian_utama="total", pembanding=[],
         jenis="konteks", kategori="kelompok umur 7–14 dan tahun 2000–2010; tidak beririsan dengan BPS (2020–2025)",
         alasan_rincian="tanpa rincian", pertanyaan=[("Tahun bersama dengan BPS?", "Tidak ada; bukan missing, serinya tidak tumpang tindih.")]),
]

# ------------------------------------------------------------------ Sprint 2: Gold dan rekonsiliasi
# Keputusan Sprint 2 ditambahkan di bawah keputusan Sprint 1 (lihat log-keputusan.csv).

# Kategori baku setiap pasangan ditetapkan dari bukti Sprint 1 (pertanyaan keterbandingan di atas),
# tidak diturunkan dari teks.
KATEGORI_BAKU = {"P1": "metode berbeda", "P2": "cakupan berbeda", "P3": "cakupan berbeda"}

for _p in PASANGAN:
    _p["kategori_baku"] = KATEGORI_BAKU[_p["id"]]
