from tkinter import Canvas, Tk, Menu, Button
import modul

def load(clvl):
    global current
    level.entryconfig(1, label=f"Current: {clvl}")
    current = modul.Pexeso((c,level), clvl)

main = Tk()
main.title('PEXESO')
level = Menu(main)
level.add_command(label = f"Current: 0")
level.add_command(label = f'Level 1',  command = lambda:[load(1), klik.destroy()])
level.add_command(label = f'Level 2',  command = lambda:[load(2), klik.destroy()])
level.add_command(label = f'Level 3',  command = lambda:[load(3), klik.destroy()])
level.add_command(label = f'Level 4',  command = lambda:[load(4), klik.destroy()])
level.add_command(label = f'Level 5',  command = lambda:[load(5), klik.destroy()])
level.add_command(label = f'Level 6',  command = lambda:[load(6), klik.destroy()])
level.add_command(label = f'Level 7',  command = lambda:[load(7), klik.destroy()])
level.add_command(label = f'Level 8',  command = lambda:[load(8), klik.destroy()])
level.add_command(label = f'Level 9',  command = lambda:[load(9), klik.destroy()])
level.add_command(label = f'Level 10', command = lambda:[load(10),klik.destroy()])
level.add_command(label = f'Level 11', command = lambda:[load(11),klik.destroy()])
level.add_command(label = f'Level 12', command = lambda:[load(12),klik.destroy()])
level.add_command(label = f'[CHEAT] Show', command = lambda:[current.cheat(),klik.destroy()])
level.add_command(label = f'[CHEAT] End', command = lambda:[current.YouWon(),klik.destroy()])
main.config(menu = level)

c = Canvas(main)
c.create_text(200,50,text='Pexeso by Patrik Bukovský 3.C')
c.create_text(200,70,text='Ak vyhráš, automaticky postupuješ na ďalší level.')
c.create_text(200,90,text='Vieš aj prechádzať medzi levelmi hore na paneli.')
c.create_text(200,110,text='Použí CHEAT pre účely testovania.')
c.create_text(190,130,text='Medzi levelom 4 a 5 hodí false error kvôli kliknutiu naviac (pri klasickom prejdení levelu).', font=('Arial',7))
klik = Button(c,text='Začať!', command = lambda:[load(1),klik.destroy()]); klik.place(x=175,y=150)
c.pack()

main.mainloop()