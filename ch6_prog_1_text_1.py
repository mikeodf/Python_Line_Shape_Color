""" ch6 No.1 
Program name: text_1.py 
Objective: Place text on a canvas. 

Keywords: canvas, text 
============================================================================79 
Comments: Using all default settings this is the bare minimum code 
to place text onto a canvas. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3  
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Basic text on Canvas') 

cw = 400                                   # canvas width 
ch = 50                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)                              

xy = 150, 20 
canvas_1.create_text(xy, text=" What is the default text size and style?") 
root.mainloop() 
