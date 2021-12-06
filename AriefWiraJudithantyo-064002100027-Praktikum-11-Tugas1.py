class data: 
    jumlah = 0
    def __init__(self,nama,nim,tahun):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.tahun = str(tahun)
        data.jumlah += 1

    def urutan(self):
        return str(f"{self.nama} ; {self.nim} ; {self.tahun}")

    def jumlahdata(self):
        print()
        print("Nama :",self.nama)
        print("NIM :",self.nim)
        print("Tahun :",self.tahun)
        print()
        input(f"Jumlah mahasiswa sekarang adalah {data.jumlah} orang\nPRESS ENTER")

while True:
    print(f"\ndata ke {(data.jumlah)+1}\nKetik exit untuk mengakhiri!")
    x = str(input("Masukkan Nama : "))
    if x == "exit":
        break
    y = str(input("Masukkan NIM : "))
    z = str(input("Masukkan angkatan : "))
    n = data(x,y,z)

    n.jumlahdata()
