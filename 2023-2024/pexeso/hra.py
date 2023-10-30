from tkinter import Canvas, Tk, Menu, Button
import modul

def load1():
    current = modul.Pexeso(o, a, c, 1)
def load2():
    current = modul.Pexeso(o, a, c, 2)
def load3():
    current = modul.Pexeso(o, a, c, 3)
def load4():
    current = modul.Pexeso(o, a, c, 4)
def load5():
    a = 150
    current = modul.Pexeso(o, a, c, 5)


o = 10
a = 200

main = Tk()
main.title('PEXESO')
level = Menu(main)
level.add_command(label = f'Level 1', command = load1)
level.add_command(label = f'Level 2', command = load2)
level.add_command(label = f'Level 3', command = load3)
level.add_command(label = f'Level 4', command = load4)
level.add_command(label = f'Level 5', command = load5)
main.config(menu = level)

c = Canvas(main)
c.create_text(200,50,text='Pexeso by Patrik Bukovský 3.C')
c.create_text(200,70,text='Ak vyhráš, automaticky postupuješ na ďalší level.')
c.create_text(200,90,text='Vieš aj prechádzať medzi levelmi hore na paneli.')
klik = Button(c,text='Začať!', command = lambda:[load1(),klik.destroy()]); klik.place(x=175,y=110)
c.pack()

main.mainloop()