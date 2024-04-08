xset = set()
yset = set()
final = 0
n = int(input())
s = int(input())
v = int(input())
for i in range(n):
    true = 0
    x,y = map(int, input().split())
    if i == 0: true = 1
    else:
        if x in xset:
            if not y in yset:
                true = 1
        else: true = 1
    if true == 1:
        for a in range(x - s + 1, x + s):  xset.add(a)
        for a in range(y - v + 1, y + v):  yset.add(a)
        final += 1
print(final)