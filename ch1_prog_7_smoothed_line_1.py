""" ch1 No.7 
Program name: smoothed_line_1.py 
Objective: Draw a line with a smooth bend on a canvas. 

Keywords: canvas, bent line, curve, smooth line 
============================================================================79 
Comments: When drawing lines with many segments you specify location of 
each segment. The end of one segment is the start of the next. 
In addition choosing the option "smooth="true" gets the line smoothed into  a curve. 
The amount of smoothness in the curve is determined by the number of spline steps. 
High numbers give a smoother curve. 
In this example the default number of splinesteps is in effect. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3    
Author:    Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Smoothed line') 
cw = 250                                      # canvas width 
ch = 200                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

x1 = 50 
y1 = 10 
x2 = 50 
y2 = 180 
x3 = 180 
y3 = 180 

canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="true") 
  
root.mainloop()
