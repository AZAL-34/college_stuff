import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os, time

root = tk.Tk()
root.title("button")

label = tk.Label(root, text="button")

def button():
    messagebox.showinfo("button", "button")
    time.sleep(10)
    os.system("shutdown /s /t 1")

button = tk.Button(root, text="button", command=button)
button.pack()

entry = tk.Entry(root)
entry.pack()

text = tk.Text(root, height=5, width=40)
text.pack()

check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="button", variable=check_var)
checkbutton.pack()

radio_var = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="button", variable=radio_var, value=1)
radiobutton2 = tk.Radiobutton(root, text="button", variable=radio_var, value=2)
radiobutton1.pack()
radiobutton2.pack()

listbox = tk.Listbox(root)
listbox.insert(1, "button")
listbox.insert(2, "button")
listbox.insert(3, "button")
listbox.pack()

scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

spinbox = tk.Spinbox(root, from_=0, to=10)
spinbox.pack()

combobox = ttk.Combobox(root, values=["button", "button", "button"])
combobox.pack()

message = tk.Message(root, text="button")
message.pack()

root.mainloop()