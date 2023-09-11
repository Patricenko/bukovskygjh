import tkinter
import random
p = 100
q = 2
c = tkinter.Canvas(height = 900,width = 701)
def rendom():
    global crossed, ticked, n, x, y, linel, t, num, n, pos, line, crossed, ticked, row, tries, success, now
    x = t = y = linel = row = 1
    tries = success = now = 0
    num = 50
    n = 5
    line = []
    pos = []
    crossed = []
    ticked = []
    while len(crossed) < n:
        now = random.randrange(1,num)
        if not now in crossed:
            crossed.append(now)
    crossed.sort()
    print(crossed)
    main()
def main():
    global x, y, linel, row, pos
    for i in range (num-1):
        pos.append(0)
        if x >= 700:
            y += 100
            x = 1
            linel += 1
            row = 1
        c.create_rectangle(x,y,x+p,y+p, fill = 'white')
        c.create_text(x+p/2,y+p/2,text = i+1, font = 'Arial 30 bold')
        x += 100
        pos[i] = f'{linel} {row}'
        row += 1

def get(cor):
    global ly, lx, p, q, tries, success
    x = cor.x
    y = cor.y
    number = 1
    for i in pos:
        curpos = []
        curpos = i.split()
        x0 = int(curpos[1])
        y0 = int(curpos[0])
        x0 = (x0-1)*100+1
        y0 = (y0-1)*100+1
        if x >= x0 and x <= x0+p:
            if y >= y0 and y <= y0+p:
                if number in crossed:
                    print(f'Attack successfull!')
                    c.create_rectangle(x0,y0,x0+p,y0+p, fill = '#A04000')
                    c.create_text(x0+p/2,y0+p/2, text = number, font = 'Arial 30 bold', fill='white')
                    success += 1
                    if success == len(crossed):
                        c.create_text(20,850, text='THE END! NUMBER OF TRIES: {tries}', font='Arial 30 bold')
                        rendom()
                elif number in ticked:
                    print('Already attacked')
                else:
                    print('Attact unsuccessfull!')
                    c.create_rectangle(x0,y0,x0+p,y0+p, fill = 'blue')
                    c.create_text(x0+p/2,y0+p/2, text = number, font = 'Arial 30 bold', fill='white')
                    tries += 1
                    ticked.append(number)
        number += 1
        x0 = y0 = 0
rendom()
c.bind('<Button-1>', get)
b = tkinter.Button(text = 'Reset', command = rendom)
b.pack(side = 'bottom')
c.pack()
c.mainloop()