def Pisah_Larik(A: list[int], N: int, B: list[int], M: int, C: list[int], L: int) -> None:
    for indeks in range(0, N, 1):
        A.insert(indeks, C[indeks])
    for indeks in range(N, M+N, 1):
        B.insert(indeks-N, C[indeks])
A = []
B = []
C = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
L = len(C)
pisah = Pisah_Larik(A, 10, B, 15, C, L)
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")