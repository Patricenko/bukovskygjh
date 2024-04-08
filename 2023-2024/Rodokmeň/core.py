import tkinter
import time
from modul import *
def createbuttons(generations, current, lastpos, string):
    if current > generations: return
    posx = WIDTH//(2**current)
    c.create_line(lastpos+20,50*(current-1)-35, lastpos+posx+20,50*current-35,fill="deeppink3",width=5)
    c.create_line(lastpos+20,50*(current-1)-35, lastpos-posx+20,50*current-35,fill="navy",width=5)
    TButton(c, text="Nič", x=lastpos+posx, y=50*current-50, level=current, bt=strom, pos=string+'1')
    TButton(c, text="Nič", x=lastpos-posx, y=50*current-50, level=current, bt=strom, pos=string+'2')
    createbuttons(generations, current + 1, lastpos + posx, string + '1')
    createbuttons(generations, current + 1, lastpos - posx, string + '2')
def createTree(g):
    global strom, c
    g = int(g)
    win.deiconify()
    c = tkinter.Canvas(win, width=WIDTH, height=HEIGHT, bg="orchid3")
    c.pack()
    c.create_text(WIDTH//2,HEIGHT//5,text="BI-TREE",font=("Arial","46","bold"))
    strom = BinaryTree(levels=g)
    TButton(c, text="Nič",x=(WIDTH-50)//2, y=10, bt=strom)
    createbuttons(g,2, (WIDTH-50)//2, "")


HEIGHT = 450
WIDTH = 1750
win = tkinter.Tk()
win.geometry(f"{WIDTH}x{HEIGHT}")
win.title("Rodokmen")
print("Pre tento WIDTH max 6 levelov")
print("Po UPDATE  tlačítka sa ukážu v termináli dve zobrazenia Binárneho Stromu")
win.withdraw()
create_input_window("Number of generations:", callback=createTree)
win.mainloop()