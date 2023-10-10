import tkinter
import random
import time
class Tkruh:
    def __init__(self, x, y, r = 25):
        self.x = x
        self.y = y
        self.r = r
        fill_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
        self.tvar = c.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = fill_color)
        self.popis = c.create_text(self.x, self.y, text=str(f'{x},{y}'))

    def zmenhodnotu(self, h):
        self.h = h
        c.itemconfig(self.popis, text = str(self.h))
    def zmenvelkost(self, r):
        self.r = self.r+r
        c.coords(self.tvar, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
    def nahodnemen(self):
        self.x = self.x+random.randrange(-20,20)
        self.y = self.y+random.randrange(-20,20)
        if self.x < self.r: self.x = self.r
        if self.x >= 500-self.r: self.x = 500-self.r
        if self.y < self.r: self.y = self.r
        if self.y >= 500-self.r: self.y = 500-self.r
        c.coords(self.tvar, self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
        self.zmenhodnotu(f'{self.x},{self.y}')
        c.coords(self.popis, self.x, self.y)
        c.update()
def leftclick(sur):
    for p in kruhy:
        p.zmenhodnotu(f'{sur.x},{sur.y}')
        if sur.x >= p.x - p.r and sur.y >= p.y - p.r and sur.x <= p.x + p.r and sur.y <= p.y + p.r:
            p.zmenhodnotu(f'GG')

def scrollclick(sur):
    for p in kruhy:
        p.zmenvelkost(5)

def rightclick(sur):
    for p in kruhy:
        p.zmenvelkost(-5)
c = tkinter.Canvas(height = 500, width = 500)
c.pack()
c.bind("<Button-3>",rightclick)
c.bind("<Button-2>",scrollclick)
c.bind('<Button-1>',leftclick)
kruhy = []
for i in range(50):
    kruhy.append(Tkruh(250,250, 20))
    kruhy[i].nahodnemen()
while True:
    time.sleep(0.1)
    for i in kruhy:
        i.nahodnemen()

c.mainloop()
