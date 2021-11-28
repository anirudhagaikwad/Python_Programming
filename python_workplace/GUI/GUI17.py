# Scale Widget
from tkinter import *  

win = Tk()  
win.geometry("200x100")
  
v = DoubleVar()  
                                                       #VERTICAL 
scale = Scale( win, variable=v, from_=1, to=50, orient=HORIZONTAL)  
scale.pack(anchor=CENTER)  
  
btn = Button(win, text="Value")  
btn.pack(anchor=CENTER)  
  
label = Label(win)  
label.pack()  
  
win.mainloop()