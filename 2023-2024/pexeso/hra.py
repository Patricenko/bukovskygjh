import tkinter
import modul

o = 10
a = 200

c = tkinter.Canvas(width = 2*o+a*4, height = 2*o+a*4)
c.pack()
current = modul.Pexeso(o, a, c)
c.bind('<Button-1>', current.click)


c.mainloop()