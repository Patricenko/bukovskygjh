import tkinter
import random as r
import time
global strana_stvorec, strana_plocha, spinkaj
strana_stvorec = 20
strana_plocha = 2**10
spinkaj = 0.1
k = int(strana_plocha**0.5)
c = tkinter.Canvas(width = k*strana_stvorec, height = k*strana_stvorec)
c.pack()
#####################################################################
def LH(k, bod, novybod):
    c.create_polygon(novybod[0] * strana_stvorec, novybod[1] * strana_stvorec,
                     novybod[0] * strana_stvorec - strana_stvorec, novybod[1] * strana_stvorec,
                     novybod[0] * strana_stvorec - strana_stvorec, novybod[1] * strana_stvorec + strana_stvorec,
                     novybod[0] * strana_stvorec + strana_stvorec, novybod[1] * strana_stvorec + strana_stvorec,
                     novybod[0] * strana_stvorec + strana_stvorec, novybod[1] * strana_stvorec - strana_stvorec,
                     novybod[0] * strana_stvorec, novybod[1] * strana_stvorec - strana_stvorec, fill="pink")
    time.sleep(spinkaj)
    c.update()
    time.sleep(spinkaj)
    c.update()
    dlazdi(k/2, bod, (novybod[0]-k/2,novybod[1]-k/2))
    dlazdi(k/2, (novybod[0],novybod[1]-1),(novybod[0]+k/2,novybod[1]-k/2))
    dlazdi(k/2, novybod,(novybod[0]+k/2,novybod[1]+k/2))
    dlazdi(k/2, (novybod[0]-1,novybod[1]), (novybod[0]-k/2,novybod[1]+k/2))
def LD(k, bod, novybod):
    c.create_polygon(novybod[0] * strana_stvorec, novybod[1] * strana_stvorec,
                     novybod[0] * strana_stvorec - strana_stvorec, novybod[1] * strana_stvorec,
                     novybod[0] * strana_stvorec - strana_stvorec, novybod[1] * strana_stvorec - strana_stvorec,
                     novybod[0] * strana_stvorec + strana_stvorec, novybod[1] * strana_stvorec - strana_stvorec,
                     novybod[0] * strana_stvorec + strana_stvorec, novybod[1] * strana_stvorec + strana_stvorec,
                     novybod[0] * strana_stvorec, novybod[1] * strana_stvorec + strana_stvorec, fill="purple")
    time.sleep(spinkaj)
    c.update()
    dlazdi(k/2, (bod[0], bod[1]), (novybod[0]-k/2, novybod[1]+k/2))
    dlazdi(k/2, (novybod[0], novybod[1]), (novybod[0]+k/2, novybod[1]+k/2))
    dlazdi(k/2, (novybod[0]-1, novybod[1]-1), (novybod[0]-k/2, novybod[1]-k/2))
    dlazdi(k/2, (novybod[0], novybod[1]-1), (novybod[0]+k/2, novybod[1]-k/2))
def PH(k, bod, novybod):
    c.create_polygon(novybod[0] * strana_stvorec, novybod[1] * strana_stvorec,
                     novybod[0] * strana_stvorec + strana_stvorec, novybod[1] * strana_stvorec,
                     novybod[0] * strana_stvorec + strana_stvorec, novybod[1] * strana_stvorec + strana_stvorec,
                     novybod[0] * strana_stvorec - strana_stvorec, novybod[1] * strana_stvorec + strana_stvorec,
                     novybod[0] * strana_stvorec - strana_stvorec, novybod[1] * strana_stvorec - strana_stvorec,
                     novybod[0] * strana_stvorec, novybod[1] * strana_stvorec - strana_stvorec, fill="magenta")
    time.sleep(spinkaj)
    c.update()
    dlazdi(k/2, (bod[0], bod[1]), (novybod[0]+k/2, novybod[1]-k/2))
    dlazdi(k/2, (novybod[0]-1, novybod[1]-1), (novybod[0]-k/2, novybod[1]-k/2))
    dlazdi(k/2, (novybod[0]-1, novybod[1]), (novybod[0]-k/2, novybod[1]+k/2))
    dlazdi(k/2, (novybod[0], novybod[1]), (novybod[0]+k/2, novybod[1]+k/2))
def PD(k, bod, novybod):
    c.create_polygon(novybod[0] * strana_stvorec, novybod[1] * strana_stvorec,
                     novybod[0] * strana_stvorec + strana_stvorec, novybod[1] * strana_stvorec,
                     novybod[0] * strana_stvorec + strana_stvorec, novybod[1] * strana_stvorec - strana_stvorec,
                     novybod[0] * strana_stvorec - strana_stvorec, novybod[1] * strana_stvorec - strana_stvorec,
                     novybod[0] * strana_stvorec - strana_stvorec, novybod[1] * strana_stvorec + strana_stvorec,
                     novybod[0] * strana_stvorec, novybod[1] * strana_stvorec + strana_stvorec, fill="blue")
    time.sleep(spinkaj)
    c.update()
    dlazdi(k/2, (bod[0], bod[1]), (novybod[0]+k/2, novybod[1]+k/2))
    dlazdi(k/2, (novybod[0]-1, novybod[1]-1), (novybod[0]-k/2, novybod[1]-k/2))
    dlazdi(k/2, (novybod[0], novybod[1]-1), (novybod[0]+k/2, novybod[1]-k/2))
    dlazdi(k/2, (novybod[0]-1, novybod[1]), (novybod[0]-k/2, novybod[1]+k/2))
def dlazdi(k, bod, novybod):
    if k >= 1:
        if bod[0] < novybod[0] and bod[1] < novybod[1]: LH(k, bod, novybod)
        elif bod[0] < novybod[0] and bod[1] >= novybod[1]: LD(k, bod, novybod)
        elif bod[0] >= novybod[0] and bod[1] < novybod[1]: PH(k, bod, novybod)
        elif bod[0] >= novybod[0] and bod[1] >= novybod[1]: PD(k, bod, novybod)

bod = (r.randint(0, k-1), r.randint(0, k-1))
c.create_rectangle(bod[0] * strana_stvorec, bod[1] * strana_stvorec, bod[0]*strana_stvorec + strana_stvorec, bod[1]*strana_stvorec + strana_stvorec,fill="black")
dlazdi(k/2, bod,(k/2,k/2))
c.mainloop()
