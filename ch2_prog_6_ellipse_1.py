""" ch2 No.6 
Program name: ellipse_1.py 
Objective: An ellipse is specified in terms of its bounding box, 
in the same way as a rectangle. 

Keywords: canvas, oval, ellipse 
============================================================================79 
Comments: An ellipse is an oval. In Python/Tkinter it is defined by the 
box it fits inside. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author:          Mike Ohlson de Fine 

""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Ellipse.') 

cw = 220                                      # canvas width 
ch = 120                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1)                              

# specify bottom-left and top-right as a set of four numbers named 'xy' 
bottom_left_x = 20 
bottom_left_y = 100 
top_right_x = 200 
top_right_y = 20 

canvas_1.create_oval(bottom_left_x, bottom_left_y, 
                       top_right_x, top_right_y, 
                         fill= 'black', outline='red', width= 4) 

root.mainloop()
