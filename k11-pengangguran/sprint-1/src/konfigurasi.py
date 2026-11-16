"""Keputusan wrangling Kasus 11 — Pengangguran.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, periode Februari/Agustus/tahunan, sel yang tidak dicacah, status ILO, ambang
anomali, dan pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 11
SLUG = "pengangguran"
JUDUL = "Pengangguran"

FORMAT_BPS = "json"

_ILO = "ILOSTAT; olahan mikrodata Sakernas (SOURCE LFS) dan sensus; OBS_STATUS B = patahan seri"
SERI = {
    "var543": dict(
        sumber="bps", tingkat="provinsi", nama="Tingkat Pengangguran Terbuka (TPT)",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="8.5.2", katalog_sdg="8.5.2", bukti_sdg="TPT = indikator 8.5.2",
        cakupan="Sakernas; tahunan 1986–2004 (tanpa 1995), Februari dan Agustus sejak 2005 sampai Februari 2026; "
                "backcast penimbang 2011–2013 dan 2018–2020 (var.note)",
    ),
    "SL.UEM.TOTL.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Unemployment, total (% of total labor force) (modeled ILO estimate)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of total labor force)'",
        sdg="8.5.2", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="estimasi model ILO (ILOEST), termasuk tahun tanpa survei", koreksi="kode SDG kosong -> 8.5.2",
    ),
    "SL.UEM.TOTL.NE.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Unemployment, total (% of total labor force) (national estimate)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of total labor force)'",
        sdg="8.5.2", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="ILO Labour Force Statistics (olahan survei nasional)", koreksi="kode SDG kosong -> 8.5.2",
    ),
    "SDG_0852_SEX_AGE_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Unemployment rate by sex and age (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT", sdg="8.5.2", katalog_sdg="8.5.2",
        bukti_sdg="nama DSD 'SDG indicator 8.5.2'", cakupan="rincian jenis kelamin dan umur (15+, 15–24, 25+); " + _ILO,
    ),
    "SDG_0852_SEX_DSB_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Unemployment rate by sex and disability status (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT", sdg="8.5.2", katalog_sdg="8.5.2",
        bukti_sdg="nama DSD 'SDG indicator 8.5.2'", cakupan="rincian jenis kelamin dan disabilitas; 2010 dari sensus; " + _ILO,
    ),
    "UNE_DEAP_SEX_AGE_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Unemployment rate by sex and age, ILO modelled/harmonized (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT", sdg="8.5.2", katalog_sdg="8.5.2",
        bukti_sdg="katalog; pengangguran per jenis kelamin dan umur",
        cakupan="tahunan dan triwulanan (FREQ A/Q, Q1 dan Q3 = Februari dan Agustus); 28 kode umur dari 4 klasifikasi; "
                "rujukan Agustus (NOTE_SOURCE); " + _ILO,
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"jenis_kelamin": {"MALE", "FEMALE"}, "umur": None, "disabilitas": None}

RUJUKAN_TAHUN = {}
# K-005: var.note: tahun 2000 tanpa Maluku (Maluku Utara baru dipisah 1999)
TIDAK_TERBIT = {("var543", 8100, "2000"): "var.note: pada tahun 2000 tanpa Maluku",
                ("var543", 8200, "2000"): "var.note: pada tahun 2000 tanpa Maluku; Maluku Utara baru dipisah dari Maluku (1999)"}
TAHUN_TERBIT = {}

STATUS_ILO = {"B", "U"}

RENTANG = {"persen": (0, 100)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="TPT BPS Agustus vs ILO SDG 8.5.2 (total, rujukan Agustus)",
         utama="var543", rincian_utama="total", pembanding=[("SDG_0852_SEX_AGE_RT", "total")], semester_utama="08",
         jenis="selisih", kategori="definisi pengangguran (BPS lebih tinggi 1–3,3 poin pada 18 tahun; dugaan cakupan BPS lebih luas) dan pengolahan",
         alasan_rincian="ILO total jenis kelamin dan umur 15+; BPS Agustus karena NOTE_SOURCE ILO 'Data reference period: August'",
         pertanyaan=[("Bulan survei ILO?", "Agustus (NOTE_SOURCE di UNE_DEAP)."),
                     ("Mengapa BPS lebih tinggi?", "ILO memakai definisi harmonisasi; BPS memakai definisi nasional. Dipastikan dari "
                      "dokumentasi Sakernas di Sprint 2.")]),
    dict(id="P2", judul="WDI estimasi nasional vs estimasi model ILO",
         utama="SL.UEM.TOTL.NE.ZS", rincian_utama="total", pembanding=[("SL.UEM.TOTL.ZS", "total")],
         jenis="selisih", kategori="metode: survei (= ILO SDG 8.5.2) vs model ILOEST yang mengisi dan menyesuaikan",
         alasan_rincian="tanpa rincian",
         pertanyaan=[("Mengapa beda?", "NE = olahan survei ILO (sama dengan SDG_0852); ZS = model ILOEST (sourceOrganization).")]),
    dict(id="P3", judul="Pengangguran menurut disabilitas (ILO): konteks",
         utama="SDG_0852_SEX_DSB_RT", rincian_utama="disabilitas=STATUS_DIS", pembanding=[],
         jenis="konteks", kategori="tidak ada padanan BPS di paket", alasan_rincian="disabilitas",
         pertanyaan=[("Ada padanan BPS?", "Tidak di paket ini.")]),
]
