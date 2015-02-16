""" ch5 No.11 
Program name: daisywheel_randomization_1.py 
Objective: Add jagged random component to lines radiating from a center. 

Keywords: line, radial, daisy-wheel, jagged, random, chaotic. 
============================================================================79 
Comments: 
A Straight line between two points has a random 'wobble' added to it. 
To confine the randomness to being deviations on either side of the line 
without overlap or looping a strategy or rotation to the x-axis, 
randomization and restore the rotation was used. 
                                                                                      
Tested on: Python 2.6, 
Author: Mike Ohlson de Fine    
   
""" 

# Execute and Demonstrate. 
# ========================== 
mean = 1.0 
std_dev = 0.5 
factor = 9.0 
num_steps = 32 
kula = 'red' 
diameter = 2 
angle_degrees = 2.0 

factor = 10 
kula = '#888800'  # Dark yellow. 
xy_line = [200.0, 200.0, 350.0, 200.0] 
xy_center = xy_line[0], xy_line[1] 
xy_list = gauss_y_scatter(xy_line, mean, std_dev, num_steps, factor) 
for j in range(180): 
    xy_list = rotate_shape(xy_list, xy_center, angle_degrees) 
    canvas_1.create_line(xy_list, fill=kula, smooth=0, width = 1) 

factor = 12 
kula = 'red' 
xy_line = [400.0, 230.0, 600.0, 200.0] 
xy_center = xy_line[0], xy_line[1] 
xy_list = gauss_y_scatter(xy_line, mean, std_dev, num_steps, factor) 
for j in range(180): 
    xy_list = rotate_shape(xy_list, xy_center, angle_degrees) 
    canvas_1.create_line(xy_list, fill=kula, smooth=0, width = 1) 

factor = 15 
kula = '#00dd00' 
xy_line = [300.0, 350.0, 500.0, 300.0] 
xy_center = xy_line[0], xy_line[1] 
xy_list = gauss_y_scatter(xy_line, mean, std_dev, num_steps, factor)  
for j in range(180): 
    xy_list = rotate_shape(xy_list, xy_center, angle_degrees) 
    canvas_1.create_line(xy_list, fill=kula, smooth=0, width = 1) 

root.mainloop() 
