""" ch5 No.8 
Program name: bubbles_randomize_1.py 
Objective: Draw a random scattering of randomly sized circles between two points. 

Keywords: random vertical, random horizontal, spots, gaussean distribution 
============================================================================79 
Comments:  We want draw a set of circular spots line with random radii (size) 
as well as vertical position components. 
                                                 
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author: Mike Ohlson de Fine     
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
from random import * 

root = Tk() 
root.title(" Randomize bubbles.") 
cw = 500                                     # canvas width 
ch = 500                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1) 

def spot_randomize_vertical(xy_line, x_delta, standard_deviation): 
    """ Draw a segmented line with randomized vertical component 
        added. 
    """ 
   num_steps = int((xy_line[2] - xy_line[0])/x_delta) 
    for i in range(num_steps): 
        radius = gauss(mean, standard_deviation) 
        y_randomized = xy_line[1] + gauss(mean, standard_deviation)     
        x_next = xy_line[0] + i * x_delta 
        canvas_1.create_oval(x_next-radius,  y_randomized-radius, x_next+3,  y_randomized+3) 


# Execute and Demonstrate. 
# ========================== 
x_delta = 2.0 
mean = 1.0 
standard_deviation = 2.0 
xy_line = 50.0, 50.0, 300.0, 50.0  # The Seed line for randomization.
spot_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 4.0 
xy_line = 50.0, 100.0, 300.0, 100.0 
spot_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 6.0 
xy_line = 50.0, 150.0, 300.0, 150.0 
spot_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 8.0 
xy_line = 50.0, 200.0, 300.0, 200.0 
spot_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 10.0 
xy_line = 50.0, 250.0, 300.0, 250.0 
spot_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 12.0 
xy_line = 50.0, 320.0, 300.0, 320.0 
spot_randomize_vertical(xy_line, x_delta, standard_deviation) 
standard_deviation = 16.0 
xy_line = 50.0, 400.0, 300.0, 400.0 
spot_randomize_vertical(xy_line, x_delta, standard_deviation) 

root.mainloop() 
