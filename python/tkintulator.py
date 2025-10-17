import os
import tkinter as tk, time

def shutdown():
    os.system("shutdown /s /t 1")

def calculate():
    root1 = tk.Tk()
    root1.title("Tkintulation")
    frame = tk.Frame(root1, bg="lightblue", width=300, height=200, borderwidth=2, relief="groove")
    frame.pack(padx=10, pady=10)
    label = tk.Label(frame, text="calculate stuff", bg="pink")
    label.pack(pady=10)
    num1 = tk.Entry(frame)
    num1.pack()
    operators = tk.OptionMenu(frame, *["+", "=", "*"])

    root1.mainloop()
#     print("pick a number.")
    
#     while True:
#         try:
#             num1 = input("> ")
#             num1 = float(num1)
#             break
#         except:
#             print("invalid input. try again.")

#     print("pick another number.")
    
#     while True:
#         try:
#             num2 = input("> ")
#             num2 = float(num2)
#             break
#         except:
#             print("invalid input. try again.")

#     print("""
# pick an operation:
# 1. +
# 2. -
# 3. *
# 4. /
# 5. //
# 6. %
# """)
    
#     while True:
#         try:
#             oper = input("> ")
#             oper = int(oper)
#             if oper < 1 or oper > 6:
#                 raise Exception
#             break
#         except:
#             print("invalid input. try again.")

#     if oper == 1:
#         final_calc = (f"{num1} + {num2} = {num1 + num2}")
#     elif oper == 2:
#         final_calc = (f"{num1} - {num2} = {num1 - num2}")
#     elif oper == 3:
#         final_calc = (f"{num1} * {num2} = {num1 * num2}")
#     elif oper == 4:
#         final_calc = (f"{num1} / {num2} = {num1 / num2}")
#     elif oper == 5:
#         final_calc = (f"{num1} // {num2} = {num1 // num2}")
#     elif oper == 2:
#         final_calc = (f"{num1} % {num2} = {num1 % num2}")

#     with open("calc_history.txt", "a") as file:
#         file.write(f"{final_calc}\n")
#     print(final_calc)

print("Welcome to the CLIculator!")
root = tk.Tk()
root.title("Tkintulator")
frame = tk.Frame(root, bg="lightblue", width=300, height=200, borderwidth=2, relief="groove")
frame.pack(padx=10, pady=10)
label = tk.Label(frame, text="Welcome to the Tkintulator!", bg="pink")
label.pack(pady=10)
button = tk.Button(frame, text="Calculate", command=calculate)
button.pack()
button1 = tk.Button(frame, text="Quit", command=shutdown)
button1.pack()
root.mainloop()