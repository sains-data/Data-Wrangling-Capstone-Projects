"""Keputusan wrangling Kasus 21 — Keamanan dan pencatatan sipil.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, pemilihan snapshot, pergantian definisi, ambang anomali, dan pasangan
rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 21
SLUG = "keamanan-pencatatan-sipil"
JUDUL = "Keamanan dan pencatatan sipil"

FORMAT_BPS = "json"

_P = dict(satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'")
SERI = {
    "var1311": dict(sumber="bps", tingkat="provinsi", **_P,
                    nama="Proporsi penduduk yang menjadi korban kejahatan kekerasan dalam 12 bulan terakhir",
                    sdg="16.1.3(a)", katalog_sdg="16.1.3", bukti_sdg="var.label diawali '16.1.3 (a)'",
                    cakupan="Susenas; periode = tahun rujukan kejadian (angka 2017 dari Susenas 2018, var.note); 2015–2024; "
                            "banyak provinsi tidak ada sejak 2020",
                    koreksi="kode SDG 16.1.3 -> 16.1.3(a)"),
    "var1312": dict(sumber="bps", tingkat="provinsi", **_P,
                    nama="Proporsi penduduk yang merasa aman berjalan sendirian di area tempat tinggalnya",
                    sdg="16.1.4", katalog_sdg="16.1.4", bukti_sdg="var.label diawali '16.1.4*'",
                    cakupan="Susenas Modul Hansos; 2014, 2017, 2020, 2025"),
    "var2738": dict(sumber="bps", tingkat="provinsi", **_P,
                    nama="Proporsi rumah tangga dengan anak 1–17 tahun yang mengalami hukuman fisik dan/atau agresi psikologis dari pengasuh",
                    sdg="16.2.1(a)", katalog_sdg="16.2.1", bukti_sdg="var.label diawali '16.2.1 (a)'",
                    cakupan="rumah tangga dengan anak 1–17; 2014 dan 2020", koreksi="kode SDG 16.2.1 -> 16.2.1(a)"),
    "var2740": dict(sumber="bps", tingkat="provinsi", **_P,
                    nama="Proporsi korban kekerasan dalam 12 bulan terakhir yang melaporkan kepada polisi",
                    sdg="16.3.1(a)", katalog_sdg="16.3.1", bukti_sdg="var.label diawali '16.3.1.(a)'",
                    cakupan="korban kekerasan; 2020–2024; jumlah provinsi berubah setiap tahun", koreksi="kode SDG 16.3.1 -> 16.3.1(a)"),
    "var1410": dict(sumber="bps", tingkat="provinsi", **_P,
                    nama="Proporsi anak umur di bawah 5 tahun yang kelahirannya dicatat lembaga pencatatan sipil",
                    sdg="16.9.1", katalog_sdg="16.9.1", bukti_sdg="definisi di var.note = indikator 16.9.1 (balita, akta kelahiran)",
                    cakupan="anak < 5 tahun; Susenas; 2015–2025"),
    "var1831": dict(sumber="bps", tingkat="provinsi", **_P,
                    nama="Persentase anak berumur 0–17 tahun yang memiliki akta kelahiran",
                    sdg="16.9.1(b)", katalog_sdg="16.9.1", bukti_sdg="nama berkas sdg16_16_9_1_b_v1831: butir nasional (b); umur 0–17, bukan balita",
                    cakupan="anak 0–17 tahun; 2015–2023; var.note hanya mengulang judul", koreksi="kode SDG 16.9.1 -> 16.9.1(b)"),
    "SP.REG.BRTH.ZS": dict(sumber="wdi", tingkat="nasional", nama="Completeness of birth registration (%)",
                           satuan="persen", katalog_satuan="—", bukti_satuan="name: '(%)'",
                           sdg="16.9.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
                           cakupan="anak < 5 tahun dengan akta terlihat atau dilaporkan (survei rumah tangga, UNICEF)",
                           koreksi="kode SDG kosong -> 16.9.1"),
    "VC.IHR.PSRC.P5": dict(sumber="wdi", tingkat="nasional", nama="Intentional homicides (per 100,000 people)",
                           satuan="per_100000_penduduk", katalog_satuan="—", bukti_satuan="name: '(per 100,000 people)'",
                           sdg="16.1.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
                           cakupan="UNODC; 6 tahun 1998–2022", koreksi="kode SDG kosong -> 16.1.1"),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {}

RUJUKAN_TAHUN = {}
TIDAK_TERBIT = {}
TAHUN_TERBIT = {}
PATAHAN_DEFINISI = {"var1311": {"2017": "var.note: mulai angka 2017 (Susenas 2018) rujukan kejadian 1 Januari–31 Desember tahun itu; "
                                        "periode berarti tahun kejadian, bukan tahun survei"}}

RENTANG = {"persen": (0, 100), "per_100000_penduduk": (0, 100000)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Akta kelahiran balita: BPS vs WDI (UNICEF)",
         utama="var1410", rincian_utama="total", pembanding=[("SP.REG.BRTH.ZS", "total")],
         jenis="selisih", kategori="metode (Susenas vs kompilasi survei UNICEF); kelompok umur sama (< 5 tahun)",
         alasan_rincian="tanpa rincian",
         pertanyaan=[("Kelompok umur sama?", "Ya: var.note var1410 'anak berusia kurang dari 5 tahun'; sourceNote WDI 'children under age 5'."),
                     ("Bagaimana var1831?", "Umur 0–17; seri terpisah, tidak dipasangkan dengan WDI.")]),
    dict(id="P2", judul="Korban kekerasan (BPS) vs pembunuhan per 100.000 (WDI): konteks",
         utama="var1311", rincian_utama="total", pembanding=[("VC.IHR.PSRC.P5", "total")],
         jenis="konteks", kategori="definisi berbeda: proporsi korban kekerasan (survei) vs pembunuhan per 100.000 (catatan polisi)",
         alasan_rincian="tanpa rincian", pertanyaan=[("Satuan?", "Persen penduduk vs per 100.000 penduduk; konsep berbeda.")]),
    dict(id="P3", judul="Akta kelahiran balita vs anak 0–17 (BPS dengan BPS)",
         utama="var1410", rincian_utama="total", pembanding=[("var1831", "total")],
         jenis="konteks", kategori="kelompok umur berbeda; tetap dua seri", alasan_rincian="tanpa rincian",
         pertanyaan=[("Boleh disatukan?", "Tidak: < 5 tahun vs 0–17 tahun.")]),
]
