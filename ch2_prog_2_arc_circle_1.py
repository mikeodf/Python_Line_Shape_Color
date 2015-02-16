""" ch2 No.2 
Program name: arc_circle_1.py 
Objective: Draw a circle as an almost complete circular arc 
	  
Keywords: circle, arc 
============================================================================79 
Comments: The syntax of the instruction is:
create_arc(x_top_left, y_top_left, x_bottom_right, x_bottom_right, start=degrees,extent=degrees,fill="cyan")  

This is not a good way to make circles because they are never complete. 
You cannot close the circle by asking for a 360 degree extent - you end up 
with a line. 359.99999999 etc. is a close as you can get. But you are always 
left with the radial line. 
If you try to make an entire disk you end up with the excluded portion - merely a line. 
Rather use the 'create_oval' function. 
                                                                                                                                                                              
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3   
Author:          Mike Ohlson de Fine   
""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('An arc circle') 
cw = 350                                     # canvas width 
ch = 350                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

xy = 20, 20, 320, 320         # bounding box from x0,y0 to x1, y1 
                                           # arc from start_angle, in degrees to finish_angle 
canvas_1.create_arc(xy, start=0, extent=359.999999999, fill="cyan") 

root.mainloop()
