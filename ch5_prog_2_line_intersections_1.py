""" ch5 No.2 
Program name: line_intersections_1.py 
Objective: Calculate the point of intersection of four straight lines. 
Indicate the intersections with circles. 

Keywords: polygons, line, intersections, intercepts, parallel 
============================================================================79 
Comments: 
                                                                                      
Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author: Mike Ohlson de Fine    
   
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title(" Intersections of four lines.") 
cw = 350                                     # canvas width 
ch = 300                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="#000044") 
canvas_1.grid(row=0, column=1)                              

line_1 = [ 30.0, 140.0, 130.0, 30.0] 
line_2 = [ 90.0, 120.0, 150.0, 180.0] 
line_3 = [ 110.0, 180.0, 120.0, 20.0] 
line_4 = [ 180.0, 140.0, 280.0, 30.0] 


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

def line_intersection(line_1, line_2): 
   """ Specify lines by their start and end positions. 
       Returned: The x, y location of the intercept point. 
   """ 
   line_a = get_line_params(line_1)  # Translate from start and end coordinates to linear equation. 
   line_b = get_line_params(line_2)  # Translate from start and end coordinates to linear equation. 
   # x_intercept = (intercept2-intercept1)/(slope1-slope2) 
   if (line_a[0] - line_b[0]) == 0: 
       print " Paralell lines may never connect." 
       lines_parallel = 1 
       return 0, 0, lines_parallel     # Parallel case. "lines_parallel" flag goes up.
   else: 
       x_intercept = (line_b[1] - line_a[1]) / (line_a[0] - line_b[0]) 
       y_intercept = x_intercept * line_a[0] + line_a[1] 
       lines_parallel = 0 
       return x_intercept, y_intercept, lines_parallel 

# Test each possibility. 
# ====================== 
canvas_1.create_line(line_1,  fill='green', width = 3) 
canvas_1.create_line(line_2,  fill='grey', width = 3) 
canvas_1.create_line(line_3,  fill='orange', width = 3) 
canvas_1.create_line(line_4,  fill='white', width = 3) 

xy = line_intersection(line_1, line_2) 
if xy[2] == 0: 
    canvas_1.create_oval(xy[0]-8, xy[1]-8,  xy[0]+8, xy[1]+8, outline = 'yellow', width = 3) 
xy = line_intersection(line_1, line_3) 
if xy[2] == 0: 
    canvas_1.create_oval(xy[0]-8, xy[1]-8,  xy[0]+8, xy[1]+8, outline = 'red', width = 3) 
xy = line_intersection(line_3, line_2) 
if xy[2] == 0: 
    canvas_1.create_oval(xy[0]-8, xy[1]-8,  xy[0]+8, xy[1]+8, outline = 'purple', width = 3) 
xy = line_intersection(line_4, line_3) 
if xy[2] == 0: 
    canvas_1.create_oval(xy[0]-8, xy[1]-8,  xy[0]+8, xy[1]+8, outline = 'yellow', width = 3) 
xy = line_intersection(line_4, line_2) 
if xy[2] == 0: 
    canvas_1.create_oval(xy[0]-8, xy[1]-8,  xy[0]+8, xy[1]+8, outline = 'yellow', width = 3) 
xy = line_intersection(line_1, line_4) 
if xy[2] == 0: 
    canvas_1.create_oval(xy[0]-8, xy[1]-8,  xy[0]+8, xy[1]+8, outline = 'yellow', width = 3) 

root.mainloop() 
