"""Aturan validasi khas Kasus 13 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K

ANAK = ["SDG_A871_SEX_AGE_RT", "SDG_B871_SEX_AGE_RT"]


def umur_anak_dari_kamus(silver):
    """Setiap baris ILO pekerja anak punya rincian umur yang terdaftar di kamus."""
    s = silver[silver["seri_kode"].isin(ANAK)]
    umur = s["rincian"].str.extract(r"umur=([^;]+)")[0]
    return s[~umur.isin(K.KODE_RINCIAN["umur"])][["seri_kode", "periode", "rincian"]]


def b871_tidak_di_bawah_a871(silver):
    """Kegiatan ekonomi + pekerjaan rumah tangga (B871) tidak lebih kecil dari kegiatan ekonomi saja (A871)."""
    s = silver[silver["seri_kode"].isin(ANAK)]
    lebar = s.pivot_table(index=["periode", "rincian"], columns="seri_kode", values="nilai").dropna()
    if len(lebar.columns) < 2:
        return pd.DataFrame()
    return lebar[lebar["SDG_B871_SEX_AGE_RT"] < lebar["SDG_A871_SEX_AGE_RT"] - 1e-9].reset_index()


def status_ilo_terdaftar(silver):
    """status_obs ILO terdaftar (B) atau kosong."""
    s = silver[silver["sumber"] == "ilostat"]
    return s[s["status_obs"].notna() & ~s["status_obs"].isin(K.STATUS_ILO)][["seri_kode", "periode", "status_obs"]]


def neet_bps_dekat_ilo(silver):
    """Peringatan: NEET BPS Indonesia berbeda > 2 poin dari ILO pada tahun sama."""
    a = silver[(silver["seri_kode"] == "var1186") & (silver["wilayah_kode"] == 9999)].set_index("periode")["nilai"]
    b = silver[(silver["seri_kode"] == "SDG_0861_SEX_RT") & (silver["rincian"] == "total")].set_index("periode")["nilai"]
    g = pd.DataFrame({"bps": a, "ilo": b}).dropna()
    return g[(g["bps"] - g["ilo"]).abs() > 2].reset_index()


ATURAN = [
    ("umur_anak_dari_kamus", "rincian umur ILO pekerja anak dari kamus", True, umur_anak_dari_kamus),
    ("b871_tidak_di_bawah_a871", "B871 >= A871 pada sel yang sama", True, b871_tidak_di_bawah_a871),
    ("status_ilo_terdaftar", "status_obs ILO terdaftar (B) atau kosong", True, status_ilo_terdaftar),
    ("neet_bps_dekat_ilo", "NEET BPS vs ILO > 2 poin (peringatan)", False, neet_bps_dekat_ilo),
]
