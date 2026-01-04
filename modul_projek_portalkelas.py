# ==========================================
# MODULE : PORTAL KELAS PBO
# Modul ini berisi class dan fungsi utama
# untuk sistem Portal Kelas berbasis PBO
# ==========================================

# ---------- CLASS INDUK ----------
# Class User adalah class induk (parent class)
# yang akan diturunkan ke class Mahasiswa dan Dosen
class User:
    def __init__(self, nama, role):
        # atribut nama menyimpan nama user
        self.nama = nama
        # atribut role menyimpan peran user
        self.role = role

    def info(self):
        # method untuk menampilkan informasi user
        return f"Nama: {self.nama}, Role: {self.role}"


# ---------- CLASS MAHASISWA ----------
# Class Mahasiswa merupakan turunan dari class User
class Mahasiswa(User):
    def __init__(self, nama, nim):
        # memanggil constructor class User
        super().__init__(nama, "Mahasiswa")
        # atribut nim menyimpan NIM mahasiswa
        self.nim = nim
        # dictionary untuk menyimpan nilai
        self.nilai = {}

    def lihat_kelas(self):
        # menampilkan kelas yang diikuti
        return "Pemrograman Berorientasi Objek"

    def lihat_nilai(self):
        # menampilkan nilai mahasiswa
        return self.nilai if self.nilai else "Nilai belum tersedia"


# ---------- CLASS DOSEN ----------
# Class Dosen merupakan turunan dari class User
class Dosen(User):
    def __init__(self, nama):
        # memanggil constructor class User
        super().__init__(nama, "Dosen")

    def input_nilai(self, mahasiswa, mata_kuliah, nilai):
        # menginput nilai mahasiswa
        mahasiswa.nilai[mata_kuliah] = nilai
        return "Nilai berhasil diinput"


# ---------- DATA ----------
# Fungsi untuk menyediakan data awal mahasiswa
def get_mahasiswa_list():
    return [
        Mahasiswa("Rendi Irfan", "24060"),
        Mahasiswa("M Qusay Assgaf", "24061"),
        Mahasiswa("Ibnu Khaldun", "24062"),
        Mahasiswa("ALfaliby Ilyas", "24063"),
        Mahasiswa("Yusmad Tharob", "24064"),
        Mahasiswa("Nabil S.jamil", "24065"),
        Mahasiswa("M Aldy Djufri", "24066"),
    ]
