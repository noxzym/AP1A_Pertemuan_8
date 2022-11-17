from numpy import array, typing

def Baca_Larik(M: int, A: typing.NDArray) -> None:
    for indeks in range(M):
        A[indeks] = int(input(f"Masukkan elemen ke-{indeks} : "))

def Cetak_Larik(M: int, A: typing.NDArray) -> None:
    for indeks in range(M):
        print(A[indeks])

def geser_kanan(A: typing.NDArray, M: int) -> None:
    temp = A[M-1]
    for indeks in range(M-1, 0, -1):
        A[indeks] = A[indeks-1]
    A[0] = temp

def geser_kiri(A: typing.NDArray, M: int) -> None:
    temp = A[0]
    for indeks in range(1, M, 1):
        A[indeks-1] = A[indeks]
    A[M-1] = temp

Nmax = 100
N = int(input("Masukkan jumlah elemen larik : "))
A = array([0] * Nmax)
Baca_Larik(N, A)
pilihan = int(input(f"Pilih salah satu : \n1. Geser Kanan \n2. Geser Kiri\nPilihan : "))
if pilihan == 1:
    geser_kanan(A, N)
elif pilihan == 2:
    geser_kiri(A, N)
else:
    print("Pilihan tidak dikenal")
Cetak_Larik(N, A)