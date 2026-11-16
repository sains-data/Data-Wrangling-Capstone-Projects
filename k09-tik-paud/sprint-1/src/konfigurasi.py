"""Keputusan wrangling Kasus 09 — Keterampilan TIK dan PAUD.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri, satuan dan kode
SDG beserta buktinya, pemilihan snapshot, sel dengan galat sampling tinggi, ambang anomali, dan pasangan
rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 9
SLUG = "tik-paud"
JUDUL = "Keterampilan TIK dan PAUD"

FORMAT_BPS = "json"

SERI = {
    "var1451": dict(
        sumber="bps", tingkat="provinsi",
        nama="Proporsi remaja dan dewasa usia 15–24 tahun dengan keterampilan TIK",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="4.4.1(a)", katalog_sdg="4.4.1", bukti_sdg="var.label diawali '4.4.1.(a)'",
        cakupan="umur 15–24; Susenas KOR; 2015–2025", koreksi="kode SDG 4.4.1 -> 4.4.1(a)",
    ),
    "var1447": dict(
        sumber="bps", tingkat="provinsi",
        nama="Proporsi remaja dan dewasa usia 15–59 tahun dengan keterampilan TIK",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="4.4.1(b)", katalog_sdg="4.4.1", bukti_sdg="var.label diawali '4.4.1.(b)'",
        cakupan="umur 15–59; 2015–2025", koreksi="kode SDG 4.4.1 -> 4.4.1(b)",
    ),
    "var1439": dict(
        sumber="bps", tingkat="provinsi",
        nama="Angka Partisipasi Kasar (APK) PAUD",
        satuan="persen_apk", katalog_satuan="tidak_ada",
        bukti_satuan="judul 'Angka Partisipasi Kasar'; var.unit kosong; APK bisa > 100",
        sdg="4.2.2", katalog_sdg="4.2.2", bukti_sdg="judul = partisipasi PAUD",
        cakupan="anak 3–6 tahun (var.note); Susenas; Papua Pegunungan 2024–2025 RSE 25–50%",
        koreksi="satuan tidak_ada -> persen_apk",
    ),
    "var1221": dict(
        sumber="bps", tingkat="provinsi",
        nama="Proporsi individu yang menguasai/memiliki telepon genggam",
        satuan="persen", katalog_satuan="persen", bukti_satuan="var.unit: 'Persen'",
        sdg="5.b.1", katalog_sdg="5.b.1", bukti_sdg="var.label diawali '5.b.1*'",
        cakupan="individu umur 5 tahun ke atas (var.note); Susenas KOR; ada di snapshot 17 dan 20 Oktober",
    ),
    "SE.PRE.ENRR": dict(
        sumber="wdi", tingkat="nasional", nama="School enrollment, preprimary (% gross)",
        satuan="persen_apk", katalog_satuan="—", bukti_satuan="name: '(% gross)'",
        sdg="4.2.2", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="UNESCO; kelompok umur resmi prasekolah; 1970–2018", koreksi="kode SDG kosong -> 4.2.2",
    ),
    "IT.NET.USER.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Individuals using the Internet (% of population)",
        satuan="persen", katalog_satuan="—", bukti_satuan="name: '(% of population)'",
        sdg="17.8.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json; pengguna internet = 17.8.1",
        cakupan="ITU; memakai internet dalam 3 bulan terakhir", koreksi="kode SDG kosong -> 17.8.1",
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

# K-011: sel dengan galat sampling tinggi menurut var.note (dipakai aturan peringatan)
RSE_TINGGI = {("var1439", 9700, "2024"), ("var1439", 9700, "2025")}

RENTANG = {"persen": (0, 100), "persen_apk": (0, 250)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="APK PAUD: BPS (3–6 tahun) vs WDI prasekolah (umur resmi)",
         utama="var1439", rincian_utama="total", pembanding=[("SE.PRE.ENRR", "total")],
         jenis="selisih", kategori="definisi (kelompok umur acuan dan jenis layanan PAUD vs pendidikan prasekolah)",
         alasan_rincian="tanpa rincian",
         pertanyaan=[("Kelompok umur BPS?", "3–6 tahun (var.note)."),
                     ("WDI?", "Prasekolah pada umur resmi jenjang; sourceNote tidak menyebut angka umur. WDI berakhir 2018.")]),
    dict(id="P2", judul="Telepon genggam (BPS) vs pengguna internet (WDI): konteks",
         utama="var1221", rincian_utama="total", pembanding=[("IT.NET.USER.ZS", "total")],
         jenis="konteks", kategori="konsep berbeda: kepemilikan perangkat vs penggunaan internet", alasan_rincian="tanpa rincian",
         pertanyaan=[("Konsep sama?", "Tidak: menguasai/memiliki telepon genggam (umur 5+) vs memakai internet 3 bulan terakhir.")]),
    dict(id="P3", judul="Keterampilan TIK 15–24 vs 15–59 (BPS dengan BPS)",
         utama="var1451", rincian_utama="total", pembanding=[("var1447", "total")],
         jenis="konteks", kategori="kelompok umur berbeda; tidak dijumlah atau dirata-rata", alasan_rincian="tanpa rincian",
         pertanyaan=[("Boleh digabung?", "Tidak: 15–59 mencakup 15–24; menggabungkan menghitung dua kali.")]),
]
