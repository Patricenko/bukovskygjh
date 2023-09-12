import tkinter as tk
c = tk.Canvas()
def square(x,y,r,z):
    c.create_rectangle(x-r,y-r,x+r,y+r)
    if r <= z:
        return print('koniec')
    square(x,y,r-z,z)

def square2(x,y,r,z):
    c.create_rectangle(x,y,x+r,y+r)
    if r <= z:
        return print('koniec')
    square2(x,y,r-z,z)

x = list(map(int,input().split()))
if x[0] == 0: square(x[1],x[2],x[3],x[4])
else: square2(x[1],x[2],x[3],x[4])

c.pack()
c.mainloop()