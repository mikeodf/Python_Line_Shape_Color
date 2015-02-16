""" ch5 No.9 
Program name: line_rotation_randomization_1.py 
Objective: Add random components to a line between two points and then 
rotate the line through a full circle. 

Keywords: line, random, chaotic. 
============================================================================79 
Comments:A Straight line between two points has a random 'wobble' added to it. 
Two styles of randomization are used. The leftmost is random in both 
vertical and horizontal components. The rightmost is only random in the 
vertical component. 
                                                                                      
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author: Mike Ohlson de Fine    
   
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
from random import * 
import math 
root = Tk() 
root.title(" Dandilions from chaos") 
cw = 1000                                   # canvas width 
ch = 600                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1)       

def rotate_shape(shape, xy_center, angle_degrees): 
    """ Rotate any shape about a cetner point xy_center. 
    """ 
    angle_rad = math.radians(angle_degrees) 
    x_cen = xy_center[0] 
    y_cen = xy_center[1] 
    new_shape = [] 
    for i in range(len(shape)/2 ): 
        x_temp = shape[2*i]  - x_cen 
        y_temp = shape[2*i+1] - y_cen 
        radian_temp  = math.atan2(y_temp, x_temp ) 
        length_temp = math.sqrt( y_temp**2 + x_temp**2) 
        new_angle = angle_rad + radian_temp 
        new_x = length_temp * math.cos(new_angle) + x_cen 
        new_y = length_temp * math.sin(new_angle) + y_cen 
        new_shape.append(new_x) 
        new_shape.append(new_y)    
    return   new_shape   # angle_deg = post rotation angle                       

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
    return xy_list 

def line_randomize_xy(xy_line, x_delta, standard_deviation): 
    """ Draw a segmented line with randomized vertical component 
        added. 
    """ 
    num_steps = int((xy_line[2] - xy_line[0])/x_delta) 
    xy_list = [] 
    for i in range(num_steps): 
        y_randomized = xy_line[1] + gauss(mean, standard_deviation)     
        x_randomized  = xy_line[0] + i * x_delta + gauss(mean, standard_deviation) 
        xy_list.append(x_randomized) 
        xy_list.append(y_randomized) 
    return xy_list 

# Execute and Demonstrate. 
# ========================== 
mean = 1.0 
standard_deviation = 6.0 
x_delta = 5.0 
angle_degrees = 6.0 

kula = '#ff8800' 
xy_line = [250.0, 300.0, 450.0, 300.0]   # The Seed line for randomization.
xy_center = xy_line[0], xy_line[1] 

for j in range(60): 
    # Orange flower. Random in both x and y 
    xy_list = line_randomize_xy(xy_line, x_delta, standard_deviation) 
    xy_list = rotate_shape(xy_list, xy_center, angle_degrees*j) 
    canvas_1.create_line(xy_list, smooth = 1, fill=kula, width = 2) 
    x_tip = xy_list[len(xy_list)-2] 
    y_tip = xy_list[len(xy_list)-1] 
    canvas_1.create_oval(x_tip -6, y_tip -6,x_tip +6, y_tip +6, fill='#ff6600',  outline= '#ff4400',width = 3) 

kula = '#0088ff' 
xy_line = [700.0, 300.0, 900.0, 300.0]   # The Seed line for randomization.
xy_center = xy_line[0], xy_line[1] 

for j in range(60): 
    # Blue Flower. Random in y component only 
    xy_list = line_randomize_vertical(xy_line, x_delta, standard_deviation) 
    xy_list = rotate_shape(xy_list, xy_center, angle_degrees*j) 
    canvas_1.create_line(xy_list, smooth = 1, fill=kula, width = 2) 
    x_tip = xy_list[len(xy_list)-2] 
    y_tip = xy_list[len(xy_list)-1] 
    canvas_1.create_oval(x_tip -7, y_tip -7,x_tip +7, y_tip +7, fill='#0066ff',  outline= '#0044ff',width = 3) 

root.mainloop() 
