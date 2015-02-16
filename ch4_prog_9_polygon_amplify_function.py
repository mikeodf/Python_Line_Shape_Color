""" ch4 No.9 
The Amplification function
"""
def amplify_2d_shape(shape, x_amplify, y_amplify): 
    """ Expand or contract a shape about the center of its bounding box. 
    """ 
    new_shape = [] 
    xy_bunch = locate_shape(python_1) 
    x_cen = xy_bunch[0][0] 
    y_cen = xy_bunch[0][1] 
    wid = xy_bunch[1][0]  
    hgt = xy_bunch[1][1] 
    x_org = x_cen - wid/2 
    y_org = y_cen - hgt/2   
    for i in range(int(len(shape)/2 )): 
        x_ampd = (shape[2*i]   - x_org)*x_amplify + x_org - wid*(x_amplify - 1)/2 
        y_ampd = (shape[2*i+1] - y_org)*y_amplify + y_org - hgt*(y_amplify - 1)/2 
        new_shape.append(x_ampd) 
        new_shape.append(y_ampd) 
    return new_shape 
