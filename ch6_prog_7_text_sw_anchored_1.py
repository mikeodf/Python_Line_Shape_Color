""" ch6 No.7  
Program name: text_sw_anchored_1.py 
Objective: Place different colored texts anchored south-west on a canvas. 

Keywords: canvas, text, color, font 
============================================================================79 
Comments: 
1. Text position orig_x, orig_y. 
2. anchor=SW. South-West.  

Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 

from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Text anchored SW with block widths of 800, 500 and 300 points/pixels.') 

cw = 900                                     # canvas width 
ch = 630                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)  

dsn= "It was a dark and stormy night; the rain fell in torrents - except at occasional intervals, when it was checked by a violent gust of wind which swept up the streets, rattling along the housetops, and fiercly agitating the scanty flame of the lamps that struggled against the darkness. In her attic bedroom Margaret Muray, wrapped in an old patchwork quilt, sat on the foot of her bed and watched the trees tossing in the frenzied lashing of the wind. Behind the trees clouds scudded frantically across the sky. Every few moments the moon ripped through them, creating wraithlike shadows that raced along the ground." 

orig_x = 50 
orig_y  = 140   
 
canvas_1.create_text(orig_x, orig_y,   anchor= SW, text=dsn,   fill='red', 
                                 width=800, font='SansSerif 10 ') 
canvas_1.create_oval(orig_x-16, orig_y-16,  orig_x+16, orig_y+16, outline='red', width =6) 

orig_y = 320   
canvas_1.create_text(orig_x, orig_y,   anchor= SW, text=dsn,   fill='brown', 
                                 width=500, font='SansSerif 10 ') 
canvas_1.create_oval(orig_x-16, orig_y-16,  orig_x+16, orig_y+16, outline='red', width =6) 

orig_y = 600   
canvas_1.create_text(orig_x, orig_y,   anchor= SW, text=dsn,   fill='blue', 
                                 width=300, font='SansSerif 10 ') 
canvas_1.create_oval(orig_x-16, orig_y-16,  orig_x+16, orig_y+16, outline='red', width =6) 

root.mainloop()
