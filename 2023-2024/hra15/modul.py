import tkinter
import random
class Unit:
    def __init__ (self, a):
        self.ihrisko = []
        self.a = a
        self.o = 10
        self.can = tkinter.Canvas(width = 2*self.o+a*4, height = 2*self.o+a*4)
        self.can.pack()
        self.colors = ['white', 'yellow', 'green']
        self.spawn()
        self.shuffle()
        self.missingx = 0
        self.missingy = 0
        self.shuffle()
        self.button()

        self.can.mainloop()

    class Stone:
        def __init__(self,x,y,value):
            self.x = x
            self.y = y
            self.v = value
            self.shape = None
            self.name = None
    def spawn(self):
        a = self.a
        o = self.o
        for i in range(4):
            row = []
            for j in range(4):
                s = (self.Stone(j, i, j + 4 * i))

                s.shape = self.can.create_rectangle(o + j * a, o + i * a, o + j * a + a, o + i * a + a, fill=self.colors[0])
                s.name = self.can.create_text(o + j * a + a // 2, o + i * a + a // 2, text=s.v + 1)
                row.append(s)
            self.ihrisko.append(row)
        self.can.delete(self.ihrisko[3][3].shape)
        self.can.delete(self.ihrisko[3][3].name)
        self.can.update()
        self.ihrisko[3][3] = None
        self.missingx = 3
        self.missingy = 3
    def getNone(self):
        i,j = self.ihrisko.index(None)
        return (i, j)

    def deep_index(lst, w):
        return [(i, sub.index(w)) for (i, sub) in enumerate(lst) if w in sub]

    def shuffle(self):
        a = self.a
        o = self.o
        for i in range(500):

            r = random.randrange(-1, 2)  # 1 = +x, 2 = +y, 0 = -x, -1 = -y

            if r == 1 and self.missingx + 1 <= 3:
                self.can.coords(self.ihrisko[self.missingy][self.missingx + 1].shape, o + self.missingx * a,
                                o + self.missingy * a, o + self.missingx * a + a, o + self.missingy * a + a)
                self.can.coords(self.ihrisko[self.missingy][self.missingx + 1].name, o + self.missingx * a + a // 2,
                                o + self.missingy * a + a // 2)

                self.ihrisko[self.missingy][self.missingx] = self.ihrisko[self.missingy][self.missingx + 1]
                self.ihrisko[self.missingy][self.missingx + 1] = None

                self.missingx = self.missingx + 1

            if r == 2 and self.missingy + 1 <= 3:
                self.can.coords(self.ihrisko[self.missingy + 1][self.missingx].shape, o + self.missingx * a,
                                o + self.missingy * a, o + self.missingx * a + a, o + self.missingy * a + a)
                self.can.coords(self.ihrisko[self.missingy + 1][self.missingx].name, o + self.missingx * a + a // 2,
                                o + self.missingy * a + a // 2)

                self.ihrisko[self.missingy][self.missingx] = self.ihrisko[self.missingy + 1][self.missingx]
                self.ihrisko[self.missingy + 1][self.missingx] = None

                self.missingy = self.missingy + 1

            if r == 0 and self.missingx - 1 >= 0:
                self.can.coords(self.ihrisko[self.missingy][self.missingx - 1].shape, o + self.missingx * a,
                                o + self.missingy * a, o + self.missingx * a + a, o + self.missingy * a + a)
                self.can.coords(self.ihrisko[self.missingy][self.missingx - 1].name, o + self.missingx * a + a // 2,
                                o + self.missingy * a + a // 2)

                self.ihrisko[self.missingy][self.missingx] = self.ihrisko[self.missingy][self.missingx - 1]
                self.ihrisko[self.missingy][self.missingx - 1] = None

                self.missingx = self.missingx - 1

            if r == -1 and self.missingy - 1 >= 0:
                self.can.coords(self.ihrisko[self.missingy - 1][self.missingx].shape, o + self.missingx * a,
                                o + self.missingy * a, o + self.missingx * a + a, o + self.missingy * a + a)
                self.can.coords(self.ihrisko[self.missingy - 1][self.missingx].name, o + self.missingx * a + a // 2,
                                o + self.missingy * a + a // 2)

                self.ihrisko[self.missingy][self.missingx] = self.ihrisko[self.missingy - 1][self.missingx]
                self.ihrisko[self.missingy - 1][self.missingx] = None

                self.missingy = self.missingy - 1


    def reset(self):
        pass
h1 = Unit(100)

