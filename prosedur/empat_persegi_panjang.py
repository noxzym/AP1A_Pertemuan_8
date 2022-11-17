from math import sqrt

pilihan = int()
panjang, lebar, hasil = float(), float(), float()

def menu():
    print(f"""
Menu Program Empat Persegi Panjang
1. Menghitung Luas
2. Menghitung Keliling
3. Menghitung Diagonal
4. Keluar dari Program
""")

def baca_dimensi() -> None:
    global panjang, lebar
    try:
        panjang = float(input(f"Masukkan Panjang : "))
        lebar = float(input(f"Masukkan Lebar : "))
    except ValueError:
        pass

def hitung_luas() -> None:
    global hasil
    luas = panjang * lebar
    hasil = luas

def hitung_keliling() -> None:
    global hasil
    keliling = 2 * (panjang + lebar)
    hasil = keliling

def hitung_diagonal() -> None:
    global hasil
    diagonal = sqrt(panjang ** 2 + lebar ** 2)
    hasil = diagonal

def tampil_hasil() -> None:
    print(f"Hasil = {hasil}")

while pilihan != 4:
    menu()

    try:
        pilihan = int(input(f"Masukkan pilihan anda : "))
    except ValueError:
        pass

    if pilihan < 4:
        baca_dimensi()

    match pilihan:
        case 1:
            hitung_luas()
        case 2:
            hitung_keliling()
        case 3:
            hitung_diagonal()
        case 4:
            print("Selesai ... sampai jumpa")
        case _:
            print("Pilihan salah, Ulangi !")
            break

    if pilihan < 4:
        tampil_hasil()
