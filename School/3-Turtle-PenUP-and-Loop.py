#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:36:28 2023

@author: office
"""

import turtle
turtle. clear() 

wn = turtle.Screen()
wn.bgcolor("Lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()
size = 20 # This is new

for i in range(30):
    tess.stamp() # Leave an impression on the canvas
    size = size + 3 # Increase the size on every iteration
    tess.forward(size) #Move tess along
    tess.right(24)  # and turn her

wn.mainloop()
turtle.bye()