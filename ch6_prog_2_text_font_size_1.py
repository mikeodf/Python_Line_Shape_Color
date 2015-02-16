""" ch6 No.2  
Program name: text_font_size_1.py 
Objective: Demonstrate a series of text sizes. 

Keywords: canvas, text, point, size. 
============================================================================79 
Comments: 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3  
Author: Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("A series of point size examples.") 

cw = 1100                                    # canvas width 
ch = 260                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)  

fox = "The quick brown fox."  
point_6 = 'Book Antiqua 6: ' 
font_6 = 'Bookantiqua 6' 
point_10 = 'Book Antiqua 10: ' 
font_10 = 'Bookantiqua 10' 
point_14 = 'Book Antiqua 14: ' 
font_14 = 'Bookantiqua 14' 
point_24 = 'Book Antiqua 24: ' 
font_24 = 'Bookantiqua 24' 
point_36 = 'Book Antiqua 36: ' 
font_36 = 'Bookantiqua 36' 
point_48 = 'Book Antiqua 48: ' 
font_48 = 'Bookantiqua 48' 
                          
x = 550 
y = 20 
column_width = 1200      
offset = 0                       
canvas_1.create_text(x,y+offset, text=point_6+fox,  width=column_width, font=font_6) 
offset = 15                       
canvas_1.create_text(x,y+offset, text=point_10+fox,  width=column_width, font=font_10) 
offset = 40                       
canvas_1.create_text(x,y+offset, text=point_14+fox,  width=column_width, font=font_14) 
offset = 70                       
canvas_1.create_text(x,y+offset, text=point_24+fox,  width=column_width, font=font_24) 
offset = 120                       
canvas_1.create_text(x,y+offset, text=point_36+fox,  width=column_width, font=font_36) 
offset = 230                       
canvas_1.create_text(x,y+offset, text=point_48+fox,  width=column_width, font=font_48) 

root.mainloop() 
