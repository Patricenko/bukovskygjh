import tkinter
c = tkinter.Canvas(width=1900, height=900)
c.pack()
def sequence():
    c.delete('all')
    print('debug start')
    pismo = 'Arial 20 bold'
    global to_input, from_input
    _to = int(to_input.get())
    _from = int(from_input.get())
    r = _to-_from
    rozy = (900/r)*19
    x = y = 5
    rozx = 100
    if r >=100:
        rozx = 50
    elif r >=1000:
        rozx = 25
    for i in range (_from,_to+1):
        if i >=100:
            pismo='Arial 10 bold' 
        elif i >=1000:
            pismo='Arial 5 bold'
        if x>=1900:
            y += rozx
            x = 5
        c.create_rectangle(x,y,x+rozx,y+rozx)
        c.create_text(x+rozx/2,y+rozx/2, text= i, font = pismo)
        x += rozx
from_label = tkinter.Label(text = "From: ")
from_label.pack()
from_input = tkinter.Entry()
from_input.pack()
to_label = tkinter.Label(text = "To:")
to_label.pack()
to_input = tkinter.Entry()
to_input.pack()
b = tkinter.Button(text = "Start", command = sequence)
b.pack()
c.mainloop()
