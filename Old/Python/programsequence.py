import tkinter
c = tkinter.Canvas()
c.pack()
def sequence():
	c.delete('all')
	global to_input, from_input
	a = int(from_input.get())
	b = int(to_input.get())
	x = y = 5
	pismo = 'Arial 7 bold'
	for i in range (a, b, 1):
		if i >= 100:
			pismo = 'Arial 5 bold'
		if x >=1050:
			y += 50		
			x = 0
		c.create_rectangle(x,y,x+10,y+10)
		c.create_text(x+5,y+5, text= i, font = pismo)
		x += 10	
from_label = tkinter.Label(text = "From: ")
from_label.pack()
from_input = tkinter.Entry()
from_input.pack()
to_label = tkinter.Label(text = "To:")
to_label.pack()
to_input = tkinter.Entry()
to_input.pack()
b = tkinter.Button(text = "Start", command = sequence)
b.pack()
c.mainloop()
