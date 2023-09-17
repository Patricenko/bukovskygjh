# uloha urobit trojuholnik v trojuholnikoch
import tkinter as tk
import random

okno = tk.Tk()
sirka = 400
vyska = 400
c = tk.Canvas(okno, width=sirka, height=vyska)
c.pack()
x1 = sirka / 2
y1 = 10
x2 = 10
y2 = vyska - 10
x3 = sirka - 10
y3 = vyska - 10
hlbka = 5  # Zmeniť hĺbku podľa potreby

def trojuholnik(c, hlbka, x1, y1, x2, y2, x3, y3):
    if hlbka == 0:
        fill_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255),
                                                  random.randint(0, 255))
        c.create_polygon(x1, y1, x2, y2, x3, y3, fill=fill_color, outline="black")
    else:
        x12 = (x1 + x2) / 2
        y12 = (y1 + y2) / 2
        x23 = (x2 + x3) / 2
        y23 = (y2 + y3) / 2
        x31 = (x3 + x1) / 2
        y31 = (y3 + y1) / 2
        trojuholnik(c, hlbka - 1, x1, y1, x12, y12, x31, y31)
        trojuholnik(c, hlbka - 1, x12, y12, x2, y2, x23, y23)
        trojuholnik(c, hlbka - 1, x31, y31, x23, y23, x3, y3)

trojuholnik(c, hlbka, x1, y1, x2, y2, x3, y3)
okno.mainloop()