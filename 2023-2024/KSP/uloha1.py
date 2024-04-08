l = []
n = int(input())
s = int(input())
v = int(input())
for i in range(n):
    x,y = map(int, input().split())
    t = 1
    for p in l:
        if p[0]-s < x < p[0]+s:
            if p[1]-v < y < p[1]+v:
                t = 0
                break
    if t == 1: l.append([x,y])
print(len(l))

