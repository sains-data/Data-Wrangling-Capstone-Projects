"""Aturan validasi khas Kasus 05 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K
from src import wilayah as W


def profesi_dari_kamus(silver):
    """Setiap baris var1477 punya rincian profesi yang ada di kamus (tidak ada 'total' atau profesi baru)."""
    s = silver[silver["seri_kode"] == "var1477"]
    sah = {f"profesi={v}" for v in K.PROFESI.values()}
    return s[~s["rincian"].isin(sah)][["periode", "wilayah_kode", "rincian"]]


def kepadatan_dua_satuan_terpisah(silver):
    """BPS per 100.000 dan WHO per 10.000 tidak boleh tercampur dalam satu seri."""
    harus = {"var1477": "per_100000_penduduk", "HWF_0001": "per_10000_penduduk", "HWF_0006": "per_10000_penduduk"}
    s = silver[silver["seri_kode"].isin(harus)]
    return s[s["satuan"] != s["seri_kode"].map(harus)][["seri_kode", "periode", "satuan"]]


def jkn_tidak_sebelum_terbit(silver):
    """Tidak ada baris JKN sebelum seri terbit (2022): tidak ada imputasi ke belakang."""
    s = silver[(silver["seri_kode"] == "var2279") & (silver["periode"] < "2022")]
    return s[["wilayah_kode", "periode", "nilai"]]


def dokter_who_dekat_bps(silver):
    """Peringatan: dokter WHO (per 10.000) lebih kecil dari dokter umum BPS (per 100.000 x 0,1) pada tahun sama.
    WHO juga menghitung spesialis, jadi angkanya seharusnya tidak lebih kecil."""
    b = silver[(silver["seri_kode"] == "var1477") & (silver["rincian"] == "profesi=dokter_umum")
               & (silver["wilayah_kode"] == W.INDONESIA)].set_index("periode")["nilai"] * 0.1
    w = silver[silver["seri_kode"] == "HWF_0001"].set_index("periode")["nilai"]
    gabung = pd.DataFrame({"bps_per_10000": b, "who_per_10000": w}).dropna()
    return gabung[gabung["who_per_10000"] < gabung["bps_per_10000"]].reset_index()


ATURAN = [
    ("profesi_dari_kamus", "rincian var1477 hanya profesi yang ada di kamus", True, profesi_dari_kamus),
    ("kepadatan_dua_satuan_terpisah", "var1477 per 100.000, HWF per 10.000 (diseragamkan di Gold, bukan di Silver)", True,
     kepadatan_dua_satuan_terpisah),
    ("jkn_tidak_sebelum_terbit", "tidak ada baris JKN sebelum 2022", True, jkn_tidak_sebelum_terbit),
    ("dokter_who_dekat_bps", "dokter WHO < dokter umum BPS setelah satuan disamakan (peringatan)", False, dokter_who_dekat_bps),
]
