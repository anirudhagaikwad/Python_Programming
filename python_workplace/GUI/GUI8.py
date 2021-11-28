import tkinter as tk
from tkinter import *
from tkinter import messagebox

win=tk.Tk()
win.geometry("500x400")

def click():
    messagebox.showinfo("hello you are clicked CheckedButton...")


def click2():
    print(B1.option_get)


checkb1=IntVar()
checkb2=IntVar()
checkb3=IntVar()

B1=Checkbutton(win,text="homepage",variable=checkb1,onvalue=1,offvalue=0,height=2,width=10,command=click2)
B2=Checkbutton(win,text="loginpage",variable=checkb2,onvalue=1,offvalue=0,height=2,width=10)
B3=Checkbutton(win,text="extrapage",variable=checkb3,onvalue=1,offvalue=0,height=2,width=10,command=click)
B1.pack()
B2.pack()
B3.pack()



win.mainloop()