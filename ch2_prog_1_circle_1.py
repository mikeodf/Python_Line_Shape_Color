""" ch2 No.1 
Program name: circle_1.py 
Objective: A circle is a special case of an oval. 

Keywords: canvas, oval, circle 
============================================================================79 
Comments: A circle is a special case of an oval and is defined by the 
box it fits inside. This bounding box is specified in the same way as rectangles, 
from bottom-left to top-right. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author:          Mike Ohlson de Fine 
""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('A circle') 

cw = 150                                      # canvas width 
ch = 140                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

# specify bottom-left and top-right as a set of four numbers named 'xy' 
xy = [20, 20, 120, 120]         

canvas_1.create_oval(xy) 
root.mainloop() 
