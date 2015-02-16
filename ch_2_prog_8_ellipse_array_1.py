""" ch2 No.8
Program name: ellipse_array_1.py 
Objective: An an array of ellipses are drawn controlling major and minor axis lengths. 

Keywords: canvas, oval, ellipse, major axis, minor axis 
============================================================================79 
Comments:  We modify the variables to read as center and major and minor axis length 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 

""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Ellipse array.') 

cw = 300                                      # canvas width 
ch = 400                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1)                              

# specify bottom-left and top-right as a set of four numbers named 'xy' 
center_x   = 150 
center_y   = 200 
major_axis = 280 
minor_axis = 140 
number_ellipses = 40 

for i in range(0, number_ellipses): 

    canvas_1.create_oval(center_x- major_axis/2, center_y- minor_axis/2, 
                         center_x+ major_axis/2, 
 center_y+ minor_axis/2, 
                         outline='red', width= 1) 
    major_axis -= 6 
    minor_axis += 6 

root.mainloop() 
