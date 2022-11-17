def tukar() -> None:
    global A, B
    temp = A
    A = B
    B = temp

A = int(input("Masukkan nilai A : "))
B = int(input("Masukkan nilai B : "))
tukar()
print("Setelah ditukar : ")
print(f"A = {A}, B = {B}")