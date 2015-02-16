""" ch3 No.7  
Program name: color_selector_mixer_1.py 
Objective: Use the color selector that comes with Tkinter. 

Keywords: color construction, selection, mixer. 
============================================================================79 
Comments: Remarkably simple.  However the Tkinter name is tkColorChoose 
and the tkinter name is tkinter.colorchooser.

Tested on: Python 2.6, 
Author: Mike Ohlson de Fine 
""" 
#from tkinter import *  # For Python 3.2.3 and higher.
from tkColorChooser import askcolor 
#from tkinter.colorchooser import askcolor 
askcolor()

