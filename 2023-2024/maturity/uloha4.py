import tkinter
import random
import math

class Oval():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.oval = c.create_oval(x-10, y-10, x+10, y+10, fill="black")
        self.move()
    def move(self):
        self.x += random.randint(-speed, speed)
        self.y += random.randint(-int(math.sqrt(speed**2 + self.x**2)), int(math.sqrt(speed**2 + self.x**2)))
        c.coords(self.oval, self.x-10, self.y-10, self.x+10, self.y+10)
        c.after(50, self.move)
def setspeed(increase):
    global speed
    if increase:
        speed += 1
    else:
        if speed > 0:
            speed -= 1
    speed_text["text"] = f"Speed: {speed}"

def on_submit():
    global c, speed_field, width, height, speed_text
    width = width_field.get()
    height = height_field.get()
    if not width.isdigit() or not height.isdigit():
        width = 800
        height = 800
    root.deiconify()
    root["width"] = int(width)
    root["height"] = int(height)
    c = tkinter.Canvas(root, width=int(width)-50, height=int(height)-100)
    c.pack()
    speed_field = tkinter.Canvas(root, width=100, height=100, bg="pink")
    speed_field.pack(fill="both")
    higher_speed = tkinter.Button(speed_field, text="+", command=lambda: [setspeed(True)])
    higher_speed.pack(side="left")
    lower_speed = tkinter.Button(speed_field, text="-", command=lambda: [setspeed(False)])
    lower_speed.pack(side="left")
    speed_text = tkinter.Label(speed_field, text="Speed: 1")
    speed_text.pack(side="left")
    for i in range(300):
        x = random.randint(0, int(width)-50)
        y = random.randint(0, int(height)-50)
        Oval(x, y)
        c.update()

    tp.destroy()


root = tkinter.Tk()
root.withdraw()
tp = tkinter.Toplevel(root)
tp.title("Zadanie 4")
width_field = tkinter.Entry(tp)
width_field.pack(side="left")
text = tkinter.Label(tp, text=" x ")
text.pack(side="left")
height_field = tkinter.Entry(tp)
height_field.pack(side="left")
submit_button = tkinter.Button(tp, text="Submit", command=on_submit)
submit_button.pack()
speed = 1
root.mainloop()