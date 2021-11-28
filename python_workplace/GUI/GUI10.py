#Message Widget

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.ttk import *

win=tk.Tk()
win.geometry("500x400")

msg=Message(win,text="Message widget...").pack()

messagebox.showinfo("Information","This is messagebox info...")



win.mainloop()