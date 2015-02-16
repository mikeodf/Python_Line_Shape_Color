""" ch1 No.3
Program name: line_styles_1.py 
Objective: Four straight lines, different styles on a canvas. 

Keywords: canvas, line, , color, dashed line, default 
============================================================================79 
Comments: When drawing lines you MUST specify the start and end points. 
Different colors, line widths and styles have been used here. 
Variable names are used instead of numerical values. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3         
Author:    Mike Ohlson de Fine 
""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Variations in line options')
cw = 500                                     # canvas width 
ch = 200                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="pink") 
canvas_1.grid(row=0, column=1) 

x_start = 10 
y_start = 10 
x_end = 400 
y_end = 20 
canvas_1.create_line(x_start, y_start, x_end, y_end, dash=(3,5), width = 3) 
  
x_start= x_end 
y_start= y_end 
x_end= 10 
y_end= 180 
canvas_1.create_line(x_start, y_start, x_end, y_end, dash=(9,), width = 5, fill= "red") 

y_end= 150 
canvas_1.create_line(x_start, y_start, x_end, y_end, dash=(19,),width= 10, fill= 'yellow')    

y_start= 0 
# If not explicitly specified line style reverts to default width = 1, 
# and default color = 'black'. 
canvas_1.create_line(x_start, y_start, x_end,y_end)     

root.mainloop() 
