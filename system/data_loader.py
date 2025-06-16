# data_loader.py
import pandas as pd

class DataLoader:
    def __init__(self, data_dir='resources'):
        self.data_dir = data_dir

    def load_data(self):
        df_karyawan = pd.read_csv(f'{self.data_dir}/main_data/karyawan.csv')
        df_kehadiran = pd.read_csv(f'{self.data_dir}/main_data/kehadiran.csv')
        df_lembur = pd.read_csv(f'{self.data_dir}/main_data/lembur.csv')
        df_pelanggaran = pd.read_csv(f'{self.data_dir}/main_data/pelanggaran.csv')
        df_bonus = pd.read_csv(f'{self.data_dir}/main_data/bonus.csv')

        df_karyawan['tanggal_masuk'] = pd.to_datetime(df_karyawan['tanggal_masuk'])
        df_kehadiran['tanggal'] = pd.to_datetime(df_kehadiran['tanggal'])
        df_kehadiran['waktu_masuk'] = pd.to_datetime(df_kehadiran['waktu_masuk'])
        df_kehadiran['waktu_keluar'] = pd.to_datetime(df_kehadiran['waktu_keluar'])
        df_lembur['tanggal'] = pd.to_datetime(df_lembur['tanggal'])
        df_lembur['jam_mulai'] = pd.to_datetime(df_lembur['jam_mulai'])
        df_lembur['jam_selesai'] = pd.to_datetime(df_lembur['jam_selesai'])
        df_pelanggaran['tanggal'] = pd.to_datetime(df_pelanggaran['tanggal'])

        return df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus

print("\n📊 Data Loader telah dilakukan...")
