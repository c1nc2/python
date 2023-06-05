#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:59:33 2023

@author: office
"""

import turtle

def draw_multicolor_square(t, sz):
    """Make turtle t draw a multi-color square of SZ."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 20 # Size of the smalLest square
for i in range (15):
    draw_multicolor_square(tess, size) 
    size = size + 10 # Increase the size for next time
    tess.forward(10) # Move tess along a Little
    tess.right(18) # and give her some turn

wn.mainloop()



