""" ch1 No.10 
Program name: concentric_squares_1.py 
Objective: Draw sets of squares all with the same center. 

Program name: rectangle_1.py 
Objective: A rectangle. 

Keywords: canvas, rectangle 
============================================================================79 
Comments: A rectangle is specified by two points: 
The top left corner (30, 30) and 
the bottom right (80, 120). Keywords: rectangle, square, concentric 
============================================================================79 
Comments: A square is just a rectangle with height equal to width. 
To place each square on the same center we use  some arithmetic using 
center and width/height values. 
This has an advantage, to seen later, of making each 'create_rectangle 
command identical. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3  
Author:          Mike Ohlson de Fine   
""" 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Concentric squares') 
cw = 200                                      # canvas width 
ch = 400                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=200, background="green") 
canvas_1.grid(row=0, column=1) 

# dark blue 
x_center = 100 
y_center = 100 
x_width  = 100 
y_height = 100 
kula = "darkblue" 
canvas_1.create_rectangle( x_center - x_width/2,  y_center - y_height/2,  x_center + x_width/2,  y_center + y_height/2, fill=kula) 

#dark red 
x_width  = 80 
y_height = 80 
kula ="darkred" 
canvas_1.create_rectangle( x_center - x_width/2,  y_center - y_height/2,  x_center + x_width/2,  y_center + y_height/2, fill=kula) 

#dark green 
x_width  = 60 
y_height = 60 
kula ="darkgreen" 
canvas_1.create_rectangle( x_center - x_width/2,  y_center - y_height/2,  x_center + x_width/2,  y_center + y_height/2, fill=kula) 

root.mainloop()
