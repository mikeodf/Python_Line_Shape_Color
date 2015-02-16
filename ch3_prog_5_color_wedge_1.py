""" ch3 No.5  
Program name: color_wedge_1.py 
Objective: Draw a single color wedge with varying brightness. 

Keywords: canvas, canvas, color, wedge 
============================================================================79 
Comments: 

Tested on: Python 2.6, Python 2.7.3, Python 3.2.3 
Author: Mike Ohlson de Fine       
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("Color wedge") 

cw = 200                                     # canvas width 
ch = 300                                      # canvas height 
chart_1 = Canvas(root, width=cw, height=ch, background="white") 
chart_1.grid(row=0, column=0) 

x_tip = 100 
y_tip = 250 
width= 50         #standard disk diameter 
hite = width*2  # median wedge height. 

# Draw the background dark-red triangle. 
kula = "#660000" 
wedge =[ x_tip, y_tip, x_tip-width,y_tip-4.4*width, x_tip+width, y_tip-4.4*width ]
chart_1.create_polygon(wedge,fill=kula) 

hFac = [0.25,   0.45,  0.75,  1.2,  1.63,  1.87,  2.05]  # Proportional height factors. 
wFac = [0.2,   0.36,  0.6,   1.0,   0.5,   0.3,  0.25]      # Proportional width factors. 

kulas = [ "#000000","#c80000", "#a00000", "#ff0000", "#ff5050", "#ff8c8c", "#ffc8c8"] 

for i in range(len(kulas)): 
    x0 = x_tip-width*wFac[i]/2 
    y0 = y_tip-hite*hFac[i]  +width*wFac[i]/2 
    x1 = x_tip+width*wFac[i]/2 
    y1 = y_tip-hite*hFac[i] - width*wFac[i]/2 
    chart_1.create_oval(x0,y0 ,x1 ,y1 ,  fill=kulas[i], outline=kulas[i]) 
    
root.mainloop()
