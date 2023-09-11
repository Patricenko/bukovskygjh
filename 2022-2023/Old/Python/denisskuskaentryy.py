import tkinter
import random
c = tkinter.Canvas()
c.pack()
def funkcia():
    c.delete('all')
    global e, x, y
    if x >= 360:
        x = 0
        y += 20
    if y >= 360:
        y = 20
    x += 3
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    f = f'#{r:02x}{g:02x}{b:02x}'
    c.create_text(x,y,text=e.get(), fill = f, font = 'Arial 15 bold')
    c.after(20,funkcia)
    
x, y = 0, 20   
l = tkinter.Label(text = 'Entry: ')
l.pack()
e = tkinter.Entry()
e.pack()
b = tkinter.Button(text='Konaj', command = funkcia)
b.pack()
c.mainloop()
