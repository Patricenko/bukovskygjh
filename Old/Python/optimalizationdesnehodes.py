p = p0 = list(input())
x = z = dolava = doprava = 0
for i in range (len(p)):
    if p[i] == '<':
        dolava += 1
    else:
        break
for i in range (len(p)-1,0,-1):
    if p[i] == '>':
        doprava += 1
    else:
        break
for i in range (dolava,len(p)-doprava-1,1):
    match p[i]:
        case '<':
            if p[i+1] == '<':
                x += 1
                
        case '=':
            if p[i+1] == '<':
                x += 1
        case '>':
            if p[i+1] == '<':
                x += 2
            elif p[i+1] == '>' or p[i+1] == '=':
                x += 1
print(x)         
            
            
