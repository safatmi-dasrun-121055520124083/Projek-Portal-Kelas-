# ==========================================
# PROJECT PBO : PORTAL KELAS (CONSOLE)
# kelompok : 3
# ==========================================

# ---------- CLASS INDUK ----------
class User:
    def __init__(self, nama, role):
        self.nama = nama
        self.role = role

    def info(self):
        print(f"Nama : {self.nama}")
        print(f"Role : {self.role}")

# ---------- CLASS MAHASISWA ----------
class Mahasiswa(User):
    def __init__(self, nama, nim):
        super().__init__(nama, "Mahasiswa")
        self.nim = nim
        self.nilai = {}

    def lihat_kelas(self):
        print("Kelas yang diikuti: Pemrograman Berorientasi Objek")

    def lihat_nilai(self):
        if not self.nilai:
            print("Nilai belum tersedia.")
        else:
            print("Nilai Mata Kuliah:")
            for mk, n in self.nilai.items():
                print(f"- {mk} : {n}")


# ---------- CLASS DOSEN ----------
class Dosen(User):
    def __init__(self, nama):
        super().__init__(nama, "Dosen")

    def input_nilai(self, mahasiswa, mata_kuliah, nilai):
        mahasiswa.nilai[mata_kuliah] = nilai
        print("Nilai berhasil diinput.")


# ---------- DATA ----------
mahasiswa_list = [
    Mahasiswa("Rendi Irfan", "24060"),
    Mahasiswa("M Qusay Assgaf", "24061"),
    Mahasiswa("Ibnu Khaldun", "24062"),
    Mahasiswa("ALfaliby Ilyas", "24063"),
    Mahasiswa("Yusmad Tharob", "24064"),
    Mahasiswa("Nabil S.jamil", "24065"),
    Mahasiswa("M Aldy Djufri", "24066"),
    Mahasiswa("Ratna Ananda", "24008"),
    Mahasiswa("Rey Maulana Haedar", "24009"),
    Mahasiswa("Arrayhan Hi Abdullah", "24010"),
    Mahasiswa("Irmansyah Saputra", "24011"),
    Mahasiswa("Devi Laras Setyawati", "24012"),
    Mahasiswa("M Solihin ALZufry", "24013"),
    Mahasiswa("Arfat Iksan", "24014"),
    Mahasiswa("Reyhan Yuslan", "24015"),
    Mahasiswa("Adjiansyah Hasanudin Miradji", "24016"),
    Mahasiswa("Algeafaris Syahindra", "24017"),
    Mahasiswa("M Rifky Alhadad", "24018"),
    Mahasiswa("Al Adawia", "24019"),
    Mahasiswa("Safatmi Dasrun", "24020"),
    Mahasiswa("Junitof Igono", "24021"),
    Mahasiswa("M Hardade Ahmad", "24022"),
    Mahasiswa("Mulyadi Mawan", "24023"),
    Mahasiswa("Nuryanti Umanailo", "24024"),
    Mahasiswa("Falki Matahari", "24025"),
    Mahasiswa("Arjun T.Marsaoly", "24026"),
   

]

dosen = Dosen("Pak ISRA")


# ---------- FUNGSI MENU MAHASISWA ----------
def menu_mahasiswa(mhs):
    while True:
        print("\n=== MENU MAHASISWA ===")
        print("1. Lihat Info")
        print("2. Lihat Kelas")
        print("3. Lihat Nilai")
        print("4. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            mhs.info()
            print("NIM  :", mhs.nim)
        elif pilihan == "2":
            mhs.lihat_kelas()
        elif pilihan == "3":
            mhs.lihat_nilai()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")


# ---------- FUNGSI MENU DOSEN ----------
def menu_dosen():
    while True:
        print("\n=== MENU DOSEN ===")
        print("1. Lihat Info")
        print("2. Input Nilai Mahasiswa")
        print("3. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            dosen.info()

        elif pilihan == "2":
            print("\nDaftar Mahasiswa:")
            for i, mhs in enumerate(mahasiswa_list):
                print(f"{i+1}. {mhs.nama} ({mhs.nim})")

            idx = int(input("Pilih mahasiswa: ")) - 1
            mk = input("Nama Mata Kuliah: ")
            nilai = input("Nilai: ")

            dosen.input_nilai(mahasiswa_list[idx], mk, nilai)

        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")


# ---------- PROGRAM UTAMA ----------
def main():
    while True:
        print("\n=== PORTAL KELAS PBO ===")
        print("1. Login Mahasiswa")
        print("2. Login Dosen")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim = input("Masukkan NIM: ")
            ditemukan = False

            for mhs in mahasiswa_list:
                if mhs.nim == nim:
                    menu_mahasiswa(mhs)
                    ditemukan = True
                    break

            if not ditemukan:
                print("Mahasiswa tidak ditemukan!")

        elif pilihan == "2":
            password = input("Masukkan password dosen: ")
            if password == "admin123":
                menu_dosen()
            else:
                print("Password salah!")

        elif pilihan == "3":
            print("Terima kasih telah menggunakan Portal Kelas.")
            break

        else:
            print("Pilihan tidak valid!")


# ---------- JALANKAN PROGRAM ----------
main()
