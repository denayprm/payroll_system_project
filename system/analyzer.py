# analyzer.py
try:
    import pandas as pd
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
    import pandas as pd

def analyze(summary):
    summary['total_compensation'] = summary['gaji_pokok'] + summary['total_bonus'] - summary['total_potongan']
    hourly = summary['gaji_pokok'] / (21 * 8)
    summary['overtime_pay'] = hourly * 1.5 * summary['total_jam_lembur']

    department_summary = summary.groupby('departemen').agg({
        'karyawan_id': 'count',
        'total_compensation': 'mean',
        'total_hari_hadir': 'mean',
        'total_jam_lembur': 'sum',
        'total_bonus': 'sum',
        'total_potongan': 'sum'
    }).rename(columns={'karyawan_id': 'jumlah_karyawan'})

    return summary, department_summary

print("\n📊 Data Analyzer telah dilakukan...")