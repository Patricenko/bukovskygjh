from tkinter import Canvas, Tk, Menu
import time
up, down, left, right = 0
def load():
    global mapa
    f = open('map.txt','r')
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
def clear():
    print('Clearing Map...')
    new()
    mapdraw()
def new():
    global mapa
    mapa = []
    a = 28
    for i in range(v):
        riadok = []
        for j in range(v):
            riadok.append(2)
        mapa.append(riadok)
def mapdraw():
    global p
    global player
    for i in range(v):
        for j in range(v):
            cmap.create_rectangle(o+j*a, o+i*a, o+j*a+a, o+i*a+a, fill = colors[mapa[i][j]])
            if colors[mapa[i][j]] == 'magenta':
                player = cmap.create_rectangle(o+j*a, o+i*a, o+j*a+a, o+i*a+a, fill = colors[mapa[i][j]])
                print(cmap.coords(player))
                p = [i,j]
                print(p)
def defeat():
    print('DEFEAT')
def clearpath():
    up, down, left, right = 0
def up(*args):
    global player, change
    clearpath()
    while up == 1:
        if colors[mapa[p[0]-1][p[1]]] == 'black' or p[0] == 0:
            defeat()
        else:
            change = 0
            time.sleep(1)
            coords = cmap.coords(player)
            print(coords)
            cmap.create_rectangle(coords[0],coords[1],coords[2],coords[3],fill = colors[2])
            player = cmap.create_rectangle(coords[0],coords[1]-a,coords[2],coords[3]-a,fill = colors[8])
            p[0] -= 1
def down(*args):
    global player, change
    change = 1
    if colors[mapa[p[0]+1][p[1]]] == 'black' or p[0] == v-1:
        defeat()
    else:
        coords = cmap.coords(player)
        cmap.create_rectangle(coords[0],coords[1],coords[2],coords[3],fill = colors[2])
        player = cmap.create_rectangle(coords[0],coords[1]+a,coords[2],coords[3]+a,fill = colors[8])
        p[0] += 1
def left(*args):
    global player, change
    change = 1
    if colors[mapa[p[0]][p[1]-1]] == 'black' or p[1] == 0:
        defeat()
    else:
        coords = cmap.coords(player)
        cmap.create_rectangle(coords[0],coords[1],coords[2],coords[3],fill = colors[2])
        player = cmap.create_rectangle(coords[0]-a,coords[1],coords[2]-a,coords[3],fill = colors[8])
        p[1] -= 1
def right(*args):
    global player, change
    change = 1
    if colors[mapa[p[0]][p[1]+1]] == 'black' or p[1] == v-1:
        defeat()
    else:
        coords = cmap.coords(player)
        cmap.create_rectangle(coords[0],coords[1],coords[2],coords[3],fill = colors[2])
        player = cmap.create_rectangle(coords[0]+a,coords[1],coords[2]+a,coords[3],fill = colors[8])
        p[1] += 1
main = Tk()
mymenu = Menu(main)
mymenu.add_command(label = 'Load New', command = load)
mymenu.add_command(label = 'Clear', command = clear)
main.config(menu = mymenu)

cpallete = Canvas(main, bg = 'lightyellow')
cpallete.grid(row = 1, column = 0)
#cpallete.bind('<Button-1>',palleteclick)
cmap = Canvas(main)
cmap.grid(row = 2, column = 0)
#cmap.bind('<Button-1>',mapclick)
o = 10
a = 28
v = 30
colors = ('white','lightgray','grey','lightblue','blue','green','yellow','red','magenta','brown','black')
color = 10
ap = v*a//len(colors)
cpallete['width'] = 2*o+v*a
cpallete['height'] = 2*o+len(colors)*ap/20
cmap['width'] = 2*o+v*a
cmap['height'] = 2*o+len(colors)*ap
cmap['bg'] = 'black'
mapa = []
new()
mapdraw()
cmap.bind_all('w', up)
cmap.bind_all('a', left)
cmap.bind_all('s', down)
cmap.bind_all('d', right)
main.mainloop()
