""" ch4 No.4 
Program name: positioned_sized_star_1.py 
Objective: Draw a series of stars each with their own start position 
	   and size (scaled larger or smaller from a prototype). 

Keywords: polygon, anchor point, scaled size, star 
============================================================================79 
Comments: A scale factor "size_scaling" is used to change the size of the stars 
By having each separate star draw itself relative to a pair variables, 
x_anchor and y_anchor as well as the size_scaling, it simple to re-position 
and re-size different stars just by reassigning the values of the anchor position. 
                               
Tested on: Python 2.6, Python 2.7, Python 3.2.3
Author: Mike Ohlson de Fine      
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Star polygon resized and repositioned') 
cw = 600                                     # canvas width 
ch = 200                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

# Small green star, anchored to an anchor point. 
size_scaling = 1 
x_anchor = 15 
y_anchor = 150 


canvas_1.create_polygon(x_anchor,        y_anchor, 
                        x_anchor + 20 * size_scaling,   y_anchor - 40* size_scaling, 
                        x_anchor + 30 * size_scaling,   y_anchor + 10* size_scaling, 
                        x_anchor,        y_anchor - 30* size_scaling, 
                        x_anchor + 40 * size_scaling,   y_anchor - 20* size_scaling, 
                           fill="green")      
# Green star, size 2, anchored to an anchor point.            
size_scaling = 2 
x_anchor = 80 
y_anchor = 120 
canvas_1.create_polygon(x_anchor,        y_anchor, 
                        x_anchor + 20 * size_scaling,   y_anchor - 40* size_scaling, 
                        x_anchor + 30 * size_scaling,   y_anchor + 10* size_scaling, 
                        x_anchor,        y_anchor - 30* size_scaling, 
                        x_anchor + 40 * size_scaling,   y_anchor - 20* size_scaling, 
                           fill="darkgreen")      
# Green star, size 3, anchored to an anchor point.                       
size_scaling = 3 
x_anchor = 160 
y_anchor = 110 
canvas_1.create_polygon(x_anchor,        y_anchor, 
                        x_anchor + 20 * size_scaling,   y_anchor - 40* size_scaling, 
                        x_anchor + 30 * size_scaling,   y_anchor + 10* size_scaling, 
                        x_anchor,        y_anchor - 30* size_scaling, 
                        x_anchor + 40 * size_scaling,   y_anchor - 20* size_scaling, 
                           fill="lightgreen")   
# Green star, size 4, anchored to an anchor point.       
size_scaling = 4 
x_anchor = 300 
y_anchor = 110 
canvas_1.create_polygon(x_anchor,        y_anchor, 
                        x_anchor + 20 * size_scaling,   y_anchor - 40* size_scaling, 
                        x_anchor + 30 * size_scaling,   y_anchor + 10* size_scaling, 
                        x_anchor,        y_anchor - 30* size_scaling, 
                        x_anchor + 40 * size_scaling,   y_anchor - 20* size_scaling, 
                           fill="forestgreen") 
root.mainloop()
