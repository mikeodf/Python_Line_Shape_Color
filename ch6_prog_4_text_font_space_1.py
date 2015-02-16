""" ch6 No.4  
Program name: text_font_space_1.py 
Objective: Draw text onto the canvas at a chosen location. 

Keywords: canvas, text, font size, overlap. 
============================================================================79 
Comments: The text is written starting at co-ordinate location x= 200 
with y progressing down the canvas in steps of 30 pixels. 
The default position has the text string centered at x= 200 which can 
look messy. 
The "width=500" is the horizontal size of the writing area, 
in pixels (not typeset point measure). 

ested on: Python 2.6, Python 2.7.3, Python 3.2.3  
Author: Mike Ohlson de Fine   
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("When font size misbehaves.") 
 
cw = 600                                     # canvas width 
ch = 350                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="#000066") 
canvas_1.grid(row=0, column=1)                              

x = 300       

# Font Family descriptions.                          
canvas_1.create_text(x, 20,  text=" text normal SansSerif 20",   fill='yellow', width=500, font='SansSerif 20 ') 
canvas_1.create_text(x, 50,  text=" text normal Arial 20",       fill='white', width=500, font='Arial 20 ') 
canvas_1.create_text(x, 80,  text=" text bold Courier 20",       fill='green', width=500, font='Courier 20 bold') 
canvas_1.create_text(x, 110, text=" bold italic BookAntiqua 20", fill='violet', width=500, font='Bookantiqua 20 bold') 

# Size comparisons. 
canvas_1.create_text(x, 200, text="psuedomorphologicalpsychosenses", fill='yellow', width=500, font='SansSerif 20 ') 
canvas_1.create_text(x, 230, text="psuedomorphologicalpsychosenses", fill='white', width=500, font='Arial 20 ') 
canvas_1.create_text(x, 260, text="psuedomorphologicalpsychosenses", fill='green', width=500, font='Courier 20 bold') 
canvas_1.create_text(x, 290, text="psuedomorphologicalpsychosenses", fill='violet', width=500, font='Bookantiqua 20 bold') 

root.mainloop()
