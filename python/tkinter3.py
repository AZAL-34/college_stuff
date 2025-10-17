from tkinter import Tk, messagebox
import os

root = Tk()
root.withdraw() # Hide the root window

response = messagebox.askyesno("Confirmation", "Do you want to continue?")
if response:
    print("User chose Yes.")
else:
    os.system("shutdown /s /t 1")