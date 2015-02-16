""" ch1 No.2 
Program name: dashed_line_1.py 
Objective: Draw some straight dashed lines on a canvas. 

Keywords: canvas, line, , dashed line, default 
============================================================================79 
Comments: Start and end points need to be specified explicitly. 
Here we also specify three dashed lines as follows: 
Firstly line: Dashed with one solid pixels followed by 11 blank pixels. 
Repeated till the end of the line is reached. 
The second line has 2 solid pixels followed by 10 blank. 
The third line has four solid black followed by 8 blank. 
In all cases the total pixels in each repeated pattern is 12 pixels. 

Here variable names are used instead of numerical values. 
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3         
Author:          Mike Ohlson de Fine 
""" 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Dashed lines')

cw = 500                                      # canvas width 
ch = 200                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch) 
canvas_1.grid(row=0, column=1) 

x_start = 10 
y_start = 20 
x_end = 400 
y_end = 20 
canvas_1.create_line(x_start, y_start, x_end,y_end, dash=(1,11), width = 3) 
y_end += 40
canvas_1.create_line(x_start, y_start+4, x_end,y_end+4, dash=(2,10), width = 4) 
y_end += 40
canvas_1.create_line(x_start, y_start+8, x_end,y_end+8, dash=(4,8), width = 5) 

root.mainloop()
