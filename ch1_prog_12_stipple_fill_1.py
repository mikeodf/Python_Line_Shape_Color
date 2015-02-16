""" ch1 No.12  
Program name: stipple_fill_1.py 
Objective: Make semi-transparent objects using stipple filling. 
Stipplebrush: stipple values: "gray12", "gray25", "gray50", or "gray75 

Keywords: canvas, rectangles, overlapp, stipple fill 
============================================================================79 
Comments: Overlapping rectangles are placed down on the canvas in the 
same sequence that they appear in the code. With stipple filling this does have an influence on the 
final impression of color. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Stipple filling') 

cw = 300                                      # canvas width 
ch = 300                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1) 

# Dark purple rectangle - painted first therefore at the bottom. 
x_start = 10 
y_start = 30 
x_width =100 
y_height = 100 
kula ="purple" 
canvas_1.create_rectangle( x_start,  y_start,
                          x_start + x_width, y_start + y_height, 
                          fill=kula, stipple = "gray12") 

# Dark red rectangle - second therefore in the middle. 
x_start = 60 
y_start = 80 
kula ="darkred" 
canvas_1.create_rectangle( x_start,  y_start, 
                          x_start + x_width, y_start + y_height, 
                          fill=kula, stipple = "gray25") 

# Dark green rectangle - painted last therefore on top of previous ones. 
x_start = 110 
y_start = 130 
kula ="darkgreen" 
canvas_1.create_rectangle( x_start,  y_start, 
                          x_start + x_width, y_start + y_height, 
                          fill=kula, stipple = "gray50") 

# Dark blue  rectangle - painted last therefore on top of previous ones. 
x_start = 160 
y_start = 180 

kula ="darkblue" 
canvas_1.create_rectangle( x_start,  y_start, 
                          x_start + x_width, y_start + y_height, 
                          fill=kula, stipple = "gray75") 
root.mainloop()
