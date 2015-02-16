""" ch1 No.8 
Program name: smoothed_lines_splinesteps_1.py 
Objective: Draw a family of lines with a progressive smoothness. 

Keywords: canvas, bent line, curve, splinesteps, smooth line 
============================================================================79 
Comments: The amount of smoothness in the curve is determined 
by the number of spline steps. High numbers give a smoother curve. 
In this example we vary the number of segments in the smoothed curve. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3    
Author:    Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Smoothed lines. Various splinesteps.') 
cw = 450                                     # canvas width 
ch = 250                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

offset = 0.0 
x1 = 250+offset 
y1 = 20 
x2 = 30+offset 
y2 = 120 
x3 = 250+offset 
y3 = 220 
my_line = [ x1, y1, x2, y2, x3, y3 ] 

canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="false") 
offset += 20.0 
x1, x2, x3 = 250+offset, 30+offset, 250+offset 
canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="true", splinesteps = 3) 
offset += 20.0 
x1, x2, x3 = 250+offset, 30+offset, 250+offset 
my_line = [ x1, y1, x2, y2, x3, y3 ] 
canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="true", splinesteps = 5) 
offset += 20.0 
x1, x2, x3 = 250+offset, 30+offset, 250+offset 
my_line = [ x1, y1, x2, y2, x3, y3 ] 
canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="true", splinesteps = 7) 
offset += 20.0 
x1, x2, x3 = 250+offset, 30+offset, 250+offset 
my_line = [ x1, y1, x2, y2, x3, y3 ] 
canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="true", splinesteps = 9) 
offset += 20.0 
x1, x2, x3 = 250+offset, 30+offset, 250+offset 
my_line = [ x1, y1, x2, y2, x3, y3 ] 
canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="true", splinesteps = 11) 
offset += 20.0 
x1, x2, x3 = 250+offset, 30+offset, 250+offset 
my_line = [ x1, y1, x2, y2, x3, y3 ] 
canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="true", splinesteps = 20) 
offset += 20.0 
x1, x2, x3 = 250+offset, 30+offset, 250+offset 
my_line = [ x1, y1, x2, y2, x3, y3 ] 
canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="true", splinesteps = 12) 
offset += 2.0 
x1, x2, x3 = 250+offset, 30+offset, 250+offset 
my_line = [ x1, y1, x2, y2, x3, y3 ] 
canvas_1.create_line(x1,y1,  x2,y2,  x3,y3, smooth="true", fill='red') 
  
root.mainloop() 
