""" ch1 No.1 
Program name: line_1.py 
Objective: Draw a straight line on a canvas. 

Keywords: canvas, line, default 
============================================================================79 
Comments: When drawing lines you MUST specify the start and end points. 
Other properties like color and line width may also be specified, but you don't 
HAVE to. Default values will be used if none are explicitly stated. 

Tested on: Python 2.6,  Python 2.7 and Python 3.2.3
Author: Mike Ohlson de Fine 
""" 
from Tkinter import *   # For Python 3.2 change Tkinter to tkinter, as shown below.
#from tkinter import *
root = Tk() 

canvas_1 = Canvas(root, width=200, height=200) 
canvas_1.grid(row=0, column=1) 

canvas_1.create_line(10, 20, 50, 100) 

root.mainloop()
