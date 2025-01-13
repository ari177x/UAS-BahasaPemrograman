#View
from tabulate import tabulate

class View:
    def tampilkan_data(self, data):
        header = ["Nama", "Umur", "Alamat"]
        tabel = [[d.nama, d.umur, d.alamat] for d in data]
        print(tabulate(tabel, header, tablefmt="grid"))

    def input_data(self):
        nama = input("Masukkan nama: ")
        while True:
            try:
                umur = int(input("Masukkan umur: "))
                if umur < 0:
                    raise ValueError
                break
            except ValueError:
                print("Umur harus berupa angka positif.")
        alamat = input("Masukkan alamat: ")
        return nama, umur, alamat

    def pesan_error(self, pesan):
        print(f"Error: {pesan}")
