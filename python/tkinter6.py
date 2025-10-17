import tkinter as tk
import os

def say_hello():
    print("skibni gtoiely")

def shutdown():
    os.system("shutdown /s /t 1")

root = tk.Tk()
root.title("skibnbni gtoieloy")

men_bar = tk.Menu(root)

file_menu = tk.Menu(men_bar, tearoff=0)
file_menu.add_command(label="Open", command=say_hello)
file_menu.add_command(label="Save", command=say_hello)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=shutdown)

men_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(men_bar, tearoff=0)
help_menu.add_command(label="About", command=say_hello)

men_bar.add_cascade(label="hELP", menu=help_menu)

view_men = tk.Menu(men_bar, tearoff=0)
view_men.add_command(label="skibni", command=say_hello)
view_men.add_command(label="gtoiely", command=say_hello)

men_bar.add_cascade(label="view", menu=view_men)

opt_menu = tk.Menu(men_bar, tearoff=0)
opt_menu.add_command(label="skibni", command=say_hello)
opt_menu.add_command(label="gtoiely", command=say_hello)

men_bar.add_cascade(label="options", menu=opt_menu)

root.config(menu=men_bar)

root.mainloop()