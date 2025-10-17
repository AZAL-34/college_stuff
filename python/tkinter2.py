import tkinter as tk
import os

def shutdown():
    os.system("shutdown /s /t 1")

root = tk.Tk()
root.title("Frames Example")

# Create a frame
frame = tk.Frame(root, bg="lightblue", width=300, height=200, borderwidth=2, relief="groove")
frame.pack(padx=10, pady=10)

# Add widgets inside the frame
label = tk.Label(frame, text="This is a frame", bg="lightblue")
label.pack(pady=10)

button = tk.Button(frame, text="Click me", command=shutdown)
button.pack()

root.mainloop()