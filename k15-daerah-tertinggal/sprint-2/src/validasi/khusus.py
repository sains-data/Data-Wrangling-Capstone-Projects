"""Aturan validasi khas Kasus 15 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd


def jumlah_desa_sama_rincian(silver):
    """Desa tertinggal: rincian jumlah = sangat tertinggal + tertinggal pada provinsi dan tahun yang sama."""
    s = silver[silver["seri_kode"] == "var2191"]
    lebar = s.pivot_table(index=["wilayah_kode", "periode"], columns="rincian", values="nilai").fillna(0)
    if lebar.empty:
        return pd.DataFrame()
    beda = lebar["total"] - lebar.get("status_desa=sangat_tertinggal", 0) - lebar.get("status_desa=tertinggal", 0)
    return lebar[beda.abs() > 0.5].assign(selisih=beda[beda.abs() > 0.5]).reset_index()


def jumlah_desa_bilangan_bulat(silver):
    """Jumlah desa adalah bilangan bulat tidak negatif."""
    s = silver[silver["satuan"] == "desa"]
    return s[(s["nilai"] < 0) | (s["nilai"] % 1 != 0)][["seri_kode", "wilayah_kode", "periode", "nilai"]]


def semester_hanya_untuk_s1_s2(silver):
    """jenis_periode semester hanya untuk periode AAAA-S1/AAAA-S2, dan tahun hanya untuk AAAA."""
    sem = (silver["jenis_periode"] == "semester") & ~silver["periode"].str.fullmatch(r"\d{4}-S[12]")
    th = (silver["jenis_periode"] == "tahun") & ~silver["periode"].str.fullmatch(r"\d{4}")
    return silver[sem | th][["seri_kode", "periode", "jenis_periode"]]


def kota_tidak_lebih_miskin(silver):
    """Peringatan: P0 perkotaan melebihi perdesaan pada provinsi dan periode yang sama."""
    s = silver[silver["seri_kode"] == "var192"]
    lebar = s.pivot_table(index=["wilayah_kode", "periode"], columns="rincian", values="nilai").dropna()
    if lebar.empty:
        return pd.DataFrame()
    return lebar[lebar["daerah=URBAN"] > lebar["daerah=RURAL"]].reset_index()


ATURAN = [
    ("jumlah_desa_sama_rincian", "desa: jumlah = sangat tertinggal + tertinggal", True, jumlah_desa_sama_rincian),
    ("jumlah_desa_bilangan_bulat", "jumlah desa bilangan bulat >= 0", True, jumlah_desa_bilangan_bulat),
    ("semester_hanya_untuk_s1_s2", "jenis_periode semester hanya AAAA-S1/S2, tahun hanya AAAA", True, semester_hanya_untuk_s1_s2),
    ("kota_tidak_lebih_miskin", "P0 perkotaan > perdesaan (peringatan)", False, kota_tidak_lebih_miskin),
]
