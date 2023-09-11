import math
move = ''
p = input()
for i in range (len(p)):
    match p[i]:
        case '^':
            move += 'v'
        case 'v':
            move += '^'
        case '<':
            move += '>'
        case '>':
            move += '<'
print(move)

