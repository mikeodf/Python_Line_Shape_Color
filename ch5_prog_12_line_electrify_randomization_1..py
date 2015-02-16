""" ch5 No.12 
Program name:  line_electrify_randomization_1.py 
Objective: Add random components to line segments. 
Test edge conditions. 

Keywords: line, random, edge cases. 
============================================================================79 
Comments:                        

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author: Mike Ohlson de Fine    
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher. 
from random import * 
import math 
root = Tk() 
root.title(" Electrify the Line.") 
cw = 600                                     # canvas width 
ch = 300                                     # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)       

def rotate_shape(shape, xy_center, angle_rad): 
    """ Rotate any shape about a center point xy_center. ( ?????????????????????????? )
    """ 
    #angle_rad = math.radians(angle_degrees) 
    x_cen = xy_center[0] 
    y_cen = xy_center[1] 
    new_shape = [] 
    for i in range(int(len(shape)/2 )): 
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

def make_horizontal(segment): 
    """ Rotate to the horizontal. 
         Detect if a line is positive going right ( direction = 1), 
         negative going left ( direction = -1) or if slope is infinite. 
         The atan2() function should take care of verticals. 
    """ 
    x1 = segment[0] 
    y1 = segment[1] 
    x2 = segment[2] 
    y2 = segment[3] 
    delt_y = y2-y1 
    delt_x = x2-x1 
    if delt_x > 0:         # Normal - x increasing, slope.
        x_direction = 1 
    if delt_x < 0:         # Negative moving line.
        x_direction = -1 
    if delt_x == 0:        # Vertical line, slope infinite. 
        x_direction = 0   
    angle = math.atan2(delt_y, delt_x)   # Angle to make line horizontal. 
    length = math.sqrt(delt_y**2 + delt_x**2) 
    return   length, angle, x_direction   

def line_randomize_vertical(xy_line, x_direction, x_delta, standard_deviation): 
    """ Draw a segmented line with randomized vertical component 
        added. 
    """ 
    going_positive = 1 
    if xy_line[2] < xy_line[0]:  # Negative going line. 
        going_positive = -1 
    if xy_line[2] > xy_line[0]:  # Normal positive going line. 
        going_positive = 1 

    num_steps = int(going_positive * (xy_line[2] - xy_line[0])/x_delta)  # A positive number. 
    xy_list = [] 
    for i in range(num_steps): 
        y_randomized = xy_line[1] + gauss(mean, standard_deviation)     
        x_next = xy_line[0] + going_positive * x_direction * i * x_delta 
        xy_list.append(x_next) 
        xy_list.append(y_randomized)   
    return xy_list 

def electrocute_line(xy_line): 
    """ Add a vertical (normal) component of random noise to a line segment. 
    """ 
    canvas_1.create_line(xy_line, fill='gray') 
    length, angle, x_direction  = make_horizontal(xy_line)                  # Horizontalization parameters. 
    temp_line = [xy_line[0], xy_line[1], xy_line[0] + x_direction * length,  xy_line[1]] # Pure horizontal line 
    canvas_1.create_line(temp_line, fill=kula) 
    temp_line = line_randomize_vertical(temp_line, x_direction, x_delta, standard_deviation) 
    xy_center = [ xy_line[0], xy_line[1] ] 
    temp_line = rotate_shape(temp_line, xy_center, angle) 
    canvas_1.create_line(temp_line, fill=kula) 

# Execute and Demonstrate. 
# ========================== 

# Edge case test lines. 
diagonal_rising_right = [ 50.0,150.0 , 150.0,50.0 ] 
diagonal_dropping_left= [ 300.0,100.0 , 100.0,250.0 ] 
horizontal_line = [ 400.0,100.0 , 550.0,100.0  ] 
vertical_line = [ 350.0,50.0 , 350.0,250.0  ] 

# Randomization parameters. 
mean = 1.0 
standard_deviation = 10.0 
x_delta = 1.0       # If this is smaller than the length of a line there are not enough randomized points to plot. 
''' Problem Alert! Still to be solved: What if a point is repeated?  There should be a 'hedge' in the code: 
    Skip over the repeated point or take some other suitable measure. 
''' 
#Original and electrified/noisified lines. 
kula = '#00dd00' 
canvas_1.create_line( diagonal_rising_right, width=2, fill='#00dd00') # Positive slope. 
electrocute_line( diagonal_rising_right)                                               

kula = 'red' 
canvas_1.create_line( diagonal_dropping_left, width=2, fill='red')     # Negative slope. 
electrocute_line(diagonal_dropping_left)                          
canvas_1.create_line( vertical_line, width=2, fill='red')                        # Infinite  slope. 
electrocute_line( vertical_line)                                

kula = 'blue' 
canvas_1.create_line( horizontal_line,width=2, fill='blue')                   # Zero slope. 
electrocute_line(horizontal_line)                            

root.mainloop() 


def electrocute_shape(shape): 
    """ Add a vertical (normal) component of random noise to each line segment 
        of a polygon shape. 
    """
    for i in range(int(len(shape)/2 -1)): 
        xy_line = [ shape[2 *i],  shape[2 *i+1], shape[2 *i+2], shape[2 *i+3] ] 
        length, angle, x_direction  = make_horizontal(xy_line)                  # Horizontalization parameters. 
        temp_line = [xy_line[0], xy_line[1], xy_line[0] + x_direction * length,  xy_line[1]] # Pure horizontal line 
        temp_line = line_randomize_vertical(temp_line, x_direction, x_delta, standard_deviation) 
        if len(temp_line) <= 2: 
            temp_line = [ temp_line[0], temp_line[1],  temp_line[0]+1, temp_line[1] ] # Hedge for x_delta too small. 
        # Rotate back to original position. 
        xy_center = [ xy_line[0], xy_line[1] ] 
        temp_line = rotate_shape(temp_line, xy_center, angle) 
        canvas_1.create_line(temp_line, fill=kula)



# Execute and Demonstrate. 
# ========================== 

# Edge case test lines. 
# Closed hexagon 
hexagon_1 =[ 402.0, 201.0, 303.0, 243.0, 301.0, 363.0, 400.0, 401.0, 504.0, 362.0, 501.0, 241.0, 402.0, 201.0] 

# Curl with pure horizontals and verticals. 
electra_1 = [ 80,112.3 , 160,52.3 , 260,52.3 , 320,112.3 , 320,192.3 , 260,252.3 , 160,252.36218 , 120,212.3 , 120,132.3 , 180,92.3 , 240,92.3 , 280,132.3 ] 

# Curl no horizontals or veticals. 
electra_2 = [80,132.36218 , 120,72.362183 , 200,52.362183 , 280,72.362183 , 320,152.36218 , 300,212.36218 , 260,252.36218 , 200,272.36218 , 140,252.36218 , 100,192.36218 , 140,132.36218 , 200,112.36218 ] 

# Randomization parameters. 
mean = 1.0 
standard_deviation = 6.0 
x_delta = 1.0           # If this is smaller than the length of a line there are not enough randomized points to plot. 
''' Problem Alert! Still to be solved: What if a point is repeated?  There should be a 'hedge' in the code: 
    Skip over the repeated point or take some other suitable measure. 
''' 
kula = '#0044cc' 
electrocute_shape(hexagon_1) 
canvas_1.create_line(hexagon_1, width=3, fill=kula) 
kula = '#00dd00' 
electrocute_shape(electra_1) 
canvas_1.create_line(electra_1, width=3, fill=kula) 
kula = '#ff4400' 
electrocute_shape(electra_2) 
canvas_1.create_line(electra_2, width=3, fill=kula) 
