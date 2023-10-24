import random
class Pexeso:
    def __init__(self, o, a, c):
        self.plocha = []
        self.vyber = None
        self.c = c
        self.a = a
        self.o = o
        self.spawn()
        self.randomize()
        self.colors = ['red','yellow','blue']
        self.items = ['BANANA','APPLE','COCONUT','PINEAPPLE','YOUR MOM', 'TOOTHPASTE','CEMETERY','SAD STORY']
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
        for i in range(4):
            row = []
            for j in range(4):
                s = (self.Karta(j, i, j + 4 * i))
                s.shape = self.c.create_rectangle(o + j * a, o + i * a, o + j * a + a, o + i * a + a, fill = 'red')
                row.append(s)
            self.plocha.append(row)
        self.vyber = self.plocha
    def IsNotIn(self,x):
        p = 0
        for i in range(4):
            for j in range(4):
                if self.plocha[j][i].obsah == x: p += 1
        if p == 0: return True
        if p == 1: return True
        if p == 2: return False
        if p > 2: print('ERROR')

    def randomize(self):
        i0 = random.randrange(0,len(self.plocha)-1)
        j0 = random.randrange(0, len(self.plocha)-1)
        i1 = random.randrange(0, len(self.plocha) - 1)
        j1 = random.randrange(0, len(self.plocha) - 1)
        if self.plocha[j0][i0]






