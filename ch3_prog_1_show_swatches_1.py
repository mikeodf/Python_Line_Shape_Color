""" ch3 No.1  
Program name: show_swatches_1.py 
Objective: Show swatches of web colours. 

Keywords: canvas, rectangle, color web color, swatch 
============================================================================79 
Explanation: We  show some named colors. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine 
   
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("Show color swatches") 

cw = 290                                      # canvas width 
ch = 200                                       # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1) 

# Colors to be displayed. "red","yellow", "blue","green" 
x_start = 20 
y_start = 20 

x_width = 250 
y_height = 40 

text_offset = 0 
text_width = 90 

blok = [x_start, y_start, x_start + x_width, y_start + y_height] 

canvas_1.create_rectangle(blok, fill="red") 
canvas_1.create_text(blok[0]+10,  blok[1] ,  text="red", width=text_width, fill ="green", anchor=NW) 

blok[1] += y_height 
blok[3] += y_height 
canvas_1.create_rectangle(blok, fill="yellow") 
canvas_1.create_text(blok[0]+10,  blok[1] ,  text="yellow", width=text_width, fill ="red", anchor=NW) 

blok[1] += y_height 
blok[3] += y_height 
canvas_1.create_rectangle(blok, fill="blue") 
canvas_1.create_text(blok[0]+10,  blok[1] ,  text="blue", width=text_width, fill ="yellow", anchor=NW) 

blok[1] += y_height 
blok[3] += y_height 
canvas_1.create_rectangle(blok, fill="green") 
canvas_1.create_text(blok[0]+10,  blok[1] ,  text="green", width=text_width, fill ="blue", anchor=NW) 

root.mainloop()
