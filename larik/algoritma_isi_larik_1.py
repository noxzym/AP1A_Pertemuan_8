from numpy import array

N = 10
A = array([0] * N)
for indeks in range(0, N, 1):
    A[indeks] = int(input(f"Masukkan elemen ke-{indeks}: "))
print(list(A))
