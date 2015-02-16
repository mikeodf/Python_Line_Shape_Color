""" ch3 No.2  
Program name: show_named_colors_1.py
Objective: Show swatches of named web named colors. 

Keywords: canvas, rectangle, color, web color, swatch 
============================================================================79 
Explanation: We need a method of showing colors from lists of color names 
The code should handle lists of variable length. 

Tested on: Python 2.6, 
Author: Mike Ohlson de Fine 
   
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("Show color swatches") 

cw = 340                                      # canvas width 
ch = 400                                       # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1) 

redColors = "orange red","red","IndianRed1","firebrick1","red4" 
  
yellowColors= "yellow","gold","orange","DarkOrange3" 

blue1Colors = "sky blue","steel blue", "dodger blue", 
"blue","blue4","midnight blue","royal blue",  "RoyalBlue4" 

x_start = 2 
y_start = 4 

x_width = 98 
x_offset = 2 

y_height = 40 
y_offset = 3 

text_offset = 0 
text_width = 90 
blok = [x_start, y_start, x_start + x_width, y_start + y_height] 

def showColors(selectedColor): 
    """A columnar color swatch display. All colors laid down in a vertical stripe. 
        The colors are grouped as named tuples. 
    """ 
    for i in range (0, len(selectedColor)): 
        kula = selectedColor[i] 
        canvas_1.create_rectangle(blok, fill=kula) 
        canvas_1.create_text(blok[0]+10,  blok[1] ,  text=kula, width=text_width, fill ="green", anchor=NW) 
        blok[1] += y_offset + y_height 
        y0 = blok[1] 
        blok[3] += y_offset + y_height 
        y1 = blok[3] 
    blok[1] = y_offset 
    blok[3] = y_offset +  y_height 
    blok[0] += x_width + 2 * x_offset 
    blok[2] += x_width + 2 * x_offset 
    # It is not necessary to return x0, y0 as they have global scope (note to self). 

# Call the function for each list of colors. 
showColors(redColors) 
showColors(yellowColors)            
showColors(blue1Colors) 

root.mainloop()
