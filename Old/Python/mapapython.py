import tkinter
c = tkinter.Canvas(width=1920, height=700)
subor = open("mapa.txt","r+")
listen = list(subor.read())
lines = subor.readline()
pocten = [0,0,0,0,0,0]
teren = ['zem','moria','puste','jazera','lesy','zasnezene','void']
x = y = 0
stetec = 'black'
link = '0'
def fvoid():
    global stetec
    stetec = 'black'
    link = '6'
def fzem():
    global stetec
    stetec = '#A04000'
    link = '0'
def fmore():
    global stetec
    stetec = '#0089FF'
    link = '1'
def fjazero():
    global stetec
    stetec = '#89ECFF'
    link = '3'
def fpust():
    global stetec
    stetec = '#DFE52B'
    link = '2'
def fles():
    global stetec
    stetec = 'green'
    link = '4'
def fsneh():
    global stetec
    stetec = 'white'
    link = '5'
def kresli(sur):
    global listen, lines, link, stetec
    docasnylist = ''
    x = (sur.x//20)*20
    y = (sur.y//20)*20
    docasnylist = lines[int(y/20)]
    c.create_rectangle(x,y,x+20,y+20, fill=stetec)
    print(f'Redrawed terrain on position: {x},{y}')
    docasnylist[int(x/20)] = link
    lines[int(y/20)] = docasnylist
    listen = lines
def pripocitaj(n):
    global pocten
    pocten[n] = int(pocten[n])+1
for i in listen:
    match i:
        case '0':
            farba = '#A04000'
            pripocitaj(int(i))  
        case '1':
            farba = '#0089FF'
            pripocitaj(int(i))
        case '2':
            farba = '#DFE52B'
            pripocitaj(int(i))
        case '3':
            farba = '#89ECFF'
            pripocitaj(int(i))
        case '4':
            farba = 'green'
            pripocitaj(int(i))
        case '5':
            farba = 'white'
            pripocitaj(int(i))
        case '6':
            farba = 'black'
            pripocitaj(int(i))
        case '\n':
            y += 20
            x = 0
            continue
    c.create_rectangle(x,y,x+20,y+20, fill = farba)
    x += 20
print (listen)
for i in range (len(pocten)):
    print (f'{teren[i]}: {pocten[i]}km2')
void = tkinter.Button(text = '', command = fvoid, bg='black')
zem = tkinter.Button(text = '', command = fzem, bg='#A04000')
pust = tkinter.Button(text = '', command = fpust, bg='#DFE52B')
lesy = tkinter.Button(text = '', command = fles, bg='green')
more = tkinter.Button(text = '', command = fmore, bg='#0089FF')
jazero = tkinter.Button(text = '', command = fjazero, bg='#89ECFF')
sneh = tkinter.Button(text = '', command = fsneh, bg='white')
void.pack(side = 'bottom', fill = 'x')
zem.pack(side = 'bottom', fill = 'x')
pust.pack(side = 'bottom', fill = 'x')
lesy.pack(side = 'bottom', fill = 'x')
more.pack(side = 'bottom', fill = 'x')
jazero.pack(side = 'bottom', fill = 'x')
sneh.pack(side = 'bottom', fill = 'x')
c.bind('<B1-Motion>', kresli)
print(listen)
c.pack()
c.mainloop()
