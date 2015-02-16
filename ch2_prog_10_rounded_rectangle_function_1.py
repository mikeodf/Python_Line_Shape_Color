""" ch2 No.10 
Program name: rounded_rectangle_function_1.py 
Objective: Draw a rounded rectangle using similar specifications to 
a conventionl rectangle. The radius of the corners also needs to be stated. 
	  
Keywords: arc circle, rounded rectangle. 
============================================================================79 
Comments: It is tricky to get each of the 34 coordinate values correct 
and ways of progressive error correction should be part of the code 
writing/testing process. 
                                                                                                                                                                            
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine 
   
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher. 
root = Tk() 
root.title('Rounded rectangle') 
cw = 500                                      # canvas width 
ch = 500                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

def round_rectangle(x_start, y_start, x_end, y_end, corner_radius, line_width, outline_kula): 
    """ Draw a rounded rectangle with all parameters selectable. 
    """ 
    len1 = x_end - x_start - 2*corner_radius 
    len2 = y_start - y_end - 2*corner_radius 

    pt1 = x_start, y_start - corner_radius 
    pt2 = x_start, y_start - corner_radius - len2 
    pt3 = x_start + corner_radius, y_end 
    pt4 = x_start + corner_radius + len1, y_end 
    pt5 = x_end,  y_end + corner_radius 
    pt6 = x_end, y_start - corner_radius 
    pt7 = x_end - corner_radius, y_start 
    pt8 = x_start + corner_radius, y_start 
 
    arc2 = pt2[0], pt2[1] + corner_radius 
    arc3 = pt3[0] + corner_radius, pt3[1] 
    arc4 = pt4[0] - corner_radius, pt4[1] + 2 *corner_radius 
    arc5 = pt5[0] , pt5[1] - corner_radius 
    arc6 = pt6[0] , pt6[1] - corner_radius 
    arc7 = pt7[0]- corner_radius, pt7[1] 
    arc8 = pt8[0] + corner_radius, pt8[1] 
    arc1 = pt1[0] , pt1[1] - corner_radius 

    canvas_1.create_line(pt1, pt2, fill=outline_kula, width = line_width) 
    canvas_1.create_line(pt3, pt4, fill=outline_kula, width = line_width) 
    canvas_1.create_line(pt5, pt6, fill=outline_kula, width = line_width) 
    canvas_1.create_line(pt7, pt8, fill=outline_kula, width = line_width) 

    canvas_1.create_arc(arc2, arc3, style=ARC, start=90,  extent=90,  outline=outline_kula, width=line_width) 
    canvas_1.create_arc(arc4, arc5, style=ARC, start=0,   extent=90,  outline=outline_kula, width=line_width) 
    canvas_1.create_arc(arc6, arc7, style=ARC, start=270, extent=90,  outline=outline_kula, width=line_width) 
    canvas_1.create_arc(arc8, arc1, style=ARC, start=-90, extent=-91, outline=outline_kula, width=line_width) 

# Test and demonstrate 
#===================== 
x_start = 50 
y_start = 400 
x_end = 400 
y_end = 50 
corner_radius =  50 
line_width = 4 
outline_kula ="darkblue" 

round_rectangle(x_start, y_start, x_end, y_end, corner_radius, line_width, outline_kula) 

root.mainloop()
