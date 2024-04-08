rangey = []
rangex = []
final = 0
n = int(input())
s = int(input())
v = int(input())
for i in range(n):
    true = 0
    x,y = map(int, input().split())
    if i == 0: true = 1
    else:
        if rangex[0] < x < rangex[1]:
            if not rangey[0] < y < rangey[1]: true = 1
        else: true = 1
    if true:
        rangex = [x - s, x + s]
        rangey = [y - v, y + v]
        final += 1
print(final)