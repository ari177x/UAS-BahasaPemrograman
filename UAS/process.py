# Process
from data import Data

class Process:
    def __init__(self):
        self.data = []

    def tambah_data(self, nama, umur, alamat):
        self.data.append(Data(nama, umur, alamat))