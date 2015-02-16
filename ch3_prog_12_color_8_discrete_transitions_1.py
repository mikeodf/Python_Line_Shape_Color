""" ch3 No.12  
Program name: color_8_discrete_transitions_1.py 
Objective:Creates 8 sets of discrete transition sequences between two end colors. 
The start and end colors can be either in R:G:B lists or as a single hex color value. 

Keywords: canvas, color transition, sequence, color blending, discrete
============================================================================79 
Comments: The start and end colors are given as as pairs of hex color value '#rrggbb'. 
The user specifies how transition steps there will be.
 The colors are labelled with their hex web designations. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine 

""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("Color transition from a start to an end color") 
canvas_1 = Canvas(root, width=1250, height=400, background="black") 
canvas_1.grid(row=0, column=1) 

fnt = 'Bookantiqua 12 bold' 
fnt_2 = 'Bookantiqua 10 bold' 

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

# hex rgb inputs. 
def discrete_kula_series(start_color, end_color, num_steps): 
    """ Create the color transition list between a start and an end color (hex rgb). 
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

def show_swatch(color_hex, x_start, y_start, width, height, gap): 
    """  Paint a swatch specified by the xy position, width and height.
          'gap' the separation between the swatch and the label.
    """ 
    panel = x_start, y_start, x_start+width, y_start+height 
    canvas_1.create_rectangle(panel, fill = color_hex) 
    y_start = y_start + height + gap 
    canvas_1.create_text(x_start + width+10, y_start-height-10, text= color_hex, fill='grey', width=200,\ 
                         anchor=NW, font=fnt) #font='Bookantiqua 16 bold' 
    color_int =  hex2rgb(color_hex) 
    canvas_1.create_text(x_start + width+10, y_start-height+10, text= color_int, fill='grey', width=200,\ 
                         anchor=NW, font=fnt_2) #font='Bookantiqua 16 bold'   
        

# color transitions 
#================================================= 
# Colors specified as Hex rrggbb (full scale = ff) 
start_color_hex_1 = '#ff0000' 
end_color_hex_1   = '#ffff00' 

#================================================ 
# Swatch geometry 
#================ 
x_start = 20 
y_start = 10 
width = 40 
height = 40 
gap = 8 
num_steps = 8 
#=============================================== 
# Generate the color series and display them.
#===============================
kulas = discrete_kula_series(start_color_hex_1, end_color_hex_1, num_steps ) 
for i in range(num_steps): 
    show_swatch(kulas[i], x_start, y_start, width, height, gap) 
    y_start += height+gap 
#================================================

root.mainloop()
