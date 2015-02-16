""" ch5 No.1 
Program name: line_parameters_1.py 
Objective: Calculate the slope and intercept parameters of straight lines. 
Prove the calculations are correct. 

Keywords: polygons, line, slope, intercept, prove 
============================================================================79 
Comments: 
                                                                                      
Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author: Mike Ohlson de Fine      
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title(" Calculate line slope and intercept.") 
cw = 380                                     # canvas width 
ch = 200                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="#000088") 
canvas_1.grid(row=0, column=1)                              

line_1 = [ 30.0, 140.0, 130.0, 30.0] 
line_2 = [ 90.0, 120.0, 150.0, 180.0] 


def get_line_params(line): 
    """ Calculate straight line parameters from two given points (ie line as a segment). 
        The returned 'line' is in the form of slope and intercept and the segment coordinates. 
    """ 
    x1 = line[0] 
    y1 = line[1] 
    x2 = line[2] 
    y2 = line[3] 
    delt_y = y2 - y1 
    delt_x = x2 - x1 
    slope = delt_y/delt_x 
    intercept = y1 - slope * x1 
    return [slope, intercept, x1, y1, x2, y2] 

def prove_line(x1, x2, line_n): 
    """ A test and development utility. 
        Verify that 'get_line_params' gives the correct slope and y-axis intercept. 
        x1, x2 are the x-coordinates of the line segment to be shown. 
    """ 
    y1 = line_n[0] * x1 + line_n[1] 
    y2 = line_n[0] * x2 + line_n[1] 
    canvas_1.create_line(x1, y1, x2, y2,  fill='orange', width =6) 

canvas_1.create_line(line_1,  fill='green', width = 3) 
canvas_1.create_line(line_2,  fill='grey', width = 3) 

line_a = get_line_params(line_1) 
prove_line(50, 100, line_a) 
line_b = get_line_params(line_2) 
prove_line(50, 100, line_b) 

root.mainloop() 
