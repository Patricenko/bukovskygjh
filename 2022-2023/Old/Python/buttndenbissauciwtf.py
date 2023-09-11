import tkinter
c = tkinter.Canvas(width=500, height=500)
c.pack()

def reklama(x,y):
    c.create_text(x,y, text= 'Ahoj som reklama', font = 'Arial 15 bold', fill = 'blue')

def animacia():
    global x
    print (f'pozicia {x}')
    c.delete('all')
    if x <= -120:
        x = 620
    x = x-3
    reklama(x,y)
    c.after(20,animacia)


x = 620
y = 250
button = tkinter.Button(text = 'Spusti reklamu ', command = animacia, bg= 'white')
button.pack()
c.mainloop()
