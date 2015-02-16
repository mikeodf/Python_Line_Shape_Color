""" ch4 No.2 
Program name: star_polygon_1.py 
Objective: Draw a 5-point star. 

Keywords: polygon. star 
============================================================================79 
Comments: A polygon is made by joining a sequence of x-y points,                                              
with the last point automatically joined to the first by a line to close 
the polygon. 
                                                                                      
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine       
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Star polygon') 
 
cw = 200                                     # canvas width 
ch = 100                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

# blue star, anchored to an anchor point. 
x_anchor = 15 
y_anchor = 50 

canvas_1.create_polygon(x_anchor,       y_anchor, 
                        x_anchor + 20,  y_anchor - 40, 
                        x_anchor + 30,  y_anchor + 10, 
                        x_anchor,       y_anchor - 30, 
                        x_anchor + 40,  y_anchor - 20, 
                        fill="blue") 
root.mainloop()
