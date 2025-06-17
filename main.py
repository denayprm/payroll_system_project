from system.data_loader import DataLoader
from system.data_cleaner import clean_data
from system.summarizer import create_monthly_summary, create_daily_records
from system.analyzer import analyze
from system.visualizer import visualize
import pandas as pd
from datetime import datetime

def main():
    print("\n📊 Memulai sistem analisis payroll...\n")

    loader = DataLoader()
    df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus = loader.load_data()
    df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus = clean_data(
        df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus
    )

    summary = create_monthly_summary(df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus)
    daily = create_daily_records(df_karyawan, df_kehadiran, df_lembur, df_pelanggaran)

    summary.to_csv('resources/output/monthly_summary.csv', index=False)
    daily.to_csv('resources/output/daily_records.csv', index=False)

    summary, dept_summary = analyze(summary)
    visualize(summary, dept_summary)

    print("\n✅ Analisis payroll selesai. Hasil telah disimpan.\n")

    now = datetime.now()
    wib_time = now.strftime("%A, %d-%m-%Y | %H:%M:%S WIB")
    print("© 2025 Deni Permana |", wib_time , "\n")

if __name__ == '__main__':
    main()
