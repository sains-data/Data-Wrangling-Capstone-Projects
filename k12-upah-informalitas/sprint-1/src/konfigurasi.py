"""Keputusan wrangling Kasus 12 — Upah dan informalitas.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, klasifikasi jabatan dan sektor ILO, status ILO, ambang anomali, dan pasangan
rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 12
SLUG = "upah-informalitas"
JUDUL = "Upah dan informalitas"

FORMAT_BPS = "json"

SERI = {
    "var1172": dict(
        sumber="bps", tingkat="provinsi", nama="Upah rata-rata per jam pekerja",
        satuan="rupiah_per_jam", katalog_satuan="rupiah_per_jam", bukti_satuan="var.unit: 'Rupiah/Jam'",
        sdg="8.5.1", katalog_sdg="8.5.1", bukti_sdg="upah per jam = indikator 8.5.1",
        cakupan="pekerja (buruh/karyawan); nominal; Sakernas; 2015–2019 angka revisi karena perubahan penimbang (var.note)",
    ),
    "var2153": dict(
        sumber="bps", tingkat="provinsi", nama="Proporsi lapangan kerja informal",
        satuan="persen", katalog_satuan="tidak_ada", bukti_satuan="judul 'Proporsi'; var.unit kosong; nilai 20–90",
        sdg="8.3.1", katalog_sdg="8.3.1", bukti_sdg="lapangan kerja informal = indikator 8.3.1",
        cakupan="Sakernas; 2018–2025; semua sektor (tidak disebut tanpa pertanian)", koreksi="satuan tidak_ada -> persen",
    ),
    "SDG_0851_SEX_OCU_NB": dict(
        sumber="ilostat", tingkat="nasional", nama="Average hourly earnings of employees by sex and occupation (IDR)",
        satuan="rupiah_per_jam", katalog_satuan="—",
        bukti_satuan="UNIT_MEASURE LC (mata uang lokal); NOTE_INDICATOR 'IDR: Indonesian rupiah'; judul DSD 'hourly earnings'",
        sdg="8.5.1", katalog_sdg="8.5.1", bukti_sdg="nama DSD 'SDG indicator 8.5.1'",
        cakupan="pekerja; nominal; rincian jenis kelamin x jabatan (ISCO-08, ISCO-88, tingkat keahlian); OBS_STATUS B = patahan",
    ),
    "SDG_0831_SEX_ECO_RT": dict(
        sumber="ilostat", tingkat="nasional", nama="Proportion of informal employment in total employment by sex and economic activity (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="UNIT_MEASURE PT",
        sdg="8.3.1", katalog_sdg="8.3.1", bukti_sdg="nama DSD 'SDG indicator 8.3.1'",
        cakupan="semua sektor termasuk pertanian (rincian SECTOR_AGR dan SECTOR_NAG); rincian jenis kelamin x sektor (dua klasifikasi)",
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"jenis_kelamin": {"MALE", "FEMALE"}, "jabatan": None, "sektor": None}

RUJUKAN_TAHUN = {}
TIDAK_TERBIT = {}
TAHUN_TERBIT = {}

STATUS_ILO = {"B"}

RENTANG = {"persen": (0, 100), "rupiah_per_jam": (0, 1_000_000)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Upah per jam: BPS (pekerja) vs ILO (rata-rata penghasilan per jam pekerja)",
         utama="var1172", rincian_utama="total", pembanding=[("SDG_0851_SEX_OCU_NB", "total")],
         jenis="selisih", kategori="metode (pengolahan Sakernas; nominal keduanya, rupiah per jam)",
         alasan_rincian="ILO total jenis kelamin dan tingkat keahlian",
         pertanyaan=[("Unit sama?", "Ya: rupiah per jam, nominal (var.unit; NOTE_INDICATOR 'IDR'). Upah riil butuh indeks harga yang "
                      "dicatat sumbernya (Sprint 2)."),
                     ("Apakah sudah disesuaikan inflasi?", "Tidak: keduanya nominal.")]),
    dict(id="P2", judul="Informalitas: BPS vs ILO",
         utama="var2153", rincian_utama="total", pembanding=[("SDG_0831_SEX_ECO_RT", "total")],
         jenis="selisih", kategori="definisi (ILO jauh lebih tinggi, ±80% vs ±58%: kriteria informal berbeda)",
         alasan_rincian="ILO total sektor (termasuk pertanian)",
         pertanyaan=[("Cakupan sektor?", "Keduanya semua sektor; ILO punya rincian tanpa pertanian (SECTOR_NAG) untuk diuji di Sprint 2."),
                     ("Mengapa beda besar?", "ILO menilai informalitas dari ciri pekerjaan dan unit usaha; BPS dari status pekerjaan. "
                      "Dipastikan dari dokumentasi di Sprint 2.")]),
]
