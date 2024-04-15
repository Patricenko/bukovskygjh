import tkinter
import customtkinter as ct
from dictionaries import *

def CenterWindowToDisplay(Screen: ct.CTk, width: int, height: int, scale_factor: float = 1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"
def changetype():
    global searchtype
    if searchtype.cget("text") == "Search by name:":
        db.erase()
        db.load("subjectToName.txt")
        searchtype.configure(text="Search by subject:")
    else:
        db.erase()
        db.load("nameToSubject.txt")
        searchtype.configure(text="Search by name:")

def draw_admin_gui():
    global stat, admin_button, admin_window
    if stat == "OFF":
        stat = "ON"
        root.geometry(CenterWindowToDisplay(root, 1000, 600, 1.0))
        admin_button.configure(text="Admin [ON]")
        admin_window = ct.CTkFrame(root, fg_color="transparent", width=500)
        admin_window.pack(side="left", anchor="e", fill="y", expand=True, padx=10)
        admin_creator = ct.CTkFrame(admin_window, fg_color="transparent", width=500)
        admin_creator.pack(side="top", anchor="w", fill="x", pady = 10)
        admin_creator_label = ct.CTkLabel(admin_creator, text="For name", font=("Arial", 16), text_color="white")
        admin_creator_label.pack(side="left", anchor="nw", padx=10)
        admin_creator_entry = ct.CTkEntry(admin_creator)
        admin_creator_entry.pack(side="left", anchor="nw")
        admin_creator_label2 = ct.CTkLabel(admin_creator, text="add subject", font=("Arial", 16), text_color="white")
        admin_creator_label2.pack(side="left", anchor="nw", padx=10)
        admin_creator_entry2 = ct.CTkEntry(admin_creator)
        admin_creator_entry2.pack(side="left", anchor="nw")
        admin_creator_button = ct.CTkButton(admin_window, text="Add", command=lambda: db.insert(admin_creator_entry.get().lower(),admin_creator_entry2.get()))
        admin_creator_button.pack(side="top", anchor="center", pady=10)
        admin_debugger = ct.CTkFrame(admin_window, fg_color="black", width=500)
        admin_debugger.pack(side="top", anchor="w", fill="both", expand=True)


    elif stat == "ON":
        stat = "OFF"
        root.geometry(CenterWindowToDisplay(root, 500, 600, 1.0))
        admin_button.configure(text="Admin [OFF]")
        admin_window.destroy()

def search(word):
    global results
    if results:
        for i in results:
            i.destroy()
    else: results = []
    if not word: return
    result = db.find(word)
    lab = ct.CTkLabel(result_window, text=f'For term "{word}" found {len(result)} results:', font=("Arial", 24), text_color="white")
    lab.pack(anchor="w", side="top", padx=10, pady=10)
    results.append(lab)
    for i in result:
        result_label = ct.CTkLabel(result_window, text=i, font=("Arial", 20), text_color="white")
        result_label.pack(anchor="w", side="top", padx=20)
        results.append(result_label)
def draw_user_gui(callback):
    global admin_button, result_window, searchtype
    def on_submit():
        user_input = input_field.get()
        callback(user_input)
    admin_button = ct.CTkButton(root, text="Admin [OFF]", command=draw_admin_gui)
    admin_button.pack(side="bottom", anchor="center", padx=10, pady=10)
    search_window = ct.CTkFrame(root, height=50)
    search_window.pack(side="top", fill="x")
    searchtype = ct.CTkButton(search_window, text="Search by name:", fg_color="transparent", command=changetype)
    searchtype.pack(side="left", fill="x", padx=10)
    input_field = ct.CTkEntry(search_window)
    input_field.pack(side="left", fill="x", expand=True)
    input_field.focus_set()
    submit_button = ct.CTkButton(search_window, text="Search", command=on_submit)
    submit_button.pack(side="right", fill="x", padx=10, pady=10)
    result_window = ct.CTkFrame(root, fg_color="transparent", width=500)
    result_window.pack(side="left", anchor="w", fill="y", expand=True)
    return


root = ct.CTk()
stat = "OFF"
results = []
db = WordDictionary()
db.load("nameToSubject.txt")
root.geometry(CenterWindowToDisplay(root, 500, 600, 1.0))
root.title("GJH professor DB")
draw_user_gui(search)
root.mainloop()