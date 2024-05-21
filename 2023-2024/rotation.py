import tkinter as tk
from tkinter import PhotoImage
import time
def rgb_to_hex(farba):
    if farba == (0, 0, 0):
        return '#ffffff'
    return '#{:02x}{:02x}{:02x}'.format(farba[0], farba[1], farba[2])

def reset():
    global img, width, height
    img = PhotoImage(file="obrazok3.png")
    width, height = img.width(), img.height()
    max_size = max(width, height)
    c["width"], c["height"] = max_size, max_size
    img["width"], img["height"] = max_size, max_size
    width, height = max_size, max_size
    c.create_image(0, 0, anchor='nw', image=img)
    c.update()
def rotate180():
    global img, width, height
    print("rotate 180")
    for y in range(height//2):
        for x in range(width):
            color1 = img.get(x, y)
            color2 = img.get(width-x-1, height-y-1)
            img.put(rgb_to_hex(color2), (x, y))
            img.put(rgb_to_hex(color1), (width-x-1, height-y-1))
        c.update()
def horizontal():
    global img, width, height
    print("rotate horizontal")
    for y in range(height):
        for x in range(width//2):
            color1 = img.get(x, y)
            color2 = img.get(width-x-1, y)
            img.put(rgb_to_hex(color2), (x, y))
            img.put(rgb_to_hex(color1), (width-x-1, y))
        c.update()

def vertical():
    global img, width, height
    print("rotate vertical")
    for y in range(height//2):
        for x in range(width):
            color1 = img.get(x, y)
            color2 = img.get(x, height-y-1)
            img.put(rgb_to_hex(color2), (x, y))
            img.put(rgb_to_hex(color1), (x, height-y-1))
        c.update()

def rotate270():
    global img, width, height
    print("rotate 270")
    for y in range(height//2):
        for x in range(width//2):
            color1 = img.get(x, y)
            color2 = img.get(height-y-1, x)
            color3 = img.get(width-x-1, height-y-1)
            color4 = img.get(y, width-x-1)
            img.put(rgb_to_hex(color2), (x, y))
            img.put(rgb_to_hex(color3), (height-y-1, x))
            img.put(rgb_to_hex(color4), (width-x-1, height-y-1))
            img.put(rgb_to_hex(color1), (y, width-x-1))
        c.update()

def rotate90():
    global img, width, height
    print("rotate 90")
    for y in range(height//2):
        for x in range(width//2):
            color1 = img.get(x, y)
            color2 = img.get(height-y-1, x)
            color3 = img.get(width-x-1, height-y-1)
            color4 = img.get(y, width-x-1)
            print(color1, color2, color3, color4)
            img.put(rgb_to_hex(color4), (x, y))
            img.put(rgb_to_hex(color1), (height-y-1, x))
            img.put(rgb_to_hex(color2), (width-x-1, height-y-1))
            img.put(rgb_to_hex(color3), (y, width-x-1))
        c.update()



root = tk.Tk()
root.title('ImageConverter')
level = tk.Menu(root)
level.add_command(label = f'Reset',  command = lambda:[reset()])
level.add_command(label = f'180',  command = lambda:[rotate180()])
level.add_command(label = f'vertical',  command = lambda:[vertical()])
level.add_command(label = f'horizontal',  command = lambda:[horizontal()])
level.add_command(label = f'90',  command = lambda:[rotate90()])
level.add_command(label = f'270',  command = lambda:[rotate270()])
root.config(menu = level)
c = tk.Canvas(root)
c.pack()
reset()
root.mainloop()