""" ch6 No.12  
Program name: fonts_available_1.py 
Objective: Discover, list and demonstrate all fonts available on your 
platform. 

Keywords: canvas, text, font inventory 
============================================================================79 
Comments: To specify fonts precisely you need to know what fonts are 
available and what they look like. The tkfont module is used here to 
do that. 

Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
import tkFont   # This does not work with Python v3
#from tkinter import font as tkFont 
root = Tk() 
root.title('Fonts available on this Computer') 

canvas_1 = Canvas(root, width =1500, height=800, background='white') 
canvas_1.grid(row=0, column=1) 

fonts_available = list( tkFont.families() ) 
fonts_available.sort() 
text_sample = '  :  abcdefghij_HIJK_12340' 
# list the font names on the system console first. 
for this_family in fonts_available : 
   # print( this_family) 
   print this_family 
# Show first third on left side of the screen . 
for i in range(int(len(fonts_available)/3)): 
    texty = fonts_available[i] 
    canvas_1.create_text(50,30 + i*20, text= texty + text_sample, 
                       fill='black', font=(texty, 12), anchor= "w") 

# Show second third in the middle of the screen . 
for j in range(int(len(fonts_available)/3), int(2*len(fonts_available)/3)): 
    texty = fonts_available[j] 
    canvas_1.create_text(500,30 + ( j - int(len(fonts_available)/3))*20, text= texty+ text_sample, 
 fill='black',font=(texty, 12),anchor= "nw") 

# Show second third on the right of screen . 
for i in range( int(2*len(fonts_available)/3), len(fonts_available)): 
    texty = fonts_available[i] 
    canvas_1.create_text(1000,30 + (i  - 2*int(len(fonts_available)/3))*20, text= texty+ text_sample, 
 fill='black',font=(texty, 12),anchor= "w") 

root.mainloop() 
