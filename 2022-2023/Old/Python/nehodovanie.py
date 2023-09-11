p = p0 = list(input())
dolava = doprava = x = z = 0
if p[len(p)-1] == '>':
    doprava = 1
if p[0] == '<':
    dolava = 1
for i in range (0, len(p)-1, 1):
    match p[i]:
        case '<':
            x += z
            z = 0
            if dolava == 0 and p[i+1] == '<':
                x += 1
        case '=':
            x += z
            z = dolava = 0
            if p[i+1] == '<':
                x += 1
        case '>':
            dolava = 0
            match p[i+1]:
                case '>':
                    if doprava == 0:
                        x += 1
                    else:
                        z += 1
                case '<':
                    x += 2
                case '=':
                    x += 1
print(x)
                
