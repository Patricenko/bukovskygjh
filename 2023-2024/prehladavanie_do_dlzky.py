import front_stack
from tkinter import Canvas, Tk, Menu
def load():
    global mapa
    f = open(f'generovane.txt','r')
    print('Loading...')
    mapa = []
    r = f.readline()
    while r != '':
        rr = r.strip().split()
        for i in range(len(rr)):
            rr[i] = int(rr[i])
        mapa.append(rr)
        r = f.readline()
    f.close()
    mapdraw()
def palleteclick(cor):
    global color
    if o<cor.x<len(colors)*ap and o<cor.y<o+ap//2:
        color = (cor.x-o)//ap
        cpallete['bg'] = colors[color]
def mapclick(cor):
    global mapa
    if o<cor.x<o+v*a and o<cor.y<o+v*a:
        row = (cor.x-o)//a
        line = (cor.y-o)//a
        if mapa[line][row] != 3:
            cmap.create_rectangle(o+row*a, o+line*a, o+row*a+a, o+line*a+a, fill = colors[mapa[line][row]])
            kroky = ((0,-1),(1,0),(0,1),(-1,0))
            rad = front_stack.TFront()
            hladam = mapa[line][row]
            rad.enqueue((line,row))
            mapa[line][row] = 2
            cmap.create_rectangle(o + row * a, o + line * a, o + row * a + a, o + line * a + a, fill=colors[color])
            while not rad.is_empty():
                prvok = rad.dequeue()
                line = prvok[0]
                row = (prvok[1])
                for p in kroky:
                    line1 = prvok[0]+p[1]
                    row1 = prvok[1]+p[0]
                    print(line, row, line1, row1)
                    if hladam == mapa[line1][row1]:
                        rad.enqueue((line1,row1))
                        mapa[line1][row1] = 2
                        cmap.create_rectangle(o + row1 * a, o + line1 * a, o + row1 * a + a, o + line1 * a + a, fill=colors[color])
                cmap.create_rectangle(o + row * a, o + line * a, o + row * a + a, o + line * a + a, fill=colors[color])
                main.update()

def mapdraw():
    for i in range(v):
        for j in range(v):
            if mapa[i][j] == 1:
                cmap.create_rectangle(o+j*a, o+i*a, o+j*a+a, o+i*a+a, fill = colors[10])
            else:
                cmap.create_rectangle(o+j*a, o+i*a, o+j*a+a, o+i*a+a, fill = colors[0])
                #cmap.create_text(o+j*a+a//2, o+i*a+a//2, text = mapa[j][i])
def pdraw():
    global ap, mapa, curnumber
    for i in range(len(colors)):
        cpallete.create_rectangle(o+i*ap, o, o+i*ap+ap, o+ap//2, fill = colors[i])

f = open("generovane.txt", "r")
l = f.readlines()
print(l)
main = Tk()
cpallete = Canvas(main, bg = 'lightyellow')
cpallete.grid(row = 1, column = 0)
cpallete.bind('<Button-1>',palleteclick)
cmap = Canvas(main)
cmap.grid(row = 2, column = 0)
cmap.bind('<Button-1>',mapclick)

o = 10
a = 20
v = 50
colors = ('white','lightgray','grey','lightblue','blue','green','yellow','red','magenta','brown','black')
color = 10
ap = v*a//len(colors)

cpallete['width'] = 2*o+v*a
cpallete['height'] = 2*o+len(colors)*ap/20
cmap['width'] = 2*o+v*a
cmap['height'] = 2*o+len(colors)*ap
cmap['bg'] = 'white'
pdraw()
load()

main.mainloop()