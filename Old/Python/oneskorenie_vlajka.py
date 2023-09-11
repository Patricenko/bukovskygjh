import tkinter
import random
c = tkinter.Canvas()
c.pack()

def kruzok():
    x = random.randint(1,380)
    y = random.randrange(1,260)
    if 100 < x < 150 or 80 < y < 130:
        f = 'yellow'
    else:
        f = 'blue'
    c.create_oval(x-5,y-5,x+5,y+5, fill = f)

for i in range (5000):
    kruzok()
    c.update()
    c.after(10)


c.mainloop()
