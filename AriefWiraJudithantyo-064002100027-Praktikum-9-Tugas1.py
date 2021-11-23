def write(a):
    file = open("biodata.txt", "w")
    file.write(str(a))
    file.close()

def read():
    file = open("biodata.txt", "r")
    print(file.read())
    file.close()

nama = str(input("Masukkan nama: "))
umur = str(input("Masukkan umur: "))
alamat = str(input("Masukkan alamat: "))
email = str(input("Masukkan email: "))
dosen = str(input("Masukkan nama dosen walimu: "))

bio = str(f"""
Nama: {nama}
Umur: {umur}
Alamat: {alamat}
Email: {email}
Dosen Wali: {dosen}
""")

print("\nData anda")
write(bio)
read()
