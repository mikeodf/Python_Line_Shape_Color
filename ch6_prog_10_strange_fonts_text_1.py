""" ch6 No.10  
Program name: strange_fonts_text_1.py 
Objective: Display unusual and creative fonts. 

Keywords: canvas, text, color, font family, size, style 
============================================================================79 
Comments: The value of defining font specification parameters via a 
function definition is that any of the parameter can become an effective 
for the duration when the program is run - they whole group of parameters 
not not need to re-declared every time new text is displayed. 

Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Unusual truetype creative fonts.') 

cw = 800                                     # canvas width 
ch = 600                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="white") 
canvas_1.grid(row=0, column=1)  

dasn= "It was a dark and stormy night; the rain fell in torrents - except at occasional intervals." 

# Unusual Fonts 
darkgarden = 'Dark Garden' 
lenka      = 'Lenka' 
onthewall  = 'OnTheWall' 
katam      = 'Katamotzikasi' 
purisa     = 'Purisa' 
graffititreat = 'Graffiti Treat' 
oldenglish = 'Old English Text MT' 
royal = 'Royal' 
chancery   = 'URW Chancery L' 

# Colours 
kula_bg = '#d8f800' 
kula_1  = '#4c10ae' 
kula_2  = '#de0052' 
kula_3  = '#9303a7' 
kula_4  = '#7109aa' 
kula_5  = '#cd0074' 
kula_6  = '#3914af' 
kula_7  = '#150873' 

def make_font(font_family, size_points, bold_norm, slant): 
    make_font = (font_family, size_points, bold_norm, slant) 
    return make_font 

orig_x = 50 

#1 
font_family = katam 
bold_norm = 'bold' 
slant = 'normal' 
size_points = 24 
orig_y = 30 
do_font = make_font(font_family, size_points, bold_norm, slant) 
canvas_1.create_text(orig_x, orig_y,  anchor= NW,  justify= RIGHT, text=dasn,   fill=kula_1, 
                                width=700, font=do_font) 
#2 
font_family = lenka 
size_points = 20 
orig_y = 80 
do_font = make_font(font_family, size_points, bold_norm, slant) 
canvas_1.create_text(orig_x, orig_y,  anchor= NW,  justify= RIGHT, text=dasn,   fill=kula_2, 
                                width=700, font= do_font) 
#3 
font_family = onthewall 
size_points = 20 
orig_y = 120 
do_font = make_font(font_family, size_points, bold_norm, slant) 
canvas_1.create_text(orig_x, orig_y,  anchor= NW,  justify= RIGHT, text=dasn,   fill=kula_3, 
                                width=700, font= do_font) 
#4 
font_family = graffititreat 
size_points = 24 
orig_y = 160 
do_font = make_font(font_family, size_points, bold_norm, slant) 
canvas_1.create_text(orig_x, orig_y,  anchor= NW,  justify= RIGHT, text=dasn,   fill=kula_4, 
                                width=700, font= do_font) 
#5 
font_family = oldenglish 
size_points = 36 
orig_y = 200 
do_font = make_font(font_family, size_points, bold_norm, slant) 
canvas_1.create_text(orig_x, orig_y,  anchor= NW,  justify= RIGHT, text=dasn,   fill=kula_5, 
                                width=700, font= do_font) 
#6 
font_family = darkgarden 
size_points = 28 
orig_y = 260 
do_font = make_font(font_family, size_points, bold_norm, slant) 
canvas_1.create_text(orig_x, orig_y,  anchor= NW,  justify= RIGHT, text=dasn,   fill=kula_6, 
                                width=700, font= do_font) 
#7 
font_family = royal 
size_points = 28 
orig_y = 340 
rdasn= "IT WAS A DARK AND STORMY NIGHT" 
do_font = make_font(font_family, size_points, bold_norm, slant) 
canvas_1.create_text(orig_x, orig_y,  anchor= NW,  justify= RIGHT, text=rdasn,   fill=kula_7, 
                                width=700, font= do_font) 

root.mainloop() 
