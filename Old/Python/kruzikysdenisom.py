import tkinter
import random
c = tkinter.Canvas()
c.pack()
def vykresli(pos):
    global a
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    f = f'#{r:02x}{g:02x}{b:02x}'
    x = pos.x
    y = pos.y
    c.create_oval(x-a, y-a, x+a, y+a, fill = f)
    a += 0.5
def vymaz(pos):
    global a
    c.delete('all')
    a = 0.5
a = 0.5
c.bind('<B1-Motion>', vykresli)
c.bind('<Button-1>', vymaz)
c.mainloop()
