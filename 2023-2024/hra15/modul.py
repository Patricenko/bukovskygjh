import tkinter
import random
class Unit:
    def __init__ (self, a):
        self.table = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
        self.a = a
        self.o = 10
        self.c = tkinter.Canvas(width = 2*self.o+a*4, height = 2*self.o+a*4)
        self.c.pack()
        self.colors = ['white', 'yellow', 'green']
        self.spawn()
        self.mix()

        self.c.mainloop()

    class Stone:
        def __init__(self,x,y,value):
            self.x = x
            self.y = y
            self.value = value
            self.shape = None
            self.dscp = None
    def spawn(self):
        a = self.a
        o = self.o
        for i in range(4):
            for j in range(4):
                if i+1+j*4 == 16:
                    self.table[i][j] = None
                    continue
                #o+i*a, o+j*a, o+i*a+a, o+j*a+a i+1+j*4
                self.table[i][j] = k = self.Stone(i,j,j*4+i+1)
                k.shape = self.c.create_rectangle(o+i*a, o+j*a, o+i*a+a, o+j*a+a, fill=self.colors[1])
                k.dscp = self.c.create_text(o+i*a+a//2,o+j*a+a//2, text = k.value)
    def getNone(self):
        i,j = self.table.index(None)
        return (i, j)

    def deep_index(lst, w):
        return [(i, sub.index(w)) for (i, sub) in enumerate(lst) if w in sub]

    def mix(self):
        for i in range(100):
            (x, y) = self.getNone()







    def reset(self):
        pass
h1 = Unit(100)

