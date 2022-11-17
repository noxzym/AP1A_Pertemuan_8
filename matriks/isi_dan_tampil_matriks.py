from numpy import array, typing

def Isi_Matriks(N: int, M: int, A: typing.NDArray) -> None:
    for brs in range(N):
        for kol in range(M):
            A[brs][kol] = int(input(f"Masukkan elemen baris = {brs} kolom = {kol}: "))

def Tampil_Matriks(N: int, M: int, A: typing.NDArray) -> None:
    for brs in range(N):
        for kol in range(M):
            print(A[brs][kol])

baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))
matriks = array([[0]*kolom]*baris)

Isi_Matriks(baris, kolom, matriks)
Tampil_Matriks(baris, kolom, matriks)