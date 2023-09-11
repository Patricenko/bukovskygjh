import tkinter
import random
import time
p = []
h = []
x = y = 0
pocet = 10
l = 100
done = 0
c = tkinter.Canvas(height = 1000, width = 1000)

def update():
    x = y = 0
    global p, h, l
    for i in range(pocet-done):
        c.create_rectangle(x,y,x+l,y+l,fill = h[i])
        c.create_text(x+l/2,y+l/2,text = p[i], font = 'Arial 30 bold')
        x += l
        time.sleep(1)

for i in range(pocet):
    r = random.randrange(-100,100)
    p.append(r)
    h.append('white')
    c.create_rectangle(x,y,x+l,y+l,fill = h[i])
    c.create_text(x+l/2,y+l/2,text = r, font = 'Arial 30 bold')
    x += l

for i in range (len(p)):
    for j in range(len(p)-1-i):
        if p[j] > p[j+1]:
            p[j], p[j + 1] = p[j + 1], p[j]
        h[j] = 'grey'
        update()
    done += 1  
    print(p)
c.pack()
c.mainloop()
