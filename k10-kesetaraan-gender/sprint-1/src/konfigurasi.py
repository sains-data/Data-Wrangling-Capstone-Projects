"""Keputusan wrangling Kasus 10 — Kesetaraan gender.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri (dua definisi ILO),
satuan dan kode SDG beserta buktinya, status pengamatan ILO, ambang anomali, dan pasangan rekonsiliasi.
Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 10
SLUG = "kesetaraan-gender"
JUDUL = "Kesetaraan gender"

FORMAT_BPS = "json"

_ILO = "ILOSTAT, Sakernas (SOURCE: LFS); OBS_STATUS B = patahan seri (NOTE_INDICATOR 'Break in series')"
SERI = {
    "var1360": dict(
        sumber="bps", tingkat="provinsi",
        nama="Proporsi perempuan umur 20–24 tahun yang berstatus kawin atau hidup bersama sebelum umur 18 tahun",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="5.3.1", katalog_sdg="5.3.1", bukti_sdg="definisi di var.note = indikator 5.3.1",
        cakupan="perempuan 20–24; kawin atau hidup bersama pertama sebelum 18 tahun; Susenas 2015–2025",
    ),
    "var2003": dict(
        sumber="bps", tingkat="provinsi",
        nama="Proporsi perempuan yang berada di posisi manajerial",
        satuan="persen", katalog_satuan="tidak_ada",
        bukti_satuan="judul 'Proporsi'; var.unit kosong; nilai 10–50 dan dekat dengan ILO (UNIT_MEASURE PT = persen)",
        sdg="5.5.2", katalog_sdg="5.5.2", bukti_sdg="judul = perempuan di posisi manajerial, indikator 5.5.2",
        cakupan="Sakernas; seluruh lapangan usaha KBLI 2015 (var.note); 2015–2025", koreksi="satuan tidak_ada -> persen",
    ),
    "SG.GEN.PARL.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Proportion of seats held by women in national parliaments (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(%)'",
        sdg="5.5.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="kursi parlemen nasional (IPU)", koreksi="kode SDG kosong -> 5.5.1",
    ),
    "SP.M18.2024.FE.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Women who were first married by age 18 (% of women ages 20-24)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of women ages 20-24)'",
        sdg="5.3.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="perempuan 20–24, kawin pertama sebelum 18 (UNICEF, survei); 8 tahun 1987–2017", koreksi="kode SDG kosong -> 5.3.1",
    ),
    "SDG_0552_NOC_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Proportion of women in senior and middle management positions (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT",
        sdg="5.5.2", katalog_sdg="5.5.2", bukti_sdg="nama DSD 'SDG indicator 5.5.2'",
        cakupan="manajer senior dan menengah saja (ISCO kategori 1 dikurangi 14/13); " + _ILO,
    ),
    "SDG_T552_NOC_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Proportion of women in managerial positions, total management (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT",
        sdg="5.5.2", katalog_sdg="5.5.2", bukti_sdg="nama DSD 'SDG indicator 5.5.2'",
        cakupan="seluruh manajemen (ISCO kategori 1); " + _ILO,
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {}

RUJUKAN_TAHUN = {}
TIDAK_TERBIT = {}
TAHUN_TERBIT = {}

RENTANG = {"persen": (0, 100)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

# K-005: kode OBS_STATUS yang ditemukan di berkas ILO kasus ini; aturan validasi menolak kode lain
STATUS_ILO = {"B"}

PASANGAN = [
    dict(id="P1", judul="Perempuan manajer: BPS vs ILO seluruh manajemen (T552)",
         utama="var2003", rincian_utama="total", pembanding=[("SDG_T552_NOC_RT", "total")],
         jenis="selisih", kategori="metode kecil (Sakernas yang sama, pengolahan ILO); definisi sama (seluruh manajemen)",
         alasan_rincian="tanpa rincian",
         pertanyaan=[("ILO mana yang sebanding?", "T552 = seluruh manajemen (ISCO 1); var.note BPS mencakup seluruh lapangan usaha. "
                      "0552 hanya manajer senior dan menengah."),
                     ("Apa yang janggal?", "ILO T552 2016 = 44,78, sedangkan 2015 22,38, 2017 27,46, dan BPS 2016 23,6; tidak bertanda B.")]),
    dict(id="P2", judul="Perempuan manajer: BPS vs ILO senior dan menengah (0552)",
         utama="var2003", rincian_utama="total", pembanding=[("SDG_0552_NOC_RT", "total")],
         jenis="selisih", kategori="definisi (0552 tanpa manajer junior)", alasan_rincian="tanpa rincian",
         pertanyaan=[("Mengapa 0552 lebih rendah?", "Manajer junior (ISCO 14/13) tidak dihitung (deskripsi DSD).")]),
    dict(id="P3", judul="Perkawinan anak: BPS vs WDI (UNICEF)",
         utama="var1360", rincian_utama="total", pembanding=[("SP.M18.2024.FE.ZS", "total")],
         jenis="selisih", kategori="tidak ada tahun beririsan (WDI berakhir 2017, BPS mulai 2015: hanya 2017)",
         alasan_rincian="keduanya perempuan 20–24, sebelum 18",
         pertanyaan=[("Batas umur sama?", "Ya: 20–24, sebelum 18 (var.note dan name WDI); BPS juga menghitung hidup bersama.")]),
]
