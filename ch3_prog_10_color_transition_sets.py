""" ch3 No.10 
code name: Various color transition sets.
""" 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# White → Grey → Black 
xy_start = [ 20, xy_start[1] ] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [100.0,   0.0 ], [ 100.0,  0.0 ], [ 100.0, 0.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# White → Violet. 
xy_start = [ 20, xy_start[1] + y_gap + swatch_height ] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [100.0,   100.0 ], [ 100.0,  0.0 ], [ 100.0, 100.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# White → Yellow
xy_start = [ 20, xy_start[1] + y_gap + swatch_height] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [100.0,   100.0 ], [ 100.0,  100.0 ], [ 100.0, 0.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# White → Blue
xy_start = [ 20, xy_start[1] + y_gap + swatch_height] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [100.0,   00.0 ], [ 100.0,  0.0 ], [ 100.0, 100.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# White → Red 
xy_start = [ 20, xy_start[1] + y_gap + swatch_height] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [100.0,   100.0 ], [ 100.0,  0.0 ], [ 100.0, 0.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# White → Green 
xy_start = [ 20, xy_start[1] + y_gap + swatch_height] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [100.0,   0.0 ], [ 100.0,  100.0 ], [ 100.0, 0.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# Red → Green 
xy_start = [ 20, xy_start[1] + y_gap + swatch_height] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [100.0,   0.0 ], [ 0.0,  100.0 ], [ 0.0, 00.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# Blue → Green 
xy_start = [ 20, xy_start[1] + y_gap + swatch_height] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [0.0,   0.0 ], [ 0.0,  100.0 ], [ 100.0, 00.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# Red - > Blue 
xy_start = [ 20, xy_start[1] + y_gap + swatch_height] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [100.0,   0.0 ], [ 0.0,  0.0 ], [ 0.0, 100.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# Red 
num_steps = 83 
xy_start = [ 20, xy_start[1] + y_gap + swatch_height] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [100.0,   0.0 ], [ 0.0,  0.0 ], [ 0.0, 0.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# Green 
xy_start = [ 103, xy_start[1] ] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [0.0,   0.0 ], [ 100.0,  0.0 ], [ 0.0, 0.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
# Blue 
xy_start = [ 186, xy_start[1] ] 
Red_ramp1, Green_ramp1, Blue_ramp1       = [0.0,   0.0 ], [ 0.0,  0.0 ], [ 100.0, 0.0 ] 
xy_start[0] = kula_ramp(xy_start, Red_ramp1, Green_ramp1, Blue_ramp1, num_steps) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
