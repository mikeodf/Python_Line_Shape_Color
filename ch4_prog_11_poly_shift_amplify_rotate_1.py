""" ch4 No.11 
Program name: poly_shift_amplify_rotate_1.py 
etc ...
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
etc.


python_1 = [ 75.2,186.9 , 76.26,177.8 , 
etc.
 , 78.2,188.1 , 76.1,188.8 ] 


def locate_shape(shape): 
    """ Calculate the bounding box location, center and dimensions. 
        x_org, y_org is the bottom-left corner, the origin. 
        wid is the width of the bounding box, hgt is the height. 
        and x_cen, y_cen is the center of the bounding box. 
    """    
etc ...
    return xy_cen, xy_size 

def amplify_2d_shape(shape, x_amplify, y_amplify): 
    """ Expand or contract a shape about the center of its bounding box. 
    """ 
   etc ...
    return new_shape 

def show_shape_metrics(shape): 
    """ Draw the shape, its bounding box, the center and graphical origin. 
    """ 
  etc ...
    return x_cen, y_cen 

def translate_shape(shape, x_shift, y_shift): 
    """ Expand or contract a shape about a given point x_center, y_center. 
        An enhancement could be to expand it about the mean of the coordinates. 
    """ 
  etc ...
    return new_shape  


def rotate_shape(shape, xy_center, angle_degrees): 
    """ Rotate any shape about a cetner point xy_center. 
    """ 
  etc ...
    return   new_shape   # angle_deg = post rotation angle 

# Determine where the center of the shape is.
xy_center = show_shape_metrics(python_1) 

# Execution and display of translation
# ===========================
for i in range(22): 
    shift_python = translate_shape(python_1, i+4, i+3) 
    canvas_1.create_polygon(shift_python, outline='green', fill='' )

# Execution and display of amplification
# ============================
for i in range(12): 
    x_amp +=  0.1 
    y_amp +=  0.1 
    amplified_python = amplify_2d_shape(python_1, x_amp, y_amp) 
    canvas_1.create_polygon(amplified_python, outline='green', fill='' ) 

# Execution and display of rotation
# =========================
for i in range(22): 
    rotate_python = rotate_shape(python_1, xy_center, i*5) 
    canvas_1.create_polygon(rotate_python, outline='red', fill='' ) 

# Display the original shape ob top of everything else.
canvas_1.create_polygon(python_1, outline='green',fill ='', width = 6 )  
canvas_1.create_polygon(python_1, outline='#008800',fill ='', width = 2 ) 

root.mainloop()
