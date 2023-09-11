p = input()
x = 0
for i in range(0, len(p)-1, 1):
    match p[i]:
        case '>':
            if p[i+1] == '<':
                x += 2
            elif p[i+1] == '>' and i+1 != len(p):
                x += 1
            elif p[i+1] == '=':
                x += 1
        case '=':
            if p[i+1] ==  '<':
                x += 1
        case '<':
            if p[i+1] == '<' and i != 0:
                x += 1
print(x)
