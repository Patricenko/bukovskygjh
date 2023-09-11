import tkinter
c = tkinter.Canvas(width=1000, height=200)
c.pack()
def rusen(x,y): #80x40 obldznik
    c.create_rectangle(x,y-40,x+80,y, fill = 'blue')
    c.create_rectangle(x+10,y-40,x+30,y-50, fill = 'green')
    c.create_rectangle(x+50,y-40,x+80,y-60, fill = 'red')
    c.create_text(x+22,y-60, text='///', font = 'Arial 15 bold')
    for i in range (10,90,20):
        x1 = x+i
        c.create_oval(x1-10,y-10,x1+10,y+10, fill = 'black')
def move():
    global x
    print (f'pozicia {x}')
    c.delete('all')
    if x <= -80:
        x = 1050
    x = x-3
    rusen(x,y)
    c.after(20,move)
x,y = 1050,180
move()       
c.mainloop()
