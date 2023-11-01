import random, time
class Pexeso:
    def __init__(self, c, level):
        self.plocha = []
        self.c = c[0]
        self.m = c[1]
        self.o = 10
        self.colors = ['red','yellow','blue','lime','black']
        with open("mena.txt") as file:
            self.choice = [line.rstrip() for line in file]
        self.items = []
        self.level = level
        self.maxlevel = 12
        match level:
            case 1:
                self.a0,self.b0,self.fs,self.a=4,4,20,200
            case 2:
                self.a0,self.b0,self.fs,self.a=4,5,20,200
            case 3:
                self.a0,self.b0,self.fs,self.a=4,6,20,200
            case 4:
                self.a0,self.b0,self.fs,self.a=4,7,20,200
            case 5:
                self.a0,self.b0,self.fs,self.a=5,6,20,150
            case 6:
                self.a0,self.b0,self.fs,self.a=6,6,20,150
            case 7:
                self.a0,self.b0,self.fs,self.a=6,7,20,150
            case 8:
                self.a0,self.b0,self.fs,self.a=6,8,20,150
            case 9:
                self.a0,self.b0,self.fs,self.a=6,9,20,150
            case 10:
                self.a0,self.b0,self.fs,self.a=6,10,20,150
            case 11:
                self.a0,self.b0,self.fs,self.a=7,10,17,125
            case 12:
                self.a0,self.b0,self.fs,self.a=7,12,17,125
        for i in range(int((self.a0 * self.b0) / 2)): self.items.append(self.choice[i])
        self.c.delete('all')
        self.c.config(width=2 * self.o + self.a * self.b0, height=2 * self.o + self.a * self.a0)
        self.list = 2*self.items
        self.active = None
        self.done = []

        self.spawn()
        self.randomize()
        self.c.bind('<Button-1>', self.click)
    class Karta:
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.shape = None
            self.obsah = None
    def spawn(self):
        a = self.a
        o = self.o
        for i in range(self.a0):
            row = []
            for j in range(self.b0):
                s = (self.Karta(j*a, i*a))
                s.shape = self.c.create_rectangle(o + j * a, o + i * a, o + j * a + a, o + i * a + a, fill = self.colors[0])
                s.obsah = self.c.create_text(o + j * a + a/2, o + i * a + a/2, text='', font=('Arial',self.fs))
                row.append(s)
            self.plocha.append(row)

    def randomize(self):
        random.shuffle(self.list)
        x = 0
        for i in range (self.a0):
            for j in range (self.b0):
                s = self.plocha[i][j]
                self.c.itemconfig(s.obsah, text=self.list[x], fill=self.colors[0])
                s.value = self.list[x]
                x += 1
    def YouWon(self):
        for i in range (self.a0):
            for j in range (self.b0):
                s = self.plocha[i][j]
                self.c.itemconfig(s.shape, fill=self.colors[2])
        wintime = self.c.create_text(self.o + self.a * self.b0/2, self.o + self.a * self.a0/2, font=('Arial bold', 200), fill=self.colors[0], text='5')
        self.c.update()
        time.sleep(1)
        for i in range (-4,0,1):
            self.c.itemconfig(wintime, text=-i)
            self.c.update()
            time.sleep(1)
        if self.level == self.maxlevel:
            self.c.itemconfig(wintime,font=('Arial',100) ,text='THE END, GG')
            return
        self.m.entryconfig(1, label=f"Current: {self.level+1}")
        self.__init__((self.c,self.m),self.level+1)
    def click(self, sur):
        a = self.a
        for i in range (self.a0):
            for j in range (self.b0):
                s = self.plocha[i][j]
                if sur.x >= s.x and sur.x <= s.x+a:
                    if sur.y >= s.y and sur.y <= s.y+a:
                        if s in self.done:
                            return
                        if not self.active:
                            self.active = s
                            self.c.itemconfig(s.shape, fill = self.colors[1])
                        else:
                            if self.active.value == s.value and self.active != s:
                                self.c.itemconfig(s.shape, fill = self.colors[3])
                                self.c.itemconfig(self.active.shape, fill = self.colors[3])
                                self.c.itemconfig(s.obsah, fill=self.colors[4])
                                self.c.itemconfig(self.active.obsah, fill=self.colors[4])
                                self.done.append(self.active)
                                self.done.append(s)

                                self.active = None
                                if len(self.done) == self.a0*self.b0:
                                    self.YouWon()
                            elif self.active.value == s.value and self.active == s:
                                return
                            else:
                                self.c.itemconfig(s.shape, fill=self.colors[1])
                                self.c.update()
                                time.sleep(0.5)
                                self.c.itemconfig(self.active.shape, fill = self.colors[0])
                                self.c.itemconfig(s.shape, fill=self.colors[0])
                                self.active = None
    def cheat(self):
        for i in range (self.a0):
            for j in range (self.b0):
                s = self.plocha[i][j]
                self.c.itemconfig(s.obsah, fill=self.colors[3])








