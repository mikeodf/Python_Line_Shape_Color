""" ch4 No.5 
Program name: poly_twists_1.py 
Objective: Demonstrate the fill rules for polygons with external and 
internal odd-even color areas. 

Keywords: canvas,  polygon, internal, external, spaces, odd-even fill 
============================================================================79 
Comments: Only internal twisted loops result in fill cancellation 

Tested on: Python 2.6, Python 2.7, Python 3.2 
Author: Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title('Twisted polygons') 
cw = 800                                     # canvas width. 
ch = 650                                      # canvas height. 
canvas_1 = Canvas(root, width=cw, height=ch, background="#664444") 
canvas_1.grid(row=0, column=1) 

twist_1 = [ 204.6,93.7 , 116.0,93.7 , 100.3,97.3 , 90.3,103.4 , 83.9,113.7 , 
 82.5,129.5 , 90.3,140.9 , 103.9,148.0 , 120,152.3 , 135.7,151.2 , 
 312.8,151.2 , 328.2,151.2 , 341.4,147.0 , 351.0,139.8 , 358.2,131.2 , 
 357.8,115.9 , 350.7,105.2 , 337.8,97.7 , 324.6,93.7 , 306.7,93.4 , 237.1,94.1 ] 
canvas_1.create_polygon(twist_1, width = 2, fill='#6a0aab',  outline='#d2f700',smooth = 1) 

twist_2 = [  191.7,222.3 , 120,222.0 , 107.8,222.3 , 95.3,224.1 , 84.2,228.4 , 74.2,241.6 , 72.5,255.2 , 80.3,268.0 , 92.8,275.2 , 108.2,279.5 , 128.2,279.1 , 185.7,280.2 , 236.7,222.7 , 309.6,222.7 , 320,222.3 , 332.1,227.0 , 343.5,236.2 , 348.9,245.2 , 348.2,259.5 , 340.3,269.5 , 326.7,277.0 , 315,279.8 , 294.6,279.8 , 235,280.2  ] 
canvas_1.create_polygon(twist_2, width = 2, fill='#9c02a7', outline='#d2f700', smooth = 1) 

twist_3 = [  136.4,349.8 , 103.9,349.8 , 89.6,349.8 , 76.0,353.4 , 65.7,361.6 , 60.7,371.6 , 60.3,384.5 , 68.5,395.2 , 83.2,404.5 , 98.9,405.9 , 119.2,406.2 , 133.2,406.6 , 169.6,349.5 , 199.2,349.1 , 232.8,349.8 , 265.3,406.6 , 294.2,406.2 , 313.9,405.9 , 325.7,398.0 , 336.4,386.2 , 336.0,372.0 , 328.2,360.9 , 315.7,353.0 , 303.5,350.5 , 281.7,349.1 , 265.71429,350.2 , 227.8,406.6 , 194.6,406.6 , 154.2,407.3 ] 
canvas_1.create_polygon(twist_3, width = 2, fill='#cb0077',  outline='#d2f700', smooth = 1) 

loop_1 = [  541.0,40.9 , 502.5,54.5 , 470,89.1 , 468.2,146.2 , 503.9,185.2 , 538.9,198.4 , 586.0,197.0 , 625,176.6 , 649.6,139.5 , 649.2,95.9 , 617.8,56.6 , 573.9,40.2 ] 
canvas_1.create_polygon(loop_1, width = 2, fill='#6a0aab' , outline='#d2f700', smooth = 1 ) 

loop_2 = [ 546.7,241.6 , 508.9,256.2 , 478.5,291.6 , 477.1,345.5 , 507.5,383.7 , 543.2,398.7 , 601.7,395.9 , 642.8,369.1 , 657.1,339.5 , 655.3,293.0 , 620,253.7 , 584.2,242.00504 , 544.6,269.5 , 520.7,284.1 , 506.7,304.5 , 507.8,338.0 , 526.0,360.5 , 550,372.7 , 586.0,371.6 , 615.3,354.1 , 629.2,327.3 , 624.2,299.1 , 606.7,278.4 , 578.2,267.0 ] 
canvas_1.create_polygon(loop_2, width = 2, fill='#9c02a7', outline= '#d2f700', smooth = 1) 

loop_3 = [ 561.0,452.0 , 523.2,464.1 , 492.1,495.2 , 482.8,537.0 , 497.5,574.1 , 537.1,604.8 , 590,609.8 , 637.5,592.0 , 665,561.6 , 671.7,522.0 , 654.6,484.8 , 622.8,459.8 , 592.5,451.2 , 555.3,479.8 , 528.2,496.6 , 515.3,523.0 , 520,550.9 , 545.7,576. , 591.4,554.1 , 611.0,541.6 , 613.5,520.5 , 598.9,506.2 , 576.7,500.9 , 552.1,508.75 , 540,527.0 , 545.7,544.5 , 566.0,556.6 , 599.6,580.2 , 618.5,570.9 , 635.3,551.6 , 639.2,528.4 , 631.0,502.3 , 609.2,484.1 , 585.3,475.9 ] 

canvas_1.create_polygon(loop_3, width = 2, fill='#cb0077', outline='#d2f700', smooth = 1) 

root.mainloop()