from numpy import array

baris = 4
kolom = 5
matriks = array([array([0]*5)]*4)

for brs in range(baris):
    for kol in range(kolom):
        matriks[brs][kol] = int(input(f"elemen baris = {brs} kolom = {kol}: "))

for brs in range(baris):
    for kol in range(kolom):
        print(matriks[brs][kol])
    print()