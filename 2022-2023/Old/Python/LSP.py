import tkinter
c = tkinter.Canvas(width=1920, height=1080)
c.pack()
subor = open("mena.txt", "r")
suborpocet = sum(1 for line in open('mena.txt', 'r')) - 1
pocetdruziniek = int(suborpocet/2)
rozy = 1000/pocetdruziniek
##########################
trvanie = 30 #v minutach###
##########################
a = 27.05/trvanie
p = 0
pozicia = []
dead = []
for i in range (pocetdruziniek):
    pozicia.append(1623)
    dead.append(0)
def move():
    global rozy, pismo, a, p
    c.delete('all')
    subor = open("mena.txt", "r")
    t = subor.readlines()
    y = 5
    posint = 0
    if str(t[0]) == 'restart\n':
        for i in range (pocetdruziniek):
            pozicia[i] = 1623
        control = 1
        p = 0
    elif str(t[0]) == 'stop\n':
        exit()
    else:
        control = 1        
    for i in range(1,suborpocet,2):
        cas = int(pozicia[posint]/a)
        fill = 'green'
        now = float(t[i+1])
        change = a*now*control
        if 487 < pozicia[posint] < 812:
            fill = "yellow"
        elif 163 < pozicia[posint] <= 487:
            fill = "orange"
        elif 0 < pozicia[posint] <= 163:
            fill = "red"
        elif pozicia[posint] <= 0 or dead[posint] == 1:
            pozicia[posint] = 1623
            cas = 0
            dead[posint] = 1
            change = 0
            fill = "red"
        if p == 0:
            change = 0
        c.create_rectangle(270,y,1900,y+rozy,width=6) #1623
        c.create_rectangle(272,y+2,272+pozicia[posint]-change,y+rozy-5,fill=fill)
        c.create_text(120,y+rozy-50, text= t[i], font = 'Arial 50 bold')
        c.create_text(120,y+rozy-25, text= f"{float(t[i+1])}  {cas}s", font = 'Arial 20 bold')
        if dead[posint] == 1:
            c.create_text(1063,y+rozy-60, text= 'Ojoj, koniec!', font = 'Arial 50 bold')

        y += rozy-1
        fill = "green"
        pozicia[posint] = pozicia[posint]-change
        posint += 1
    if p%5 == 0:
        print(f'[{p}]_pozicia = {pozicia}')
    p += 1
    c.after(985,move)
move()
c.mainloop()