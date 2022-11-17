def Cari_elemen(A: list[int], N: int, x: int) -> int:
    indikator = "N"
    posisi = 0
    indeks = 1
    while indeks < N + 1 and indikator == "N":
        if A[indeks] == x:
            indikator = "Y"
            posisi = indeks
        indeks = indeks + 1

    return posisi

print(Cari_elemen([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10, 7))