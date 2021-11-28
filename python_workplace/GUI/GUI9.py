import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.ttk import *

win=tk.Tk()
win.geometry("500x400")

def click():
    messagebox.showinfo("hello you are clicked CheckedButton...")


v=StringVar(win,"1")
style=Style(win)
style.configure("TRadiobutton",background="light blue",foreground="orange",font=("arial",14,"bold"))
optinos={
    "Opt A":"1","Opt B":"2","Opt C":"3","Opt D":"4",
}



for(txt,val) in optinos.items():
    Radiobutton(win,text=txt,variable=v,value=val).pack(side=TOP,ipady=4)


win.mainloop()