from tkinter import Canvas, Tk, Menu, Button, Label
from functools import partial
import core
archive = []
p = -1
def click(i):
    global entry, p, archive
    entry = entry + i
    output.config(text = entry)
    if i == "=":
        output.config(text = core.calc(entry))
        entry = core.calc(entry)
        archive.append(entry)
        p += 1
    elif i == "C":
        output.config(text = "RESET")
        entry = ""
    elif i == "<":
        p -= 1
        output.config(text = archive[p])
    main.update()

main = Tk()
main.title('KALKULAČKA')
main.geometry("400x600")
output = Label(main, bg = "white", width = 55, height=7, anchor = "nw", font = ("Arial",30))
output.pack()
order = ["C","(",")","/","1","2","3","*","4","5","6","-","7","8","9","+","<","0","^","="]
buttons = []
i = 0
entry = ""
for y in range (110,610,100):
    for x in range(0,400,100):
        B = Button(main, width = 2, fg = "white", bg = "grey", text=order[i], font=("Arial", 55, "bold"), anchor = "n", command = partial(click, order[i]))
        B.place(x=x, y=y)
        buttons.append(B)
        i += 1
main.mainloop()