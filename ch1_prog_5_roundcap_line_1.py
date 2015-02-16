""" ch1 No.5 
Program name: roundcap_line_1.py 
Objective: Draw straight with rounded ends. 

Keywords: canvas, line, , arrowed line, default 
============================================================================79 
Comments: You specify capstyle=ROUND.
The rounded bit is at both start and finish of the line. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3  
Author:  Mike Ohlson de Fine 
""" 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('ROUND end caps on lines') 
cw = 450                                     # canvas width 
ch = 130                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch) 
canvas_1.grid(row=0, column=1) 

x_start = 30 
y_start = 20 
x_end = 400 
y_end = 20 
canvas_1.create_line(x_start, y_start,    x_end,y_end,          capstyle= ROUND, width = 1) 
canvas_1.create_line(x_start, y_start+10, x_end,y_end+10, capstyle= ROUND,  width = 4) 
canvas_1.create_line(x_start, y_start+20, x_end,y_end+20, capstyle= ROUND,  width = 8) 
canvas_1.create_line(x_start, y_start+36, x_end,y_end+36, capstyle= ROUND,  width = 16) 
canvas_1.create_line(x_start, y_start+66, x_end,y_end+66, capstyle= ROUND,  width = 32) 
root.mainloop() 
