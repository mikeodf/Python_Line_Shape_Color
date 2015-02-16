""" ch5 No.6 
Program name: line_randomize_1.py 
Objective: Draw two segmented sets of lines with a confined but random (Gaussean)components. 

Keywords: random vertical, distribution 
============================================================================79 
Comments:  We draw a set of segmented line with partially random 
vertical components using the function line_randomize_vertical(...). 
 We also draw a set of segmented line with partially random vertical 
as well as horizontal components using the function line_randomize_xy(...). 

A gaussean random distribution is used. 
                                                 
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author: Mike Ohlson de Fine     
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
from random import * 

root = Tk() 
root.title(" Randomize lines.") 
cw = 750                                     # canvas width 
ch = 500                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 
 
def line_randomize_vertical(xy_line, x_delta, standard_deviation): 
    """ Draw a segmented line with randomized vertical component 
        added. 
    """ 
    num_steps = int((xy_line[2] - xy_line[0])/x_delta) 
    xy_list = [] 
    for i in range(num_steps): 
        y_randomized = xy_line[1] + gauss(mean, standard_deviation)     
        x_next = xy_line[0] + i * x_delta 
        xy_list.append(x_next) 
        xy_list.append(y_randomized) 
    canvas_1.create_line(xy_list, width = 3) 

def line_randomize_xy(xy_line, x_delta, standard_deviation): 
    """ Draw a segmented line with randomized vertical component 
        added. 
    """ 
    num_steps = int((xy_line[2] - xy_line[0])/x_delta) 
    xy_list = [] line_randomize_1.py 
    for i in range(num_steps): 
        y_randomized = xy_line[1] + gauss(mean, standard_deviation)     
        x_randomized  = xy_line[0] + i * x_delta + gauss(mean, standard_deviation) 
        xy_list.append(x_randomized) 
        xy_list.append(y_randomized) 
    canvas_1.create_line(xy_list, width = 3) 
 

# Execute and Demonstrate. 
# ========================== 
x_delta = 2.0 
mean = 1.0 
standard_deviation = 2.0 
xy_line = 100.0, 50.0, 300.0, 50.0 
line_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 4.0 
xy_line = 100.0, 100.0, 300.0, 100.0 
line_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 6.0 
xy_line = 100.0, 150.0, 300.0, 150.0 
line_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 8.0 
xy_line = 100.0, 200.0, 300.0, 200.0 
line_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 10.0 
xy_line = 100.0, 250.0, 300.0, 250.0 
line_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 12.0 
xy_line = 100.0, 320.0, 300.0, 320.0 
line_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 16.0 
xy_line = 100.0, 400.0, 300.0, 400.0 
line_randomize_vertical(xy_line, x_delta, standard_deviation) 

standard_deviation = 2.0 
xy_line = 500.0, 50.0, 700.0, 50.0 
line_randomize_xy(xy_line, x_delta, standard_deviation) 
standard_deviation = 4.0 
xy_line = 500.0, 100.0, 700.0, 100.0 
line_randomize_xy(xy_line, x_delta, standard_deviation) 
standard_deviation = 6.0 
xy_line = 500.0, 150.0, 700.0, 150.0 
line_randomize_xy(xy_line, x_delta, standard_deviation) 
standard_deviation = 8.0 
xy_line = 500.0, 200.0, 700.0, 200.0 
line_randomize_xy(xy_line, x_delta, standard_deviation) 
standard_deviation = 10.0 
xy_line = 500.0, 250.0, 700.0, 250.0 
line_randomize_xy(xy_line, x_delta, standard_deviation) 
standard_deviation = 12.0 
xy_line = 500.0, 320.0, 700.0, 320.0 
line_randomize_xy(xy_line, x_delta, standard_deviation) 
standard_deviation = 16.0 
xy_line = 500.0, 400.0, 700.0, 400.0 
line_randomize_xy(xy_line, x_delta, standard_deviation) 

root.mainloop() 
