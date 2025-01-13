# Main
from view import View
from process import Process

def main():
    proses = Process()
    tampil = View()

    while True:
        print("\n1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama, umur, alamat = tampil.input_data()
            proses.tambah_data(nama, umur, alamat)
        elif pilihan == "2":
            tampil.tampilkan_data(proses.data)
        elif pilihan == "3":
            break
        else:
            tampil.pesan_error("Pilihan tidak valid.")

if __name__ == "__main__":
    main()