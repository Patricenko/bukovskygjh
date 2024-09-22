# 9.9.2024
import random
t = 20

def bubble_sort(p: list, n = t) -> list:
    for i in range(n):
        for j in range(n-1):
            if p[j] > p[j+1]:
                p[j], p[j+1] = p[j+1], p[j]
    return p

def merge(l: list, r: list) -> list:
    p = []
    while l and r:
        if l[0] < r[0]:
            p.append(l.pop(0))
        else:
            p.append(r.pop(0))
    return p + l + r

def merge_sort(p: list) -> list:
    if len(p) <= 1:
        return p
    else:
        l = merge_sort(p[:len(p)//2])
        r = merge_sort(p[len(p)//2:])
        return merge(l, r)

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


