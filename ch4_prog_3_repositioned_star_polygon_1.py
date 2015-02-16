""" ch4 No.3 
Program name: repositioned_star_polygon_1.py 
Objective: Draw a series of stars each with their own start position. 

Keywords: polygon, anchor point, star 
============================================================================79 
Comments:Each separate star is drawn relative to a pair variables, 
x_anchor and y_anchor It simple to re-position different stars just 
by reassigning the values of the anchor position. 
                                                                                      
Tested on: Python 2.6, Python 2.7,Python 3.2.3
Author: Mike Ohlson de Fine    
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Star polygon repositioned') 
cw = 300                                     # canvas width 
ch = 100                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

# Green star, fixed to an anchor point. 
x_anchor = 15 
y_anchor = 50 
canvas_1.create_polygon(x_anchor,        y_anchor, 
                        x_anchor + 20,   y_anchor - 40, 
                        x_anchor + 30,   y_anchor + 10, 
                        x_anchor,        y_anchor - 30, 
                        x_anchor + 40,   y_anchor - 20, 
                           fill="green")     

# Red star, fixed to an anchor point.             
x_anchor = 70 
y_anchor = 70 
canvas_1.create_polygon(x_anchor,        y_anchor, 
                        x_anchor + 20,   y_anchor - 40, 
                        x_anchor + 30,   y_anchor + 10, 
                        x_anchor,        y_anchor - 30, 
                        x_anchor + 40,   y_anchor - 20, 
                           fill="red")      

# Blue star, fixed to an anchor point.             
x_anchor = 200 
y_anchor = 60 
canvas_1.create_polygon(x_anchor,        y_anchor, 
                        x_anchor + 20,   y_anchor - 40, 
                        x_anchor + 30,   y_anchor + 10, 
                        x_anchor,        y_anchor - 30, 
                        x_anchor + 40,   y_anchor - 20, 
                           fill="blue") 

root.mainloop()
