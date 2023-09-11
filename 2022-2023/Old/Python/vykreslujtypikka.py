import tkinter
import random

c = tkinter.Canvas()
c.pack()

def stvorcek(suradnice):
    x = random.randrange(300)
    y = random.randrange(200)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    f = f'#{r:02x}{g:02x}{b:02x}'
    c.create_rectangle(x,y,x+20,y+20, fill = f)
def kruzok(suradnice):
    x = random.randrange(300)
    y = random.randrange(200)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    f = f'#{r:02x}{g:02x}{b:02x}'
    c.create_oval(x,y,x+20,y+20, fill = f)
    

c.bind_all('s', stvorcek)
c.bind_all('k', kruzok)

c.mainloop()



