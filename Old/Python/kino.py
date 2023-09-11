#[[],[],[]]
# for rad in kino:
#   for sedadlo in rad:
#       f.write(sedadlo)
#   f.write('\n')

import tkinter
kino = []
x = y = 0 
def klik(sur):
    x = (sur.x//50)
    y = (sur.y//50)
    match kino[y][x]:
        case '0':
            color = 'green'
            kino[y][x] = '1'
        case '1':
            color = 'red'
            kino[y][x] = '2'
        case '2':
            color = 'grey'
            kino[y][x] = '0'
    c.create_rectangle(x*50,y*50,x*50+50,y*50+50, fill=color)
def load(vstup):
    kino = []
    f = open('kino.txt','r')
    r = f.readlines()
    while r != '':
        rad = r.strip().split()
        kino.append(rad)
        r = f.readline()
    f.close()
    print(kino)
    return kino
def structure():
    

load(1)
