ch 3 No.13
# color transitions 
#================================================= 
# Colors specified as Hex rrggbb (full scale = ff) 
start_color_hex_1 = '#ff0000' 
end_color_hex_1   = '#ffff00' 

start_color_hex_2 = '#00ffff' 
end_color_hex_2  =  '#0000ff' 

start_color_hex_3 = '#000000' 
end_color_hex_3 =  '#ffffff' 

start_color_hex_4 = '#0088ff' 
end_color_hex_4 =  '#000033' 

start_color_hex_5 = '#00ff00' 
end_color_hex_5 =  '#ff0000' 

start_color_hex_6 = '#fff700' 
end_color_hex_6 =  '#0000ff' 
 
start_color_hex_7 = '#e339a4' 
end_color_hex_7   = '#7746d7' 

start_color_hex_8 = '#890043' 
end_color_hex_8   = '#2a0671' 

#================================================ 
# Swatch geometry 
#================ 
x_start = 20 
y_start = 10 
width = 40 
height = 40 
gap = 8 
num_steps = 8 
#=============================================== 
# Generate the color series and display them.
#===============================
kulas = discrete_kula_series(start_color_hex_1, end_color_hex_1, num_steps ) 
for i in range(num_steps): 
    show_swatch(kulas[i], x_start, y_start, width, height, gap) 
    y_start += height+gap 

x_start += width + 110 
y_start = 10 
kulas = discrete_kula_series(start_color_hex_2, end_color_hex_2, num_steps ) 
for i in range(num_steps): 
    show_swatch(kulas[i], x_start, y_start, width, height, gap) 
    y_start += height+gap 

x_start += width + 110 
y_start = 10 
kulas = discrete_kula_series(start_color_hex_3, end_color_hex_3, num_steps ) 
for i in range(num_steps): 
    show_swatch(kulas[i], x_start, y_start, width, height, gap) 
    y_start += height+gap 

x_start += width + 110 
y_start = 10 
kulas = discrete_kula_series(start_color_hex_4, end_color_hex_4, num_steps ) 
for i in range(num_steps): 
    show_swatch(kulas[i], x_start, y_start, width, height, gap) 
    y_start += height+gap 

x_start += width + 110 
y_start = 10 
kulas = discrete_kula_series(start_color_hex_5, end_color_hex_5, num_steps ) 
for i in range(num_steps): 
    show_swatch(kulas[i], x_start, y_start, width, height, gap) 
    y_start += height+gap 

x_start += width + 110 
y_start = 10 
kulas = discrete_kula_series(start_color_hex_6, end_color_hex_6, num_steps ) 
for i in range(num_steps): 
    show_swatch(kulas[i], x_start, y_start, width, height, gap) 
    y_start += height+gap 

x_start += width + 110 
y_start = 10 
kulas = discrete_kula_series(start_color_hex_7, end_color_hex_7, num_steps ) 
for i in range(num_steps): 
    show_swatch(kulas[i], x_start, y_start, width, height, gap) 
    y_start += height+gap 

x_start += width + 110 
y_start = 10 
kulas = discrete_kula_series(start_color_hex_8, end_color_hex_8, num_steps ) 
for i in range(num_steps): 
    show_swatch(kulas[i], x_start, y_start, width, height, gap) 
    y_start += height+gap 
