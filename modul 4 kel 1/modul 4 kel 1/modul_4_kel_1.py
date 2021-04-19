import percobaan2

#Function dengan non return type
def non_return_func(praktikan1, praktikan2, praktikan3, praktikan4):
    print(f"Selamat Datang di Praktikum DKP 2021 {praktikan1}, {praktikan2}, {praktikan3} dan {praktikan4}")

#Function dengan return type
def return_func(shift):
    print(f"Shift kalian adalah ", shift)
    if (shift == 1) or (shift == 2) :
        return print(f"Fungsi return mengembalikan nilai menjadi ", shift * 2)
    else:
        return print("Tidak ada shift tersebut")

#Function dengan Arbitrary Type
def arbitrary_func(*penutup):
    for nama in penutup:
        print("Terimakasih", nama)

#Anonymous Function
anonim_func = lambda jenispercobaan1, jenispercobaan2, kelompok: print(f"Ini adalah percobaan {jenispercobaan1} dan {jenispercobaan2} kelompok ", kelompok )

#Pemanggilan Fungsi
non_return_func("Daffa", "Afrizal", "Kamil", "Rafi")
return_func(1)
anonim_func("method", "function", 5)
arbitrary_func("Daffa", "Afrizal", "Kamil", "Rafi")

#Membuat object
p2 = percobaan2.contoh_method("Daffa", "Afrizal", "Kamil", "Rafi")

#Memanggil method dengan self parameter
p2.mulai()

#Memanggil method dengan parameter
p2.selesai(5

arbitrary_func("Daffa", "Afrizal", "Kamil", "Rafi")