class Mahasiswa :
    empCount = 0

    def __init__(self,name,nim,angkatan):
        self.name = name
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.empCount += 1

    def displayCount(self):
        print("total Mahasiswa %d" % Mahasiswa.empCount)
    def displayEmployee(self):
        print("Name: ", self.name,"Nim :" , self.nim,"Angkatan: ", self.angkatan)

nama = input ("Nama anda : ")
nim = input ("Nim : ")
angkatan = input ("Angkatan : ")

nama1 = Mahasiswa(nama, nim, angkatan)

print(f"Nama : {nama1.name}")
print(f"Nim : {nama1.nim}")
print(f"Angkatan: {nama1.angkatan}")

print(f"total mahasiswa: {nama1.empCount}")


