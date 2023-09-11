import tkinter
import random
c = tkinter.Canvas(width=1000)
c.pack()
def program():
    c.delete('all')
    global t
    x = y = 50
    for i in t.get():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        f = f'#{r:02x}{g:02x}{b:02x}'
        c.create_text(x, y, fill = f, text = i, font = 'Comic S 72 bold')
        print (f'letter: {i}, color: {f}, position: {x}')
        x = x+55
    
t = tkinter.Entry()
t.pack(side = 'left')
b = tkinter.Button(text= 'SET' , command = program)
b.pack(side = 'left')

c.mainloop()
