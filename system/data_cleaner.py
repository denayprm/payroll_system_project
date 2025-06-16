# data_cleaner.py
import pandas as pd

def clean_data(df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus):
    df_karyawan.drop_duplicates(inplace=True)
    df_kehadiran.drop_duplicates(inplace=True)

    df_bonus['jumlah_bonus'] = pd.to_numeric(df_bonus['jumlah_bonus'], errors='coerce')
    df_pelanggaran['sanksi_potongan'] = pd.to_numeric(df_pelanggaran['sanksi_potongan'], errors='coerce')
    df_lembur['durasi_jam'] = pd.to_numeric(df_lembur['durasi_jam'], errors='coerce')

    return df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus

print("\n📊 Data Cleaner telah dilakukan...")
