from numpy import array, typing

N = 100
A = array([0]*N)
K = 0

def Baca_Larik(M: int, A: typing.NDArray) -> None:
    for indeks in range(M):
        A[indeks] = int(input(f"Masukkan elemen ke-{indeks}: "))

K = int(input("Masukkan Jumlah Elemen Larik ( < 100 ) : "))

Baca_Larik(K, A)

print(list(filter(None, A)))