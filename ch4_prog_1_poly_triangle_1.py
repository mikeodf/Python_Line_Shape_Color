""" ch4 No.1  
Program name: poly_triangle_1.py 
Objective: Draw a triangle - the simplest polygon. 

Keywords: polygon. triangle 
============================================================================79 
Comments: a polygon is made by joining a sequence of x-y points,                                              
with the last point automatically joined to the first by a line to close 
the polygon. 
                                                                                      
Tested on: Python 2.6, Python 2.7, Python 3.2.3
Author: Mike Ohlson de Fine       
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 

cw = 300                                     # canvas width 
ch = 100                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

#                                        point 1    point 2     point 3 
canvas_1.create_polygon(200,10,   250,50,     50,70,      fill="red") 

root.mainloop() 
