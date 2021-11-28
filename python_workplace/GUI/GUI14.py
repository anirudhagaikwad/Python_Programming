# canvas Widget

import tkinter

# init tk
root = tkinter.Tk()

# creating canvas
mCanvas = tkinter.Canvas(root, bg="white", height=300, width=300)

# drawing two arcs
coord = 10, 10, 300, 300
arc1 = mCanvas.create_arc(coord, start=0, extent=150, fill="pink")
arc2 = mCanvas.create_arc(coord, start=150, extent=215, fill="blue")

# adding canvas to window and display it
mCanvas.pack()
root.mainloop()
