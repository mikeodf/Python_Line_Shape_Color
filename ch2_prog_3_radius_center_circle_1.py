""" ch2 No.3 
Program name: radius_center_circle_1.py 
Objective: A circle specified in terms of its radius and center position. 

Keywords: canvas, oval, circle, center, radius 
============================================================================79 
Comments:A circle is a special case of an oval and is defined by the 
box it fits inside. The bounding box here is defined in terms of the radius 
and position of the center. This is a more convenient and logical  way of drawing a circle (geometrically speaking). 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Radius and center circle.') 

cw = 150                                      # canvas width 
ch = 140                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

# specify bottom-left and top-right as a set of four numbers named 'xy' 
center_x = 80 
center_y = 60 
Radius = 80         

canvas_1.create_oval(center_x - Radius/2, center_y - Radius/2, 
                                   center_x + Radius/2, center_y + Radius/2) 
root.mainloop()
