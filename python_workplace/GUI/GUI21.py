#LabelFrame Widget

from tkinter import *  
  
win = Tk()  
win.geometry("300x200")  
  
labelframe1 = LabelFrame(win, text="Happy Thoughts!!!")  
labelframe1.pack(fill="both", expand="yes")  
  
toplabel = Label(labelframe1, text="You can put your happy thoughts here")  
toplabel.pack()  
  
labelframe2 = LabelFrame(win, text = "Changes You want!!")  
labelframe2.pack(fill="both", expand = "yes")  
  
bottomlabel = Label(labelframe2, text = "You can put here the changes you want,If any!")  
bottomlabel.pack()  
  
win.mainloop()  