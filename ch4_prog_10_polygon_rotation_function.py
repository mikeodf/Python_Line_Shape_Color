""" ch4 No.10 
The rotation function
"""
def rotate_shape(shape, xy_center, angle_degrees): 
    """ Rotate any shape about a cetner point xy_center. 
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

Execution and display of rotation code

xy_center = show_shape_metrics(python_1) 
for i in range(22): 
    rotate_python = rotate_shape(python_1, xy_center, i*5) 
    canvas_1.create_polygon(rotate_python, outline='red', fill='' ) 

xy_center = -100, -100 
for i in range(12): 
    rotate_python = rotate_shape(python_1, xy_center, i*1) 
    canvas_1.create_polygon(rotate_python, outline='green', fill='' ) 

xy_center = 10, 500 
for i in range(22): 
    rotate_python = rotate_shape(python_1, xy_center, i*2) 
    canvas_1.create_polygon(rotate_python, outline='yellow', fill='' ) 

canvas_1.create_polygon(python_1, outline='green',fill ='', width = 6 ) 
canvas_1.create_polygon(python_1, outline='#008800',fill ='', width = 2 )
