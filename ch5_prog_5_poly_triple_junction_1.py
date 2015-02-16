""" ch5 No.5 
Program name: poly_triple_junction_1.py 
Objective: Draw the internal portion of lines where they penetrate polygons. 

{ The code inserted here are the numerical list composing the set of polygon sun_poly
and the functions:
def get_line_params(line): ...
def inner_box(line_1, line_2): …
def inner_intersection(line_1, line_2): ...
def internal_segment(lines, polygons): ...
- all the above are identical to those in the example above }
"""

# Execute and Demonstrate – dense raster of horizontal lines.. 
# ============================================ 
x_start, y_start, line_length, gap = 10, 10, 630, 10 
new_line = [x_start, y_start, x_start+line_length, y_start] 
for i in range(60): 
    for j in range(len(sun_poly)): 
        internal_segment(new_line, sun_poly[j],'red') 
    new_line =  [x_start, y_start+i*gap, x_start+line_length, y_start+i*gap] 

y_start = 15 
new_line = [x_start, y_start, x_start+line_length, y_start] 
for i in range(60): 
    for j in range(len(sun_poly)): 
        internal_segment(new_line, sun_poly[j],'green') 
    new_line =  [x_start, y_start+i*gap, x_start+line_length, y_start+i*gap] 

root.mainloop() 
