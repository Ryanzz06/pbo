# Nama: muh ryan nurwangsah
# NIM: D0221302
# Kelas: Informatika H

print("Nama     :   Muh Ryan Nurwangsah")
print("NIM      :   D0221302")
print("kelas    :   INFORMATIKA H")

import math #utk mendapat nilai pi, digunakan dalam menghitung luas/volume tabung

#parent class
class BangunRuang:
    def luas(self):
        pass

    def volume(self):
        pass

    def printLuas(self):
        print("Luas : ", self.luas())

    def printVolume(self):
        print("Volume   : ", self.volume())

class Balok(BangunRuang):
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.tinggi = 0

    def luas(self):
        luas = 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
        return luas

    def volume(self):
        volume = self.panjang * self.lebar * self.tinggi
        return volume

class Tabung(BangunRuang):
    def __init__(self):
        self.jari_jari = 0
        self.tinggi = 0
    
    def luas(self):
        luas = 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)
        return round(luas, 2)
 
    def volume(self):
        volume = math.pi * (self.jari_jari ** 2) * self.tinggi
        return round(volume, 2)
    

class Kubus(BangunRuang):
    def __init__(self):
        self.sisi = 0

    def luas(self):
        luas = 6 * (self.sisi**2)
        return luas

    def volume(self):
        volume = self.sisi**3
        return volume

def ulang():
    print("Ingin menghitung lagi? (yes/no)")
    inp = input("Pilihlah pilihan di atas  : ").lower()
    return True if inp == "yes" else False

#panggilan class
balok = Balok()
tabung = Tabung()
kubus = Kubus()

while True:
    print("""\n1. Menghitung Balok
2. Menghitung Tabung
3. Menghitung Kubus
4. Berhenti""")
    pilihan = input("Pilihlah pilihan di atas  : ")

    if pilihan == "1":
        while True:
            print("""\n1. Mencari Luas
2. Mencari Volume
3. Kembali""")
            p1 = input("Pilihlah pilihan di atas  : ")
            
            if p1 == "1":
                while True:
                    balok.panjang = float(input("Masukkan Nilai Panjang : "))
                    balok.lebar = float(input("Masukkan Nilai Lebar : "))
                    balok.tinggi = float(input("Masukkan Nilai Tinggi   : "))

                    print()
                    balok.printLuas()

                    if ulang() != True:
                        break
            elif p1 == "2":
                while True:
                    balok.panjang = float(input("Masukkan Nilai Panjang : "))
                    balok.lebar = float(input("Masukkan Nilai Lebar : "))
                    balok.tinggi = float(input("Masukkan Nilai Tinggi   : "))

                    print()
                    balok.printVolume()

                    if ulang() != True:
                        break
            elif p1 == "3":
                break
            else:
                print("Masukkan pilihan yang Benar!")
    elif pilihan == "2":
         while True:
            print("""\n1. Mencari Luas
2. Mencari Volume
3. Kembali""")
            p2 = input("Pilihlah pilihan di atas  : ")
            
            if p2 == "1":
                while True:
                    tabung.jari_jari = float(input("Masukkan Nilai Jari-jari    : "))
                    tabung.tinggi = float(input("Masukkan Nilai Tinggi  : "))

                    print()
                    tabung.printLuas()

                    if ulang() != True:
                        break
            elif p2 == "2":
                while True:
                    tabung.jari_jari = float(input("Masukkan Nilai Jari-jari    : "))
                    tabung.tinggi = float(input("Masukkan Nilai Tinggi  : "))

                    print()
                    tabung.printVolume()

                    if ulang() != True:
                        break
            elif p2 == "3":
                break
            else:
                print("Masukkan Pilihan yang Benar!")
    elif pilihan == "3":
         while True:
            print("""\n1. Mencari Luas
2. Mencari Volume
3. Kembali""")
            p3 = input("Pilihlah pilihan di atas  : ")
            
            if p3 == "1":
                while True:
                    kubus.sisi = float(input("Masukkan Nilai Sisi   : "))

                    print()
                    kubus.printLuas()

                    if ulang() != True:
                        break
            elif p3 == "2":
                while True:
                    kubus.sisi = float(input("Masukkan Nilai Sisi : "))
                    
                    print()
                    kubus.printVolume()

                    if ulang() != True:
                        break
            elif p3 == "3":
                break
            else:
                print("Masukkan Pilihan yang Benar!")
    elif pilihan == "4":
        break
    else:
        print("Masukkan Pilihan yang Benar!")

print("Telah Selesai!")