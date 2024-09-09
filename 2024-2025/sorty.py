# 9.9.2024
import random
t = 20

def randomize(n: int, p = []) -> list:
    for i in range(n):
        p.append(random.randint(1, 1000))
    return p
def max_sort(p: list, n = t) -> list:
    global max_p
    for i in range(n):
        if i == 0:
            max_p = 0
        if p[i] >= p[max_p]:
            max_p = i
    p[max_p], p[n-1] = p[n-1], p[max_p]
    if n > 1:
        max_sort(p, n-1)
    return p

p = randomize(t)
print("Unsorted:", p)
print("Sorted:", max_sort(p))


