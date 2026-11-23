"""Aturan validasi khas Kasus 20 (panduan kelompok bagian 4.4), plus tiga aturan peringatan.

Setiap fungsi menerima Silver dan mengembalikan baris yang melanggar (kosong = lolos).
"""
import pandas as pd

from src import konfigurasi as K

LUAS = {"ribu_hektar", "hektar", "km2"}


def luas_tidak_negatif_satu_satuan(silver):
    """Luas tidak negatif, dan satu seri luas hanya satu satuan."""
    s = silver[silver["satuan"].isin(LUAS)]
    buruk = s[s["nilai"] < 0]
    ganda = s.groupby("seri_kode")["satuan"].nunique()
    return pd.concat([buruk[["seri_kode", "wilayah_kode", "periode", "nilai"]],
                      ganda[ganda > 1].rename("satuan").reset_index()], ignore_index=True)


def komponen_dari_kamus(silver):
    """Rincian var2532 hanya enam komponen IKLH dari kamus; tidak ada total buatan."""
    s = silver[silver["seri_kode"] == "var2532"]
    sah = {f"komponen={v}" for v in K.KOMPONEN.values()}
    return s[~s["rincian"].isin(sah)][["periode", "wilayah_kode", "rincian"]]


def _selisih_jumlah(silver, seri, toleransi):
    s = silver[silver["seri_kode"] == seri]
    lebar = s.pivot_table(index=["wilayah_kode", "periode"], columns="rincian", values="nilai")
    if "total" not in lebar:
        return pd.DataFrame()
    rinci = lebar.drop(columns="total")
    lengkap = rinci.notna().all(axis=1) & lebar["total"].notna()
    beda = (rinci.sum(axis=1) - lebar["total"])[lengkap]
    return beda[beda.abs() > toleransi].round(3).rename("selisih").reset_index()


def jumlah_rincian_lahan(silver):
    """Lahan kritis dan kawasan hutan: jumlah rincian = rincian jumlah (toleransi pembulatan)."""
    return pd.concat([_selisih_jumlah(silver, "var588", 1.0).assign(seri_kode="var588"),
                      _selisih_jumlah(silver, "var1304", 0.15).assign(seri_kode="var1304")], ignore_index=True)


def hutan_plus_non_hutan(silver):
    """Peringatan: luas hutan + non hutan berbeda dari jumlah (tabel statis; CSV pratampil menandainya di kolom cek)."""
    return _selisih_jumlah(silver, K.LUAS, 0.15)


def kolom_2020_tergeser(silver):
    """Peringatan: luas hutan 2020 menyimpang > 50% dari rata-rata 2019 dan 2021 di provinsi yang sama.
    Pola ini muncul bila kolom tahun di tabel sumber tidak sejajar dengan baris nama provinsi."""
    s = silver[(silver["seri_kode"] == K.LUAS) & (silver["rincian"] == "tutupan=hutan")]
    lebar = s.pivot_table(index="wilayah_kode", columns="periode", values="nilai")
    if not {"2019", "2020", "2021"} <= set(lebar.columns):
        return pd.DataFrame()
    acuan = (lebar["2019"] + lebar["2021"]) / 2
    rel = (lebar["2020"] - acuan) / acuan
    hasil = lebar.loc[rel.abs() > 0.5, ["2019", "2020", "2021"]].assign(simpangan=rel[rel.abs() > 0.5].round(2))
    return hasil.reset_index()


ATURAN = [
    ("luas_tidak_negatif_satu_satuan", "luas >= 0 dan satu satuan per seri", True, luas_tidak_negatif_satu_satuan),
    ("komponen_dari_kamus", "rincian IKLH hanya enam komponen dari kamus", True, komponen_dari_kamus),
    ("jumlah_rincian_lahan", "lahan kritis dan kawasan hutan: jumlah rincian = rincian jumlah (peringatan)", False, jumlah_rincian_lahan),
    ("kolom_2020_tergeser", "luas hutan 2020 menyimpang > 50% dari 2019–2021 (peringatan: baris sumber tergeser)", False,
     kolom_2020_tergeser),
    ("hutan_plus_non_hutan", "luas hutan + non hutan ≠ jumlah (peringatan; ditandai 'cek' di CSV)", False, hutan_plus_non_hutan),
]
