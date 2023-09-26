import tkinter
import random as r
import time
a = 32
s = 9
a = 5
strana_stvorec = 2**a
strana_plocha = 2**s
c = tkinter.Canvas(width = strana_plocha, height = strana_plocha)
c.pack()
def zistikvadrant(socha,hlbka):
    kvadrant = strana_plocha / (2*hlbka)
    if socha[0] < kvadrant:
        if socha[1] < kvadrant: return 0
        if socha[1] >= kvadrant: return 2
    if socha[0] >= kvadrant:
        if socha[1] < kvadrant: return 1
        if socha[1] >= kvadrant: return 3
# vymazat potom plocha(), len na ucely ukazania
def plocha():
    for i in range(strana_plocha//strana_stvorec):
        for j in range(strana_plocha//strana_stvorec):
            c.create_rectangle(i*strana_stvorec+2,j*strana_stvorec+2, i*strana_stvorec + strana_stvorec+2, j*strana_stvorec + strana_stvorec+2)
def dlazdi(socha,hlbka):
    if hlbka == 0:
        socha = (r.randint(0, strana_plocha//strana_stvorec)*strana_stvorec, r.randint(0, strana_plocha//strana_stvorec)*strana_stvorec)
        c.create_rectangle(socha[0]+2,socha[1]+2,socha[0]+strana_stvorec+2, socha[1]+strana_stvorec+2, fill = "red")
        print(socha)
        return dlazdi(socha,hlbka+1)
    else:
        time.sleep(0.5)
        c.update()
        k = zistikvadrant(socha,hlbka)
        bod = strana_plocha // (2*hlbka)
        print(bod)
        match k:
            case 0:
                PD(bod)
            case 1:
                LD(bod)
            case 2:
                PH(bod)
            case 3:
                LH(bod)
    return dlazdi(socha,hlbka+1)
def LH(bod):
    return c.create_polygon(bod,bod)
def PH(bod):
    return
def LD(bod):
    return
def PD(bod):
    return

plocha()
dlazdi((0,0),0)

c.mainloop()