import tkinter
import random
c = tkinter.Canvas()
c.pack()

def funkcia(suradnice):
    global a
    x = suradnice.x
    y = suradnice.y
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    f = f'#{r:02x}{g:02x}{b:02x}'
    c.create_oval(x-a,y-a,x+a,y+a, fill = f)
    a = a+0.5
def funkcia2(suradnice):
    global a
    c.delete('all')
    a = 0.5
a = 0.5
c.bind('<Button-1>', funkcia2)
c.bind('<B1-Motion>', funkcia)
c.mainloop()
