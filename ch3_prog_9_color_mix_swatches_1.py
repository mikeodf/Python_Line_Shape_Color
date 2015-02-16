""" ch3 No.9  
Program name: color_mix_swatches_1.py 
Objective: Draw a colored ractangle composed of vertical lines only. 
Vary the colors according to three controlled RGB 
percentage numbers (0% = 0 , 100% = 255) 

Keywords: rectangle, lines, progressive, color spectrum, color mixing, function 
============================================================================79 
Comments: Draw a smooth linear spectrum of color. 
                                                                                      
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine       
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("Red-Green-Blue Color Transition Spectrum") 
cw = 1580                                   # canvas width 
ch = 200                                      # canvas height 
canvas = Canvas(root, width=cw, height=ch, background="black") 
canvas.grid(row=0, column=1)                              

# Color variation lists: Transition ramps or tapers. 
Red_ramp1, Red_ramp2, Red_ramp3         = [100.0,   0.0 ], [0.0,   0.0 ],     [0.0,   100.0 ] 
Green_ramp1, Green_ramp2 , Green_ramp3  = [ 0.0,  100.0 ], [ 100.0,  0.0 ],   [ 0.0,  00.0  ] 
Blue_ramp1, Blue_ramp2 , Blue_ramp3     = [ 0.0,    0.0 ], [ 0.0,    100.0 ], [ 100.0,    0.0 ] 

Red_ramp4, Red_ramp5, Red_ramp6  = [100.0, 100.0], [100.0, 0.0 ],  [0.0,    0.0 ] 
Red_ramp7, Red_ramp8, Red_ramp9  = [0.0,    0.0 ], [0.0,  100.0],  [100.0, 100.0] 

Green_ramp4, Green_ramp5 , Green_ramp6  = [ 0.0, 100.0 ], [ 100.0,  100.0 ],   [ 100.0,  100.0  ] 
Green_ramp7, Green_ramp8 , Green_ramp9  = [ 100.0,  0.0 ], [ 0.0,  0.0 ],   [ 0.0, 00.0  ] 

Blue_ramp4, Blue_ramp5 , Blue_ramp6     = [ 0.0,  0.0 ], [ 0.0,  0.0 ], [ 0.0, 100.0 ] 
Blue_ramp7, Blue_ramp8 , Blue_ramp9     = [ 100.0, 100.0 ], [ 100.0, 100.0 ], [ 100.0,  0.0 ] 

xy_start  = [ 20, 20 ]          # Bottom left.     
swatch_height = 60           # Swatch height. 
y_gap = 20                        # Gap between swatches 

num_steps = 255 

def rgb2hex(redFl, greenFl, blueFl): 
    """ Convert Red %, Green %, Blue % to numerical hex web color. 
        Return: the hex web color. 
    """ 
    red = int(redFl) 
    green = int(greenFl) 
    blue = int(blueFl) 
    rgb = red, green, blue 
    return '#%02x%02x%02x' % rgb 


def kula_ramp( xy_start, Red_ramp, Green_ramp, Blue_ramp, num_steps, ): 
     """ Paint a rectangular color mixture swatch with primary colors expressed. 
         Each transitional color is one pixel wide. 
         as % percent values (ie. from 0 to 100. 
     """     
     redShift   =  (Red_ramp[1]-Red_ramp[0])/num_steps    
     greenShift =  (Green_ramp[1]-Green_ramp[0])/num_steps 
     blueShift  =  (Blue_ramp[1]-Blue_ramp[0])/num_steps 
     
     for m in range(num_steps): 
         # Red channel.                                
         redValue   = (Red_ramp[0] + redShift* m)* 2.55  # Current red amount in 0-255 range. 
         if redValue >= 255.0:               # Ensure redValue remains less than FF hexadecimal. 
             redValue = 255.0 
         if redValue <= 0.0:                 # Ensure redValue remains greater than 0. 
             redValue = 0.0 

         # Green channel. 
         greenValue   = (Green_ramp[0] + greenShift* m)* 2.55  # Current green amount in 0-255 range. 
         if greenValue >= 255.0: 
             greendValue = 255.0 
         if greenValue <= 0.0: 
             greendValue = 0.0 

         # Blue channel. 
         blueValue   = (Blue_ramp[0] + blueShift* m)* 2.55  # Current blue amount in 0-255 range. 
         if blueValue >= 255.0: 
             blueValue = 255.0 
         if blueValue <= 0.0: 
             blueValue = 0.0 
         kula = rgb2hex(redValue, greenValue, blueValue)    # Convert to web hex color. 
         canvas.create_line(xy_start[0]+m, xy_start[1], xy_start[0]+m, xy_start[1]+swatch_height, fill= kula, width = 1) 
     return xy_start[0]+num_steps  

# Rainbow Spectrum. 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
xy_start[0] = kula_ramp(xy_start, Red_ramp4, Green_ramp4, Blue_ramp4, num_steps) 
xy_start[0] = kula_ramp(xy_start, Red_ramp5, Green_ramp5, Blue_ramp5, num_steps) 
xy_start[0] = kula_ramp(xy_start, Red_ramp6, Green_ramp6, Blue_ramp6, num_steps) 
xy_start[0] = kula_ramp(xy_start, Red_ramp7, Green_ramp7, Blue_ramp7, num_steps) 
xy_start[0] = kula_ramp(xy_start, Red_ramp8, Green_ramp8, Blue_ramp8, num_steps) 
xy_start[0] = kula_ramp(xy_start, Red_ramp9, Green_ramp9, Blue_ramp9, num_steps) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
root.mainloop()
