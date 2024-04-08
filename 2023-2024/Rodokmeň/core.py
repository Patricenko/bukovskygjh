import tkinter
import time
from modul import *
def createbuttons(generations, current, lastpos, string):
    if current > generations: return
    posx = WIDTH//(2**current)
    TButton(win, text="Nič", x=lastpos+posx, y=50*current-50, level=current, bt=strom, pos=string+'1')
    TButton(win, text="Nič", x=lastpos-posx, y=50*current-50, level=current, bt=strom, pos=string+'2')
    createbuttons(generations, current + 1, lastpos + posx, string + '1')
    createbuttons(generations, current + 1, lastpos - posx, string + '2')
def draw_tree(g):
    g = int(g)
    global HEIGHT, WIDTH, strom
    HEIGHT = 600
    WIDTH = 1500
    win.geometry(f"{WIDTH}x{HEIGHT}")
    win.deiconify()
    strom = BinaryTree(levels=g)
    TButton(win, text="Nič",x=(WIDTH-50)//2, y=0, bt=strom)
    createbuttons(g,2, (WIDTH-50)//2, "")

win = tkinter.Tk()
win.title("Rodokmen")
print("Pre tento WIDTH max 6 levelov")
print("Po UPDATE  tlačítka sa ukážu v termináli dve zobrazenia Binárneho Stromu")
win.withdraw()
create_input_window("Number of generations:", callback=draw_tree)
win.mainloop()