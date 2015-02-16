""" ch1 No.6 
Program name: segmented_line_1.py 
Objective: Draw a line with a sharp bend on a canvas. 

Keywords: canvas, bent line , segmented line
============================================================================79 
Comments: When drawing lines with many segments you specify location of 
each segment. The end of one segment is the start of the next. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author:    Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 

cw = 300                                      # canvas width 
ch = 200                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

x1 = 50 
y1 = 10 

x2 = 50 
y2 = 180 

x3 = 180 
y3 = 180 

canvas_1.create_line(x1,y1,  x2,y2,  x3,y3) 
  
root.mainloop()
