try:
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
    import random
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas', 'numpy'])
    from datetime import datetime, timedelta
    import random
    import pandas as pd
    import numpy as np

# Set random seed for reproducibility
np.random.seed(24)

# Generate Tabel Karyawan
def generate_karyawan():
    karyawan_id = list(range(1, 11))
    nama = [
        "Budi Santoso", "Dewi Putri", "Ahmad Hidayat", "Siti Rahayu",
        "Rudi Hermawan", "Nina Wati", "Eko Prasetyo", "Linda Kusuma",
        "Doni Prakoso", "Maya Anggraini"
    ]
    jabatan = [
        "Manager", "Supervisor", "Staff", "Staff",
        "Senior Staff", "Staff", "Supervisor", "Staff",
        "Staff", "Senior Staff"
    ]
    departemen = [
        "IT", "HR", "Finance", "Marketing",
        "IT", "Finance", "Marketing", "HR",
        "IT", "Finance"
    ]

    # Generate tanggal masuk random between 2020-2024
    tanggal_masuk = [
        datetime(random.randint(2020, 2024), random.randint(1, 12), random.randint(1, 28))
        for _ in range(10)
    ]

    # Generate gaji pokok based on jabatan
    gaji_pokok = []
    for jab in jabatan:
        if jab == "Manager":
            gaji = random.randint(15000000, 20000000)
        elif jab == "Supervisor":
            gaji = random.randint(10000000, 15000000)
        elif jab == "Senior Staff":
            gaji = random.randint(7000000, 10000000)
        else:
            gaji = random.randint(5000000, 7000000)
        gaji_pokok.append(gaji)

    status_kepegawaian = ["Tetap", "Tetap", "Kontrak", "Tetap", "Tetap", "Kontrak", "Tetap", "Probation", "Kontrak", "Tetap"]

    email = [f"{nama[i].lower().replace(' ', '.')}@company.com" for i in range(10)]
    nomor_telepon = [f"08{random.randint(10000000000, 99999999999)}" for _ in range(10)]

    df_karyawan = pd.DataFrame({
        'karyawan_id': karyawan_id,
        'nama': nama,
        'jabatan': jabatan,
        'departemen': departemen,
        'tanggal_masuk': tanggal_masuk,
        'gaji_pokok': gaji_pokok,
        'status_kepegawaian': status_kepegawaian,
        'email': email,
        'nomor_telepon': nomor_telepon
    })

    return df_karyawan

# Generate Tabel Kehadiran
def generate_kehadiran(karyawan_ids):
    data = []
    kehadiran_id = 1

    for day in range(1, 32):  # January 2025
        for karyawan_id in karyawan_ids:
            if random.random() > 0.1:  # 90% chance of attendance
                status = "Hadir"
                keterlambatan = random.randint(0, 30) if random.random() > 0.8 else 0
                waktu_masuk = datetime(2025, 1, day, 8, random.randint(0, 30))
                waktu_keluar = datetime(2025, 1, day, 17, random.randint(0, 30))
            else:
                status = random.choice(["Izin", "Sakit", "Tanpa Keterangan"])
                keterlambatan = 0
                waktu_masuk = None
                waktu_keluar = None

            data.append({
                'kehadiran_id': kehadiran_id,
                'karyawan_id': karyawan_id,
                'tanggal': datetime(2025, 1, day),
                'waktu_masuk': waktu_masuk,
                'waktu_keluar': waktu_keluar,
                'status_kehadiran': status,
                'keterlambatan_menit': keterlambatan,
                'keterangan': f"Keterangan untuk {status}"
            })
            kehadiran_id += 1

    return pd.DataFrame(data)

# Generate Tabel Lembur
def generate_lembur(karyawan_ids):
    data = []
    lembur_id = 1

    for day in range(1, 32):  # January 2025
        for karyawan_id in karyawan_ids:
            if random.random() > 0.8:  # 20% chance of overtime
                jam_mulai = datetime(2025, 1, day, 17, 30)
                durasi = random.randint(1, 4)
                jam_selesai = jam_mulai + timedelta(hours=durasi)

                data.append({
                    'lembur_id': lembur_id,
                    'karyawan_id': karyawan_id,
                    'tanggal': datetime(2025, 1, day),
                    'jam_mulai': jam_mulai,
                    'jam_selesai': jam_selesai,
                    'durasi_jam': durasi,
                    'status_approval': random.choice(['Disetujui', 'Ditolak']),
                    'keterangan': f"Lembur proyek {random.randint(1, 5)}"
                })
                lembur_id += 1

    return pd.DataFrame(data)

# Generate Tabel Pelanggaran
def generate_pelanggaran(karyawan_ids):
    data = []
    pelanggaran_id = 1

    jenis_pelanggaran = [
        "Terlambat Berulang", "Absen Tanpa Keterangan",
        "Pelanggaran Dress Code", "Kelalaian Tugas"
    ]

    for karyawan_id in karyawan_ids:
        if random.random() > 0.7:  # 30% chance of violation
            tingkat = random.choice(["Ringan", "Sedang", "Berat"])
            if tingkat == "Ringan":
                potongan = random.randint(50000, 200000)
            elif tingkat == "Sedang":
                potongan = random.randint(200001, 500000)
            else:
                potongan = random.randint(500001, 1000000)

            data.append({
                'pelanggaran_id': pelanggaran_id,
                'karyawan_id': karyawan_id,
                'tanggal': datetime(2025, 1, random.randint(1, 31)),
                'jenis_pelanggaran': random.choice(jenis_pelanggaran),
                'deskripsi': f"Deskripsi pelanggaran {pelanggaran_id}",
                'tingkat_keparahan': tingkat,
                'sanksi_potongan': potongan
            })
            pelanggaran_id += 1

    return pd.DataFrame(data)

# Generate Tabel Bonus
def generate_bonus(karyawan_ids):
    data = []
    bonus_id = 1

    jenis_bonus = ["Performa", "Proyek", "Tahunan", "Prestasi"]

    for karyawan_id in karyawan_ids:
        if random.random() > 0.5:  # 50% chance of bonus
            jenis = random.choice(jenis_bonus)
            if jenis == "Performa":
                jumlah = random.randint(1000000, 3000000)
            elif jenis == "Proyek":
                jumlah = random.randint(2000000, 5000000)
            elif jenis == "Tahunan":
                jumlah = random.randint(5000000, 10000000)
            else:
                jumlah = random.randint(1000000, 2000000)

            data.append({
                'bonus_id': bonus_id,
                'karyawan_id': karyawan_id,
                'periode_bulan': 1,  # January
                'periode_tahun': 2025,
                'jenis_bonus': jenis,
                'jumlah_bonus': jumlah,
                'keterangan': f"Bonus {jenis} periode Januari 2025"
            })
            bonus_id += 1

    return pd.DataFrame(data)

# Generate all data and save to CSV
df_karyawan = generate_karyawan()
df_kehadiran = generate_kehadiran(df_karyawan['karyawan_id'])
df_lembur = generate_lembur(df_karyawan['karyawan_id'])
df_pelanggaran = generate_pelanggaran(df_karyawan['karyawan_id'])
df_bonus = generate_bonus(df_karyawan['karyawan_id'])

# Save to CSV files
df_karyawan.to_csv('resources/main_data/karyawan.csv', index=False)
df_kehadiran.to_csv('resources/main_data/kehadiran.csv', index=False)
df_lembur.to_csv('resources/main_data/lembur.csv', index=False)
df_pelanggaran.to_csv('resources/main_data/pelanggaran.csv', index=False)
df_bonus.to_csv('resources/main_data/bonus.csv', index=False)