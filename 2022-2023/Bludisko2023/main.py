from tkinter import Canvas, Tk, Menu
import time
def load():
    global mapa
    f = open(f'map{curmap}.txt','r')
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
    global coins, hp
    print('Clearing Map...')
    new()
    mapdraw()
    hp = 5
    coins = 0
    pdraw()
    load()
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
def up(*args):
    global player, coins, hp
    if colors[mapa[p[0]-1][p[1]]] == 'black' or p[0] == 0:
        pass
    else:
        coords = cmap.coords(player)
        print(coords)
        print(colors[mapa[p[0]-1][p[1]]])
        if colors[mapa[p[0]-1][p[1]]] == 'yellow':
            coins += 1
        elif colors[mapa[p[0]-1][p[1]]] == 'red':
            hp -= 1
        cmap.create_rectangle(coords[0],coords[1],coords[2],coords[3],fill = colors[2])
        player = cmap.create_rectangle(coords[0],coords[1]-a,coords[2],coords[3]-a,fill = colors[8])
        p[0] -= 1
        pdraw()
def down(*args):
    global player, coins, hp
    if colors[mapa[p[0]+1][p[1]]] == 'black' or p[0] == v-1:
        pass
    else:
        coords = cmap.coords(player)
        print(colors[mapa[p[0]+1][p[1]]])
        if colors[mapa[p[0]+1][p[1]]] == 'red':
            hp -= 1
        if colors[mapa[p[0]+1][p[1]]] == 'yellow':
            coins += 1
        cmap.create_rectangle(coords[0],coords[1],coords[2],coords[3],fill = colors[2])
        player = cmap.create_rectangle(coords[0],coords[1]+a,coords[2],coords[3]+a,fill = colors[8])
        p[0] += 1
        pdraw()
def left(*args):
    global player, coins, hp
    change = 1
    if colors[mapa[p[0]][p[1]-1]] == 'black' or p[1] == 0:
        pass
    else:
        coords = cmap.coords(player)
        print(colors[mapa[p[0]][p[1]-1]])
        if colors[mapa[p[0]][p[1]-1]] == 'yellow':
            coins += 1
        if colors[mapa[p[0]][p[1]-1]] == 'red':
            hp -= 1
        cmap.create_rectangle(coords[0],coords[1],coords[2],coords[3],fill = colors[2])
        player = cmap.create_rectangle(coords[0]-a,coords[1],coords[2]-a,coords[3],fill = colors[8])
        p[1] -= 1
        pdraw()
def right(*args):
    global player, coins, hp
    if colors[mapa[p[0]][p[1]+1]] == 'black' or p[1] == v-1:
        pass
    else:
        coords = cmap.coords(player)
        print(colors[mapa[p[0]][p[1]+1]])
        if colors[mapa[p[0]][p[1]+1]] == 'yellow':
            coins += 1
        if colors[mapa[p[0]][p[1]+1]] == 'red':
            hp -= 1
        cmap.create_rectangle(coords[0],coords[1],coords[2],coords[3],fill = colors[2])
        player = cmap.create_rectangle(coords[0]+a,coords[1],coords[2]+a,coords[3],fill = colors[8])
        p[1] += 1
        pdraw()
def before():
    global curmap, curnumber
    if curmap != 1:
        curmap -= 1
        mymenu.entryconfig(1,label = f"Load [map{curmap}.txt]" , command = load)
        clear()
        load()
def after():
    global curmap, curnumber
    if curmap > 0:
        curmap += 1
        mymenu.entryconfig(1,label = f"Load [map{curmap}.txt]" , command = load)
        clear()
        load()
def pdraw():
    cpallete.delete('all')
    for i in range(hp):
        cpallete.create_oval(40*i+5,10,40*i+40+5,50, fill='red')
    cpallete.create_oval(700,0,760,60, fill='yellow')
    cpallete.create_text(730,30,text=f'{coins}', fill='black', font='Arial 50 bold')
    cpallete.create_oval(40*i+5,10,40*i+40+5,50, fill='red')
    
curmap = 1
main = Tk()
mymenu = Menu(main)
curload = mymenu.add_command(label = f'Load [map{curmap}.txt]', command = load)
mymenu.add_command(label = 'Reset', command = clear)
mymenu.add_command(label = '<', command = before)
mymenu.add_command(label = '>', command = after)
main.config(menu = mymenu)

cpallete = Canvas(main, bg = 'black')
cpallete.grid(row = 1, column = 0)
hp = 5
coins = 0
#cpallete.bind('<Button-1>',palleteclick)
cmap = Canvas(main)
cmap.grid(row = 2, column = 0)
#cmap.bind('<Button-1>',mapclick)
o = 10
a = 28
v = 50
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
pdraw()
load()
cmap.bind_all('w', up)
cmap.bind_all('a', left)
cmap.bind_all('s', down)
cmap.bind_all('d', right)
main.mainloop()
