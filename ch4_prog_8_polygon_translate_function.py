""" ch4 No.8 
Polygon Shifting
"""
def translate_shape(shape, x_shift, y_shift): 
    """ Shift (translate) a shape about a given point x_center, y_center. 
    """ 
    new_shape = [] 
    for i in range(int(len(shape)/2 )): 
        x_new = shape[2*i]  + x_shift 
        y_new = shape[2*i+1] + y_shift 
        new_shape.append(x_new) 
        new_shape.append(y_new) 
    return new_shape  

shift_python = translate_shape(python_1, x_shift, y_shift) 
canvas_1.create_polygon(shift_python, outline= 'green', fill='', width=2, smooth=1 )
