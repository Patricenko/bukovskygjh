import tkinter as tk
import time
c = tk.Canvas()
def circle(x,y,r,z):
    time.sleep(0.5)
    c.create_oval(x-r,y-r,x+r,y+r)
    if r <= z:
        return print('koniec')
    circle(x+2*r-z,y,r-z,z)

x = list(map(int,input().split()))
circle(x[0],x[1],x[2],x[3])

c.pack()
c.mainloop()