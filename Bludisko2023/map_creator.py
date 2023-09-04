from tkinter import Canvas, Tk, Menu
def save():
    global curmap
    f = open(f'map{curmap}.txt','w')
    print('Saving...')
    for i in range (len(mapa)):
        for j in range(len(mapa[i])):
            f.write(f'{mapa[i][j]} ')
        f.write('\n')
    f.close()
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
        mapa[line][row] = color
        cmap.create_rectangle(o+row*a, o+line*a, o+row*a+a, o+line*a+a, fill = colors[mapa[line][row]])
def mapmotion(cor):
    global mapa
    if o<cor.x<o+v*a and o<cor.y<o+v*a:
        row = (cor.x-o)//a
        line = (cor.y-o)//a
        mapa[line][row] = color
        cmap.create_rectangle(o+row*a, o+line*a, o+row*a+a, o+line*a+a, fill = colors[mapa[line][row]])

def pdraw():
    global ap, mapa, curnumber
    for i in range(len(colors)):
        cpallete.create_rectangle(o+i*ap, o, o+i*ap+ap, o+ap//2, fill = colors[i])
    curnumber = cpallete.create_text(o+20,o+20,text=f"{curmap}", font="Arial 30 bold")
def mapdraw():
    for i in range(v):
        for j in range(v):
            cmap.create_rectangle(o+j*a, o+i*a, o+j*a+a, o+i*a+a, fill = colors[mapa[i][j]])
def before():
    global curmap, curnumber
    if curmap != 1:
        curmap -= 1
        cpallete.delete(curnumber)
        curnumber = cpallete.create_text(o+20,o+20,text=f"{curmap}", font="Arial 30 bold")
        mymenu.entryconfig(1,label = f"Save as [map{curmap}.txt]" , command = save)
        mymenu.entryconfig(2,label = f"Load [map{curmap}.txt]" , command = load)
        load()
def after():
    global curmap, curnumber
    if curmap > 0:
        curmap += 1
        cpallete.delete(curnumber)
        curnumber = cpallete.create_text(o+20,o+20,text=f"{curmap}", font="Arial 30 bold")
        mymenu.entryconfig(1,label = f"Save as [map{curmap}.txt]" , command = save)
        mymenu.entryconfig(2,label = f"Load [map{curmap}.txt]" , command = load)
        load()
curmap = 1
main = Tk()
mymenu = Menu(main)
curcommand = mymenu.add_command(label = f'Save as [map{curmap}.txt]', command = save)
curload = mymenu.add_command(label = f'Load [map{curmap}.txt]', command = load)
mymenu.add_command(label = 'Clear', command = clear)
mymenu.add_command(label = '<', command = before)
mymenu.add_command(label = '>', command = after)
main.config(menu = mymenu)

cpallete = Canvas(main, bg = 'lightyellow')
cpallete.grid(row = 1, column = 0)
cpallete.bind('<Button-1>',palleteclick)
cmap = Canvas(main)
cmap.grid(row = 2, column = 0)
cmap.bind('<Button-1>',mapclick)
cmap.bind('<B1-Motion>', mapmotion)
o = 10
a = 28
v = 30
colors = ('white','lightgray','grey','lightblue','blue','green','yellow','red','magenta','brown','black')
color = 10
ap = v*a//len(colors)
#main['width'] = 
cpallete['width'] = 2*o+v*a
cpallete['height'] = 2*o+len(colors)*ap/20
cmap['width'] = 2*o+v*a
cmap['height'] = 2*o+len(colors)*ap
cmap['bg'] = 'black'
mapa = []
new()
pdraw()
mapdraw()
load()
main.mainloop()
