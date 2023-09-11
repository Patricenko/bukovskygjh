import tkinter
import random

c = tkinter.Canvas()
c.pack()

def vytvor(a):
    print(a.keysym)    
    x = random.randrange(300)
    y = random.randrange(200)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    f = f'#{r:02x}{g:02x}{b:02x}'
    if a.keysym == 'Right':
        c.create_rectangle(x,y,x+50,y+50, fill = f)
        c.create_text(x+25,y+25, text = a.keysym)
    elif a.keysym == 'Left':
        c.create_oval(x,y,x+50,y+50, fill = f)
        c.create_text(x+25,y+25, text = a.keysym)

c.bind_all('<Key>', vytvor)

c.mainloop()
