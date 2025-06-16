# main.py
from data_loader import DataLoader
from data_cleaner import clean_data
from summarizer import create_monthly_summary, create_daily_records
from analyzer import analyze
from visualizer import visualize
import pandas as pd


def main():
    print("\n📊 Memulai sistem analisis payroll...")

    loader = DataLoader()
    df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus = loader.load_data()
    df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus = clean_data(
        df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus
    )

    summary = create_monthly_summary(df_karyawan, df_kehadiran, df_lembur, df_pelanggaran, df_bonus)
    daily = create_daily_records(df_karyawan, df_kehadiran, df_lembur, df_pelanggaran)

    summary.to_csv('resources/monthly_summary.csv', index=False)
    daily.to_csv('resources/daily_records.csv', index=False)

    summary, dept_summary = analyze(summary)
    visualize(summary, dept_summary)

    print("\n✅ Analisis payroll selesai. Hasil telah disimpan.")

if __name__ == '__main__':
    main()
