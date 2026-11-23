"""Aturan validasi khas Kasus 16 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K


def tanpa_imputasi(silver):
    """Tidak ada nilai imputasi: pendapatan pemerintah hanya 2015–2016 dan di bawah-median hanya tahun terbit."""
    batas = {"var1254": {"2015", "2016"}, "var2011": {str(t) for t in range(2018, 2024)}}
    s = silver[silver["seri_kode"].isin(batas)]
    luar = [p not in batas[k] for k, p in zip(s["seri_kode"], s["periode"])]
    return s[luar][["seri_kode", "wilayah_kode", "periode"]]


def layanan_dari_kamus(silver):
    """Rincian var2016 hanya empat layanan dari kamus; tidak ada total buatan."""
    s = silver[silver["seri_kode"] == "var2016"]
    sah = {f"layanan={v}" for v in K.LAYANAN.values()}
    return s[~s["rincian"].isin(sah)][["periode", "wilayah_kode", "rincian"]]


def ilo_status_dan_proyeksi(silver):
    """status_obs ILO terdaftar (A, R, M) atau kosong; tahun > 2026 terdaftar sebagai proyeksi."""
    s = silver[silver["sumber"] == "ilostat"]
    salah_status = s[s["status_obs"].notna() & ~s["status_obs"].isin(K.STATUS_ILO)]
    depan = s[s["periode"].str[:4].astype(int) > K.TAHUN_UNDUH]
    salah_tahun = depan[[p not in K.PROYEKSI.get(k, set()) for k, p in zip(depan["seri_kode"], depan["periode"])]]
    return pd.concat([salah_status, salah_tahun])[["seri_kode", "periode", "status_obs"]]


def bps_dekat_wdi(silver):
    """Peringatan: di bawah 50% median BPS Indonesia berbeda > 3 poin dari WDI pada tahun sama."""
    a = silver[(silver["seri_kode"] == "var2011") & (silver["wilayah_kode"] == 9999)].set_index("periode")["nilai"]
    b = silver[silver["seri_kode"] == "SI.DST.50MD"].set_index("periode")["nilai"]
    g = pd.DataFrame({"bps": a, "wdi": b}).dropna()
    return g[(g["bps"] - g["wdi"]).abs() > 3].reset_index()


ATURAN = [
    ("tanpa_imputasi", "tidak ada tahun di luar tahun terbit (tanpa imputasi)", True, tanpa_imputasi),
    ("layanan_dari_kamus", "rincian layanan dasar dari kamus", True, layanan_dari_kamus),
    ("ilo_status_dan_proyeksi", "status ILO terdaftar; tahun > 2026 terdaftar proyeksi", True, ilo_status_dan_proyeksi),
    ("bps_dekat_wdi", "di bawah 50% median BPS vs WDI > 3 poin (peringatan)", False, bps_dekat_wdi),
]
