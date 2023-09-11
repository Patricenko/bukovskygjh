import math
x = list(map(int,input().split())) # po4et kvaskov
n = x[0]
k = x[1]
t = x[2]
t0 = 0
kvasky = []
for i in range (t):
    for j in range(n):
        if int(kvasky[j]) == 0:
            kvasok[j] = 6
            for u in range(k):
                kvasky.append(8)
        kvasky[j] = int(kvasky[j]) + 1
print(len(kvasky))
        
        
