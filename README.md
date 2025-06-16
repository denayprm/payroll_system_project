# Tentang Projek Payroll System

## Mata Kuliah: Big Data

### Judul

Proyek Implementasi Big Data: Sistem Penghitung Gaji Karyawan

### Deskripsi Kasus

Proyek ini akan mengembangkan sistem penghitung gaji karyawan berbasis big data yang dapat mengelola dan menganalisis data kehadiran, performa, dan kompensasi karyawan. Sistem akan menghitung gaji harian, mingguan, bulanan, dan tahunan dengan mempertimbangkan bonus, lembur, serta pemotongan gaji akibat ketidakhadiran, keterlambatan, dan pelanggaran lainnya.

## Pembuat

Deni Permana - 2210512015

## Sumber Data

Data Dummy Link: [Google Drive](https://drive.google.com/drive/folders/1o1scgiQmazd1ZR5lt5pk8opVavOTBCIL?usp=sharing)

### 📋 Struktur Tabel Data

#### 🧍‍♂️ Tabel Karyawan

| Kolom             | Deskripsi                        |
|-------------------|----------------------------------|
| karyawan_id (PK)  | ID unik karyawan                 |
| nama              | Nama lengkap karyawan            |
| jabatan           | Posisi/jabatan karyawan          |
| departemen        | Departemen karyawan              |
| tanggal_masuk     | Tanggal mulai bekerja            |
| gaji_pokok        | Gaji pokok per bulan             |
| status_kepegawaian| Tetap/kontrak/probation          |
| email             | Email karyawan                   |
| nomor_telepon     | Nomor telepon karyawan           |

#### ⏰ Tabel Kehadiran

| Kolom               | Deskripsi                                 |
|---------------------|-------------------------------------------|
| kehadiran_id (PK)   | ID unik record kehadiran                  |
| karyawan_id (FK)    | ID karyawan                               |
| tanggal             | Tanggal kehadiran                         |
| waktu_masuk         | Waktu check-in                            |
| waktu_keluar        | Waktu check-out                           |
| status_kehadiran    | Hadir/izin/sakit/tanpa keterangan         |
| keterlambatan_menit | Jumlah menit terlambat                    |
| keterangan          | Keterangan tambahan                       |

#### ⏳ Tabel Lembur

| Kolom             | Deskripsi                            |
|-------------------|----------------------------------------|
| lembur_id (PK)    | ID unik record lembur                 |
| karyawan_id (FK)  | ID karyawan                           |
| tanggal           | Tanggal lembur                        |
| jam_mulai         | Waktu mulai lembur                    |
| jam_selesai       | Waktu selesai lembur                  |
| durasi_jam        | Durasi lembur dalam jam               |
| status_approval   | Disetujui/ditolak                     |
| keterangan        | Keterangan lembur                     |

#### ⚠️ Tabel Pelanggaran

| Kolom              | Deskripsi                         |
|--------------------|-----------------------------------|
| pelanggaran_id (PK)| ID unik pelanggaran               |
| karyawan_id (FK)   | ID karyawan                       |
| tanggal            | Tanggal pelanggaran               |
| jenis_pelanggaran  | Kategori pelanggaran              |
| deskripsi          | Deskripsi pelanggaran             |
| tingkat_keparahan  | Ringan/sedang/berat               |
| sanksi_potongan    | Jumlah potongan gaji              |

#### 💰 Tabel Bonus

| Kolom              | Deskripsi                                    |
|--------------------|----------------------------------------------|
| bonus_id (PK)      | ID unik bonus                                |
| karyawan_id (FK)   | ID karyawan                                  |
| periode_bulan      | Bulan bonus                                  |
| periode_tahun      | Tahun bonus                                  |
| jenis_bonus        | Kategori bonus (performa/proyek/lainnya)     |
| jumlah_bonus       | Nominal bonus                                |
| keterangan         | Keterangan bonus                             |

## 📊 Laporan Visualisasi Gaji

![Payroll Report](resources/output/payroll_report.png)
