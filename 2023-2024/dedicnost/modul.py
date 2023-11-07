import tkinter
class TPanel:
    def __init__(self, pocet):
        self.pocet = pocet
        self.r = 60
        self.c = tkinter.Canvas(width=500, height=500)
        self.c.pack()
        self.c.bind("<Button-1>",self.laveklik)
        self.c.bind("<Button-2>", self.stredklik)
        self.c.bind("<Button-3>",self.praveklik)
        self.c.bind("<Double-1>", self.prepni_znacku)
        self.znacky = []
        self.aktivna = None
        self.vytvor()
        self.c.mainloop()
    class TZnacka:
        def __init__(self,cnv,r,x,rychlost = 60):
            self.cnv = cnv
            self.r = r
            self.rychlost = rychlost
            self.x = 2*x*self.r
            self.y = 150
            self.o = 10
            self.tvary = []
            self.kresli()
        def kresli(self):
            self.tvary.append(self.cnv.create_oval(self.r + self.x - self.r, self.y - self.r, self.r + self.x + self.r, self.y + self.r, fill = 'red'))
            self.tvary.append(self.cnv.create_oval(self.r + self.x - self.r + self.o, self.y - self.r + self.o, self.r + self.x + self.r - self.o, self.y + self.r - self.o,fill='white'))
            self.tvary.append(self.cnv.create_text(self.x + self.r, self.y, text=self.rychlost, font='Arial 40 bold'))
        def zmen_rychlost(self, zmena):
            self.rychlost += zmena
            self.cnv.itemconfig(self.tvary[2],text=self.rychlost)
    class TZnackaparova(TZnacka):
        def kresli(self):
            self.tvary = []
            x = self.x*2*self.r+self.r
            self.tvary.append(self.cnv.create_oval(self.r + self.x - self.r, self.y - self.r, self.r + self.x + self.r, self.y + self.r, fill='black'))
            self.tvary.append(self.cnv.create_oval(self.r + self.x - self.r + self.o, self.y - self.r + self.o,self.r + self.x + self.r - self.o, self.y + self.r - self.o, fill='white'))
            self.tvary.append(self.cnv.create_text(x + self.r, self.y, text=self.rychlost, font='Arial 40 bold'))
            self.tvary.append(self.cnv.create_line(x - self.r, self.y - self.r, x + self.r, self.y + self.r))
    def prepni_znacku(self, sur):
        for i in self.znacky:
            self.c.delete(i)
        self.znacky[self.aktivna] = self.TZnackaparova(self.c, self.r, self.aktivna)
    def laveklik(self,sur):
        self.znacky[int(sur.x//(2*self.r))].zmen_rychlost(10)
    def stredklik(self, sur):
        self.aktivna = int(sur.x//(2 * self.r))
    def praveklik(self,sur):
        self.znacky[int(sur.x//(2 * self.r))].zmen_rychlost(-10)
    def vytvor(self):
        for i in range(self.pocet):
            self.znacky.append(self.TZnacka(self.c,self.r,i))

dialnica = TPanel(4)
print(dialnica.pocet)
