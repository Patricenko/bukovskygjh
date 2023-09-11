import tkinter


c = tkinter.Canvas()
c.pack()


def kruzok(suradnice):
    x = suradnice.x
    y = suradnice.y
    c.create_oval(x-5,y-5,x+5,y+5, fill = 'red')

def stvorcek(suradnice):
    x = suradnice.x
    y = suradnice.y
    c.create_rectangle(x-5,y-5,x+5,y+5, fill = 'blue')
def trojuholnicek(suradnice):
    x = suradnice.x
    y = suradnice.y
    c.create_triangel(x-5,y-5,x+5,y+5, fill = 'blue')
    

    
c.bind('<B1-Motion>', kruzok)
c.bind('<B3-Motion>', stvorcek)
c.bind('<B2-Motion>', trojuholnicek)

c.mainloop()
