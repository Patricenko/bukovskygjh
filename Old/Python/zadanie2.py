import time
p = open('zadanie2.txt','r')
list = []
win = 0
last = 0
while p:
    list = []
    list = p.readline()
    if list == '':
        break
    match list[2]:
        case 'X':
            win +=1
            now = 'ROCK'
            if list[0] == 'B':
                win += 0
            elif list[0] == 'A':
                win += 3
            elif list[0] == 'C':
                win += 6
        case 'Y':
            win += 2
            now = 'PAPER'
            if list[0] == 'A':
                win += 6
            elif list[0] == 'B':
                win += 3
            elif list[0] == 'C':
                win += 0
        case 'Z':
            win += 3
            now = 'SCISSORS'
            if list[0] == 'B':
                win += 6
            elif list[0] == 'A':
                win += 0
            elif list[0] == 'C':
                win += 3
    print(int(win)-int(last))
    last = win
print(win)
p.close()
