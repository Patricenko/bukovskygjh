import tkinter
import random
c = tkinter.Canvas()
c.pack()
def bolito(suradnice):
    for i in range (50,1,-5):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        f = f'#{r:02x}{g:02x}{b:02x}'
        x = suradnice.x
        y = suradnice.y
        c.create_oval(x-i,y-i,x+i,y+i, fill = f)   

c.bind('<Button-1>', bolito)

c.mainloop()

