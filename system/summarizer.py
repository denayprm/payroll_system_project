# summarizer.py
import pandas as pd

def create_monthly_summary(df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus):
    kehadiran_summary = df_kehadiran.groupby('karyawan_id').agg({
        'status_kehadiran': lambda x: (x == 'Hadir').sum(),
        'keterlambatan_menit': 'sum'
    }).rename(columns={
        'status_kehadiran': 'total_hari_hadir',
        'keterlambatan_menit': 'total_keterlambatan'
    })

    lembur_summary = df_lembur[df_lembur['status_approval'] == 'Disetujui'].groupby('karyawan_id').agg({
        'durasi_jam': 'sum'
    }).rename(columns={'durasi_jam': 'total_jam_lembur'})

    pelanggaran_summary = df_pelanggaran.groupby('karyawan_id').agg({
        'sanksi_potongan': 'sum'
    }).rename(columns={'sanksi_potongan': 'total_potongan'})

    bonus_summary = df_bonus.groupby('karyawan_id').agg({
        'jumlah_bonus': 'sum'
    }).rename(columns={'jumlah_bonus': 'total_bonus'})

    summary = df_karyawan.merge(kehadiran_summary, on='karyawan_id', how='left') \
                        .merge(lembur_summary, on='karyawan_id', how='left') \
                        .merge(pelanggaran_summary, on='karyawan_id', how='left') \
                        .merge(bonus_summary, on='karyawan_id', how='left')

    summary.fillna(0, inplace=True)
    return summary

def create_daily_records(df_karyawan, df_kehadiran, df_lembur, df_pelanggaran):
    daily = df_kehadiran.merge(df_karyawan, on='karyawan_id', how='left')
    daily = daily.merge(df_lembur[['karyawan_id', 'tanggal', 'durasi_jam']], on=['karyawan_id', 'tanggal'], how='left')
    daily = daily.merge(df_pelanggaran[['karyawan_id', 'tanggal', 'sanksi_potongan']], on=['karyawan_id', 'tanggal'], how='left')
    daily.fillna(0, inplace=True)
    return daily
