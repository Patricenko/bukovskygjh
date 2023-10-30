import random, time
class Pexeso:
    def __init__(self, o, a, c):
        self.plocha = []
        self.c = c
        self.a = a
        self.o = o
        self.colors = ['red','yellow','blue','lime','black']
        self.items = ['Arthas','Jaina','Thrall','Sylvannas','Archimonde', 'Kelthuzad','Algalon','Raszageth']
        self.list = 2*self.items
        self.active = None
        self.done = []

        self.spawn()
        self.randomize()
    class Karta:
        def __init__(self,x,y,value):
            self.x = x
            self.y = y
            self.v = value
            self.shape = None
            self.obsah = None
    def spawn(self):
        a = self.a
        o = self.o
        x = 0
        for i in range(4):
            row = []
            for j in range(4):
                x += 1
                s = (self.Karta(j*a, i*a, j + 4 * i))
                s.shape = self.c.create_rectangle(o + j * a, o + i * a, o + j * a + a, o + i * a + a, fill = 'red')
                s.obsah = self.c.create_text(o + j * a + a/2, o + i * a + a/2, text=x, font=('Arial',20))
                row.append(s)
            self.plocha.append(row)

    def randomize(self):
        random.shuffle(self.list)
        print(self.list)
        x = 0
        for i in range (4):
            for j in range (4):
                s = self.plocha[j][i]
                self.c.itemconfig(s.obsah, text=self.list[x], fill=self.colors[0])
                s.value = self.list[x]
                x += 1
    def YouWon(self):
        for i in range (4):
            for j in range (4):
                s = self.plocha[j][i]
                self.c.itemconfig(s.shape, fill=self.colors[2])
    def click(self, sur):
        a = self.a
        for i in range (4):
            for j in range (4):
                s = self.plocha[j][i]
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
                                if len(self.done) == 16:
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








