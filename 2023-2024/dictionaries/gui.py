import tkinter
from dictionaries import *
def load_e_to_l():
    level.entryconfig(1, label=f"-> English to Latin")
    level.entryconfig(2, label=f"Latin to English")
    with open()
def load_l_to_e():
    level.entryconfig(1, label=f"English to Latin")
    level.entryconfig(2, label=f"-> Latin to English")
def draw_admin_gui():
    global c2
    global stat
    if not stat: stat = "OFF"
    print(stat)
    if stat == "OFF":
        stat = "ON"
        root.geometry("1000x1000")
        c2 = tkinter.Canvas(root, width=500, height=400, bg="grey")
        c2.pack(side="right", fill="y")
    elif stat == "ON":
        stat = "OFF"
        c2.destroy()
        root.geometry("500x1000")
    level.entryconfig(3, label=f"Admin panel [{stat}]")

def find(word):
    pass
def draw_user_gui(callback):
    def on_submit():
        user_input = input_field.get()
        callback(user_input)

    window = tkinter.Canvas(root, width=1000, height=1000, bg="lime")
    window.pack(side="top", fill="x")
    tkinter.Label(window, text="Text to find:").pack(side="left", fill="x", padx=10)
    input_field = tkinter.Entry(window)
    input_field.pack(side="left", fill="x", expand=True)
    input_field.focus_set()
    submit_button = tkinter.Button(window, text="Submit", command=on_submit)
    submit_button.pack(side="right", fill="x", padx=10, pady=10)

root = tkinter.Tk()
root.geometry('500x1000')
root.title("Dictionary by Patrik Bukovsky")
stat = ""
active = ""
level = tkinter.Menu(root)
level.add_command(label = f'-> English to Latin',  command = lambda:[load_e_to_l()])
level.add_command(label = f'Latin to English {active}',  command = lambda:[load_l_to_e()])
level.add_command(label = f'Admin Panel [OFF]',  command = lambda:[draw_admin_gui()])
root.config(menu = level)
draw_user_gui(find)
load_e_to_l()
root.mainloop()