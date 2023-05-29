#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:25:42 2023

@author: office
"""

class Rectangle:
    """ A class to manufacture rectangle objects"""

    def __init__(self, posn, w, h):
        """Initialize rectangle at posn, with width W, h """
        self. corner = posn
        self.width = W
        self. height = h

def __str__(self):
    return " ({0}, {1}, {2})"
format (self. corner, self width, self. height)

box = Rectangle (Point (0, 0), 100, 200)
bomb = Rectangle(Point (100, 80), 5, 10)
print("box: ", box)
print("bomb: ", bomb)