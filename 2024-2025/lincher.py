import customtkinter as ct
from tkinter import filedialog

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

root = ct.CTk()
root.title("Custom Launcher")
root.geometry("800x600")
root.wm_iconbitmap("icon.ico")

root.mainloop()