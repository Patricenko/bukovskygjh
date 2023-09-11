import tkinter
import random
c = tkinter.Canvas()
c.pack()
def bolito():
    global y1
    global x1
    global x2
    global f1
    global f2
    global x
    c.delete('all')
    if x1 == x2:
        c.create_text(190,100, text='KBOOM', font = 'Arial 35 bold')
    elif x1 >= 0 and x2 <= 0:
        x1 = 10
        x2 = 370
        y1 = random.randint(0,260)
        x = ''
        x = f1
        f1 = f2
        f2 = x
    elif x1 <= 0 and x2 >=380:
        x1 = 370
        x2 = 10
        y1 = random.randint(0,260)
    c.create_oval(x1-10,y1-10,x1+10,y1+10, fill = f1)
    c.create_oval(x2-10,y1-10,x2+10,y1+10, fill = f2)
    x1 = x1+2
    x2 = x2-2
    c.after(20,bolito)
    

x1 = 10
x2 = 370
f1 = 'red'
f2 = 'blue'
x = ''
y1 = random.randint(0,260)
bolito()

c.mainloop()






import tkinter
import random
c = tkinter.Canvas()
c.pack()
def funkcia(suradnice):
    # najprv definujem suradnice
    global x1
    global y1
    x = suradnice.x
    y = suradnice.y
    c.create_oval(x-2,y-2,x+2,y+2, fill = 'black')
    if x1 == 0 and y1 == 0:
        c.create_oval(x-2,y-2,x+2,y+2, fill = 'black')
    else:
        c.create_oval(x-2,y-2,x+2,y+2, fill = 'black')
        c.create_line(x1,y1,x,y)
    x1 = x
    y1 = y
x1 = 0
y1 = 0
c.bind('<Button-1>', funkcia)
c.mainloop()
