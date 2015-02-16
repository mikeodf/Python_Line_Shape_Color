""" ch3 No.11  
Program name: rainbow_1.py 
Objective: Draw a rainbow. 

Keywords: canvas, rainbow, color, rotation. 
============================================================================79 
Comments: A general purpose shape rotation function is used. The shape in 
this case is a straight line segment.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher. 
from copy import * 
from copy import * 
import math 
root = Tk() 
root.title("Rainbow.") 
canvas_1 = Canvas(root, width=800, height=450, background="#000000") 
canvas_1.grid(row=0, column=1) 

def rotate_shape(shape, xy_center, angle_degrees): 
    """ Rotate any shape about a center point xy_center. 
    """ 
    angle_rad = math.radians(angle_degrees) 
    x_cen = xy_center[0] 
    y_cen = xy_center[1] 
    new_shape = [] 
        for i in range(int(len(shape)/2) ):  
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

kulas_1 = ['#550000', '#aa0000', '#ff0000','#ffff00', '#00ff00', '#00ffff', '#0000ff', '#ff00ff','#660066', '#330044'] 
kulas_2 = ['#440000', '#ff0000','#000000','#ffff00','#000000', '#00ff00','#000000', '#00ffff','#000000', '#0000ff','#000000', '#ff00ff','#440044'] 

line_1 = [20,420,   25,420,    32,420, 40,420,   50,420,    60,420,  70,420,  80,420,  88,420, 94,420,   100,420,    104,420] 
line_2 = [160,420,  165,420,  170,420, 175,420,  180,420, 185,420,   190,420, 195,420, 200,420, 205,420, 210,420, 215,420, 220,420, 225,420, 230,420  , 235,420 ] 

xy_center = 400.0, 420.0 
for j in range(10): 
    line_a = line_1[2*j], line_1[2*j+1], line_1[2*j+2], line_1[2*j+3] 
    for i in range(720): 
        new_shape = rotate_shape(line_a, xy_center, 0.25*i ) 
        canvas_1.create_line(new_shape, fill=kulas_1[j], width=3 ) 

for j in range(12): 
    line_b = line_2[2*j], line_2[2*j+1], line_2[2*j+2], line_2[2*j+3] 
    for i in range(360): 
        new_shape = rotate_shape(line_b, xy_center, 0.5*i ) 
        canvas_1.create_line(new_shape, fill=kulas_2[j], width=1 ) 


root.mainloop()
