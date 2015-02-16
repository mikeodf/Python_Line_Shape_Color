""" ch6 No.9  
Program name: text_justify_align_1.py 
Objective: Place different colored texts and font types on a canvas. 

Keywords: canvas, text, color, font 
============================================================================79 
Comments: 
1. Font type, size and color can be specified. Tkinter will 
apply a 'best-guess' font if the exact font specified is not available 
on your platform. 

2. anchor=anchorPos:  Text position orig_x, orig_y is where the text is centered (by default). 
   This can be overriden by anchor options like "anchor= NW". 

anchorPos Specifies which part of the text (the text's bounding box, more exactly) that should be placed at the given position. 
Use one of N, NE, E, SE, S, SW, W, NW or CENTER. Default is CENTER. 

3. justify=how (ACTIVE WHEN LINE OVERFLOWS OCCUR) 
Specifies how to justify the text within its bounding region. How must be one of the values "LEFT", "RIGHT", or "CENTER". This option will only matter if the text is displayed as multiple lines. If the option is omitted, it defaults to left. 

4. tags=tagList 
Specifies a set of tags to apply to the item. TagList consists of a list of tag names, which replace any existing tags for the item. TagList may be an empty list. 

5. width=lineLength 
Specifies a maximum line length for the text. If this option is zero (the default) the text is broken into lines only at newline characters. However, if this option is non-zero then any line that would be longer than lineLength is broken just before a space character to make the line shorter than lineLength; the space character is treated as if it were a newline character. 

Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Various justifications with NW anchor points. Column widths of 300 pixels.') 

cw = 800                                      # canvas width 
ch = 700                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)  

dasn= "It was a dark and stormy night; the rain fell in torrents - except at occasional intervals, when it was checked by a violent gust of wind which swept up the streets, rattling along the housetops, and fiercly agitating the scanty flame of the lamps that struggled against the darkness. In her attic bedroom Margaret Muray, wrapped in an old patchwork quilt, sat on the foot of her bed and watched the trees tossing in the frenzied lashing of the wind. Behind the trees clouds scudded frantically across the sky. Every few moments the moon ripped through them, creating wraithlike shadows that raced along the ground." 


orig_y = 50 
orig_x = 50 
canvas_1.create_text(orig_x, orig_y,  anchor= NW,  justify= RIGHT, text=dasn,   fill='brown',\ 
                                 width=300, font='SansSerif 10 ') 
canvas_1.create_oval(orig_x-16, orig_y-16,  orig_x+16, orig_y+16, outline='red', width =6) 
orig_y = 50 
orig_x = 420 
canvas_1.create_text(orig_x, orig_y,    anchor= NW, justify= LEFT, text=dasn,   fill='blue',\ 
                                 width=300, font='SansSerif 10 ') 
canvas_1.create_oval(orig_x-16, orig_y-16,  orig_x+16, orig_y+16, outline='red', width =6) 

orig_y = 400                                
orig_x = 50 
canvas_1.create_text(orig_x, orig_y,  anchor= NW,  justify= LEFT, text=dasn,   fill='dark green',\ 
                                 width=300, font='SansSerif 10 ') 
canvas_1.create_oval(orig_x-16, orig_y-16,  orig_x+16, orig_y+16, outline='red', width =6)  
orig_y = 400       
orig_x = 420 
canvas_1.create_text(orig_x, orig_y,    anchor= NW, justify= RIGHT, text=dasn,   fill='red',\ 
                                 width=300, font='SansSerif 10 ') 
canvas_1.create_oval(orig_x-16, orig_y-16,  orig_x+16, orig_y+16, outline='red', width =6) 

root.mainloop() 
