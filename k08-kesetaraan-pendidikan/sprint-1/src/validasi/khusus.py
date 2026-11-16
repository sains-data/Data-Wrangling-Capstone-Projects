"""Aturan validasi khas Kasus 08 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd


def rasio_paritas_masuk_akal(silver):
    """Rasio paritas positif dan di 0,2–3 setelah skala disamakan (BPS ditulis x100, WDI x1)."""
    s = silver[silver["seri_kode"].isin(["var2595", "var2600", "SE.ENR.PRSC.FM.ZS"])].copy()
    s["paritas"] = s["nilai"].where(s["satuan"] != "rasio_x100", s["nilai"] / 100)
    return s[(s["paritas"] <= 0.2) | (s["paritas"] > 3)][["seri_kode", "wilayah_kode", "periode", "nilai"]]


def satu_satuan_per_jenis(silver):
    """Rasio bersatuan 'rasio', angka partisipasi bersatuan 'persen' (bukan tidak_ada)."""
    harus = {"var2595": "rasio_x100", "var2600": "rasio_x100", "SE.ENR.PRSC.FM.ZS": "rasio",
             "var304": "persen", "var1980": "persen", "var2211": "persen"}
    s = silver[silver["seri_kode"].isin(harus)]
    return s[s["satuan"] != s["seri_kode"].map(harus)][["seri_kode", "periode", "satuan"]]


def apm_tanpa_total(silver):
    """APM, penyelesaian, dan APS tidak punya total buatan dari menjumlah jenjang/kelompok umur."""
    s = silver[silver["seri_kode"].isin(["var304", "var1980", "var2211"])]
    return s[s["rincian"] == "total"][["seri_kode", "wilayah_kode", "periode"]]


def penyelesaian_sma_tidak_melebihi_sd(silver):
    """Peringatan: tingkat penyelesaian SMA melebihi SD pada provinsi dan tahun yang sama."""
    s = silver[silver["seri_kode"] == "var1980"]
    lebar = s.pivot_table(index=["wilayah_kode", "periode"], columns="rincian", values="nilai").dropna()
    if lebar.empty:
        return pd.DataFrame()
    return lebar[lebar["jenjang=sma"] > lebar["jenjang=sd"]].reset_index()


ATURAN = [
    ("rasio_paritas_masuk_akal", "rasio paritas di 0,2–3 (BPS dibagi 100)", True, rasio_paritas_masuk_akal),
    ("satu_satuan_per_jenis", "rasio BPS rasio_x100, rasio WDI rasio, angka partisipasi persen", True, satu_satuan_per_jenis),
    ("apm_tanpa_total", "APM, penyelesaian, APS tanpa total buatan", True, apm_tanpa_total),
    ("penyelesaian_sma_tidak_melebihi_sd", "penyelesaian SMA > SD pada sel yang sama (peringatan)", False,
     penyelesaian_sma_tidak_melebihi_sd),
]
