import tkinter as tk
c = tk.Canvas()

def circle(x,y,r):
    c.create_oval(x-r,y-r,x+r,y+r)
    r -= 1
    x += 2*r + 1
    if r == 1:
        return
    circle(x,y,r)

x = list(map(int,input().split()))
circle(x[0],x[1],x[2])
c.pack()
c.mainloop()