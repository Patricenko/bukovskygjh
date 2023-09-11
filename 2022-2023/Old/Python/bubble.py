p = s = list(input())
# BUUBLESORT
for i in range (len(p)):
    for j in range(len(p)-1-i):
        if p[j] > p[j+1]:
            p[j], p[j + 1] = p[j + 1], p[j]
print(p)
# WINDSORT
for i in range (len(s)):
    for j in range(len(s)-i):
        if s[i] > s[j+i]:
            s[i], s[j + i] = s[j + i], s[i]
print(s)
