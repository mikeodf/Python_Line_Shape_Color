""" ch5 No.10 
Program name: line_rough_randomization_1.py 
Objective: Add jagged random components to a line between two points. 

Keywords: line, jagged, random, chaotic. 
============================================================================79 
Comments: A Straight line between two points has a random 'wobble' added to it. 
To confine the randomness to being deviations on either side of the line 
without overlap or looping a strategy or rotation to the x-axis, 
randomization and restore the rotation was used. 
                                                                                      
Tested on: Python 2.6, 
Author: Mike Ohlson de Fine    
   
""" 
from Tkinter import * 
from random import * 
import math 
root = Tk() 
root.title(" Dandilions from chaos") 
cw = 650                                     # canvas width 
ch = 600                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1)       

def rotate_shape(shape, xy_center, angle_degrees): 
    """ Rotate any shape about a center point xy_center. 
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


def gauss_y_scatter(xy_line, mean, std_dev, num_steps, factor): 
    """ Generate a list of points randomly scattered about a straight line. 
        xy_line are the start and end coordintes of the line and should be 
        given as floats. 
        Strategy: rotate line to the horizontal, create the scatter in y only, 
        rotate line back to original angle. 
    """ 
    xx = xy_line[2] - xy_line[0] 
    yy = xy_line[3] - xy_line[1] 
    len_1 = math.sqrt( xx*xx + yy*yy)  # Length of the line.
    alpha = math.atan2(yy,xx)                # Angle of line with the horizontal.

    # Generate the randomization. Assume the line is horizontal and of length len_1 
    x_delta = len_1/num_steps 
    xy_list = [xy_line[0] + factor* gauss(mean, std_dev), xy_line[1] + factor* gauss(mean, std_dev)] 
    for i in range(num_steps):                # Generate the list of horizontal randomize points. 
        y_rand =  factor* gauss(mean, std_dev) # random.gauss(mean, sigma) 
        x_progressive =  i * x_delta 
        beta = math.atan2(y_rand, x_progressive) 
        len_2 =  math.sqrt( x_progressive *x_progressive + y_rand * y_rand) 

        # Restore the horizontal randomized line to it's original position. 
        x_3 = xy_line[0] + len_2 * math.cos(alpha - beta) 
        y_3 = xy_line[1] + len_2 * math.sin(alpha - beta) 
        xy_list.append(x_3) 
        xy_list.append(y_3) 
    return xy_list 


# Execute and Demonstrate. 
# ========================== 
mean = 1.0 
std_dev = 0.5 
factor = 3 
num_steps = 20 
kula = 'red' 
diameter = 2 
angle_degrees = 4.0 

factor = 10 
kula = 'yellow' 
xy_line = [200.0, 200.0, 350.0, 200.0] 
xy_center = xy_line[0], xy_line[1] 

for j in range(90): 
    xy_list = rotate_shape(xy_line, xy_center, angle_degrees*j) 
    xy_list = gauss_y_scatter(xy_list, mean, std_dev, num_steps, factor) 
    canvas_1.create_line(xy_list, fill=kula, smooth=0, width = 2) 

factor = 12 
kula = 'red' 
xy_line = [400.0, 230.0, 600.0, 200.0]   # The Seed line for randomization.
xy_center = xy_line[0], xy_line[1] 

for j in range(90): 
    xy_list = rotate_shape(xy_line, xy_center, angle_degrees*j) 
    xy_list = gauss_y_scatter(xy_list, mean, std_dev, num_steps, factor) 
    canvas_1.create_line(xy_list, fill=kula, smooth=0, width = 2) 

factor = 15 
kula = 'green' 
xy_line = [300.0, 350.0, 500.0, 300.0]   # The Seed line for randomization.
xy_center = xy_line[0], xy_line[1] 

for j in range(90): 
    xy_list = rotate_shape(xy_line, xy_center, angle_degrees*j) 
    xy_list = gauss_y_scatter(xy_list, mean, std_dev, num_steps, factor) 
    canvas_1.create_line(xy_list, fill=kula, smooth=0, width = 2) 

root.mainloop() 
