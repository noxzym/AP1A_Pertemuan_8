def Gabung_Larik(A: list[int], N: int, B: list[int], M: int, C: list[int]) -> None:
    global L
    L = N + M
    for indeks in range(0,  N, 1):
        C.insert(indeks, A[indeks])
    for indeks in range(N,  L, 1):
        C.insert(indeks, B[indeks-N])

A = [1,2,3,4,5]
B = [11,12,13,14,15]
C = []
L = 0
Gabung_Larik(A, len(A), B, len(B), C)
print(C, L)