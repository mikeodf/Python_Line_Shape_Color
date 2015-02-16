""" ch2 No.5 
Program name:loop_generated_concentric_circles_3.py  
Objective: Use a for loop to generate a large set of concentric circles . 

Keywords: canvas, oval, circle, center, radius 
============================================================================79 
Comments: A circle is a special case of an oval and is defined by the 
box it fits inside. The bounding box here is defined in terms of the radius 
and position of the center. This is a more convenient and logical  way of drawing a circle (geometrically speaking). 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author:          Mike Ohlson de Fine 
""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Radius and center circle.') 

cw = 300                                     # canvas width 
ch = 300                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="darkblue") 
canvas_1.grid(row=0, column=1)                              

# specify bottom-left and top-right as a set of four numbers named 'xy' 
center_x = 150 
center_y = 150 
Radius = 150 
number_of_rings = 40 

for i in range(0, number_of_rings): 
        
    canvas_1.create_oval(center_x - Radius, center_y - Radius, 
                         center_x + Radius, center_y + Radius, 
                         fill= 'red', outline='blue', width= 2) 
    Radius -= 4 

root.mainloop() 
