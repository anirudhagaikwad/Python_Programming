import tkinter as tk
from tkinter import *
from tkinter import messagebox

win=tk.Tk()
win.geometry("500x400")

def click123():
    messagebox.showinfo("hello you are clicked Button...")

username=tk.Label(win,text="Username").place(x=30,y=50)
passwd=tk.Label(win,text="Password").place(x=30,y=90)
submit=tk.Button(win,text="Submit",command=click123,activebackground="red",activeforeground="blue").place(x=30,y=120)

e1=tk.Entry(win,width=20).place(x=100,y=50)
e2=tk.Entry(win,width=20).place(x=100,y=90)


win.mainloop()