"""Aturan khas Kasus 02 diuji dengan baris yang sengaja dirusak."""
import pandas as pd

from src.validasi import khusus


def test_aturan_khusus_lolos_pada_silver_asli(silver_contoh):
    for nama, _, keras, fungsi in khusus.ATURAN:
        if keras:
            assert fungsi(silver_contoh).empty, nama


def test_balita_lebih_kecil_dari_bayi_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[(rusak["seri_kode"] == khusus.BALITA) & (rusak["wilayah_kode"] == 9999)][0]
    rusak.loc[i, "nilai"] = 0.5
    assert not khusus.balita_tidak_kurang_dari_bayi(rusak).empty


def test_tahun_interpolasi_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    baris = rusak[rusak["seri_kode"] == khusus.BALITA].iloc[[0]].copy()
    baris["periode"] = "2014"
    rusak = pd.concat([rusak, baris], ignore_index=True)
    assert not khusus.bps_hanya_tahun_terbit(rusak).empty


def test_rujukan_hilang_tertangkap(silver_contoh):
    rusak = silver_contoh.copy()
    i = rusak.index[rusak["seri_kode"] == khusus.BAYI][0]
    rusak.loc[i, "rujukan_tahun"] = None
    assert not khusus.survei_kematian_punya_rujukan(rusak).empty
