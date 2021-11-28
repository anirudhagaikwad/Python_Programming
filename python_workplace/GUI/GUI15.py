# Listbox Widget
from tkinter import *

top = Tk()

top.geometry("200x250")

lbl = Label(top, text="List of Programming Languages")

listbox = Listbox(top)

listbox.insert(1,"Python")

listbox.insert(2, "Java")

listbox.insert(3, "C")

listbox.insert(4, "C++")

lbl.pack()
listbox.pack()
  
top.mainloop()
