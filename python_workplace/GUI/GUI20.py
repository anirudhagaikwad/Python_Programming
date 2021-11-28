#Tkinter MessageBox

from tkinter import *  
from tkinter import messagebox  
  
win = Tk()  
win.geometry("100x100")  
messagebox.askquestion("Confirm","Are you sure about it?")  

#messagebox.askretrycancel("Application"," wanna try again?")

#messagebox.showerror("errorWindow","oops!!!Error")

#messagebox.showwarning("warning","This is a Warning")

win.mainloop()  