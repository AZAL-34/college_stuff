import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json



def shopstuff():
    def viewstock():
        place = select_loc.get()
        with open("stock.json") as file:
            stock = json.load(file)
            fish = stock[place]["fish"]
            chips = stock[place]["chips"]
            coke = stock[place]["coke"]
        messagebox.showinfo(f"Stock for {place}", f"Fish: {fish}\nChips: {chips}\nCoke: {coke}")

    shopmenu = tk.Tk()
    title = tk.Label(shopmenu, text="Select Location:")
    title.pack()
    location = tk.StringVar()
    select_loc = ttk.Combobox(shopmenu, values=["Newcastle Upon Tyne", "Alnwick", "Newton Aycliffe", "Thirsk", "Whitby"], textvariable=location, state="readonly")
    select_loc.pack()
    stockman = tk.Button(shopmenu, text="Manage Stock", command=man_stock)
    stockman.pack()
    stockview = tk.Button(shopmenu, text="View Stock", command=viewstock)
    stockview.pack()
    thing_that_puts_a_gap_between_the_buttons = tk.Label(shopmenu, text="")
    thing_that_puts_a_gap_between_the_buttons.pack()
    salesrec = tk.Button(shopmenu, text="Record Sales", command=viewstock)
    salesrec.pack()
    salesview = tk.Button(shopmenu, text="View Sales", command=viewstock)
    salesview.pack()
    # the last two buttons above are using a placeholder command.

    shopmenu.mainloop()

def man_stock():
    stockmenu = tk.Tk()
    stockmenu.mainloop()

def warehousestuff():
    pass

mainmenu = tk.Tk()
title = tk.Label(mainmenu, text="Select:")
title.pack()
shop_button = tk.Button(mainmenu, text="Shop", command=shopstuff)
shop_button.pack()
warehouse_button = tk.Button(mainmenu, text="Warehouse", command=warehousestuff)
warehouse_button.pack()
mainmenu.mainloop()