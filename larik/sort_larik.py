def Sort_Larik(A: list[int], N: int):
    temp = 0
    for idx1 in range(N-1):
        for idx2 in range(idx1, N):
            if A[idx1] > A[idx2]:
                temp = A[idx1]
                A[idx1] = A[idx2]
                A[idx2] = temp

A = [9, 1, 6, 10, 4, 2, 3, 5, 8, 7]
N = len(A)
Sort_Larik(A, N)
print(A)