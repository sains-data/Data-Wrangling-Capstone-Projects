"""Keputusan wrangling Kasus 06 — Melek aksara.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, cara membaca tabel statis, ambang anomali, dan pasangan rekonsiliasi. Setiap
keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 6
SLUG = "melek-aksara"
JUDUL = "Melek aksara"

FORMAT_BPS = "json"

RINCI = "tabel:sdg4_amh_rinci"
SERI = {
    "var1458": dict(
        sumber="bps", tingkat="provinsi",
        nama="Angka melek aksara penduduk 15 tahun ke atas",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="4.6.1", katalog_sdg="4.6.1", bukti_sdg="berkas sdg4_amh; angka melek aksara dewasa sebagai ukuran 4.6.1",
        cakupan="penduduk 15+; Susenas; 2014–2025; tabel ringkas tanpa rincian",
    ),
    RINCI: dict(
        sumber="bps", tingkat="provinsi",
        nama="Angka melek aksara penduduk 15 tahun ke atas menurut klasifikasi desa dan jenis kelamin",
        satuan="persen", katalog_satuan="persen", bukti_satuan="judul tabel statis (angka melek aksara, persen)",
        sdg="4.6.1", katalog_sdg="4.6.1", bukti_sdg="judul tabel statis sama konsepnya dengan var1458",
        cakupan="penduduk 15+; tabel statis (HTML) 2009–2025; rincian perkotaan/perdesaan x laki-laki/perempuan",
    ),
    "SE.ADT.LITR.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Literacy rate, adult total (% of people ages 15 and above)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of people ages 15 and above)'",
        sdg="4.6.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="penduduk 15+; UNESCO UIS; 13 tahun tidak berurutan 1980–2020", koreksi="kode SDG kosong -> 4.6.1",
    ),
}

# K-004: tabel statis dibaca dari HTML di JSON; urutan tingkat header (di atas kolom) dan rincian
TABEL_STATIS = {
    RINCI: dict(berkas="sdg4_amh_rinci", header=("daerah", "jenis_kelamin", "tahun"),
                dimensi={"daerah": ("daerah", {"perkotaan": "URBAN", "perdesaan": "RURAL"}),
                         "jenis_kelamin": ("jenis_kelamin", {"laki_laki": "MALE", "perempuan": "FEMALE"})},
                total={"perkotaan_perdesaan", "laki_laki_perempuan"}),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"daerah": {"URBAN", "RURAL"}, "jenis_kelamin": {"MALE", "FEMALE"}}

RUJUKAN_TAHUN = {}
TIDAK_TERBIT = {}
TAHUN_TERBIT = {}

RENTANG = {"persen": (0, 100)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Total tabel rinci vs tabel ringkas var1458 (BPS dengan BPS)",
         utama="var1458", rincian_utama="total", pembanding=[(RINCI, "total")],
         jenis="selisih", kategori="dua tabel penerbit yang sama; selisih (bila ada) dilaporkan, tidak disamakan paksa",
         alasan_rincian="rincian total = perkotaan+perdesaan dan laki-laki+perempuan",
         pertanyaan=[
             ("Mana sumber total kanonik?", "var1458 (tabel dinamis, ber-kode wilayah); tabel rinci dipakai untuk rincian."),
             ("Apakah identik?", "Dihitung untuk semua provinsi dan tahun yang sama di aturan peringatan total_rinci_sama_ringkas."),
         ]),
    dict(id="P2", judul="Melek aksara BPS (Indonesia) vs WDI (UNESCO)",
         utama="var1458", rincian_utama="total", pembanding=[("SE.ADT.LITR.ZS", "total")],
         jenis="selisih", kategori="metode (Susenas vs kompilasi UNESCO dari sensus/survei)",
         alasan_rincian="keduanya penduduk 15+ tanpa rincian",
         pertanyaan=[("Tahun yang sama?", "WDI hanya 13 tahun; irisan dengan var1458 dihitung di reports/pasangan-rekonsiliasi.md."),
                     ("Definisi sama?", "Keduanya bisa membaca dan menulis, penduduk 15+ (sourceNote WDI, judul BPS).")]),
    dict(id="P3", judul="Melek aksara tabel rinci (2009–2025) vs WDI",
         utama=RINCI, rincian_utama="total", pembanding=[("SE.ADT.LITR.ZS", "total")],
         jenis="selisih", kategori="metode", alasan_rincian="rincian total",
         pertanyaan=[("Mengapa pasangan ini?", "Tabel rinci mulai 2009, lebih banyak tahun beririsan dengan WDI.")]),
]

# ------------------------------------------------------------------ Sprint 2: Gold dan rekonsiliasi
# Keputusan Sprint 2 ditambahkan di bawah keputusan Sprint 1 (lihat log-keputusan.csv).

# Kategori baku setiap pasangan ditetapkan dari bukti Sprint 1 (pertanyaan keterbandingan di atas),
# tidak diturunkan dari teks.
KATEGORI_BAKU = {"P1": "belum terjelaskan", "P2": "metode berbeda", "P3": "metode berbeda"}

for _p in PASANGAN:
    _p["kategori_baku"] = KATEGORI_BAKU[_p["id"]]
