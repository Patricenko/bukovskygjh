import math
x = input()
z = 0
for i in range (len(x)-1):
    match x[i]:
        case '>':
            match x[i+1]:
                case '<':
                    z += 2
                case '=':
                    z += 1
                case '>':
                    z += 1
        case '=':
            match x[i+1]:
                case '<':
                    z += 1
        case '<':
            match x[i+1]:
                case '<':
                    z += 1
print(z)
