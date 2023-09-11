import tkinter
import random
c = tkinter.Canvas(width=701, height=701)
x = t = y = linel = row = 1
p = 100
q = 2
line = []
pos = []
crossed = []
zreby = []
def rendom():
    global zreby
    zreby.clear()
    for i in range (3):
        zreby.append(random.randrange(1,50))
    #print(zreby) #TESTING
for i in range (49):
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
def send():
    global ly, lx, uloz, crossed, zreby, p
    for i in crossed:
        if i in zreby:
            print(f'You won! One of the numbers was {i}! Starting new game...')
            c.delete('line')
            crossed.clear()
            rendom()
def get(cor):
    global ly, lx, p, q
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
                    print(f'Number {number} already crossed, removed from choice.')
                    c.create_rectangle(x0,y0,x0+p,y0+p, fill = 'white')
                    c.create_text(x0+p/2,y0+p/2, text = number, font = 'Arial 30 bold')
                    crossed.remove(number)
                    
                elif len(crossed) <= q:
                    print(f'New cross on number: {number}')
                    c.create_line(x0,y0,x0+p,y0+p, width = 2, tags = 'line')
                    c.create_line(x0,y0+p,x0+p,y0, width = 2, tags = 'line')
                    crossed.append(number)
                else:
                    print('Maximum number of crossed lines reached ({q}) or clicked out of platform')
        number += 1
        x0 = y0 = 0
rendom()
c.bind('<Button-1>', get)
b = tkinter.Button(text = "Send", command = send)
b.pack()
c.pack()
c.mainloop()
