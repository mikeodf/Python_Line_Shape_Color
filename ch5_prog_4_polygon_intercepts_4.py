""" ch5 No.4 
Program name: polygon_intercepts_4.py 
Objective: Draw the internal portion lines where they penetrate polygons. 

Keywords: polygons, line, intercepts, segments, polygons 
============================================================================79 
Comments: A polygon is made by joining a sequence of x-y points,                                              
with the last point automatically joined to the first by a line to close 
the polygon. 
                                                                                      
Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author: Mike Ohlson de Fine     
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title(" Lines of intersection inside an array of polygons") 
cw = 650                                     # canvas width 
ch = 650                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1)                              


poly_1 =[ 402.0, 201.0, 303.0, 243.0, 301.0, 363.0, 400.0, 401.0, 504.0, 362.0, 501.0, 241.0, 402.0, 201.0] 
poly_2 =[382.0, 103.0, 383.0, 184.0, 302.0, 219.0, 245.0, 176.0, 382.0, 103.0 ] 
poly_3 =[231.0, 210.0, 283.0, 241.0, 282.0, 362.0, 226.0, 392.0, 231.0, 210.0 ] 
poly_4 =[237.0, 413.0, 297.0, 384.0, 394.0, 421.0, 380.0, 495.0, 237.0, 413.0 ] 
poly_5 =[411.0, 498.0, 415.0, 421.0, 516.0, 385.0, 561.0, 425.0, 411.0, 498.0 ] 
poly_6 =[575.0, 395.0, 523.0, 360.0, 519.0, 241.0, 574.0, 196.0, 575.0, 395.0 ] 
poly_7 =[557.0, 181.0, 502.0, 224.0, 411.0, 184.0, 405.0, 99.0, 557.0, 181.0  ] 
sun_poly = [poly_1, poly_2, poly_3, poly_4,poly_5, poly_6, poly_7] 

line_1 = [ 15.0, 10.0, 600.0, 100.0] 
line_2 = [ 15.0, 10.0, 600.0, 200.0] 
line_3 = [ 15.0, 10.0, 600.0, 300.0] 
line_4 = [ 15.0, 10.0, 600.0, 400.0] 
line_5 = [ 15.0, 10.0, 600.0, 500.0] 
line_6 = [ 15.0, 10.0, 600.0, 600.0] 
line_7 = [ 15.0, 10.0, 500.0, 600.0] 
line_8 = [ 15.0, 10.0, 400.0, 600.0] 
line_9 = [ 15.0, 10.0, 300.0, 600.0] 
lines = [line_1, line_2, line_3, line_4, line_5 , line_6, line_7, line_8, line_9] 

 
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


def inner_intersection(line_1, line_2): 
   """ Specify lines as slope=m and Y intercept c 
       Returned: The x, y location of the intercept point AND "seg_intersect". 
       If the segments do not intersect then "seg_intersect" = FALSE, otherwise TRUE. 
   """ 
   line_a = get_line_params(line_1)  # Translate from start and end coordinates to linear equation. 
   line_b = get_line_params(line_2)  # Translate from start and end coordinates to linear equation. 
   # x_intercept = (intercept2-intercept1)/(slope1-slope2) 
   x_intercept = (line_b[1] - line_a[1]) / (line_a[0] - line_b[0]) 
   y_intercept = x_intercept * line_a[0] + line_a[1] 
   # Is the intersection inside x components of each segment? Get the smallest rectangle. 
   xy_box = inner_box(line_1, line_2) 
   if (xy_box[0][1] <= x_intercept) and ( x_intercept <= xy_box[0][2]): 
       seg_intersect = TRUE       
   else: 
       seg_intersect = FALSE      # Default assumption that intersection is external to the segments. 
   return x_intercept, y_intercept, seg_intersect 


def internal_segment(lines, polygons): 
    """  Draw segments of intersection where arrays of lines cut arrays of polygons. 
         The polygons could be other sets of lines ( ie not necessarily polygons). 
         
    """ 
    xy_intercepts = []  # The set of intersection points within each segment-internal box. 
    for i in range(0, len(polygons)/2-1): 
        line_temp = [polygons[2*i], polygons[2*i+1], polygons[2*i+2], polygons[2*i+3] ] 
        x, y, seg_intersect = inner_intersection(lines, line_temp) 
        if seg_intersect == 1: 
            xy_intercepts.append(x) 
            xy_intercepts.append(y) 
        if len(xy_intercepts)==4: 
            canvas_1.create_line(xy_intercepts,  fill='red', width =4) 

# Execute and Demonstrate. 
# ========================== 
for m in range(len(lines)): 
    canvas_1.create_line(lines,  fill='grey', width = 3) 
for n in range(len(sun_poly)): 
    canvas_1.create_line(sun_poly[n],  fill='green', width = 4) 

for i in range(len(lines)): 
    for j in range(len(sun_poly)): 
        internal_segment(lines[i], sun_poly[j]) 

root.mainloop()
