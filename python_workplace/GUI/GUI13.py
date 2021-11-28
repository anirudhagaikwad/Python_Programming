# Frame Widget

from tkinter import *
 
root = Tk() 
root.geometry("300x150") 

w = Label(root, text ='SES', font = "80") 
w.pack() 

frame = Frame(root) 
frame.pack() 

bottomframe = Frame(root) 
bottomframe.pack(side = BOTTOM) 

button1 = Button(frame, text ="Block1", fg ="red") 
button1.pack(side = LEFT) 

button2 = Button(frame, text ="Block2", fg ="brown") 
button2.pack(side = LEFT) 

button3 = Button(frame, text ="Block3", fg ="blue") 
button3.pack(side = LEFT) 

button4 = Button(bottomframe, text ="Block4", fg ="orange") 
button4.pack(side = BOTTOM) 

button5 = Button(bottomframe, text ="Block5", fg ="orange") 
button5.pack(side = BOTTOM) 

button6 = Button(bottomframe, text ="Block6", fg ="orange") 
button6.pack(side = BOTTOM) 

root.mainloop()