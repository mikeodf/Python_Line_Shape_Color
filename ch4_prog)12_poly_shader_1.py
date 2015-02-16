""" ch4 No.12 
Program name: poly_shader_1.py 
Objective: Color a polygon shape using a transition sequence between two end colors. 

Keywords: canvas, color transition, sequence, polygon, shape. 
============================================================================79 
Comments: The polygon shape is re-drawn repeatedly on the same center, 
 decreasing the size each time. This effectively creates layers within 
 the shape. Each shape layer is filled with a slightly different color. 
The start and end colors are given as as pairs of hex color value '#rrggbb'. 
"discrete_kula_series(...) returns the color sequence used. 

Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author: Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher. 
root = Tk() 
root.title("Color shading of shapes.") 
canvas_1 = Canvas(root, width=950, height=350, background="#000000") 
canvas_1.grid(row=0, column=1) 

sun = [375.7,49.5 , 456.4,62.3 , 525,93.0 , 587.8,138.0 
 , 637.8,202.3 , 675,283.7 , 687.1,356.6 , 684.2,438.0 
 , 662.8,509.5 , 630.7,569.5 , 582.8,625.9 , 530,665.2 
 , 454.2,698.0 , 360.7,710.9 , 270.7,696.6 , 200,665.9 
 , 130.7,610.9 , 70.7,518.7 , 42.1,416.6 , 48.5,307.3 
 , 89.2,205.9 , 152.1,129.5 , 243.5,73.7 , 324.2,52.3 ] 

def hex2rgb(hex_color): 
    """ Convert a hex color of the from '#rrggbb' 
        to three element tuple of base 10 integers corresponging to (red, green, blue). 
    """ 
    start_kula = 0,0,0 
    end_kula = 0,0,0 
    n1 = [1,  3, 5] 
    n2 = [3,  5, 7] 
    rgb_color = [] 
    for i in range(0,3): 
        a = n1[i] 
        b = n2[i] 
        kula_slice = hex_color[a:b] 
        #print ' kula_slice: ', kula_slice 
        c = int(kula_slice, 16) 
       
        rgb_color.append(c)  # '16' is the base from which to convert. 
    rgb_color = tuple(rgb_color) 
    return rgb_color 

# RGB inputs 
def discrete_kula_series(start_color, end_color, num_steps): 
    """ Create the color transion list between a start and an end color (hex rgb). 
         Generate Color Transition Series as hex RGB inputs 
    """ 
    start_color_int = hex2rgb(start_color) 
    end_color_int = hex2rgb( end_color) 
    delt_red = (end_color_int[0] - start_color_int[0])/(num_steps - 1) 
    delt_green = (end_color_int[1] - start_color_int[1])/(num_steps - 1) 
    delt_blue = (end_color_int[2] - start_color_int[2])/(num_steps - 1) 
    color_series_int = [] 
    color_series_hex = [] 
    for i in range(num_steps+1): 
        next_red = start_color_int[0]+i*delt_red 
        if next_red <=0.0: 
            next_red = 0.0 
        next_green = start_color_int[1]+i*delt_green 
        if next_green <=0.0: 
            next_green = 0.0 
        next_blue = start_color_int[2]+i*delt_blue 
        if next_blue <=0.0: 
            next_blue = 0.0 
        next_color_int = next_red, next_green, next_blue 
        color_series_int.append(next_color_int) 
        if i < num_steps: 
            next_color_hex = '#%02x%02x%02x' % next_color_int 
            color_series_hex.append(next_color_hex) 
            color_series_int.append(next_color_int) 
        else: 
            next_color_hex =  '#%02x%02x%02x' % end_color_int 
            color_series_hex.append(next_color_hex)  
            color_series_int.append(next_color_int)      
    return color_series_hex 


def locate_shape(shape): 
    """ Calculate the bounding box location, center and dimensions. 
        x_org, y_org is the bottom-left corner, the origin. 
        wid is the width of the bounding box, hgt is the height. 
        and x_cen, y_cen is the center of the bounding box. 
    """    
    x_list = [] 
    y_list = [] 
    for i in range(int(len(shape)/2)):    # Separate out the x and components. 
        x_list.append(shape[2*i]) 
        y_list.append(shape[2*i+1]) 
    x_org = min(x_list) 
    y_org = min(y_list) 
    wid = max(x_list) - x_org 
    hgt = max(y_list) - y_org 
    x_cen = x_org + wid/2.0 
    y_cen = y_org + hgt/2.0 
    xy_cen = [x_cen, y_cen] 
    xy_size = [ wid, hgt] 
    return xy_cen, xy_size 

def amplify_2d_shape(shape, x_amplify, y_amplify): 
    """ Expand or contract a shape about the center of its bounding box. 
    """ 
    new_shape = [] 
    xy_bunch = locate_shape(shape) 
    x_cen = xy_bunch[0][0] 
    y_cen = xy_bunch[0][1] 
    wid = xy_bunch[1][0]  
    hgt = xy_bunch[1][1] 
    x_org = x_cen - wid/2 
    y_org = y_cen - hgt/2   
    for i in range(int(len(shape)/2 )): 
        x_ampd = (shape[2*i]   - x_org)*x_amplify + x_org - wid*(x_amplify - 1)/2 
        y_ampd = (shape[2*i+1] - y_org)*y_amplify + y_org - hgt*(y_amplify - 1)/2 
        new_shape.append(x_ampd) 
        new_shape.append(y_ampd) 
    return new_shape 
 
def translate_shape(shape, x_shift, y_shift): 
    """ Expand or contract a shape about a given point x_center, y_center. 
        An enhancement could be to expand it about the mean of the coordinates. 
    """ 
    new_shape = [] 
    for i in range(int(len(shape)/2) ): 
        x_new = shape[2*i]  + x_shift 
        y_new = shape[2*i+1] + y_shift 
        new_shape.append(x_new) 
        new_shape.append(y_new) 
    return new_shape  

def shrinking_series(shape, start_color, end_color, x_amplify, y_amplify, number_layers): 
    """ Shaded image assembly and display. 
    """ 
    kulas = discrete_kula_series(start_color, end_color, number_layers) 
    canvas_1.create_polygon(shape, outline='', fill=kulas[0], smooth=0 )    
    for i in range(number_layers): 
        shape = amplify_2d_shape(shape, x_amplify, y_amplify ) 
        canvas_1.create_polygon(shape, outline='', fill=kulas[i], smooth=0 ) 

#**************************************************************************** 
# Execute and Demonstrate. 
# ==========================

# Initialization setup. 
new_sun = amplify_2d_shape(sun,0.4, 0.4 )   # Starting Shape. 

# Example 1 - Yellow-to-blue concentrics 
new_sun = translate_shape(new_sun, -200, -200 )   # Starting Shape. 
number_layers = 12 
start_color = '#ffff00' 
end_color   = '#0000ff' 
x_amplify = 0.96 
y_amplify = 0.96 
shrinking_series(new_sun, start_color, end_color, x_amplify, y_amplify, number_layers) 

# Example 2 - Red-to-black cat's eye. 
new_sun = translate_shape(new_sun, 300, 0 )   # Starting Shape. 
start_color = '#ff0000' 
end_color   = '#000000' 
x_amplify = 0.7 
y_amplify = 0.999 
shrinking_series(new_sun, start_color, end_color, x_amplify, y_amplify, number_layers) 

# Example 2 - Purple glow. 
new_sun = translate_shape(new_sun, 300, 0 )   # Starting Shape. 
start_color = '#000000' 
end_color   = '#8800ff' 
x_amplify = 0.96 
y_amplify = 0.8 
shrinking_series(new_sun, start_color, end_color, x_amplify, y_amplify, number_layers) 

root.mainloop()
