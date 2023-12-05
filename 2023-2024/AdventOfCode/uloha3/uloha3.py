f = open("input.txt", "r")
l = f.readline()
v = 0
tab = []
while l != "":
    x = list(l)
    active = 0
    for i in range (len(x)):
        if x[i].isnumeric():
            if active == 0:
                try:
                    active = 1
                    val = x[i]
                    if x[i+1].isnumeric():
                        x[i] = x[i]+x[i+1]
                        val = x[i]
                        if x[i+2].isnumeric():
                            x[i] = x[i] + x[i+2]
                            val = x[i]
                except: pass
            else: x[i] = val
        else: active = 0
    tab.append(x)
    l = f.readline()
for i in range(len(tab)):
    for j in range(len(tab[i])):
        if not tab[i][j].isnumeric():
            if tab[i][j] != ".":
                try:
                    if tab[i-1][j-1].isnumeric():
                        v += int(tab[i-1][j-1])
                        tab[i][j] = f'{tab[i][j]} + {tab[i-1][j-1]}'
                        break
                except: continue
                try:
                    if tab[i-1][j].isnumeric():
                        v += int(tab[i-1][j])
                        tab[i][j] = f'{tab[i][j]} + {tab[i-1][j]}'
                        break
                except: continue
                try:
                    if tab[i-1][j+1].isnumeric():
                        v += int(tab[i-1][j+1])
                        tab[i][j] = f'{tab[i][j]} + {tab[i-1][j+1]}'
                        break
                except: continue
                try:
                    if tab[i][j-1].isnumeric():
                        v += int(tab[i][j-1])
                        tab[i][j] = f'{tab[i][j]} + {tab[i][j-1]}'
                        break
                except: continue
                try:
                    if tab[i][j+1].isnumeric():
                        v += int(tab[i][j+1])
                        tab[i][j] = f'{tab[i][j]} + {tab[i][j+1]}'
                        break
                except: continue
                try:
                    if tab[i+1][j-1].isnumeric():
                        v += int(tab[i+1][j-1])
                        tab[i][j] = f'{tab[i][j]} + {tab[i+1][j-1]}'
                        break
                except: continue
                try:
                    if tab[i+1][j].isnumeric():
                        v += int(tab[i+1][j])
                        tab[i][j] = f'{tab[i][j]} + {tab[i+1][j]}'
                        break
                except: continue
                try:
                    if tab[i+1][j+1].isnumeric():
                        v += int(tab[i+1][j+1])
                        tab[i][j] = f'{tab[i][j]} + {tab[i+1][j+1]}'
                        break
                except: continue


for i in tab: print(i)
print(v)


from re import *
from functools import reduce
def main():
    s = lambda p, M: sub(p, '.', M).splitlines()
    with open('input.txt') as f:
        D, K, G = s('[^\d\n]', L:=f.read()), s('[\d]', L), s('[^*\n]', L)
    h = ['.'*(w:=len(D[0])+2)]
    p = lambda M: ''.join(h+[f'.{l}.' for l in M]+h)
    d, k, g = p(D), p(K), p(G)
    S = [(m.start(), m.end()) for m in finditer('[^.]+', d)]
    C = lambda m: [i=='1' for i in sub('[^.]', '1', m)]
    K, G = C(k), C(g)
    c = lambda i, T: {i+j: T[i+j] for j in[-w-1,-w,-w+1,-1,1,w-1,w,w+1]}
    print(sum([int(d[slice(*r)]) for r in S if any([any(c(i, K).values()) for i in range(*r)])]))
    L = {i: set() for i in range(len(G))}
    for r in S: [L[j].add(r) for i in range(*r) for j,v in c(i,K).items() if v]
    prod = lambda l: reduce(lambda x, y: x*y, l, 1)
    print(sum([prod([int(d[slice(*r)]) for r in v]) for _, v in L.items() if len(v)==2]))
if __name__ == '__main__':
    main()