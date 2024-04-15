import tkinter, time, asyncio
import customtkinter as ct
from dictionaries import *

def timerevent(run=True):
    global admin_debugger
    if run:
        for i in debuglist:
            entrylabel = ct.CTkLabel(admin_debugger, text=i, font=("Times New Roman", 16), text_color="lime")
            entrylabel.pack(side="top", anchor="w", padx=10)
        debuglist.clear()
        admin_debugger.update()
        admin_debugger.after(50, timerevent)

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
    global stat, admin_button, admin_window, searchtype, admin_debugger

    def erasedebugger():
        for i in admin_debugger.winfo_children():
            if i != admin_debugger_button and i != admin_debugger_name: i.destroy()

    if stat == "OFF":
        stat = "ON"
        if searchtype.cget("text") == "Search by subject:": filename = "subjectToName.txt"
        else: filename = "nameToSubject.txt"
        root.geometry(CenterWindowToDisplay(root, 800, 600, 1.0))
        admin_button.configure(text="Admin [ON]")
        admin_window = ct.CTkFrame(root, fg_color="transparent", width=500)
        admin_window.pack(side="left", anchor="e", fill="y", expand=True, padx=10)
        admin_creator = ct.CTkFrame(admin_window, fg_color="transparent", width=500)
        admin_creator.pack(side="top", anchor="w", fill="x", pady = 5)
        admin_creator_label = ct.CTkLabel(admin_creator, text="For teacher", font=("Arial", 16), text_color="white")
        admin_creator_label.pack(side="left", anchor="nw", padx= 5)
        admin_creator_entry = ct.CTkEntry(admin_creator)
        admin_creator_entry.pack(side="left", anchor="nw")
        admin_creator_label2 = ct.CTkLabel(admin_creator, text="add subject", font=("Arial", 16), text_color="white")
        admin_creator_label2.pack(side="left", anchor="nw", padx=10)
        admin_creator_entry2 = ct.CTkEntry(admin_creator)
        admin_creator_entry2.pack(side="left", anchor="nw")
        admin_creator_button = ct.CTkButton(admin_window, text="Add and Save", font=defaultFont, command=lambda: debuglist.append(db.insert(admin_creator_entry.get().lower(),admin_creator_entry2.get().upper(),filename)))
        admin_creator_button.pack(side="top", anchor="center", pady=5)
        admin_debugger = ct.CTkFrame(admin_window, fg_color="gray9", width=500)
        admin_debugger.pack(side="top", anchor="w", fill="both", expand=True)
        admin_debugger_button = ct.CTkButton(admin_debugger, text="EraseAll", command=lambda: erasedebugger(), width=10)
        admin_debugger_button.pack(side="right", anchor="n", padx=10, pady=10)
        admin_debugger_name = ct.CTkLabel(admin_debugger, text="[Debug console]", font=("Times New Roman", 20),text_color="lime")
        admin_debugger_name.pack(side="top", anchor="w", padx=10, pady=10)
        timerevent()
    elif stat == "ON":
        stat = "OFF"
        root.geometry(CenterWindowToDisplay(root, 500, 600, 1.0))
        admin_button.configure(text="Admin [OFF]")
        admin_window.destroy()
        timerevent(False)
def search(word):
    global results
    if results:
        for i in results:
            i.destroy()
    else: results = []
    if not word: debuglist.append("No search term provided."); return
    result = db.find(word)
    lab = ct.CTkLabel(result_window, text=f'For term "{word}" found {len(result)} results:', font=("Arial", 24), text_color="white")
    debuglist.append(f"Found {len(result)} results for term '{word}'.")
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
    searchtype = ct.CTkButton(search_window, text="Search by name:", fg_color="transparent", font=defaultFont, command=changetype)
    searchtype.pack(side="left", fill="x", padx=10)
    input_field = ct.CTkEntry(search_window)
    input_field.pack(side="left", fill="x", expand=True)
    input_field.focus_set()
    submit_button = ct.CTkButton(search_window, text="Search", command=on_submit, font=defaultFont)
    submit_button.pack(side="right", fill="x", padx=10, pady=10)
    result_window = ct.CTkFrame(root, fg_color="transparent", width=300)
    result_window.pack(side="left", anchor="w", fill="y", expand=True)
    return

ct.set_default_color_theme("green")
ct.set_appearance_mode("dark")
defaultFont = ("Arial", 16, "bold")
root = ct.CTk()
root.wm_iconbitmap("gjh_logo.ico")
stat = "OFF"
results = []
debuglist = []
db = WordDictionary()
debuglist.append(db.load("nameToSubject.txt"))
root.geometry(CenterWindowToDisplay(root, 500, 600, 1.0))
root.title("GJH Teacher Database")
draw_user_gui(search)
root.mainloop()