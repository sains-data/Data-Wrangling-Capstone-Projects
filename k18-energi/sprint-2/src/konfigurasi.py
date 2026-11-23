"""Keputusan wrangling Kasus 18 — Energi: listrik dan bahan bakar memasak.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, cara membaca tabel statis, kategori bahan bakar bersih, provinsi yang tidak
dicacah, ambang anomali, dan pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 18
SLUG = "energi"
JUDUL = "Energi: listrik dan bahan bakar memasak"

FORMAT_BPS = "json"

BB = "tabel:sdg7_bahan_bakar"
SERI = {
    "var87": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga dengan sumber penerangan utama listrik PLN",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="7.1.1", katalog_sdg="7.1.1", bukti_sdg="berkas sdg7_listrik_pln; proksi akses listrik",
        cakupan="rumah tangga; hanya listrik PLN (bukan semua sumber listrik); Susenas 1993–2025 tanpa 2005; "
                "var.def: provinsi tidak dicacah 2000–2001, hanya ibu kota 2002",
    ),
    BB: dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase rumah tangga menurut bahan bakar utama untuk memasak",
        satuan="persen", katalog_satuan="persen", bukti_satuan="judul tabel statis 'Persentase Rumah Tangga'",
        sdg="7.1.2", katalog_sdg="7.1.2", bukti_sdg="bahan bakar memasak = dasar indikator 7.1.2 (bahan bakar bersih)",
        cakupan="tabel statis (HTML) 2001, 2007–2021; 6 jenis + jumlah; gas/elpiji termasuk gas kota/biogas, lainnya termasuk "
                "rumah tangga yang tidak memasak (catatan tabel)",
    ),
    "EG.ELC.ACCS.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Access to electricity (% of population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of population)'",
        sdg="7.1.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="penduduk; semua sumber listrik (industri, survei nasional, sumber internasional)", koreksi="kode SDG kosong -> 7.1.1",
    ),
    "EG.CFT.ACCS.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Access to clean fuels and technologies for cooking (% of population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of population)'",
        sdg="7.1.2", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="penduduk; menurut pedoman WHO minyak tanah tidak termasuk bersih (sourceNote)", koreksi="kode SDG kosong -> 7.1.2",
    ),
}

# K-002: tabel statis bahan bakar dibaca dari HTML (header tahun x jenis bahan bakar)
TABEL_STATIS = {
    BB: dict(berkas="sdg7_bahan_bakar", header=("tahun", "bahan_bakar"),
             dimensi={"bahan_bakar": ("bahan_bakar", {})}, total={"jumlah"}),
}
# K-008: kategori untuk Gold (Sprint 2); minyak tanah tidak bersih mengikuti sourceNote WDI (pedoman WHO)
KATEGORI_BAHAN_BAKAR = {"listrik": "bersih", "gas_elpiji": "bersih", "minyak_tanah": "tidak_bersih",
                        "arang_briket": "tidak_bersih", "kayu": "tidak_bersih", "lainnya": "tidak_ditentukan"}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"bahan_bakar": set(KATEGORI_BAHAN_BAKAR)}

DERET = {BB: ["bahan_bakar=gas_elpiji", "bahan_bakar=minyak_tanah", "bahan_bakar=kayu"]}

RUJUKAN_TAHUN = {}
_TIDAK = {(1100, "2000"): "var.def: tahun 2000 Susenas tidak dicacah di NAD (Aceh)",
          (8100, "2000"): "var.def: tahun 2000 Susenas tidak dicacah di Maluku",
          (8200, "2000"): "var.def: Maluku tidak dicacah 2000; Maluku Utara baru dipisah dari Maluku (1999)",
          (1100, "2001"): "var.def: tahun 2001 Susenas tidak dicacah di NAD (Aceh)"}
TIDAK_TERBIT = {("var87", k, p): b for (k, p), b in _TIDAK.items()}
for _r in DERET[BB]:
    TIDAK_TERBIT[(BB, 1100, "2001")] = "sel '-' di tabel bahan bakar 2001; Susenas 2001 tidak dicacah di Aceh (var.def var87)"
CAKUPAN_PARSIAL = {("var87", "2002"): (1100, 8100, 8200, 9400)}
TAHUN_TERBIT = {}

# K-009: rincian jumlah komposisi bahan bakar bisa 100,01 karena pembulatan; batas atas persen diberi kelonggaran 0,05
RENTANG = {"persen": (0, 100.05)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Listrik: BPS (rumah tangga, PLN saja) vs WDI (penduduk, semua sumber)",
         utama="var87", rincian_utama="total", pembanding=[("EG.ELC.ACCS.ZS", "total")],
         jenis="selisih", kategori="definisi (PLN saja vs semua sumber listrik; rumah tangga vs penduduk)",
         alasan_rincian="tanpa rincian",
         pertanyaan=[("Apakah BPS mencakup semua listrik?", "Tidak: judul 'Sumber Penerangan Utama dari Listrik PLN'."),
                     ("Unit WDI?", "Persentase penduduk (name WDI).")]),
    dict(id="P2", judul="Bahan bakar bersih: BPS (gas/elpiji + listrik, dijumlahkan di Gold) vs WDI",
         utama=BB, rincian_utama="bahan_bakar=gas_elpiji", pembanding=[("EG.CFT.ACCS.ZS", "total")],
         jenis="selisih", kategori="definisi (kategori bersih; rumah tangga vs penduduk); BPS berakhir 2021",
         alasan_rincian="kategori bersih = listrik + gas/elpiji (KATEGORI_BAHAN_BAKAR); minyak tanah tidak bersih",
         pertanyaan=[("Apa yang bersih menurut WDI?", "sourceNote: pedoman WHO, minyak tanah tidak termasuk."),
                     ("Bagaimana 'lainnya'?", "Termasuk rumah tangga yang tidak memasak (catatan tabel); tidak dimasukkan ke bersih.")]),
]

# ------------------------------------------------------------------ Sprint 2: Gold dan rekonsiliasi
# Keputusan Sprint 2 ditambahkan di bawah keputusan Sprint 1 (lihat log-keputusan.csv).

# Kategori baku setiap pasangan ditetapkan dari bukti Sprint 1 (pertanyaan keterbandingan di atas),
# tidak diturunkan dari teks.
KATEGORI_BAKU = {"P1": "definisi berbeda", "P2": "definisi berbeda"}

for _p in PASANGAN:
    _p["kategori_baku"] = KATEGORI_BAKU[_p["id"]]
