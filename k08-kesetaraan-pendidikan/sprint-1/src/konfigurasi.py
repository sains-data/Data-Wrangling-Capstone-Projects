"""Keputusan wrangling Kasus 08 — Kesetaraan pendidikan.

Semua keputusan khas kasus ada di berkas ini supaya mudah ditinjau: identitas seri (jenjang dan jenis
rasio dari judul), satuan dan kode SDG beserta buktinya, kamus jenjang dan kelompok umur, pergantian
definisi, ambang anomali, dan pasangan rekonsiliasi. Setiap keputusan juga tercatat di log-keputusan.csv.
Ini salah satu jawaban yang dapat dipertahankan, bukan satu-satunya.
"""

KASUS = 8
SLUG = "kesetaraan-pendidikan"
JUDUL = "Kesetaraan pendidikan"

FORMAT_BPS = "json"

SERI = {
    "var304": dict(
        sumber="bps", tingkat="provinsi",
        nama="Angka Partisipasi Murni (APM) menurut jenjang SD, SMP, SM",
        satuan="persen", katalog_satuan="tidak_ada",
        bukti_satuan="judul 'Angka Partisipasi Murni'; var.unit kosong; APM hanya siswa usia jenjang, jadi <= 100",
        sdg="4.1", katalog_sdg="4.5.1",
        bukti_sdg="APM per jenjang bukan indeks paritas; jenjang dasar-menengah = target 4.1; berkas tidak menulis kode indikator",
        cakupan="Susenas; 2003–2025; mulai 2007 termasuk paket A/B/C (var.note)",
        koreksi="satuan tidak_ada -> persen; kode SDG 4.5.1 -> 4.1",
    ),
    "var2595": dict(
        sumber="bps", tingkat="provinsi",
        nama="Rasio APK SMA/sederajat kuintil pengeluaran terendah terhadap kuintil tertinggi",
        satuan="rasio_x100", katalog_satuan="tidak_ada",
        bukti_satuan="judul 'Rasio APK ... kuintil terendah/kuintil tertinggi'; var.unit kosong; nilai 32–124, Indonesia ±77: rasio dikali 100",
        sdg="4.5.1", katalog_sdg="4.5.1", bukti_sdg="var.label diawali '4.5.1*'; indeks paritas kuintil",
        cakupan="jenjang SMA; paritas kuintil (bukan jenis kelamin); 2020–2025", koreksi="satuan tidak_ada -> rasio_x100",
    ),
    "var2600": dict(
        sumber="bps", tingkat="provinsi",
        nama="Rasio APK perguruan tinggi perempuan terhadap laki-laki",
        satuan="rasio_x100", katalog_satuan="tidak_ada",
        bukti_satuan="judul 'Rasio APK ... perempuan/laki-laki'; var.unit kosong; nilai 62–260, Indonesia ±115: rasio dikali 100",
        sdg="4.5.1", katalog_sdg="4.5.1", bukti_sdg="var.label diawali '4.5.1*'; indeks paritas jenis kelamin",
        cakupan="jenjang perguruan tinggi; paritas jenis kelamin; 2020–2025", koreksi="satuan tidak_ada -> rasio_x100",
    ),
    "var1980": dict(
        sumber="bps", tingkat="provinsi",
        nama="Tingkat penyelesaian pendidikan menurut jenjang",
        satuan="persen", katalog_satuan="tidak_ada", bukti_satuan="var.note: 'persentase anak dan remaja yang berhasil menyelesaikan'",
        sdg="4.1.2", katalog_sdg="4.1.2", bukti_sdg="definisi di var.note = completion rate (umur 3–5 tahun di atas umur lulus)",
        cakupan="SD, SMP, SMA; 2015–2023", koreksi="satuan tidak_ada -> persen",
    ),
    "var2211": dict(
        sumber="bps", tingkat="provinsi",
        nama="Angka Partisipasi Sekolah (APS) menurut kelompok umur",
        satuan="persen", katalog_satuan="tidak_ada", bukti_satuan="judul 'Angka Partisipasi Sekolah'; var.unit kosong; nilai <= 100",
        sdg="—", katalog_sdg="—", bukti_sdg="tidak ada kode di berkas; APS tidak dipakai sebagai indikator SDG di kasus ini",
        cakupan="umur 7–12, 13–15, 16–18, 19–23; 2015–2025; var.note berisi definisi indikator lain (disabilitas)",
        koreksi="satuan tidak_ada -> persen; var.note tidak dipakai (salah tempel)",
    ),
    "SE.ENR.PRSC.FM.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="School enrollment, primary and secondary (gross), gender parity index (GPI)",
        satuan="rasio", katalog_satuan="—", bukti_satuan="name: 'gender parity index'",
        sdg="4.5.1", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="SD dan sekolah menengah; paritas jenis kelamin; 1970–2018", koreksi="kode SDG kosong -> 4.5.1",
    ),
    "SE.PRM.CMPT.ZS": dict(
        sumber="wdi", tingkat="nasional", nama="Primary completion rate, total (% of relevant age group)",
        satuan="persen_apk", katalog_satuan="—",
        bukti_satuan="sourceNote: gross intake ratio to the last grade, tanpa memandang umur (bisa > 100)",
        sdg="4.1.2", katalog_sdg="—", bukti_sdg="tercantum di metadata/sumber46_indikator.json",
        cakupan="rasio masuk kasar ke kelas terakhir SD; UNESCO", koreksi="kode SDG kosong -> 4.1.2",
    ),
}

RINCIAN_TOTAL_BPS = {"tidak ada"}
RINCIAN_BPS = {
    "var304": ("jenjang", {"SD/sederajat": "sd", "SMP/sederajat": "smp", "SM/sederajat": "sm"}),
    "var1980": ("jenjang", {"SD / Sederajat": "sd", "SMP / Sederajat": "smp", "SMA / Sederajat": "sma"}),
    "var2211": ("umur", {"7-12": "7-12", "13-15": "13-15", "16-18": "16-18", "19-23": "19-23"}),
}
RINCIAN_TOTAL_WHO = {"TOTAL", ""}
RINCIAN_DIMENSI = {}
RINCIAN_NILAI = {}
KODE_RINCIAN = {"jenjang": {"sd", "smp", "sm", "sma"}, "umur": {"7-12", "13-15", "16-18", "19-23"}}

DERET = {"var304": ["jenjang=sd", "jenjang=smp", "jenjang=sm"],
         "var1980": ["jenjang=sd", "jenjang=smp", "jenjang=sma"],
         "var2211": ["umur=7-12", "umur=13-15", "umur=16-18", "umur=19-23"]}

RUJUKAN_TAHUN = {}
TIDAK_TERBIT = {}
TAHUN_TERBIT = {}
PATAHAN_DEFINISI = {"var304": {"2007": "var.note: mulai 2007 APM mencakup pendidikan nonformal (paket A, B, C)"}}

# K-007: rasio BPS ditulis dikali 100 (paritas = 100), rasio WDI apa adanya (paritas = 1); diseragamkan di Gold
RENTANG = {"persen": (0, 100), "rasio": (0, 5), "rasio_x100": (0, 500), "persen_apk": (0, 250)}

ANOMALI = {"k_iqr": 1.5, "min_titik_samping": 6, "lompat_relatif": 0.20, "porsi_patahan": 0.70}

PASANGAN = [
    dict(id="P1", judul="Penyelesaian SD: BPS (kohort umur) vs WDI (rasio masuk kasar kelas terakhir)",
         utama="var1980", rincian_utama="jenjang=sd", pembanding=[("SE.PRM.CMPT.ZS", "total")],
         jenis="selisih", kategori="definisi berbeda: umur 3–5 tahun di atas umur lulus (BPS) vs siswa baru kelas terakhir tanpa memandang umur (WDI)",
         alasan_rincian="BPS jenjang=sd",
         pertanyaan=[("Definisi BPS?", "var.note: persentase anak yang menyelesaikan jenjang pada rentang umur 3–5 tahun di atas umur lulus."),
                     ("Definisi WDI?", "sourceNote: gross intake ratio to the last grade of primary, regardless of age; bisa > 100.")]),
    dict(id="P2", judul="Paritas: BPS APK PT perempuan/laki-laki vs WDI GPI SD+menengah",
         utama="var2600", rincian_utama="total", pembanding=[("SE.ENR.PRSC.FM.ZS", "total")],
         jenis="konteks", kategori="definisi berbeda: jenjang berbeda (PT vs SD dan menengah); skala BPS x100, WDI x1",
         alasan_rincian="tanpa rincian",
         pertanyaan=[("Jenis paritas sama?", "Ya, jenis kelamin. Jenjang berbeda, dan WDI berakhir 2018 sedangkan BPS mulai 2020.")]),
    dict(id="P3", judul="Paritas kuintil APK SMA (BPS): tanpa pembanding di paket",
         utama="var2595", rincian_utama="total", pembanding=[],
         jenis="konteks", kategori="tidak ada seri paritas kuintil di paket pembanding", alasan_rincian="tanpa rincian",
         pertanyaan=[("Apa jenis rasionya?", "Kuintil pengeluaran terendah dibagi tertinggi (judul JSON), bukan jenis kelamin.")]),
]
