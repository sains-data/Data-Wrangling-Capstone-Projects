"""Keputusan wrangling Kasus 15 — Kemiskinan dan daerah tertinggal.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, rincian daerah dan status desa, aturan periode semester, ambang anomali, dan
pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 15
SLUG = "daerah-tertinggal"
JUDUL = "Kemiskinan dan daerah tertinggal"

FORMAT_BPS = "json"

_DESA = "Indeks Desa (Podes) mulai 2019; 2018 memakai Indeks Pembangunan Desa yang tidak sebanding (var.note); 34 provinsi, tanpa baris Indonesia"
SERI = {
    "var192": dict(
        sumber="bps", tingkat="provinsi",
        nama="Persentase penduduk miskin (P0) menurut daerah",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="1.2.1", katalog_sdg="10.1.1",
        bukti_sdg="P0 terhadap garis kemiskinan nasional = indikator 1.2.1; nama berkas sdg10_10_1_1_f menandai pemakaiannya "
                  "sebagai butir nasional 10.1.1(f)",
        cakupan="2007–2011 tahunan; 2012 ke atas Semester 1 (Maret) dan Semester 2 (September); 2023 hanya Maret; "
                "Kalimantan Utara 2013–2014 dan Papua sebelum 2024 berbatas lama (var.note)",
        koreksi="kode SDG 10.1.1 -> 1.2.1 (berkas dipakai BPS sebagai butir 10.1.1(f))",
    ),
    "var2190": dict(
        sumber="bps", tingkat="provinsi", nama="Jumlah desa mandiri",
        satuan="desa", katalog_satuan="desa", bukti_satuan="var.unit: 'Desa'",
        sdg="10.1.1(d)", katalog_sdg="10.1.1", bukti_sdg="nama berkas sdg10_10_1_1_d_v2190: butir nasional (d)",
        cakupan=_DESA, koreksi="kode SDG 10.1.1 -> 10.1.1(d)",
    ),
    "var2191": dict(
        sumber="bps", tingkat="provinsi", nama="Jumlah desa tertinggal dan sangat tertinggal",
        satuan="desa", katalog_satuan="desa", bukti_satuan="var.unit: 'Desa'",
        sdg="10.1.1(c)", katalog_sdg="10.1.1", bukti_sdg="nama berkas sdg10_10_1_1_c_v2191: butir nasional (c)",
        cakupan=_DESA + "; rincian sangat tertinggal, tertinggal, jumlah", koreksi="kode SDG 10.1.1 -> 10.1.1(c)",
    ),
    "SI.POV.NAHC": dict(
        sumber="wdi", tingkat="nasional", nama="Poverty headcount ratio at national poverty lines (% of population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of population)'",
        sdg="1.2.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="angka tahunan = P0 BPS Maret dibulatkan satu desimal (dicek di data)", koreksi="kode SDG kosong -> 1.2.1",
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada", "jumlah"}
RINCIAN_BPS = {
    "var192": ("daerah", {"Perkotaan": "URBAN", "Perdesaan": "RURAL"}),
    "var2191": ("status_desa", {"Desa Sangat Tertinggal": "sangat_tertinggal", "Desa Tertinggal": "tertinggal"}),
}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"daerah": {"URBAN", "RURAL"}, "status_desa": {"sangat_tertinggal", "tertinggal"}}

RUJUKAN_TAHUN = {}
# K-005: Jakarta tidak punya desa (seluruhnya kelurahan), jadi tidak dinilai Indeks Desa
TIDAK_TERBIT = {(s, 3100, str(th)): "DKI Jakarta tidak punya desa (seluruh wilayahnya kelurahan); tidak ada di ketiga tahun Indeks Desa"
                for s in ("var2190", "var2191") for th in (2019, 2020, 2021)}

# K-012: sumber dan daftar desa Indeks Desa berganti setiap tahun (var.note)
_ID = {"2020": "var.note: Indeks Desa 2020 dari Updating Podes 2020 dan daftar desa Kepmendagri 146/2020 (2019: Podes 2018 + "
               "Updating 2019, Kepmendagri 414/2019)",
       "2021": "var.note: Indeks Desa 2021 dari Pendataan Podes 2021 (2020: Updating Podes 2020)"}
PATAHAN_DEFINISI = {"var2190": _ID, "var2191": _ID}
TAHUN_TERBIT = {}

RENTANG = {"persen": (0, 100), "desa": (0, 100_000)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="P0 Indonesia: BPS Maret (Semester 1) vs WDI tahunan",
         utama="var192", rincian_utama="total", pembanding=[("SI.POV.NAHC", "total")], semester_utama="S1",
         jenis="selisih", kategori="pembulatan: WDI = P0 Maret BPS dibulatkan satu desimal; tahun 2007–2011 BPS tahunan",
         alasan_rincian="rincian jumlah (perkotaan + perdesaan); semester Maret",
         pertanyaan=[("Semester mana yang dipakai WDI?", "Maret (S1): nilai WDI sama dengan P0 Maret yang dibulatkan, misalnya 2020 9,78 -> 9,8."),
                     ("Mengapa bukan rata-rata dua semester?", "Rata-rata 2020 (9,98) tidak cocok dengan WDI 9,8; semester tidak dirata-rata di Silver.")]),
    dict(id="P2", judul="Desa tertinggal dan mandiri: tanpa pembanding nasional di paket",
         utama="var2191", rincian_utama="total", pembanding=[("var2190", "total")],
         jenis="konteks", kategori="tidak ada baris Indonesia; agregat nasional dijumlahkan dari 34 provinsi di Gold",
         alasan_rincian="rincian jumlah", pertanyaan=[("Ada angka Indonesia?", "Tidak; hanya 34 provinsi (2019–2021).")]),
]
