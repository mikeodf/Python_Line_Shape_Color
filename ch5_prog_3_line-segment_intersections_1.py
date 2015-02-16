""" ch5 No.3 
Program name: line-segment_intersections_1.py 
Objective: Calculate the point of intersection of four straight line-segments. 
Differentiate between internal and external intersections. 
Avoid parallel line errors. 

Keywords: polygons, line, intersections, intercepts, parallel 
============================================================================79 
Comments: 
                                                                                      
Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author: Mike Ohlson de Fine    
   
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title(" Intersections of four line-segments.") 
cw = 400                                     # canvas width 
ch = 250                                      # canvas height 
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
 
def inner_box(line_1, line_2): 
    """ Purpose: Provide coordinates of inner-bow within which an intersection point 
        should lie is the line segments intersect. 
        This function returns the coordinates of the inner box that would contain 
        the intersection of both line segments (if they intersected). 
        The lines are defined by their end points.        
    """ 
    x1 = line_1[0] 
    x2 = line_1[2] 
    x3 = line_2[0] 
    x4 = line_2[2] 
    y1 = line_1[1] 
    y2 = line_1[3] 
    y3 = line_2[1] 
    y4 = line_2[3] 
    x_list = sorted([x1,x2,x3,x4]) 
    y_list = sorted([y1,y2,y3,y4]) 
    inner_box = x_list[1],y_list[1], x_list[2], y_list[2] 
    return x_list, y_list 

def line_intersection(line_1, line_2): 
   """ Specify lines by their start and end positions. 
       Returned: The x, y location of the intercept point. 
   """ 
   line_a = get_line_params(line_1)  # Translate from start and end coordinates to linear equation. 
   line_b = get_line_params(line_2)  # Translate from start and end coordinates to linear equation. 
   # x_intercept = (intercept2-intercept1)/(slope1-slope2) 
   if (line_a[0] - line_b[0]) == 0: 
       print " Paralell lines may never connect." 
       #print( " Paralell lines may never connect." )
       lines_parallel = 1 
       return 0, 0, lines_parallel  # Parallel case. Raise "lines_parallel" flag. 
   else: 
       x_intercept = (line_b[1] - line_a[1]) / (line_a[0] - line_b[0]) 
       y_intercept = x_intercept * line_a[0] + line_a[1] 
       lines_parallel = 0 
       return x_intercept, y_intercept, lines_parallel 

def inner_intersection(line_1, line_2): 
   """ Specify lines as slope=m and Y intercept c 
       Returned: The x, y location of the intercept point AND "seg_intersect". 
       If the segments do not intersect then "seg_intersect" = FALSE, otherwise TRUE. 
   """ 
   line_a = get_line_params(line_1)  # Translate from start and end coordinates to linear equation. 
   line_b = get_line_params(line_2)  # Translate from start and end coordinates to linear equation. 
   # x_intercept = (intercept2-intercept1)/(slope1-slope2) 
   if (line_a[0] - line_b[0]) == 0:   # Are the two lines parallel? 
       print " Paralell lines: ", line_1," and ", line_2 
       #print " Paralell lines: ", line_1," and ", line_2 
       lines_parallel = 1 
       return 0, 0, 0, lines_parallel  # Parallel case. Raise "lines_parallel" flag and exit function. 
   else:                               # Non-parallel case. 
       lines_parallel = 1      # Lower the “lines_parallel” flag.
       x_intercept = (line_b[1] - line_a[1]) / (line_a[0] - line_b[0]) 
       y_intercept = x_intercept * line_a[0] + line_a[1] 
       xy = x_intercept, y_intercept 
       # Is the intersection inside x components of each segment? Get the smallest rectangle. 
       xy_box = inner_box(line_1, line_2) 
       if (xy_box[0][1] <= x_intercept) and ( x_intercept <= xy_box[0][2]): 
           seg_intersect = TRUE     # Intersection of segments. 
           canvas_1.create_oval(xy[0]-9, xy[1]-9,  xy[0]+9, xy[1]+9, outline = 'red', width = 4) 
       else: 
           seg_intersect = FALSE      # Intersection is external to the segments. 
           canvas_1.create_oval(xy[0]-7, xy[1]-7,  xy[0]+7, xy[1]+7, outline = 'yellow', width = 2) 
       return x_intercept, y_intercept, seg_intersect, lines_parallel 

# Test each possibility. 
# ====================== 
canvas_1.create_line(line_1,  fill='green', width = 3) 
canvas_1.create_line(line_2,  fill='grey', width = 3) 
canvas_1.create_line(line_3,  fill='orange', width = 3) 
canvas_1.create_line(line_4,  fill='white', width = 3) 

xy = inner_intersection(line_1, line_2) 
xy = inner_intersection(line_1, line_3) 
xy = inner_intersection(line_3, line_2) 
xy = inner_intersection(line_4, line_3) 
xy = inner_intersection(line_4, line_2) 
xy = inner_intersection(line_1, line_4) 

root.mainloop() 
