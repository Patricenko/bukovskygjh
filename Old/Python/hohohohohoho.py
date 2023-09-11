import tkinter
c = tkinter.Canvas(width=1920, height=700)
subor = open("mapa.txt","r")
listen = list(subor.read())
pocten = [0,0,0,0,0,0]
teren = ['zem','moria','puste','jazera','lesy','zasnezene']
x = y = 0
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
        case '\n':
            y += 20
            x = 0
            continue
    c.create_rectangle(x,y,x+20,y+20, fill = farba)
    x += 20
print (listen)
for i in range (len(pocten)):
    print (f'{teren[i]}: {pocten[i]}km2')
print(listen)
c.pack()
c.mainloop()
