import tkinter
c = tkinter.Canvas()
c.pack()
def bod(pos):
    global x0,y0
    x = pos.x
    y = pos.y
    if x0 != 0 and y0 != 0:
        c.create_line(x0,y0,x,y, fill = 'black', width = 4)
    x0 = x
    y0 = y
    c.create_oval(x-4, y-4, x+4, y+4, fill='black')
x0 = y0 = 0  
c.bind('<Button-1>', bod)
c.mainloop()
