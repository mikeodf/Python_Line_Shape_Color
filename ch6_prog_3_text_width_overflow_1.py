""" ch6 No.3  
Program name: text_width_overflow_1.py 
Objective: Draw text onto the canvas at a chosen location. 

Keywords: canvas,text 
============================================================================79 
 Comments: The text is written starting at co-ordinate location (x,y) = 200,20. 
The "width=200" is the horizontal size of the writing area. The text column grows upwards with each
new line.

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3  
Author: Mike Ohlson de Fine. 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("When Text Overflows.")

cw = 300                                    # canvas width 
ch = 260                                     # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

xy = 150, 100                               
canvas_1.create_text(xy, text=" TEXT LARGE, Arial 20 point. So what happens if we have not allowed sufficient width on one line?", fill='red', width=200, font='Arial 20') 

root.mainloop()
