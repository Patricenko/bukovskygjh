import tkinter
def kresli():
    for j in range(6):
        for i in range(6):
            can.create_rectangle(o+i*a,o+j*a,o+i*a+a,o+j*a+a, fill = farby[h[j][i]])
def leftclick(s):
    r = (s.y-o)//a
    s = (s.x-o)//a
    r1 = r-1
    r2 = r+1
    s1 = s-1
    s2 = s+1
    if r1<0:
        r1 = 0
    if r2 > 5:
        r2 = 5
    if s1<0:
        s1 = 0
    if s2 > 5:
        s2 = 5
    for j in range(r1,r2+1):
        for i in range(s1,s2+1):
            h[j][i] = not(h[j][i])
            can.create_rectangle(o+i*a,o+j*a,o+i*a+a,o+j*a+a, fill = farby[h[j][i]])   
a = 30
o = 10
h = []
for i in range(6):
    riadok = []
    for i in range(6):
        riadok.append(0)
    h.append(riadok)
farby = ('white', 'blue')
can = tkinter.Canvas()
can.pack()
can.bind('<Button-1>',leftclick)

kresli()
