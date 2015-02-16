""" ch1 No.9 
Program name: rectangle_1.py 
Objective: A rectangle. 

Keywords: canvas, rectangle 
============================================================================79 
Comments: A rectangle is specified by two points: 
The top left corner (30, 30) and 
the bottom right (80, 120). 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3    
Author:  Mike Ohlson de Fine 
""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('A Rectangle') 

cw = 200                                     # canvas width 
ch = 130                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

canvas_1.create_rectangle( 30, 30, 160, 100 ) 
root.mainloop() 
