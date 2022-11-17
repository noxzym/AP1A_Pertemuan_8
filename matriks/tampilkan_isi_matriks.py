from numpy import array

baris = 4
kolom = 5
A = array([[0]*kolom]*baris)

for brs in range(baris):
    for kol in range(kolom):
        print(list(A[brs][kol]))