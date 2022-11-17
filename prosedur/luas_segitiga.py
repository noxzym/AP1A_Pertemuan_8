def Hit_Luas_Segi_3(a: float, t: float) -> None:
    global luas
    luas = a * t / 2.0

alas = float(input("Masukkan alas segitiga : "))
tinggi = float(input("Masukkan tinggi segitiga : "))
luas = 0
Hit_Luas_Segi_3(alas, tinggi)
print(f"Luas segitiga = {luas}")