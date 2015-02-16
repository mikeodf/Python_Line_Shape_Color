""" ch3 No.4  
Program name: all_color_names_1.py 
Objective: Show a palette using web colors that are known to Tkinter/Python. 

Keywords: canvas, rectangle, color web color, redundant colors. 
============================================================================79 
Comment: Python or Tkinter has a large collection of colors with known names. 
A selection is shown here. There is no systematic way of way of linking names to hue. 
A reduced list is more useful. 

Author:          Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("All the named colors that Tkinter recognizes") 

cw = 1200                                     # canvas width 
ch = 1100                                      # canvas height 
canvas_1 = Canvas(root, width=cw, height=ch, background="black") 
canvas_1.grid(row=0, column=1) 

#  THE  WHITES 
whiteColors = "snow", "ghost white", "white smoke", "gainsboro", "floral white", "old lace", "linen", 
"antique white", "papaya whip", "blanched almond", "bisque", "peach puff", "navajo white", "moccasin", 
"cornsilk", "ivory", "lemon chiffon", "seashell", "honeydew", "mint cream", "thistle", "snow2", "snow3", 
"snow4", "seashell2", "seashell3", "seashell4", "AntiqueWhite1", "AntiqueWhite2", "AntiqueWhite3", 
"AntiqueWhite4", "bisque2", "bisque3", "bisque4", "PeachPuff2", "PeachPuff3", "PeachPuff4", "NavajoWhite2", 
"NavajoWhite3", "NavajoWhite4" 

# THE BLUES 
blue1Colors = "azure", "alice blue", "azure2", "azure3", "azure4", "SlateBlue1", "SlateBlue2", "SlateBlue3", 
"SlateBlue4", "RoyalBlue1", "RoyalBlue2", "RoyalBlue3", "RoyalBlue4", "blue2","blue4", "DodgerBlue2", "DodgerBlue3",
"DodgerBlue4", "SteelBlue1", "SteelBlue2", "SteelBlue3", "SteelBlue4", "DeepSkyBlue2", "DeepSkyBlue3", "DeepSkyBlue4",
"SkyBlue1", "SkyBlue2", "SkyBlue3", "SkyBlue4", "LightSkyBlue1", "LightSkyBlue2", "LightSkyBlue3", "LightSkyBlue4", 
"SlateGray1", "SlateGray2", "SlateGray3", "SlateGray4", "LightSteelBlue1", "LightSteelBlue2", "LightSteelBlue3", 
"LightSteelBlue4", "LightBlue1", "LightBlue2", "LightBlue3", "LightBlue4", "lavender", "lavender blush", 
"LavenderBlush2", "LavenderBlush3", "LavenderBlush4","midnight blue", "navy", "cornflower blue" 

blue2Colors =  "dark slate blue","slate blue", "medium slate blue", "light slate blue", "medium blue", 
"royal blue", "blue", "dodger blue",\ 
"deep sky blue", "sky blue", "light sky blue", "steel blue", "light steel blue", "light blue", "powder blue" 

# turquoiseColors = "pale turquoise", "dark turquoise", "medium turquoise", "turquoise"  - these are web colors but they do not work in Python/Tkinter.

# THE CYANS 
cyanColors = "LightCyan2", "LightCyan3", "LightCyan4","pale turquoise", "dark turquoise", "medium turquoise", 
"turquoise", "PaleTurquoise1", "PaleTurquoise2", "PaleTurquoise3","PaleTurquoise4", "CadetBlue1", "CadetBlue2", 
"CadetBlue3", "CadetBlue4","turquoise1", "turquoise2", "turquoise3","turquoise4", "cyan2", "cyan3", "cyan4", 
"cyan", "light cyan", "cadet blue" 

# THE MAGENTAS 
magentaColors = "magenta","violet","plum","orchid", "medium orchid", "dark orchid", "dark violet", 
"blue violet", "purple", "purple1","purple2","purple3","purple4","medium purple","MediumPurple1", 
"MediumPurple2","MediumPurple3", "MediumPurple4","thistle1","thistle2","thistle3","thistle4","PaleVioletRed1","PaleVioletRed2", "PaleVioletRed3","PaleVioletRed4", 
"maroon1","maroon2","maroon3","maroon4","VioletRed1","VioletRed2","VioletRed3","VioletRed4", 
"magenta2","magenta3","magenta4","orchid1","orchid2","orchid3","orchid4","plum1","plum2","plum3","plum4", 
"MediumOrchid1","MediumOrchid2","MediumOrchid3","MediumOrchid4","DarkOrchid1","DarkOrchid2","DarkOrchid3","DarkOrchid4" 

# THE REDS 
redColors =  "coral", "light coral", "tomato", "orange red", "red", "hot pink", "deep pink", "pink", "light pink", 
"pale violet red", "maroon", "medium violet red", "violet red", "misty rose","MistyRose2","MistyRose3", 
"MistyRose4","salmon1","salmon2","salmon3","salmon4","LightSalmon2","LightSalmon3","LightSalmon4", 
"tomato2","tomato3","tomato4","OrangeRed2","OrangeRed3","OrangeRed4","red2","red3","red4", 
"IndianRed","LightCoral","Salmon","DarkSalmon","LightSalmon","Red","FireBrick" 
# dud name : ,"crimson" 

pinkColors =  "DeepPink","DeepPink2","DeepPink3","DeepPink4","MediumVioletRed","PaleVioletRed","HotPink","HotPink1","HotPink2", 
"HotPink3","HotPink4","Pink","pink1","pink2","pink3","pink4","LightPink","LightPink1","LightPink2","LightPink3","LightPink4" 

# THE YELLOWS 
yellowColors = yellowcolor= "pale goldenrod",	"light goldenrod yellow", "light yellow", "yellow", "gold", 
"light goldenrod", "goldenrod", "LightGoldenrod1", "LightGoldenrod2", "LightGoldenrod3", "LightGoldenrod4", 
"LightYellow2", "LightYellow3",	"LightYellow4","yellow2","yellow3","yellow4","gold2","gold3","gold4", 
"goldenrod1","goldenrod2","goldenrod3","goldenrod4","DarkGoldenrod1","DarkGoldenrod2","DarkGoldenrod3", 
"DarkGoldenrod4","LemonChiffon2","LemonChiffon3","LemonChiffon4","cornsilk2","cornsilk3","cornsilk4", 
"ivory2","ivory3","ivory4","honeydew2","honeydew3","honeydew4" 

# THE ORANGES 
orangeColors =  "Orange","orange2","orange3","orange4","DarkOrange","DarkOrange1","DarkOrange2","DarkOrange3","DarkOrange4", 
"Coral","coral1","coral2","coral3","coral4","salmon1","salmon2","salmon3","salmon4","LightSalmon","LightSalmon2","LightSalmon3", 
"LightSalmon4","dark salmon","salmon","light salmon","orange","dark orange","OrangeRed","Tomato","tomato2","tomato3","tomato4", 
"OrangeRed2","OrangeRed3","OrangeRed4","red2","red3","red4"  

# GOLDS 
goldColors = "Gold","Yellow","LightYellow","LemonChiffon","LightGoldenrodYellow","PapayaWhip","Moccasin","PeachPuff","PaleGoldenrod", 
"Khaki","DarkKhaki" 

# PURPLES 
purpleColors = "Lavender","Thistle","Plum","Violet","Orchid","Magenta","MediumOrchid","MediumPurple", 
"BlueViolet","DarkViolet","DarkOrchid","DarkMagenta","Purple","SlateBlue","DarkSlateBlue","MediumSlateBlue" 
# dud names:"Fuchsia","Amethyst","Indigo", 

# THE GREENS 
greenColors = "medium aquamarine", "aquamarine", "dark green", "dark olive green", "dark sea green", "sea green", 
"medium sea green", "light sea green", "pale green", "spring green", "lawn green", "green","chartreuse", 
"medium spring green", "green yellow", "lime green", "yellow green", "forest green", "olive drab", "dark khaki", 
"khaki", "aquamarine2", "aquamarine4", "DarkSeaGreen1", "DarkSeaGreen2", "DarkSeaGreen3", "DarkSeaGreen4", 
"SeaGreen1", "SeaGreen2", "SeaGreen3", "PaleGreen1", "PaleGreen2", "PaleGreen3", "PaleGreen4", 
"SpringGreen2", "SpringGreen3", "SpringGreen4", "green2", "green3", "green4", 
"chartreuse2", "chartreuse3", "chartreuse4", "OliveDrab1", "OliveDrab2", "OliveDrab4", 
"DarkOliveGreen1", "DarkOliveGreen2", "DarkOliveGreen3", "DarkOliveGreen4", 
"khaki1", "khaki2", "khaki3", "khaki4" 

# BROWNS 
brown1Colors = "Cornsilk","BlanchedAlmond","Bisque","NavajoWhite","Wheat","BurlyWood","Tan","RosyBrown","SandyBrown","Goldenrod", 
"DarkGoldenrod","Peru","Chocolate","SaddleBrown","Sienna","Brown","Maroon" 
brown2Colors = "dark goldenrod", "rosy brown", "indian red", "saddle brown", "sienna", 
"peru","burlywood","beige","wheat","sandy brown", "tan","chocolate","firebrick","brown", 
"RosyBrown1","RosyBrown2","RosyBrown3","RosyBrown4","IndianRed1","IndianRed2","IndianRed3", 
"IndianRed4","sienna1","sienna2","sienna3","sienna4","burlywood1","burlywood2","burlywood3", 
"burlywood4","brown1","brown2","brown3","brown4","wheat1","wheat2","wheat3","wheat4","tan1", 
"tan2","tan4","chocolate1","chocolate2","chocolate3","firebrick1","firebrick2","firebrick3","firebrick4" 

# GREYS 
greyColors = "Gainsboro","LightGrey","DarkGray","Gray","DimGray","LightSlateGray","SlateGray","DarkSlateGray" 
# dud names:"Silver", 

x_start = 10 
y_start = 25 
x_width = 90 
x_offset = 6 
y_height = 16 
y_offset = 3 
text_offset = 2 
text_width = 90 
kbk = [x_start, y_start, x_start + x_width, y_start + y_height] 

#column 1 
for i in range (0,len(redColors)): 
    kula = redColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(x_start+text_offset,  kbk[1] ,  text=kula, width=text_width, fill ="white", anchor=NW) 
    kbk[1] += y_offset + y_height 
    kbk[3] += y_offset + y_height 
 
#column 2 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width + 2*x_offset 

kbk[1] = y_offset + y_height 
kbk[3] = y_offset + 2 * y_height 

for i in range (0,len(yellowColors)): 
    kula = yellowColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset + y_height 
    kbk[3] += y_offset +  y_height 
 
# column 3 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width + 2*x_offset 

kbk[1] = y_offset + y_height 
kbk[3] = y_offset + 2 * y_height 

for i in range (0,len(brown1Colors)): 
    kula = brown1Colors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset + y_height 
    kbk[3] += y_offset + y_height 

kbk[1] += y_offset  + y_height 
kbk[3] += y_offset  + y_height 
for i in range (0,len(brown2Colors)): 
    kula = brown2Colors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

# column 4 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width + 2*x_offset 

kbk[1] = y_offset  + y_height 
kbk[3] = y_offset  + 2 * y_height 
for i in range (0,len(greenColors)): 
    kula = greenColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

# column 5 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width+ 2*x_offset 

kbk[1] = y_offset  + y_height 
kbk[3] = y_offset  + 2 * y_height 
for i in range (0,len(blue1Colors)): 
    kula = blue1Colors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

# column 6 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width + 2*x_offset 

kbk[1] = y_offset  + y_height 
kbk[3] = y_offset  + 2 * y_height 
for i in range (0,len(blue2Colors)): 
    kula = blue2Colors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

kbk[1] += y_offset  + y_height 
kbk[3] += y_offset  + y_height 
for i in range (0,len(cyanColors)): 
    kula = cyanColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

# column 7 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width + 2*x_offset 

kbk[1] = y_offset  + y_height 
kbk[3] = y_offset  + 2 * y_height 
for i in range (0,len(magentaColors)): 
    kula = magentaColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

# column 8 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width + 2*x_offset 

kbk[1] = y_offset  + y_height 
kbk[3] = y_offset  + 2 * y_height 
for i in range (0,len(whiteColors)): 
    kula = whiteColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height  
    kbk[3] += y_offset  + y_height 

# column 9 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width + 2*x_offset 

kbk[1] = y_offset  + y_height 
kbk[3] = y_offset  + 2 * y_height 
for i in range (0,len(greyColors)): 
    kula = greyColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

kbk[1] += y_offset  + y_height 
kbk[3] += y_offset  + y_height 
for i in range (0,len(orangeColors)): 
    kula = orangeColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

# column 10 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width + 2*x_offset 

kbk[1] = y_offset  + y_height 
kbk[3] = y_offset  + 2 * y_height 
for i in range (0,len(pinkColors)): 
    kula = pinkColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

# column 11 
kbk[0] += x_width + 2*x_offset 
kbk[2] += x_width + 2*x_offset 

kbk[1] = y_offset  + y_height 
kbk[3] = y_offset  + 2 * y_height 
for i in range (0,len(goldColors)): 
    kula = goldColors[i] 
    canvas_1.create_rectangle(kbk, fill=kula) 
    canvas_1.create_text(kbk[0]+10,  kbk[1] ,  text=kula, width=text_width, fill ="black", anchor=NW) 
    kbk[1] += y_offset  + y_height 
    kbk[3] += y_offset  + y_height 

root.mainloop()
