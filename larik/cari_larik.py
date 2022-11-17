def Cari_elemen(A: list[int], N: int, x: int) -> str:
    indikator = "N"
    posisi = 0
    indeks = 1
    
    try:
        while indeks < N + 1 and indikator == "N":
            if A[indeks] == x:
                indikator = "Y"
                posisi = indeks
            indeks += 1
    except IndexError:
        pass

    return f"Indikator = {indikator}, Posisi = {posisi if indikator == 'Y' else 'Tidak ada'}"

print(Cari_elemen([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 10, 11))