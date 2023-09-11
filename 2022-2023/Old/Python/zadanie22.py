#ROCK = A, PAPER = B, SCISSORS = C, X = LOSE, Y = DRAW, Z = WIN
f = open('zadanie22.txt','r')
line = f.readline()
win = 0
while line != '':
    match line[0]:
        case 'A':
            match line[2]:
                case 'X':
                    win += 3+0
                case 'Y':
                    win += 1+3
                case 'Z':
                    win += 2+6
        case 'B':
            match line[2]:
                case 'X':
                    win += 1+0
                case 'Y':
                    win += 2+3
                case 'Z':
                    win += 3+6
        case 'C':
            match line[2]:
                case 'X':
                    win += 2+0
                case 'Y':
                    win += 3+3
                case 'Z':
                    win += 1+6
    line = f.readline()
    print(win)
print(f'SCORE: {win}')
