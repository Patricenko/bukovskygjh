import tkinter

def draw_admin_gui():
    root.geometry("1000x1000")

def find(word):
    pass
def draw_user_gui(callback):
    def on_submit():
        user_input = input_field.get()
        callback(user_input)
        window.destroy()

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
level = tkinter.Menu(root)
level.add_command(label = f'English to Latin',  command = lambda:[draw_admin_gui()])
level.add_command(label = f'Latin to English',  command = lambda:[draw_admin_gui()])
level.add_command(label = f'Admin Panel',  command = lambda:[draw_admin_gui()])
root.config(menu = level)
draw_user_gui(find)
root.mainloop()