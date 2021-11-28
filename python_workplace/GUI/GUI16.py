#Scrollbar Widget

from tkinter import *  
  
win= Tk()  
sbb = Scrollbar(win)  
sbb.pack(side = RIGHT, fill = Y)  
  
mylist = Listbox(win, yscrollcommand = sbb.set)  
  
for line in range(45):  
    mylist.insert(END, "Value " + str(line))  
  
mylist.pack(side = LEFT)
sbb.config(command = mylist.yview)
  
mainloop()