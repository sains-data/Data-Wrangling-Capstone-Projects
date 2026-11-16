"""Aturan validasi khas Kasus 22 (panduan kelompok bagian 4.4), plus tiga aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos). Berkas yang angkanya
dijumlahkan dari kab/kota dibaca dari reports/bnpb-agregasi.csv (ditulis src/silver/bangun.py).
"""
import pandas as pd

from src.laporan import ROOT

KUNCI = ["seri_kode", "wilayah_kode", "periode", "rincian"]
CACAH = {"kejadian", "korban_meninggal", "korban_hilang", "korban_luka_sakit", "korban_mengungsi",
         "korban_terdampak", "korban_terdampak_mengungsi", "jumlah_penduduk"}


def _bnpb(silver):
    return silver[silver["sumber"] == "bnpb"]


def berkas_kabkota():
    jalur = ROOT / "reports" / "bnpb-agregasi.csv"
    return set(pd.read_csv(jalur)["_berkas_raw"]) if jalur.exists() else set()


def cacah_bilangan_bulat(silver):
    """Jumlah kejadian dan jiwa adalah bilangan bulat (galat titik mengambang rumus Excel sudah dibulatkan)."""
    b = _bnpb(silver)
    b = b[b["seri_kode"].isin(CACAH)]
    return b[b["nilai"] != b["nilai"].round()][KUNCI + ["nilai", "_berkas_raw"]]


def jenis_menjumlah_ke_total(silver):
    """Di berkas yang memuat baris Total dan baris per jenis, jumlah jenis = Total."""
    b = _bnpb(silver)
    k = ["seri_kode", "wilayah_kode", "periode", "_berkas_raw"]
    total = b[b["rincian"] == "total"].set_index(k)["nilai"].rename("total")
    jenis = b[b["rincian"].str.startswith("jenis_bencana=") & ~b["rincian"].str.contains(";")]
    jml = jenis.groupby(k)["nilai"].sum().rename("jumlah_jenis")
    g = pd.concat([total, jml], axis=1, join="inner")
    return g[(g["total"] - g["jumlah_jenis"]).abs() > 1e-9].reset_index()


def per_100rb_dihitung_ulang(silver):
    """Angka per 100.000 = pembilang / Jumlah Penduduk x 100.000 (selisih > 0,01 = gagal). Pembilang dari tabel
    provinsi 2025 dengan wilayah (termasuk baris INDONESIA) dan jenis yang sama."""
    b = _bnpb(silver)
    b = b[b["periode"] == "2025"]
    pend = b[b["seri_kode"] == "jumlah_penduduk"].drop_duplicates("wilayah_kode").set_index("wilayah_kode")["nilai"]
    # tabel satu ukuran per provinsi; rekapitulasi nasional 2025 tidak dipakai agar baris Indonesia tidak terhitung dua kali
    tabel = b[b["_berkas_raw"].str.contains("menurut-provinsi-2025")
              & ~b["_berkas_raw"].str.contains("per-100|rekapitulasi")]
    hasil = []
    for laju, pembilang in (("korban_mengungsi_per_100rb", ["korban_mengungsi"]),
                            ("korban_meninggal_hilang_per_100rb", ["korban_meninggal", "korban_hilang"])):
        n = tabel[tabel["seri_kode"].isin(pembilang)].groupby(["wilayah_kode", "rincian"])["nilai"].sum()
        r = b[b["seri_kode"] == laju].set_index(["wilayah_kode", "rincian"])["nilai"]
        g = pd.concat([r.rename("terbit"), n.rename("pembilang")], axis=1, join="inner").reset_index()
        g["hitung"] = g["pembilang"] / g["wilayah_kode"].map(pend) * 100_000
        g["seri_kode"] = laju
        hasil.append(g[(g["hitung"] - g["terbit"]).abs() > 0.01])
    return pd.concat(hasil, ignore_index=True)


def _kab_vs_prov(silver):
    b = _bnpb(silver)
    kab = berkas_kabkota()
    a = b[b["_berkas_raw"].isin(kab)]
    p = b[~b["_berkas_raw"].isin(kab) & (b["wilayah_kode"] != 9999)]
    m = a.merge(p, on=KUNCI, suffixes=("_kabkota", "_provinsi"))
    m["selisih"] = m["nilai_kabkota"] - m["nilai_provinsi"]
    return m[KUNCI + ["nilai_kabkota", "nilai_provinsi", "selisih", "_berkas_raw_kabkota", "_berkas_raw_provinsi"]]


def kejadian_kabkota_tidak_kurang(silver):
    """Peringatan: kejadian hasil jumlah kab/kota < angka provinsi. Kejadian lintas kab/kota dihitung di setiap
    kab/kota terdampak (Keterangan), jadi jumlah kab/kota boleh lebih besar, tidak boleh lebih kecil."""
    m = _kab_vs_prov(silver)
    m = m[(m["seri_kode"] == "kejadian") & (m["selisih"] < 0)]
    return m.drop_duplicates(KUNCI + ["nilai_kabkota", "nilai_provinsi"])


def korban_kabkota_sama_provinsi(silver):
    """Peringatan: korban hasil jumlah kab/kota berbeda dari angka provinsi (satu orang tidak dihitung dua kali)."""
    m = _kab_vs_prov(silver)
    m = m[(m["seri_kode"] != "kejadian") & (m["selisih"] != 0)]
    return m.drop_duplicates(KUNCI + ["nilai_kabkota", "nilai_provinsi"])


def indonesia_sama_lintas_berkas(silver):
    """Peringatan: baris Indonesia untuk seri, tahun, dan jenis yang sama berbeda antarberkas (berkas jumlahan
    kab/kota tidak ikut). Silver tidak diubah; berkas yang dipakai Gold diputuskan di Sprint 2."""
    b = _bnpb(silver)
    b = b[(b["wilayah_kode"] == 9999) & ~b["_berkas_raw"].isin(berkas_kabkota())]
    g = b.groupby(KUNCI)["nilai"].agg(["nunique", "min", "max", "size"])
    return g[g["nunique"] > 1].reset_index()


ATURAN = [
    ("cacah_bilangan_bulat", "kejadian dan jiwa bilangan bulat", True, cacah_bilangan_bulat),
    ("jenis_menjumlah_ke_total", "jumlah per jenis = baris Total di berkas yang sama", True, jenis_menjumlah_ke_total),
    ("per_100rb_dihitung_ulang", "angka per 100.000 = pembilang / penduduk x 100.000", True, per_100rb_dihitung_ulang),
    ("kejadian_kabkota_tidak_kurang", "kejadian jumlah kab/kota < provinsi (peringatan)", False, kejadian_kabkota_tidak_kurang),
    ("korban_kabkota_sama_provinsi", "korban jumlah kab/kota ≠ provinsi (peringatan)", False, korban_kabkota_sama_provinsi),
    ("indonesia_sama_lintas_berkas", "baris Indonesia berbeda antarberkas (peringatan)", False, indonesia_sama_lintas_berkas),
]
