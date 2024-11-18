def zadanie_3(A: int, B: int):
    while A != B:
        if A < B:
            B -= A
        else:
            A -= B
    return A

def riesenie_3(A: int, B: int):
    while A % B != 0:
        A, B = B, A % B
    return B


def zadanie_4(A, N):
    vysl = 1
    for i in range(N):
        vysl *= A
    return vysl

def riesenie_4(A, N):
    while N > 0:
        if N % 2 == 1:
            A = A * A
        N = N // 2
    return A

A = 2
B = 4
print(riesenie_3(A, B))
print("riesenie: ", riesenie_4(A, B), "kontrola: ", 2**B)
