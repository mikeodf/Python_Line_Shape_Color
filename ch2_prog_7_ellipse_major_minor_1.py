""" ch2 No.7 
Program name: ellipse_major_minor_1.py 
Objective: An ellipse here is specified in terms of its center 
and major and minor axis lengths. 

Keywords: canvas, oval, ellipse, major axis, minor axis 
============================================================================79 
Comments:  We modify the variables to read as center and 
major and minor axis length 

from tkinter import *  # For Python 3.2.3 and higher.
Author:          Mike Ohlson de Fine 
""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Ellipse.') 

cw = 300                                      # canvas width 
ch = 300                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1)                              

# specify bottom-left and top-right as a set of four numbers named 'xy' 
center_x   = 150 
center_y   = 150 
major_axis = 280 
minor_axis = 140 

canvas_1.create_oval(center_x- major_axis/2, center_y- minor_axis/2, 
                     center_x+ major_axis/2, center_y+ minor_axis/2, 
                         fill= 'black', outline='red', width= 4) 

root.mainloop() 
