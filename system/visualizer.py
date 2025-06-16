# visualizer.py
try:
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import os
    import plotly.express as px
    import plotly.graph_objects as go
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
    import plotly.graph_objects as go
    import plotly.io as pio

def visualize(summary, dept_summary):
    os.makedirs('resources', exist_ok=True)

    # 1. Daftar Gaji Tertinggi
    top10 = summary.sort_values('total_compensation', ascending=False).head(10)

    # 2. Daftar Gaji Terendah
    bottom10 = summary.sort_values('total_compensation', ascending=True).head(10)

    # 3. Grafik Total Gaji, Bonus, Potongan per Bulan
    if {'bulan', 'tahun'}.issubset(summary.columns):
        bulanan = summary.groupby(['tahun', 'bulan']).agg({
            'total_compensation': 'sum',
            'total_bonus': 'sum',
            'total_potongan': 'sum'
        }).reset_index().sort_values(['tahun', 'bulan'])
    else:
        bulanan = None

    # 4. Visualisasi Kinerja Karyawan & Kehadiran (statis)
    plt.figure(figsize=(18, 12))

    plt.subplot(2, 2, 1)
    sns.barplot(x='total_compensation', y='nama', data=top10, palette='Greens_r', hue='nama', legend=False)
    plt.title('10 Karyawan dengan Gaji Tertinggi')

    plt.subplot(2, 2, 2)
    sns.barplot(x='total_compensation', y='nama', data=bottom10, palette='Reds_r', hue='nama', legend=False)
    plt.title('10 Karyawan dengan Gaji Terendah')

    plt.subplot(2, 2, 3)
    sns.scatterplot(data=summary, x='total_hari_hadir', y='total_compensation', hue='departemen')
    plt.title('Kinerja: Kehadiran vs Gaji')

    plt.subplot(2, 2, 4)
    corr = summary[['total_hari_hadir', 'total_jam_lembur', 'total_bonus', 'total_potongan', 'total_compensation']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Korelasi Variabel')

    plt.tight_layout()
    plt.savefig('resources/output/payroll_report.png')
    plt.close()
    print("📊 Grafik statis disimpan sebagai 'resources/output/payroll_report.png'")

    # 5. Grafik Interaktif Plotly (disimpan sebagai HTML)
    fig1 = px.bar(
        top10,
        x='total_compensation',
        y='nama',
        orientation='h',
        color='departemen',
        title='🔝 Top 10 Gaji Tertinggi',
        labels={'total_compensation': 'Total Gaji', 'nama': 'Nama Karyawan'}
    )
    pio.write_html(fig1, file='resources/output/top10_gaji_tertinggi.html', auto_open=False)

    fig2 = px.bar(
        bottom10,
        x='total_compensation',
        y='nama',
        orientation='h',
        color='departemen',
        title='🔻 10 Gaji Terendah',
        labels={'total_compensation': 'Total Gaji', 'nama': 'Nama Karyawan'}
    )
    pio.write_html(fig2, file='resources/output/bottom10_gaji_terendah.html', auto_open=False)

    if bulanan is not None:
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(name='Gaji', x=bulanan['bulan'], y=bulanan['total_compensation']))
        fig3.add_trace(go.Bar(name='Bonus', x=bulanan['bulan'], y=bulanan['total_bonus']))
        fig3.add_trace(go.Bar(name='Potongan', x=bulanan['bulan'], y=bulanan['total_potongan']))
        fig3.update_layout(
            title='📆 Statistik Gaji, Bonus, Potongan per Bulan',
            barmode='group'
        )
        pio.write_html(fig3, file='resources/output/statistik_perbulan.html', auto_open=False)

    fig4 = px.scatter(
        summary,
        x='total_hari_hadir',
        y='total_compensation',
        color='departemen',
        hover_name='nama',
        title='📈 Kehadiran vs Gaji',
        labels={'total_hari_hadir': 'Hari Hadir', 'total_compensation': 'Gaji'}
    )
    pio.write_html(fig4, file='resources/output/kehadiran_vs_gaji.html', auto_open=False)

        # Grafik Informasi Lengkap Semua Karyawan per Bulan (12 bulan)
    if {'bulan', 'tahun'}.issubset(summary.columns):
        info12 = summary.copy()
        info12['periode'] = info12['bulan'] + ' ' + info12['tahun'].astype(str)

        fig5 = px.bar(
            info12,
            x='nama',
            y='total_compensation',
            color='departemen',
            animation_frame='periode',
            hover_data=['total_bonus', 'total_potongan'],
            title='📅 Gaji Bersih, Bonus, dan Potongan Selama 12 Bulan per Karyawan',
            labels={
                'total_compensation': 'Gaji Bersih',
                'nama': 'Nama Karyawan',
                'departemen': 'Departemen'
            }
        )
        fig5.update_layout(xaxis={'categoryorder': 'total descending'})
        pio.write_html(fig5, file='resources/output/rekapitulasi_12bulan_per_karyawan.html', auto_open=False)

        print("🗂️ Grafik interaktif informasi 12 bulan disimpan di 'resources/output/rekapitulasi_12bulan_per_karyawan.html'")

    print("🌐 Semua grafik interaktif disimpan ke dalam folder 'resources/output' sebagai file HTML.")
