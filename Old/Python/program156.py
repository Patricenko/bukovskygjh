import tkinter
import random
c = tkinter.Canvas()
c.pack()
def funkcia():
    global e
    x = y = 30
    text = e.get()
    for i in range(len(text)):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        f = f'#{r:02x}{g:02x}{b:02x}'
        if i%2 == 0:
            y = 30
        else:
            y += 15
        c.create_text(x,y,text=text[i], font = 'Arial 35 bold', fill = f)
        x += 35
e = tkinter.Entry()
e.pack(side='left')
b = tkinter.Button(text='Spusti', command=funkcia)
b.pack(side='left')
c.mainloop()
