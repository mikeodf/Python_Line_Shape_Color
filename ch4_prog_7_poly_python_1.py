""" ch4 No.7 
Program name: poly_python_1.py 
Objective: Illustrate polygon shape parameters. 

Keywords: canvas, shapedemonstration, center, bounding box. 
============================================================================79 
Comments: Take note of the instruction  "for i in range(int(len(shape)/2)):" in the function "locate_shape(shape)". It has to have the "int(...) in order to work under Python 3.xx. 
Without it we get and error as follows: 

  for i in range(len(shape)/2):    # Separate out the x and components. 
TypeError: 'float' object cannot be interpreted as an integer 

Under Python 2.xx the form "for i in range(len(shape)/2):" works fine. 

Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author: Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher. 
root = Tk() 
root.title("Show a Python.") 
canvas_1 = Canvas(root, width=500, height=400, background="white") 
canvas_1.grid(row=0, column=1) 

python_1 = [ 75.2,186.9 , 76.26,177.8 , 73.9,167.9 , 72.5,160.3, 72.6,147.2 
 , 78.2,125.0 , 90.4,106.8 , 106.0,93.4 , 129.0,83.8 , 155.3,81.1 
 , 182.3,88.6 , 203.5,103.5 , 218.9,124.5 , 227.7,155.0 , 224.7,183.1 
 , 213.3,205.8 , 200.7,222.5 , 197.7,244.2 , 205.8,263.9 , 225.2,278.3 
 , 246.2,281.6 , 265.4,275.0 , 279.8,260.9 , 286.1,243.7 , 283.8,224.2 
 , 273.7,204.0 , 266.1,182.6 , 264.9,159.6 , 272.7,134.1 , 288.3,112.4 
 , 309.6,97.0 , 333.8,89.1 , 362.1,90.6 , 387.3,101.3 , 404.0,116.7 
 , 413.1,131.3 , 416.9,138.9 , 420.3,145.8 , 425.7,150.2 , 433.6,151.5 
 , 440.6,161.4 , 441.4,171.0 , 440.9,176.3 , 440.9,181.6 , 435.6,184.6 
 , 430.3,184.3 , 425.0,182.8 , 419.7,182.1 , 411.3,175.8 , 408.2,165.8 
 , 409.1,159.3 , 408.8,153.3 , 405.4,147.2 , 399.7,141.9 , 389.9,136.4 
 , 382.8,132.1 , 376.2,127.3 , 360.3,120.7 , 341.4,119.7 , 324.2,126.0 
 , 310.3,138.6 , 301.0,156.8 , 299.7,175.8 , 304.5,192.9 , 316.1,214.9 
 , 321.4,233.8 , 322.9,252.8 , 317.6,274.5 , 305.8,295.5 , 288.6,311.6 
 , 265.4,323.2 , 237.1,326.0, 211.1,318.79 , 190.1,304.8 , 172.4,282.1 
 , 165.6,257.3 , 167.4,225.2 , 179.5,199.5 , 190.6,182.3 , 195.4,160.38 
 , 190.9,138.4 , 177.0,119.4 , 155.3,108.3 , 131.0,106.1 , 108.0,114.4 
 , 92.4,130.3 , 85.1,144.7 , 84.0,157.3 , 84.6,170.4 , 82.3,183.1 
 , 78.2,188.1 , 76.1,188.8 ] 


def locate_shape(shape): 
    """ Calculate the bounding box location, center and dimensions. 
         x_org, y_org is the bottom-left corner, the origin. 
         wid is the width of the bounding box, hgt is the height. 
         and x_cen, y_cen is the center of the bounding box. 
    """    
    x_list = [] 
    y_list = [] 
    for i in range(int(len(shape)/2)):    # Separate out the x and components. 
        x_list.append(shape[2*i]) 
        y_list.append(shape[2*i+1]) 
    x_org = min(x_list) 
    y_org = min(y_list) 
    wid = max(x_list) - x_org 
    hgt = max(y_list) - y_org 
    x_cen = x_org + wid/2.0 
    y_cen = y_org + hgt/2.0 
    xy_cen = [x_cen, y_cen] 
    xy_size = [ wid, hgt] 
    return xy_cen, xy_size 

def show_shape_metrics(shape): 
    """ Draw the shape, its bounding box, the center and graphical origin. 
    """ 
    xy_bunch = locate_shape(shape) #return xy_cen, xy_size 
    x_cen = xy_bunch[0][0] 
    y_cen = xy_bunch[0][1] 
    wid = xy_bunch[1][0] 
    hgt = xy_bunch[1][1] 
    x_org = x_cen - wid/2 
    y_org = y_cen - hgt/2 
    canvas_1.create_oval(x_cen-5, y_cen-5,  x_cen+5, y_cen+5, outline= 'red', fill='', width=1 )    
    canvas_1.create_rectangle(x_cen- wid/2, y_cen-hgt/2,  x_cen+wid/2, y_cen+hgt/2, outline= 'black', fill='', width=1 )      
    canvas_1.create_rectangle(x_org -8, y_org -8, x_org +8, y_org +8, outline= 'red', fill='', width=1 ) 

show_shape_metrics(python_1) 
canvas_1.create_polygon(python_1, outline='black', fill='', width= 4 ) 

root.mainloop()
