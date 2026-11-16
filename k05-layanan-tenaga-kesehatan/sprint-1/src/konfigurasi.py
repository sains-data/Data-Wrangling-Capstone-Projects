"""Keputusan wrangling Kasus 05 — Layanan dan tenaga kesehatan.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, kamus profesi tenaga kesehatan, deret yang diprofilkan, ambang anomali, dan
pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 5
SLUG = "layanan-tenaga-kesehatan"
JUDUL = "Layanan dan tenaga kesehatan"

FORMAT_BPS = "json"

SERI = {
    "var1402": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase unmet need pelayanan kesehatan",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="3.8.1(a)", katalog_sdg="3.8.1",
        bukti_sdg="nama tabel BPS 'sdg3_3_8_1_a_v1402' (manifest_asal.json): butir nasional (a); indikator global 3.8.1 "
                  "adalah indeks cakupan layanan esensial (UHC_INDEX_REPORTED)",
        cakupan="penduduk yang punya keluhan kesehatan tetapi tidak berobat; Susenas; 2015–2025",
        koreksi="kode SDG 3.8.1 -> 3.8.1(a)",
    ),
    "var2279": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase penduduk yang memiliki Jaminan Kesehatan Nasional (JKN)",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="3.8.2(a)", katalog_sdg="3.8.2",
        bukti_sdg="nama tabel BPS 'sdg3_3_8_2_a_v2279': butir nasional (a); indikator global 3.8.2 adalah pengeluaran "
                  "kesehatan katastrofik (FINPROTECTION_CATA_TOT_10_POP)",
        cakupan="memiliki BPJS PBI, BPJS Non PBI, atau Jamkesda (var.note); Susenas Maret; seri baru terbit 2022",
        koreksi="kode SDG 3.8.2 -> 3.8.2(a)",
    ),
    "var1477": dict(
        sumber="bps", tingkat="provinsi",
        nama="Kepadatan tenaga kesehatan menurut profesi (per 100.000 penduduk)",
        satuan="per_100000_penduduk", katalog_satuan="tidak_ada",
        bukti_satuan="var.note: '(per 100.000 penduduk)'; var.unit dan kolom satuan CSV kosong",
        sdg="3.c.1", katalog_sdg="—",
        bukti_sdg="nama tabel BPS 'sdg3_3_c_1_v1477' dan judul 'Kepadatan Dan Distribusi Tenaga Kesehatan' = 3.c.1",
        cakupan="10 profesi di turvar; SDM Kesehatan Kemenkes (var.note); 2016–2018; Indonesia hanya 2018",
        koreksi="satuan tidak_ada -> per_100000_penduduk; kode SDG kosong -> 3.c.1",
    ),
    "HWF_0001": dict(
        sumber="who_gho", tingkat="nasional", nama="Medical doctors (per 10 000 population)",
        satuan="per_10000_penduduk", katalog_satuan="—", bukti_satuan="kolom RATE_PER_10000_N; UnitOfMeasure",
        sdg="3.c.1", katalog_sdg="3.c.1", bukti_sdg="metadata WHO",
        cakupan="dokter umum, spesialis, dan dokter tanpa rincian (DefinitionText)", koreksi="IND_NAME 'Density of doctors'",
    ),
    "HWF_0006": dict(
        sumber="who_gho", tingkat="nasional", nama="Nursing and midwifery personnel (per 10 000 population)",
        satuan="per_10000_penduduk", katalog_satuan="—", bukti_satuan="kolom RATE_PER_10000_N; UnitOfMeasure",
        sdg="3.c.1", katalog_sdg="3.c.1", bukti_sdg="metadata WHO",
        cakupan="perawat dan bidan digabung; aktif atau terdaftar tergantung sumber (DefinitionText)",
    ),
    "UHC_INDEX_REPORTED": dict(
        sumber="who_gho", tingkat="nasional", nama="UHC service coverage index",
        satuan="indeks", katalog_satuan="—", bukti_satuan="kolom INDEX_N; UnitOfMeasure: rata-rata skor 14 indikator penanda",
        sdg="3.8.1", katalog_sdg="3.8.1", bukti_sdg="metadata WHO", cakupan="indeks 0–100, tahunan 2000–2023",
    ),
    "FINPROTECTION_CATA_TOT_10_POP": dict(
        sumber="who_gho", tingkat="nasional", nama="Population with household health spending > 10% of budget (%)",
        satuan="persen", katalog_satuan="—", bukti_satuan="kolom PERCENT_POP_N",
        sdg="3.8.2", katalog_sdg="3.8.2", bukti_sdg="metadata WHO",
        cakupan="rincian komposisi rumah tangga, daerah, jenis kelamin dan umur kepala rumah tangga",
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {"DIM_SEX": "jenis_kelamin", "DIM_AGE": "umur", "DIM_DEG_URB": "daerah",
                   "DIM_HOUSEHOLD_COMP_BY_AGE": "komposisi_rt", "DIM_POP_TYPE": "jenis_penduduk"}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"jenis_kelamin": {"FEMALE", "MALE"}, "daerah": {"URBAN", "RURAL"}, "umur": None,
                "komposisi_rt": None, "jenis_penduduk": None}

# K-006: profesi tenaga kesehatan dari turvar BPS -> rincian profesi=<kode>
PROFESI = {"Dokter Umum": "dokter_umum", "Dokter Gigi": "dokter_gigi", "Perawat": "perawat", "Bidan": "bidan",
           "Farmasi": "farmasi", "Kesehatan Masyarakat": "kesehatan_masyarakat",
           "Kesehatan Lingkungan": "kesehatan_lingkungan", "Gizi": "gizi",
           "Ahli Teknologi Laboratorium Medik": "atlm", "Pekarya": "pekarya"}
RINCIAN_BPS = {"var1477": ("profesi", PROFESI)}
KODE_RINCIAN["profesi"] = set(PROFESI.values())

# K-004: var1477 tidak punya baris total; tiga profesi yang punya pembanding WHO diprofilkan dan diberi grid.
DERET = {"var1477": ["profesi=dokter_umum", "profesi=perawat", "profesi=bidan"]}

RUJUKAN_TAHUN = {}
TIDAK_TERBIT = {}
TAHUN_TERBIT = {"var1402": {str(t) for t in range(2015, 2026)}, "var2279": {"2022", "2023", "2024", "2025"},
                "var1477": {"2016", "2017", "2018"}}

RENTANG = {"persen": (0, 100), "per_100000_penduduk": (0, 100000), "per_10000_penduduk": (0, 10000), "indeks": (0, 100)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Dokter: BPS dokter umum (per 100.000) vs WHO semua dokter (per 10.000)",
         utama="var1477", rincian_utama="profesi=dokter_umum", pembanding=[("HWF_0001", "total")],
         jenis="selisih", kategori="definisi (WHO termasuk dokter spesialis) setelah satuan diseragamkan (BPS x 0,1)",
         alasan_rincian="BPS profesi=dokter_umum; dokter gigi tidak termasuk 'medical doctors'",
         pertanyaan=[
             ("Satuan?", "BPS per 100.000 penduduk (var.note), WHO per 10.000; disamakan di Gold dengan faktor 0,1."),
             ("Siapa yang dihitung WHO?", "Generalists, specialist medical practitioners, dan medical doctors not further defined."),
             ("Tahun mana?", "Hanya 2018: baris Indonesia var1477 hanya ada untuk 2018."),
         ]),
    dict(id="P2", judul="Perawat dan bidan: BPS (dua rincian dijumlahkan di Gold) vs WHO HWF_0006",
         utama="var1477", rincian_utama="profesi=perawat", pembanding=[("HWF_0006", "total")],
         jenis="selisih", kategori="definisi (aktif vs terdaftar) setelah perawat + bidan dijumlahkan dan satuan diseragamkan",
         alasan_rincian="WHO menggabungkan perawat dan bidan; BPS memisahkan; penjumlahan sah karena penyebutnya sama (penduduk)",
         pertanyaan=[
             ("Boleh menjumlahkan perawat dan bidan?", "Ya: keduanya per 100.000 penduduk yang sama, jadi kepadatannya bisa dijumlahkan."),
             ("Aktif atau terdaftar?", "DefinitionText WHO: tergantung sumber data; BPS tidak menyebut."),
         ]),
    dict(id="P3", judul="Unmet need pelayanan (BPS) vs indeks cakupan UHC (WHO): konteks",
         utama="var1402", rincian_utama="total", pembanding=[("UHC_INDEX_REPORTED", "total")],
         jenis="konteks", kategori="definisi berbeda: persentase penduduk tidak berobat vs indeks 14 indikator layanan",
         alasan_rincian="tanpa rincian", pertanyaan=[("Kode sama?", "Katalog 3.8.1 untuk keduanya; var1402 butir nasional (a).")]),
    dict(id="P4", judul="Kepemilikan JKN (BPS) vs pengeluaran kesehatan katastrofik (WHO): konteks",
         utama="var2279", rincian_utama="total", pembanding=[("FINPROTECTION_CATA_TOT_10_POP", "total")],
         jenis="konteks", kategori="definisi berbeda: kepemilikan jaminan vs beban pengeluaran rumah tangga",
         alasan_rincian="WHO rincian total", pertanyaan=[("Tahun bersama?", "WHO berakhir 2021, JKN mulai 2022: tidak ada.")]),
]
