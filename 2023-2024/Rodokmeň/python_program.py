import tkinter
import time
class TButton:
    def __init__(self, text):
        self.root = 0
        self.text = 0
        self.button = tkinter.Button(win, text=self.text)


    def updatebutton(self, text):
        self.text = text
    def setposition(self,x,y,w=50,h=50):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.button.place(x=self.x,y=self.y, width=self.width,height=self.height)
def create_input_window(prompt="Enter your input"):
    def on_submit():
        global user_input
        user_input = input_field.get()
        print(f"You entered: {user_input}")
        window.destroy()
    window = tkinter.Tk()
    window.title("Input Window")
    tkinter.Label(window, text=prompt).pack(side="top", fill="x", pady=10)
    input_field = tkinter.Entry(window)
    input_field.pack(side="top", fill="x", padx=10)
    input_field.focus_set()
    submit_button = tkinter.Button(window, text="Submit", command=on_submit)
    submit_button.pack(side="bottom", fill="x", padx=10, pady=10)
    window.mainloop()


def createbutton(generationes, x, y, space):
    if generationes == 0: return
    generationes -= 1
    space = space/2
    print(space)
    left = TButton(0)
    left.setposition(x - space, y)
    right = TButton(0)
    right.setposition(x + space, y)

    createbutton(generationes, x - x/2, y + 50, space)
    createbutton(generationes, x + x/2, y + 50, space)


def draw_tree(g):
    global win
    global generations
    generations = g
    global HEIGHT, WIDTH
    HEIGHT = 600
    WIDTH = 1200
    win = tkinter.Tk()
    win.geometry(f"{WIDTH}x{HEIGHT}")
    win.title("Rodokmen")
    btn = tkinter.Button(win,text=0)
    btn.place(x=WIDTH//2-50, y=10, width=50, height=50)
    createbutton(generations-1, x=WIDTH//2-50, y=60, space=WIDTH/2)
    win.mainloop()

create_input_window("Number of generations:")
draw_tree(int(user_input))