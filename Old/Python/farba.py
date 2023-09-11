import tkinter
import random

c = tkinter.Canvas()
c.pack()

def farba(px):
    if px==0:
        return 'red'
    elif px==1:
        return 'green'
    else:
        return 'yellow'

for i in range (300):
    x = random.randint(10,300)
    y = random.randint(10,200)
    a = random.randint(2,30)
    f = random.randint(0,3)
    c.create_rectangle(x, y, x+a, y+a, fill = farba(f))


c.mainloop()
