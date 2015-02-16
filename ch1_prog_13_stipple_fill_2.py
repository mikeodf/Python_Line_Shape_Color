""" ch1 No.13  
Program name: stipple_fill_2.py 
Objective: Stipple filled rectangles with distinctive borders. 
Stipplebrush: stipple values: "gray12", "gray25", "gray50", or "gray75 

Keywords: canvas, rectangles, overlap, stipple fill, dashed outline 
============================================================================79 
Comments:Border color and width with stipple filling has a marked influence on the 
final impression of color. 

Tested on: Python 2.6, 
Author:          Mike Ohlson de Fine 
""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Stipple filling') 

cw = 320                                     # canvas width 
ch = 320                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1) 

# Dark purple rectangle - painted first therefore at the bottom 
x_start = 30 
y_start = 30 
x_width =100 
y_height = 100 
kula ="purple" 
canvas_1.create_rectangle( x_start,  y_start, 
                          x_start + x_width, y_start + y_height, 
                          fill=kula, outline= "darkred", width=4, stipple = "gray12") 

# Dark red rectangle - second therefore in the middle. 
x_start = 80 
y_start = 80 
kula ="darkred" 
canvas_1.create_rectangle( x_start,  y_start, 
                          x_start + x_width, y_start + y_height, 
                          fill=kula, outline= "darkgreen", width=12, stipple = "gray25") 

# Dark green rectangle - painted last therefore on top of previous ones. 
x_start = 130 
y_start = 130 
kula ="darkgreen" 
canvas_1.create_rectangle( x_start,  y_start, 
                          x_start + x_width, y_start + y_height, 
                          fill=kula, outline= "darkblue", width=16, stipple = "gray50") 

# Dark blue  rectangle - painted last therefore on top of previous ones. 
x_start = 180 
y_start = 180 

kula ="darkblue" 
canvas_1.create_rectangle( x_start,  y_start, 
                          x_start + x_width, y_start + y_height, 
                          fill=kula, outline= "purple", width=20, stipple = "gray75") 

# Dark purple rectangle - painted first therefore at the bottom. 
x_start = 180 
y_start = 30 
x_width =100 
y_height = 100 
kula ="purple" 
canvas_1.create_rectangle( x_start,  y_start, 
                          x_start + x_width, y_start + y_height,
                          fill=kula, outline= "red", width=4, dash=16, stipple = "gray12") 
root.mainloop() 
