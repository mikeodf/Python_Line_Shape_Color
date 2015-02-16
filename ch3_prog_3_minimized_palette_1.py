""" ch3 No.3  
Program name: minimized_palette_1.py 
Objective: Show a reduced palette of web colours that are recognized by python. 

Keywords: canvas, rectangle, color web color, reduced set, pallette 
============================================================================79 
Comment: Python/Tkinter has a large collection of colors with known names. 
Many are similar and therefore redundant 
A selection offering a broad choice is shown here. 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine  
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("A reduced pallette of named colors") 

cw = 1150                                     # canvas width 
ch = 500                                       # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1) 


# Reds - reduced set 
#===================== 
red1Colors = "orange red", 
"red","red3","red4",
"IndianRed1", 
"firebrick1","firebrick4" 

# Browns  - reduced set 
#====================== 
brown1Colors = "sienna1","sienna3","sienna4","tan1","tan4" 

# Yellows  - reduced set 
#========================= 
yellowColors= "yellow","gold", "gold3","gold4", 
"orange","dark orange","DarkOrange3","DarkOrange4" 

# Pink - reduced set 
# =================== 
pinkColors =  "orchid1","orchid3","orchid4", 
"light pink","hot pink","HotPink3", 
"deep pink","DeepPink4" 

# Magenta - Maroon - reduced set 
# ============================== 
magenta1Colors = "magenta","magenta3","magenta4", 
"maroon2","maroon","maroon4", 

# Purple - Maroon - reduced set 
# ============================== 
magenta2Colors = "purple", "purple3","purple4", 
"MediumOrchid","DarkOrchid","DarkOrchid4", 
"SlateBlue2", "SlateBlue4", 

# Blues  - reduced set 
#======================= 
blue1Colors = "sky blue","steel blue", "dodger blue", 
"DodgerBlue4","blue","blue4","midnight blue", 
"royal blue",  "RoyalBlue4" 

# Cyan -  reduced set 
#======================= 
cyanColors = "cyan", "cyan3", "cyan4" 

# Greens reduced set 
#====================== 
green1Colors = "green yellow","chartreuse","chartreuse3", "chartreuse4", 
"green", "green3", "green4", 
"MediumSpringGreen","spring green",  "SpringGreen3","SpringGreen4" 

green2Colors = "pale green", "PaleGreen3", "PaleGreen4", 
"OliveDrab4","DarkOliveGreen1", 
"DarkOliveGreen3","DarkOliveGreen4" 

# Grey -  reduced set 
#======================= 
greyColors = "Gray","snow4","DimGray", 
"SlateGray1",  "SlateGray3", "SlateGray4", 
"DarkSlateGray", "SteelBlue3",  "SteelBlue4", 

#    WHITES 
#======================= 
white1Colors = "white",  
"lemon chiffon", "lavender blush","thistle","plum", 

x_start = 2 
y_start = 4 

x_width = 90 
x_offset = 2 

y_height = 40 
y_offset = 3 

text_offset = 0 
text_width = 90 
blok = [x_start, y_start, x_start + x_width, y_start + y_height] 

def showColors(selectedColor): 
    """Basic columnar color swatch display. All colors are laid down in a vertical stripe. 
       The colors are grouped as a  named tuple. 
    """ 
    for i in range (0 ,len(selectedColor)): 
        kula = selectedColor[i] 
        canvas_1.create_rectangle(blok, fill=kula) 
        canvas_1.create_text(blok[0]+10,  blok[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
        blok[1] += y_offset + y_height 
        y0 = blok[1] 
        blok[3] += y_offset + y_height 
        y1 = blok[3] 
    blok[1] = y_offset 
    blok[3] = y_offset +  y_height 
    blok[0] += x_width + 2 * x_offset 
    blok[2] += x_width + 2 * x_offset 
    return y0,y1 

showColors(red1Colors) 
showColors(brown1Colors) 
showColors(yellowColors)            
showColors(pinkColors) 
showColors(magenta1Colors) 
showColors(magenta2Colors) 
showColors(blue1Colors) 
showColors(cyanColors) 
showColors(green1Colors) 
showColors(green2Colors)    
showColors(greyColors)   
showColors(white1Colors)  

root.mainloop()
