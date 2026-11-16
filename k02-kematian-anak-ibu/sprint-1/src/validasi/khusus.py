"""Aturan validasi khas Kasus 02 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K

BALITA, BAYI = "var1373", "var1584"     # dipastikan dari var.label (log K-003)


def balita_tidak_kurang_dari_bayi(silver):
    """Pada wilayah, periode, dan jendela rujukan yang sama, AKBa >= AKB."""
    s = silver[silver["seri_kode"].isin([BALITA, BAYI]) & (silver["rincian"] == "total")]
    lebar = s.pivot_table(index=["wilayah_kode", "periode", "rujukan_tahun"], columns="seri_kode", values="nilai").dropna()
    if not {BALITA, BAYI} <= set(lebar.columns):
        return pd.DataFrame()
    return lebar[lebar[BALITA] < lebar[BAYI]].reset_index()


def bps_hanya_tahun_terbit(silver):
    """Tidak ada baris BPS di luar tahun yang diterbitkan (artinya tidak ada tahun hasil interpolasi)."""
    b = silver[silver["sumber"] == "bps"]
    terbit = [p in K.TAHUN_TERBIT.get(s, set()) for s, p in zip(b["seri_kode"], b["periode"])]
    return b[[not t for t in terbit]][["seri_kode", "wilayah_kode", "periode", "nilai"]]


def survei_kematian_punya_rujukan(silver):
    """Setiap baris seri kematian BPS membawa jendela rujukan."""
    s = silver[silver["seri_kode"].isin([BALITA, BAYI])]
    return s[s["rujukan_tahun"].isna()][["seri_kode", "wilayah_kode", "periode"]]


def who_wdi_balita_berdekatan(silver):
    """Peringatan: WHO dan WDI kematian balita (rincian total, tahun sama) berbeda lebih dari 10%."""
    s = silver[silver["seri_kode"].isin(["MDG_0000000007", "SH.DYN.MORT"]) & (silver["rincian"] == "total")]
    lebar = s.pivot_table(index="periode", columns="seri_kode", values="nilai").dropna()
    if lebar.empty:
        return pd.DataFrame()
    rel = (lebar["MDG_0000000007"] - lebar["SH.DYN.MORT"]).abs() / lebar["SH.DYN.MORT"]
    return lebar[rel > 0.10].assign(selisih_relatif=rel[rel > 0.10].round(3)).reset_index()


ATURAN = [
    ("balita_tidak_kurang_dari_bayi", "AKBa (var1373) ≥ AKB (var1584) pada wilayah, periode, dan rujukan yang sama", True,
     balita_tidak_kurang_dari_bayi),
    ("bps_hanya_tahun_terbit", "tidak ada tahun BPS di luar tahun terbit (tidak ada interpolasi tanpa penanda)", True,
     bps_hanya_tahun_terbit),
    ("survei_kematian_punya_rujukan", "baris var1373/var1584 punya rujukan_tahun", True, survei_kematian_punya_rujukan),
    ("who_wdi_balita_berdekatan", "WHO vs WDI kematian balita berbeda > 10% (peringatan: selisih vintage yang besar)", False,
     who_wdi_balita_berdekatan),
]
