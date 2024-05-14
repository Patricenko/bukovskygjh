import tkinter as ctk
from tkinter import PhotoImage
from random import randrange

def rgb_to_hex(farba):
    return '#{:02x}{:02x}{:02x}'.format(farba[0], farba[1], farba[2])
def reset():
    global img, width, height
    img = PhotoImage(file="obrazok.png")
    width, height = img.width(), img.height()
    c["width"], c["height"] = width, height + 100
    c.create_image(0, 0, anchor='nw', image=img)
    c.update()
def bandw():
    global img, width, height
    print("black and white")
    for y in range(height):
        for x in range(width):
            color = img.get(x, y)
            apx = (color[0] + color[1] + color[2]) // 3
            new_color = '#' + 3 * '{:02x}'.format(apx)
            img.put(new_color, (x, y))
        c.update()
def rbandw():
    global img, width, height
    for y in range(height):
        for x in range(width):
            color = img.get(x, y)
            priemer = (color[0] + color[1] + color[2]) // 3
            if priemer > 127:
                new_color = 'white'
            else:
                new_color = 'black'
            img.put(new_color,(x,y))
        c.update()

def negative():
    for y in range(height):
        for x in range(width):
            color = img.get(x, y)
            r, g, b = color
            nr, ng, nb = 255 - r, 255 - g, 255 - b
            new_color = '#{:02x}{:02x}{:02x}'.format(nr, ng, nb)
            print(new_color)
            img.put(new_color, (x, y))
        c.update()
def pixel():
    def pomiesaj(zx, zy, velkost):
        for y1 in range(velkost):
            for x1 in range(velkost):
                x2, y2 = randrange(velkost), randrange(velkost)
                color1 = img.get(zx + x1, zy + y1)
                color2 = img.get(zx + x2, zy + y2)
                img.put(rgb_to_hex(color2), (zx + x1, zy + y1))
                img.put(rgb_to_hex(color1), (zx + x2, zy + y2))
    velkost = 10
    for y in range(0, height - velkost, velkost):
        for x in range(0, width - velkost, velkost):
            pomiesaj(x, y, velkost)
        c.update()
def u1():
    for y in range(height):
        for x in range(width):
            color = img.get(x, y)
            apx = (color[0] + color[1] + color[2]) // 3
            nr, ng, nb = 255 - apx, 255 - apx, 255 - apx
            new_color = '#' + 3 * '{:02x}'.format(nr, ng, nb)
            img.put(new_color, (x, y))
        c.update()
def u2():
    def pomiesaj(zx, zy, velkost):
        for y1 in range(velkost):
            for x1 in range(velkost):
                if randrange(2) == 0:
                    x2, y2 = randrange(velkost), randrange(velkost)
                    color1 = img.get(zx + x1, zy + y1)
                    color2 = img.get(zx + x2, zy + y2)
                    img.put(rgb_to_hex(color2), (zx + x1, zy + y1))
                    img.put(rgb_to_hex(color1), (zx + x2, zy + y2))
    velkost = 10
    for y in range(0, height - velkost, velkost):
        for x in range(0, width - velkost, velkost):
            pomiesaj(x, y, velkost)
        c.update()
def u3():
    for y in range(0, height, 32):
        for x in range(0, width, 32):
            color = img.get(x, y)
            color = rgb_to_hex(color)
            for y1 in range(y, y+32, 1):
                for x1 in range(x, x+32, 1):
                    img.put(color, (x1, y1))
            c.update()
def u4():
    for y in range(height):
        for x in range(width):
            if randrange(20) == 0:
                color = img.get(x, y)
                radius = 20
                center = (x, y)
                for y1 in range(x, x+radius):
                    for x1 in range(y, y+radius):
                        dx = x - center[0]
                        dy = y - center[1]
                        distance = (dx * dx + dy * dy) ** 0.5
                        if distance <= radius:
                            img.put(rgb_to_hex(color), (x1, y1))
                c.update()
def u5():
    pass
def u6():
    pass

root = ctk.Tk()
root.title('ImageConverter')
level = ctk.Menu(root)
level.add_command(label = f'Reset',  command = lambda:[reset()])
level.add_command(label = f'BlackAndWhite',  command = lambda:[bandw()])
level.add_command(label = f'Realistic BlackAndWhite',  command = lambda:[rbandw()])
level.add_command(label = f'Negative',  command = lambda:[negative()])
level.add_command(label = f'Pixelated',  command = lambda:[pixel()])
level.add_command(label = f'U1',  command = lambda:[u1()])
level.add_command(label = f'U2',  command = lambda:[u2()])
level.add_command(label = f'U3',  command = lambda:[u3()])
level.add_command(label = f'U4',  command = lambda:[u4()])
level.add_command(label = f'U5',  command = lambda:[u5()])
level.add_command(label = f'U6',  command = lambda:[u6()])
root.config(menu = level)
c = ctk.Canvas(root)
c.pack()
reset()
root.mainloop()