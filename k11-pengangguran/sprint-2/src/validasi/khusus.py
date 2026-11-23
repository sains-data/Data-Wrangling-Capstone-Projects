"""Aturan validasi khas Kasus 11 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K

POLA = {"tahun": r"\d{4}", "bulan": r"\d{4}-(0[1-9]|1[0-2])", "triwulan": r"\d{4}-Q[1-4]", "semester": r"\d{4}-S[12]"}


def jenis_periode_sesuai_bentuk(silver):
    """jenis_periode sesuai bentuk periode di setiap baris (tahun AAAA, bulan AAAA-MM, triwulan AAAA-Qn)."""
    cocok = [bool(pd.Series([p]).str.fullmatch(POLA.get(j, "$^")).iloc[0]) for p, j in zip(silver["periode"], silver["jenis_periode"])]
    return silver[[not c for c in cocok]][["seri_kode", "periode", "jenis_periode"]]


def bps_hanya_feb_agu_atau_tahun(silver):
    """Bulan BPS hanya Februari (02) atau Agustus (08); bulan tidak dirata-rata menjadi tahun sesudah 2004."""
    b = silver[silver["seri_kode"] == "var543"]
    bulan = b[b["jenis_periode"] == "bulan"]["periode"].str[-2:]
    salah_bulan = b.loc[bulan.index[~bulan.isin(["02", "08"])]]
    tahun_baru = b[(b["jenis_periode"] == "tahun") & (b["periode"] > "2004")]
    return pd.concat([salah_bulan, tahun_baru])[["periode", "jenis_periode", "wilayah_kode"]]


def status_ilo_terdaftar(silver):
    """status_obs ILO hanya kode yang ditemukan dan didaftar (B, U) atau kosong."""
    s = silver[silver["sumber"] == "ilostat"]
    return s[s["status_obs"].notna() & ~s["status_obs"].isin(K.STATUS_ILO)][["seri_kode", "periode", "status_obs"]]


def bps_agustus_dekat_ilo(silver):
    """Peringatan: TPT BPS Agustus berbeda > 1 poin dari ILO SDG 8.5.2 total pada tahun yang sama."""
    b = silver[(silver["seri_kode"] == "var543") & (silver["wilayah_kode"] == 9999) & silver["periode"].str.endswith("-08")]
    b = b.set_index(b["periode"].str[:4])["nilai"]
    i = silver[(silver["seri_kode"] == "SDG_0852_SEX_AGE_RT") & (silver["rincian"] == "total")].set_index("periode")["nilai"]
    g = pd.DataFrame({"bps_agustus": b, "ilo": i}).dropna()
    g["selisih"] = (g["bps_agustus"] - g["ilo"]).round(2)
    return g[g["selisih"].abs() > 1].reset_index()


ATURAN = [
    ("jenis_periode_sesuai_bentuk", "jenis_periode sesuai bentuk periode (termasuk triwulan ILO)", True, jenis_periode_sesuai_bentuk),
    ("bps_hanya_feb_agu_atau_tahun", "bulan BPS hanya 02/08; tidak ada tahun buatan sesudah 2004", True, bps_hanya_feb_agu_atau_tahun),
    ("status_ilo_terdaftar", "status_obs ILO terdaftar (B, U) atau kosong", True, status_ilo_terdaftar),
    ("bps_agustus_dekat_ilo", "TPT BPS Agustus vs ILO > 1 poin (peringatan: definisi)", False, bps_agustus_dekat_ilo),
]
