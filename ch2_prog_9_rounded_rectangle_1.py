""" ch2 No.9 
Program name: rounded_rectangle_1.py 
Objective: Draw a rounded rectangle using similar specifications to 
a conventionl rectangle. The radius of the corners also needs to be stated. 
	  
Keywords: arc circle, rounded rectangle. 
============================================================================79 
Comments: It is tricky to get each of the 34 coordinate values corrrect 
and ways of progressive error correction should be part of the code 
writing/testing process. 
                                                                                                                                                                           
Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author:          Mike Ohlson de Fine    
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Rounded rectangle') 
cw = 260                                      # canvas width 
ch = 260                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

start_x = 50 
start_y = 200 
end_x = 200 
end_y = 50 
Radius =  40 

len1 = end_x - start_x - 2*Radius 
len2 = start_y - end_y - 2*Radius 


pt1 = start_x, start_y - Radius 
pt2 = start_x, start_y - Radius - len2 
pt3 = start_x + Radius, end_y 
pt4 = start_x + Radius + len1, end_y 
pt5 = end_x,  end_y + Radius 
pt6 = end_x, start_y - Radius 
pt7 = end_x - Radius, start_y 
pt8 = start_x + Radius, start_y 
 
arc2 = pt2[0], pt2[1] + Radius 
arc3 = pt3[0] + Radius, pt3[1] 
arc4 = pt4[0] - Radius, pt4[1] + 2 *Radius 
arc5 = pt5[0] , pt5[1] - Radius 
arc6 = pt6[0] , pt6[1] - Radius 
arc7 = pt7[0]- Radius, pt7[1] 
arc8 = pt8[0] + Radius, pt8[1] 
arc1 = pt1[0] , pt1[1] - Radius 

canvas_1.create_line(pt1, pt2, fill="darkblue", width = 4) 
canvas_1.create_line(pt3, pt4, fill="darkblue", width = 4) 
canvas_1.create_line(pt5, pt6, fill="darkblue", width = 4) 
canvas_1.create_line(pt7, pt8, fill="darkblue", width = 4) 

canvas_1.create_arc(arc2, arc3, start=90, extent=90, outline="darkblue", width=4) 
canvas_1.create_arc(arc4, arc5, start=0, extent=90, outline="darkblue", width=4) 
canvas_1.create_arc(arc6, arc7, start=270, extent=90, outline="darkblue", width=4) 

canvas_1.create_arc(arc8, arc1, start=-90, extent=-90, outline="darkblue", width=4) 
canvas_1.create_rectangle(arc8, arc1,  outline="red") 

root.mainloop()
