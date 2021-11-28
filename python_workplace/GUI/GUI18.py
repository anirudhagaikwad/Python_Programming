#Tkinter Toplevel Widget Example
from tkinter import *  
  
win = Tk()  
  
win.geometry("200x200")  
  
def open():  
    top = Toplevel(win) 
    top.geometry("500x500") 
    top.mainloop()  
  
btn = Button(win, text="open", command=open)  
  
btn.place(x=75, y=50)  
  
win.mainloop()