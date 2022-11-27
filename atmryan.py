#nama : muh ryan nurwangsah
#nim : D0221302

pin = 60203
saldo = 1000000
print("silahkan masukkan pin atau password yang tertera")
print("pin saya adalah ",pin)

input_pin = int(input("Masukkan Pin: "))
while input_pin == pin :
    print('''1. Cek saldo
2. Tarik tunai
3. Setor tunai
4. Transfer
5. Berhenti''')
    input_perintah = int(input("Masukkan Perintah: "))
    if input_perintah == 1:
        print("Saldo: Rp"+str(saldo))
    elif input_perintah == 2:
        tarik = int(input("Masukkan Jumlah yang ditarik: Rp"))
        if tarik > saldo:
            print("Saldo tidak cukup")
        else:
            print("Rp"+str(tarik)+" ditarik")
            
