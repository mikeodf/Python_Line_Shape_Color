""" ch6 No.5  
Program name: text_anchored_1.py
Objective: Draw text onto the canvas using anchor points for location. 

Keywords: canvas, text, arial, courier, sans serif, book antiqua, anchor.
============================================================================79 
Comments: The text is written starting at co-ordinate location x= 600, with y progressing down the canvas
 in steps of 30 pixels. 
The default position has the text string anchored by it SW (bottom-left) or NE (top right corner). 

Tested on: Python 2.6, Python 2.7, Python 3.2, 
Author:          Mike Ohlson de Fine    
   
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('South West and North East Anchor points') 

cw = 900                                     # canvas width 
ch = 250                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="dark green") 
canvas_1.grid(row=0, column=1)                              

xy = 200, 20        
                          
################      South West (SW) anchored     ############################################### 
canvas_1.create_text(450, 50,  text="SansSerif 12 anchored at SW corner",    fill='red', width=600, font='SansSerif 16 ',     anchor= SW) 
canvas_1.create_text(450, 100,  text="Arial 12 anchored at SW corner",        fill='blue', width=600, font='Arial 16',         anchor= SW) 
canvas_1.create_text(450, 150, text="Courier 12 anchored at SW corner",       fill='green', width=600, font='Courier 16',      anchor= SW) 
canvas_1.create_text(450, 200, text="BookAntiqua 12 anchored at SW corner",  fill='violet', width=600, font='Bookantiqua 16', anchor= SW) 
#=================================================================================

#################   North East (NE) anchored################################################## 
canvas_1.create_text(450, 50,  text="SansSerif 12 anchored at NE corner",    fill='red', width=600, font='SansSerif 16',      anchor= NE) 
canvas_1.create_text(450, 100,  text="Arial 12 anchored at NE corner",        fill='blue', width=600, font='Arial 16',         anchor= NE) 
canvas_1.create_text(450, 150, text="Courier 12 anchored at NE corner",       fill='green', width=600, font='Courier 16',      anchor= NE) 
canvas_1.create_text(450, 200, text="BookAntiqua 12 anchored at NE corner",  fill='violet', width=600, font='Bookantiqua 16', anchor= NE) 
#=================================================================================
root.mainloop()
