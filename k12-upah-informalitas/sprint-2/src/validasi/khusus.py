"""Aturan validasi khas Kasus 12 (panduan kelompok bagian 4.4), plus satu aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K


def upah_positif_satu_satuan(silver):
    """Upah positif dan bersatuan rupiah_per_jam (BPS dan ILO)."""
    s = silver[silver["seri_kode"].isin(["var1172", "SDG_0851_SEX_OCU_NB"])]
    return s[(s["nilai"] <= 0) | (s["satuan"] != "rupiah_per_jam")][["seri_kode", "periode", "nilai", "satuan"]]


def total_klasifikasi_lain_sama(silver):
    """Total klasifikasi lain (ISCO08_TOTAL, ISCO88_TOTAL, AGGREGATE_TOTAL) sama dengan total utama pada sel yang sama."""
    buruk = []
    for seri, dim, lain in [("SDG_0851_SEX_OCU_NB", "jabatan", ["ISCO08_TOTAL", "ISCO88_TOTAL"]),
                            ("SDG_0831_SEX_ECO_RT", "sektor", ["AGGREGATE_TOTAL"])]:
        s = silver[silver["seri_kode"] == seri].copy()
        utama = s[~s["rincian"].str.contains(f"{dim}=")].rename(columns={"rincian": "rincian_utama"})
        utama = utama.set_index(["periode", "rincian_utama"])["nilai"]
        for kode in lain:
            x = s[s["rincian"].str.contains(f"{dim}={kode}")].copy()
            x["rincian_utama"] = x["rincian"].str.replace(rf";?{dim}={kode}", "", regex=True).str.strip(";").replace("", "total")
            g = x.set_index(["periode", "rincian_utama"])["nilai"].rename("lain").to_frame().join(utama.rename("utama"))
            g = g.dropna()
            buruk.append(g[(g["lain"] - g["utama"]).abs() > 1e-6].reset_index().assign(seri_kode=seri, kode=kode))
    return pd.concat(buruk, ignore_index=True) if buruk else pd.DataFrame()


def status_ilo_terdaftar(silver):
    """status_obs ILO terdaftar (B) atau kosong."""
    s = silver[silver["sumber"] == "ilostat"]
    return s[s["status_obs"].notna() & ~s["status_obs"].isin(K.STATUS_ILO)][["seri_kode", "periode", "status_obs"]]


def upah_bps_dekat_ilo(silver):
    """Peringatan: upah per jam BPS Indonesia berbeda > 20% dari ILO total pada tahun sama."""
    a = silver[(silver["seri_kode"] == "var1172") & (silver["wilayah_kode"] == 9999)].set_index("periode")["nilai"]
    b = silver[(silver["seri_kode"] == "SDG_0851_SEX_OCU_NB") & (silver["rincian"] == "total")].set_index("periode")["nilai"]
    g = pd.DataFrame({"bps": a, "ilo": b}).dropna()
    g["selisih_relatif"] = ((g["bps"] - g["ilo"]) / g["ilo"]).round(3)
    return g[g["selisih_relatif"].abs() > 0.2].reset_index()


ATURAN = [
    ("upah_positif_satu_satuan", "upah > 0 dan bersatuan rupiah_per_jam", True, upah_positif_satu_satuan),
    ("total_klasifikasi_lain_sama", "total klasifikasi lain = total utama", True, total_klasifikasi_lain_sama),
    ("status_ilo_terdaftar", "status_obs ILO terdaftar (B) atau kosong", True, status_ilo_terdaftar),
    ("upah_bps_dekat_ilo", "upah BPS vs ILO berbeda > 20% (peringatan)", False, upah_bps_dekat_ilo),
]
