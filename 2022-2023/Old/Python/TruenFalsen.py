import tkinter
c = tkinter.Canvas(width=701, height=701)
p = 100
x = y = 0
pole = []
riadok = []
def get(cor):
    global pole
    x = cor.x // p
    y = cor.y // p
    cor.y//p #riadok
    cor.x//p #stlpec
    if not pole[y][x]:
        pole[y][x] = True
        c.create_rectangle(x*p,y*p,x*p+p,y*p+p, fill = 'green')
for i in range(36):
    if i % 6 == 0 and i != 0:
        y += p
        x = 0
        pole.append(riadok)
    riadok.append(False)
    c.create_rectangle(x,y,x+p,y+p, fill = 'white')
    x += p

print(pole)
c.bind('<Button-1>', get)
c.pack()
c.mainloop()
