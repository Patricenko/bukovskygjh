p = list(input())
x = 0
for i in range(len(p)-1):
    if p[i] == '>':
        if p[i+1] == '<':
            x += 2
        else:
            x += 1
    elif p[i] == '=' or p[i] == '<':
        if p[i+1] ==  '<':
            x += 1
    else:
        break
print(x)
        
