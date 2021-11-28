# Menu Widget

from tkinter import *
from tkinter import messagebox

root = Tk()

def hello():
    print("hello!")


def click():
    messagebox.showinfo("hello you are clicked ...")
        




menubar = Menu(root)
menubar.add_command(label="Hello", command=hello)
menubar.add_command(label="Quit!", command=root.quit)
menubar.add_command(label="dont_Quit", command=click)
root.config(menu=menubar)

root.mainloop()