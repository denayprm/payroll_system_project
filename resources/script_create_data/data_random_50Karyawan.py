import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Create directory if not exists
os.makedirs('resources', exist_ok=True)

# Generate Tabel Karyawan

def generate_karyawan():
    karyawan_id = list(range(1, 51))
    nama_depan = ["Budi", "Dewi", "Ahmad", "Siti", "Rudi", "Nina", "Eko", "Linda", "Doni", "Maya", "Andi", "Fitri", "Tono", "Yuni", "Bagus", "Citra", "Joko", "Rina", "Hendra", "Wulan", "Fajar", "Ayu", "Tari", "Dika", "Rosa"]
    nama_belakang = ["Santoso", "Putri", "Hidayat", "Rahayu", "Hermawan", "Wati", "Prasetyo", "Kusuma", "Prakoso", "Anggraini", "Saputra", "Nugroho", "Wijaya", "Sari", "Anindya", "Utami", "Setiawan", "Handayani", "Permadi", "Susanto", "Pertiwi", "Supriyadi", "Kartika", "Ramadhan", "Maulani"]
    jabatan_choices = ["Manager", "Supervisor", "Senior Staff", "Staff"]
    departemen_choices = ["IT", "HR", "Finance", "Marketing"]

    data = []
    for i in karyawan_id:
        nama = f"{random.choice(nama_depan)} {random.choice(nama_belakang)}"
        jabatan = random.choice(jabatan_choices)
        departemen = random.choice(departemen_choices)
        tanggal_masuk = datetime(random.randint(2019, 2024), random.randint(1, 12), random.randint(1, 28))

        if jabatan == "Manager":
            gaji = random.randint(15000000, 20000000)
        elif jabatan == "Supervisor":
            gaji = random.randint(10000000, 15000000)
        elif jabatan == "Senior Staff":
            gaji = random.randint(7000000, 10000000)
        else:
            gaji = random.randint(5000000, 7000000)

        status = random.choice(["Tetap", "Kontrak", "Probation"])
        email = f"{nama.lower().replace(' ', '.')}@company.com"
        no_hp = f"08{random.randint(1000000000, 9999999999)}"

        data.append([i, nama, jabatan, departemen, tanggal_masuk, gaji, status, email, no_hp])

    return pd.DataFrame(data, columns=[
        'karyawan_id', 'nama', 'jabatan', 'departemen', 'tanggal_masuk',
        'gaji_pokok', 'status_kepegawaian', 'email', 'nomor_telepon'
    ])

# Generate Tabel Kehadiran

def generate_kehadiran(karyawan_ids):
    data = []
    kehadiran_id = 1
    for bulan in range(7, 13):  # Juli - Des 2024
        for hari in range(1, 29):
            for karyawan_id in karyawan_ids:
                tanggal = datetime(2024, bulan, hari)
                data.extend(generate_daily_attendance(karyawan_id, tanggal, kehadiran_id))
                kehadiran_id += 1

    for bulan in range(1, 7):  # Jan - Jun 2025
        for hari in range(1, 29):
            for karyawan_id in karyawan_ids:
                tanggal = datetime(2025, bulan, hari)
                data.extend(generate_daily_attendance(karyawan_id, tanggal, kehadiran_id))
                kehadiran_id += 1

    return pd.DataFrame(data)

def generate_daily_attendance(karyawan_id, tanggal, kehadiran_id):
    if random.random() > 0.1:
        status = "Hadir"
        keterlambatan = random.randint(0, 30) if random.random() > 0.8 else 0
        waktu_masuk = datetime(tanggal.year, tanggal.month, tanggal.day, 8, random.randint(0, 30))
        waktu_keluar = datetime(tanggal.year, tanggal.month, tanggal.day, 17, random.randint(0, 30))
    else:
        status = random.choice(["Izin", "Sakit", "Tanpa Keterangan"])
        keterlambatan = 0
        waktu_masuk = None
        waktu_keluar = None

    return [{
        'kehadiran_id': kehadiran_id,
        'karyawan_id': karyawan_id,
        'tanggal': tanggal,
        'waktu_masuk': waktu_masuk,
        'waktu_keluar': waktu_keluar,
        'status_kehadiran': status,
        'keterlambatan_menit': keterlambatan,
        'keterangan': f"Keterangan untuk {status}"
    }]

# Generate Tabel Lembur

def generate_lembur(karyawan_ids):
    data = []
    lembur_id = 1
    for bulan in range(7, 13):
        tahun = 2024
        for hari in range(1, 29):
            for karyawan_id in karyawan_ids:
                if random.random() > 0.8:
                    jam_mulai = datetime(tahun, bulan, hari, 17, 30)
                    durasi = random.randint(1, 4)
                    jam_selesai = jam_mulai + timedelta(hours=durasi)
                    data.append({
                        'lembur_id': lembur_id,
                        'karyawan_id': karyawan_id,
                        'tanggal': datetime(tahun, bulan, hari),
                        'jam_mulai': jam_mulai,
                        'jam_selesai': jam_selesai,
                        'durasi_jam': durasi,
                        'status_approval': random.choice(['Disetujui', 'Ditolak']),
                        'keterangan': f"Lembur proyek {random.randint(1, 5)}"
                    })
                    lembur_id += 1

    for bulan in range(1, 7):
        tahun = 2025
        for hari in range(1, 29):
            for karyawan_id in karyawan_ids:
                if random.random() > 0.8:
                    jam_mulai = datetime(tahun, bulan, hari, 17, 30)
                    durasi = random.randint(1, 4)
                    jam_selesai = jam_mulai + timedelta(hours=durasi)
                    data.append({
                        'lembur_id': lembur_id,
                        'karyawan_id': karyawan_id,
                        'tanggal': datetime(tahun, bulan, hari),
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
    jenis_pelanggaran = ["Terlambat Berulang", "Absen Tanpa Keterangan", "Pelanggaran Dress Code", "Kelalaian Tugas"]
    for bulan in range(7, 19):
        tahun = 2024 if bulan <= 12 else 2025
        bulan_real = bulan if bulan <= 12 else bulan - 12
        for karyawan_id in karyawan_ids:
            if random.random() > 0.7:
                tanggal = datetime(tahun, bulan_real, random.randint(1, 28))
                tingkat = random.choice(["Ringan", "Sedang", "Berat"])
                potongan = random.randint(50000, 1000000)
                data.append({
                    'pelanggaran_id': pelanggaran_id,
                    'karyawan_id': karyawan_id,
                    'tanggal': tanggal,
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
    for bulan in range(7, 19):
        tahun = 2024 if bulan <= 12 else 2025
        bulan_real = bulan if bulan <= 12 else bulan - 12
        for karyawan_id in karyawan_ids:
            if random.random() > 0.5:
                jenis = random.choice(jenis_bonus)
                jumlah = random.randint(1000000, 10000000)
                data.append({
                    'bonus_id': bonus_id,
                    'karyawan_id': karyawan_id,
                    'periode_bulan': bulan_real,
                    'periode_tahun': tahun,
                    'jenis_bonus': jenis,
                    'jumlah_bonus': jumlah,
                    'keterangan': f"Bonus {jenis} periode {bulan_real}/{tahun}"
                })
                bonus_id += 1
    return pd.DataFrame(data)

# Generate data
karyawan_df = generate_karyawan()
karyawan_ids = karyawan_df['karyawan_id'].tolist()
kehadiran_df = generate_kehadiran(karyawan_ids)
lembur_df = generate_lembur(karyawan_ids)
pelanggaran_df = generate_pelanggaran(karyawan_ids)
bonus_df = generate_bonus(karyawan_ids)

# Simpan ke CSV
karyawan_df.to_csv('resources/main_data/karyawan.csv', index=False)
kehadiran_df.to_csv('resources/main_data/kehadiran.csv', index=False)
lembur_df.to_csv('resources/main_data/lembur.csv', index=False)
pelanggaran_df.to_csv('resources/main_data/pelanggaran.csv', index=False)
bonus_df.to_csv('resources/main_data/bonus.csv', index=False)
