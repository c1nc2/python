#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:55:10 2023

@author: office
"""

import turtle
turtle.clear()

def draw_square(t, sz):
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets function")

alex = turtle.Turtle() # Create alex
draw_square(alex, 50) # Call the function to draw the square
wn.mainloop()
turtle.bye()