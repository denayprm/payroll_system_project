# summarizer.py
import pandas as pd

def create_monthly_summary(df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus):
    # Ambil info bulan dan tahun dari df_bonus untuk keperluan grafik
    df_bonus['periode'] = pd.to_datetime(df_bonus['periode_tahun'].astype(str) + '-' + df_bonus['periode_bulan'].astype(str) + '-01')
    df_bonus['bulan'] = df_bonus['periode'].dt.strftime('%B')
    df_bonus['tahun'] = df_bonus['periode'].dt.year

    bonus_summary = df_bonus.groupby(['karyawan_id', 'bulan', 'tahun']).agg({
        'jumlah_bonus': 'sum'
    }).rename(columns={'jumlah_bonus': 'total_bonus'}).reset_index()

    # Buat kombinasi untuk tiap karyawan dan periode
    summary_list = []

    for (karyawan_id, bulan, tahun), df_b in bonus_summary.groupby(['karyawan_id', 'bulan', 'tahun']):
        karyawan_info = df_karyawan[df_karyawan['karyawan_id'] == karyawan_id].iloc[0]

        hadir = df_kehadiran[(df_kehadiran['karyawan_id'] == karyawan_id) &
                            (df_kehadiran['tanggal'].dt.month_name() == bulan) &
                            (df_kehadiran['tanggal'].dt.year == tahun)]

        lembur = df_lembur[(df_lembur['karyawan_id'] == karyawan_id) &
                        (df_lembur['tanggal'].dt.month_name() == bulan) &
                        (df_lembur['tanggal'].dt.year == tahun) &
                        (df_lembur['status_approval'] == 'Disetujui')]

        pelanggaran = df_pelanggaran[(df_pelanggaran['karyawan_id'] == karyawan_id) &
                                    (df_pelanggaran['tanggal'].dt.month_name() == bulan) &
                                    (df_pelanggaran['tanggal'].dt.year == tahun)]

        summary_list.append({
            'karyawan_id': karyawan_id,
            'nama': karyawan_info['nama'],
            'departemen': karyawan_info['departemen'],
            'jabatan': karyawan_info['jabatan'],
            'gaji_pokok': karyawan_info['gaji_pokok'],
            'status_kepegawaian': karyawan_info['status_kepegawaian'],
            'bulan': bulan,
            'tahun': tahun,
            'total_hari_hadir': (hadir['status_kehadiran'] == 'Hadir').sum(),
            'total_keterlambatan': hadir['keterlambatan_menit'].sum(),
            'total_jam_lembur': lembur['durasi_jam'].sum(),
            'total_potongan': pelanggaran['sanksi_potongan'].sum(),
            'total_bonus': df_b['total_bonus'].sum()
        })

    summary_df = pd.DataFrame(summary_list)
    summary_df.fillna(0, inplace=True)
    return summary_df


def create_daily_records(df_karyawan, df_kehadiran, df_lembur, df_pelanggaran):
    daily = df_kehadiran.merge(df_karyawan, on='karyawan_id', how='left')
    daily = daily.merge(df_lembur[['karyawan_id', 'tanggal', 'durasi_jam']], on=['karyawan_id', 'tanggal'], how='left')
    daily = daily.merge(df_pelanggaran[['karyawan_id', 'tanggal', 'sanksi_potongan']], on=['karyawan_id', 'tanggal'], how='left')
    daily['bulan'] = daily['tanggal'].dt.strftime('%B')
    daily['tahun'] = daily['tanggal'].dt.year
    daily.fillna(0, inplace=True)
    return daily
