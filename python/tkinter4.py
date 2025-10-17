import tkinter as tk

def create_pack_example(root):
    frame = tk.Frame(root, bg="lightblue", bd=2, relief="solid")
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    label1 = tk.Label(frame, text="Pack Eaxampe 1")
    label1.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

    label2 = tk.Label(frame, text="Pack Example 2")
    label2.pack(side=tk.LEFT, fill=tk.Y)


    
def create_place_example(root):
    frame = tk.Frame(root, bg="lightyellow", bd=2, relief="solid")
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    label1 = tk.Label(frame, text="Place Example 1", bg="red")
    label1.place(x=10, y=10, width=100, height=30)

    label2 = tk.Label(frame, text="Place Example 2", bg="green")
    label2.place(x=120, y=10, width=100, height=30)

    label3 = tk.Label(frame, text="Place Exmpaek0nel 3", bg="blue")
    label3.place(x=10, y=50, width=210, height=30)

root = tk.Tk()
root.title("hnkjofe\lkjho;fse fl uh")

create_place_example(root)
create_pack_example(root)

root.mainloop
