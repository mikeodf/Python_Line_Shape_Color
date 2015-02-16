""" ch2 No.11  """
def round_rectangle_centered(x_center, y_center, x_width, y_height, corner_radius, line_width, outline_kula): 
    """ Draw a rounded rectangle with all parameters selectable. 
        The center, width and height are the primary choices. 
    """ 

    pt1 = x_center - x_width/2, y_center + y_height/2 - corner_radius # Left lower. 
    pt2 = x_center - x_width/2, y_center - y_height/2 + corner_radius # Left upper. 
    pt3 = x_center - x_width/2 + corner_radius, y_center - y_height/2 # Top left. 
    pt4 = x_center + x_width/2 - corner_radius, y_center - y_height/2 # Top right. 
    pt5 = x_center + x_width/2 , y_center - y_height/2 +corner_radius # Right upper. 
    pt6 = x_center + x_width/2, y_center + y_height/2 - corner_radius # Right lower. 
    pt7 = x_center + x_width/2 - corner_radius, y_center + y_height/2 # Bottom right. 
    pt8 = x_center - x_width/2 + corner_radius, y_center + y_height/2 # Bottom left. 
 
    arc2 = pt2[0], pt2[1] + corner_radius 
    arc3 = pt3[0] + corner_radius , pt3[1] 
    arc4 = pt4[0] - corner_radius, pt4[1] + 2 *corner_radius 
    arc5 = pt5[0] , pt5[1] - corner_radius 
    arc6 = pt6[0] , pt6[1] - corner_radius 
    arc7 = pt7[0]- corner_radius , pt7[1] 
    arc8 = pt8[0] + corner_radius , pt8[1] 
    arc1 = pt1[0] , pt1[1] - corner_radius 
 
    canvas_1.create_line(pt1, pt2, fill=outline_kula, width = line_width) 
    canvas_1.create_line(pt3, pt4, fill=outline_kula, width = line_width) 
    canvas_1.create_line(pt5, pt6, fill=outline_kula, width = line_width) 
    canvas_1.create_line(pt7, pt8, fill=outline_kula, width = line_width) 

    canvas_1.create_arc(arc2, arc3, style=ARC, start=89,  extent=92,  outline=outline_kula, width=line_width) # Top left. 
    canvas_1.create_arc(arc4, arc5, style=ARC, start=0,   extent=91,  outline=outline_kula, width=line_width) # Top right. 
    canvas_1.create_arc(arc6, arc7, style=ARC, start=269, extent=91,  outline=outline_kula, width=line_width) # Bottom right. 
    canvas_1.create_arc(arc8, arc1, style=ARC, start=-90, extent=-91, outline=outline_kula, width=line_width) # Bottom left.
