"""Keputusan wrangling Kasus 01 — Kerawanan pangan provinsi.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, cara menulis rincian, sel yang dinyatakan tidak terbit, ambang anomali, dan
pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 1
SLUG = "kerawanan-pangan"
JUDUL = "Kerawanan pangan provinsi"

# K-002: JSON dipakai sebagai sumber Silver BPS (CSV identik nilainya, JSON membawa judul, satuan, catatan).
FORMAT_BPS = "json"

SERI = {
    "var1473": dict(
        sumber="bps", tingkat="provinsi",
        nama="Prevalensi Ketidakcukupan Konsumsi Pangan (Prevalence of Undernourishment)",
        satuan="persen", katalog_satuan="persen",
        bukti_satuan="var.unit: 'Persen'; kolom satuan CSV 'Persen'",
        sdg="2.1.1", katalog_sdg="2.1.1",
        bukti_sdg="judul = prevalensi ketidakcukupan konsumsi pangan, sama dengan indikator global 2.1.1",
        cakupan="seluruh penduduk; sumber Susenas (var.note); tahunan 2017–2025",
    ),
    "var1474": dict(
        sumber="bps", tingkat="provinsi",
        nama="Prevalensi penduduk dengan kerawanan pangan sedang atau berat (Skala Pengalaman Kerawanan Pangan, FIES)",
        satuan="persen", katalog_satuan="persen",
        bukti_satuan="var.unit: 'Persen'",
        sdg="2.1.2", katalog_sdg="2.1.2",
        bukti_sdg="judul dan var.note: kerawanan pangan sedang atau parah menurut FIES, indikator global 2.1.2",
        cakupan="seluruh penduduk; FIES setidaknya sekali dalam 12 bulan terakhir; sumber Susenas (var.note)",
    ),
    "SN.ITK.DEFC.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Prevalence of undernourishment (% of population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of population)'",
        sdg="2.1.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json (Sustainable Development Goals)",
        cakupan="estimasi FAO; sourceNote: angka 2.5 dapat berarti kurang dari 2,5%",
        koreksi="kode SDG kosong -> 2.1.1",
    ),
    "SN.ITK.MSFI.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Prevalence of moderate or severe food insecurity in the population (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(%)'",
        sdg="2.1.2", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="estimasi FAO; rumah tangga dengan sedikitnya satu orang dewasa mengalami kerawanan sedang atau berat",
        koreksi="kode SDG kosong -> 2.1.2",
    ),
    "NUTSTUNTINGPREV": dict(
        sumber="who_gho", tingkat="nasional", nama="Stunting in children (under 5)",
        satuan="persen", katalog_satuan="—", bukti_satuan="kolom RATE_PER_100_N",
        sdg="2.2.1", katalog_sdg="2.2.1", bukti_sdg="metadata WHO", cakupan="balita; estimasi tahunan 2000–2024",
    ),
    "NUTOVERWEIGHTPREV": dict(
        sumber="who_gho", tingkat="nasional", nama="Overweight in children (under 5)",
        satuan="persen", katalog_satuan="—", bukti_satuan="kolom RATE_PER_100_N",
        sdg="2.2.2", katalog_sdg="2.2.2", bukti_sdg="metadata WHO", cakupan="balita; estimasi tahunan 2000–2024",
    ),
    "NUTRITION_WH_2": dict(
        sumber="who_gho", tingkat="nasional", nama="Wasting in children (under 5)",
        satuan="persen", katalog_satuan="—", bukti_satuan="kolom RATE_PER_100_N",
        sdg="2.2.2", katalog_sdg="2.2.2", bukti_sdg="metadata WHO",
        cakupan="balita; angka survei (12 tahun survei 1996–2023) dengan rincian umur, jenis kelamin, daerah",
    ),
}

# Rincian (K-006). Nilai kosong dan TOTAL sama-sama berarti "tidak dirinci" pada dimensi itu.
RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {"DIM_SEX": "jenis_kelamin", "DIM_AGE": "umur", "DIM_DEG_URB": "daerah",
                   "DIM_POP_WEALTH_QUINTILE": "kuintil", "DIM_POP_WEALTH_DECILE": "desil",
                   "DIM_HOUSEHOLDWEALTH": "kekayaan", "DIM_WEALTHTERCILE": "tersil",
                   "DIM_POP_EDU_LEVELMOTHER": "pendidikan_ibu"}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"jenis_kelamin": {"FEMALE", "MALE"}, "daerah": {"URBAN", "RURAL"}, "umur": None,
                "kuintil": None, "desil": None, "kekayaan": None, "tersil": None, "pendidikan_ibu": None}

RUJUKAN_TAHUN = {}

# Tidak ada catatan penerbit yang menyatakan sel tertentu tidak terbit (var.note hanya menyebut sumber).
TIDAK_TERBIT = {}
TAHUN_TERBIT = {s: {str(t) for t in range(2017, 2026)} for s in ("var1473", "var1474")}

RENTANG = {"persen": (0, 100)}

# Ambang anomali (K-004). Panel 9 tahun: arah ke samping dipakai (>= 6 periode per provinsi).
ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

# Batas sensor WDI (K-010): sourceNote SN.ITK.DEFC.ZS menyebut angka 2.5 dapat berarti < 2,5%.
SENSOR_WDI = {"SN.ITK.DEFC.ZS": 2.5}

PASANGAN = [
    dict(id="P1", judul="Ketidakcukupan konsumsi pangan: BPS (Susenas) vs WDI (FAO)",
         utama="var1473", rincian_utama="total", pembanding=[("SN.ITK.DEFC.ZS", "total")],
         jenis="selisih", kategori="metode (sumber data dan model berbeda); periode angka FAO belum terjawab dari paket",
         alasan_rincian="keduanya seluruh penduduk tanpa rincian; BPS baris Indonesia",
         pertanyaan=[
             ("Apakah definisinya sama?", "Ya: keduanya prevalence of undernourishment (judul var1473 dan name WDI)."),
             ("Apakah angka FAO satu tahun atau rata-rata beberapa tahun?",
              "Metadata WDI di paket tidak menyebutnya (name, sourceNote, sourceOrganization). Dicatat sebagai pertanyaan "
              "terbuka; Sprint 2 memastikannya dari dokumentasi FAO sebelum selisih per tahun ditafsirkan."),
             ("Dari survei apa angkanya?", "BPS: Susenas (var.note). WDI: sourceOrganization FAO, tanpa keterangan survei."),
         ]),
    dict(id="P2", judul="Kerawanan pangan sedang atau berat (FIES): BPS vs WDI (FAO)",
         utama="var1474", rincian_utama="total", pembanding=[("SN.ITK.MSFI.ZS", "total")],
         jenis="selisih", kategori="sumber data dan cara estimasi berbeda; definisi FIES sama",
         alasan_rincian="keduanya seluruh penduduk tanpa rincian",
         pertanyaan=[
             ("Apakah keduanya FIES?", "Ya: var.note BPS menyebut FIES 12 bulan terakhir; sourceNote WDI menyebut moderately or severely food insecure."),
             ("Apa satuan analisisnya?", "BPS: penduduk. WDI: penduduk yang tinggal di rumah tangga rawan pangan (rumah tangga sebagai unit klasifikasi)."),
         ]),
    dict(id="P3", judul="Gizi balita WHO (stunting, overweight, wasting): konteks, bukan pasangan BPS",
         utama="NUTSTUNTINGPREV", rincian_utama="total",
         pembanding=[("NUTOVERWEIGHTPREV", "total"), ("NUTRITION_WH_2", "total")],
         jenis="konteks", kategori="definisi berbeda: status gizi balita, bukan kecukupan pangan penduduk",
         alasan_rincian="rincian total (jenis kelamin, umur, daerah TOTAL atau kosong)",
         pertanyaan=[
             ("Apakah ada padanan BPS di paket?", "Tidak; dua seri BPS mengukur penduduk, ketiga seri WHO mengukur balita."),
             ("Mengapa NUTRITION_WH_2 hanya 12 tahun?", "Angka survei (bukan estimasi tahunan model); tahun antara survei tidak ada."),
         ]),
]
