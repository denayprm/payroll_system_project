# visualizer.py
try:
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import os
    import plotly.express as px
    import plotly.io as pio
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'seaborn', 'matplotlib', 'pandas', 'plotly'])
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import os
    import plotly.express as px
    import plotly.io as pio

def visualize(summary, dept_summary):
    os.makedirs('resources', exist_ok=True)

    # ✅ Tampilkan 5 karyawan dengan gaji tertinggi
    top_earners = summary.sort_values('total_compensation', ascending=False).head(5)
    print("\n📋 5 Karyawan dengan Gaji Tertinggi:")
    print(top_earners[['nama', 'departemen', 'total_compensation']])

    # ✅ Buat visualisasi ramah anak-anak (warna cerah dan label besar)
    plt.figure(figsize=(18, 12))

    # 1. Gaji Tertinggi
    plt.subplot(2, 2, 1)
    sns.barplot(x='total_compensation', y='nama', data=top_earners, palette='YlGnBu')
    plt.title('5 Karyawan dengan Gaji Tertinggi', fontsize=16)
    plt.xlabel('Total Gaji (Rp)', fontsize=12)
    plt.ylabel('Nama Karyawan', fontsize=12)

    # 2. Kompensasi per Departemen (Boxplot)
    plt.subplot(2, 2, 2)
    sns.boxplot(x='departemen', y='total_compensation', data=summary, palette='Set2')
    plt.title('Gaji per Departemen', fontsize=16)
    plt.xticks(rotation=45)

    # 3. Bonus per Departemen
    plt.subplot(2, 2, 3)
    dept_summary['total_bonus'].plot(kind='bar', color='orange')
    plt.title('Total Bonus per Departemen', fontsize=16)
    plt.xticks(rotation=45)
    plt.ylabel('Bonus (Rp)', fontsize=12)

    # 4. Korelasi antar variabel
    plt.subplot(2, 2, 4)
    corr = summary[['total_hari_hadir', 'total_jam_lembur', 'total_bonus', 'total_potongan', 'total_compensation']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Korelasi Antar Variabel', fontsize=16)

    plt.tight_layout()
    plt.savefig('resources/payroll_report.png')
    plt.close()
    print("\n📊 Grafik statis disimpan sebagai 'resources/payroll_report.png'")

    # ✅ Grafik Interaktif dengan Plotly
    fig = px.bar(
        top_earners,
        x='total_compensation',
        y='nama',
        orientation='h',
        color='departemen',
        title='5 Karyawan dengan Gaji Tertinggi (Interaktif)',
        labels={'total_compensation': 'Total Gaji (Rp)', 'nama': 'Nama Karyawan'}
    )
    pio.write_html(fig, file='resources/top_earners_interactive.html', auto_open=False)
    print("🌐 Grafik interaktif disimpan sebagai 'resources/top_earners_interactive.html'")
