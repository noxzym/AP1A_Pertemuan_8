def digit(d: int) -> str:
    kata = ""

    match d:
        case 1:
            kata = " satu"
        case 2:
            kata = " dua"
        case 3:
            kata = " tiga"
        case 4:
            kata = " empat"
        case 5:
            kata = " lima"
        case 6:
            kata = " enam"
        case 7:
            kata = " tujuh"
        case 8:
            kata = " delapan"
        case 9:
            kata = " sembilan"

    return kata

angka, sisa, d1, d2, d3, d4 = int(), int(), int(), int(), int(), int()
angka1, angka2, angka3, angka4 = str(), str(), str(), str()

angka = int(input("Masukkan sebuah angka (maks 4 digit) : "))

d4 = angka // 1000
sisa = angka % 1000
d3 = sisa // 100
sisa = sisa % 100
d2 = sisa // 10
sisa = sisa % 10
d1 = sisa

if d4 > 1:
    angka4  = digit(d4) + " ribu"
elif d4 == 1:
    angka4 = "seribu"

if d3 > 1:
    angka3 = digit(d3) + " ratus"
elif d3 == 1:
    angka3 = "seratus"

if d2 > 1:
    angka2 = digit(d2) + " puluh"
    if d1 > 1:
        angka1 = digit(d1)
elif d2 == 1:
    if d1 == 0:
        angka2 = "sepuluh"
    elif d1 == 1:
        angka2 = "sebelas"
    else:
        angka2 = digit(d1) + " belas"

if d1 > 1:
    angka1 = digit(d1)

print(f"angka = {angka4 + angka3 + angka2 + angka1}")