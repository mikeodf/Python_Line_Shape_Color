""" ch6 No.11  
Program name: python_text_banner_1.py 
Objective: Display a banner with DIY fonts. 

Keywords: canvas, polygon, diy fonts. 
============================================================================79 
Comments: 

Tested on: Python 2.6, Python 2.7, Python 3.2.3 
Author: Mike Ohlson de Fine 
""" 
from Tkinter import * 
#from tkinter import *  # For Python 3.2.3 and higher.
root = Tk() 
root.title("Python Banner.") 
canvas_1 = Canvas(root, width=750, height=400, background="#000044") 
canvas_1.grid(row=0, column=1) 

p_1 = [15.7,340.2  , 39.3,250.2  , 39.3,119.5   , 135.0,116.6 , 
       167.1,139.5 , 181.4,165.2 , 181.4,209.5  , 163.6,231.6 , 
       134.3,248.1 , 85.7,253.1  , 102.1,339.5  ] 

p_2 = [85.7,168.8  , 106.4,168.8 , 117.9,175.9 , 
       117.1,187.4 , 107.1,196.6 , 91.4,196.6] 

t_1 = [192.1,84.5  , 264.3,115.9 , 299.3,118.1  , 369.3,85.9  , 
       367.9,136.6 , 306.4,156.6 , 331.4,338.8  , 254.3,340.9 , 
       275.7,158.1 , 189.3,121.6  ] 

o_1 = [492.1,118.1 , 459.3,158.1 , 456.4,228.8 , 468.6,278.8 , 
       489.3,320.9 , 507.9,337.4 , 528.6,338.1 , 541.4,324.5 , 
       569.3,278.8 , 579.3,221.6 , 577.1,151.6 , 559.3,126.6 , 
       538.6,117.4 , 505.7,117.4  ] 

o_2 = [519.3,170.9 , 510.7,174.5 , 506.4,181.6 , 509.3,193.1 , 
       524.3,196.6 , 533.6,187.4 , 532.9,176.6 , 527.9,171.6  ] 

n_1 = [561.4,335.9 , 592.9,295.9 , 603.6,119.5 , 637.9,127.4 , 
       664.3,201.6 , 674.3,127.4 , 717.1,113.1 , 697.9,271.6 , 
       725.0,341.6 , 669.3,338.8 , 631.4,232.4 , 624.3,337.4  ] 

y_1 = [198.6,145.2 , 200.0,229.5 , 157.1,312.4 , 122.1,340.9 , 
       236.4,338.1 , 200.0,310.2 , 231.4,228.8 , 259.3,169.5 , 
       235.7,160.2 , 222.9,190.9 , 221.4,156.6] 

h_1 = [361.4,153.8 , 383.6,145.9 , 384.3,198.1 , 405.0,193.8 , 
       403.6,140.2 , 432.9,130.2 , 439.3,338.8 , 414.3,338.8 , 
       410.0,255.9 , 388.6,258.8 , 387.9,338.1 , 359.3,339.5] 

# Dark glow. 
canvas_1.create_polygon(p_1, outline='#640000', fill='', width=16 ) 
canvas_1.create_polygon(y_1, outline='#640000', fill='', width=16 ) 
canvas_1.create_polygon(t_1, outline='#640000', fill='', width=16 ) 
canvas_1.create_polygon(h_1, outline='#640000', fill='', width=16 ) 
canvas_1.create_polygon(o_1, outline='#640000', fill='', width=16 ) 
canvas_1.create_polygon(n_1, outline='#640000', fill='', width=16 ) 

# Main body. 
canvas_1.create_polygon(p_1, outline='red', fill='#880000', width=6 ) 
canvas_1.create_polygon(p_2, outline='red', fill="#000044", width=6 ) 
canvas_1.create_polygon(y_1, outline='red', fill='#880000', width=6 ) 
canvas_1.create_polygon(t_1, outline='red', fill='#880000', width=6 ) 
canvas_1.create_polygon(h_1, outline='red', fill='#880000', width=6 ) 
canvas_1.create_polygon(o_1, outline='red', fill='#880000', width=6 ) 
canvas_1.create_polygon(o_2, outline='red', fill="#000044", width=6 ) 
canvas_1.create_polygon(n_1, outline='red', fill='#880000', width=6 ) 

# Inner incandescence. 
canvas_1.create_polygon(p_1, outline='#ff8888', fill='', width=2 ) 
canvas_1.create_polygon(p_2, outline='#ff8888', fill='', width=2 ) 
canvas_1.create_polygon(y_1, outline='#ff8888', fill='', width=2 ) 
canvas_1.create_polygon(t_1, outline='#ff8888', fill='', width=2 ) 
canvas_1.create_polygon(h_1, outline='#ff8888', fill='', width=2 ) 
canvas_1.create_polygon(o_1, outline='#ff8888', fill='', width=2 ) 
canvas_1.create_polygon(o_2, outline='#ff8888', fill='', width=2 ) 
canvas_1.create_polygon(n_1, outline='#ff8888', fill='', width=2 ) 

root.mainloop()
