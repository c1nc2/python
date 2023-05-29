#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:44:31 2023

@author: office
"""

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0): 
        """Create new point at x, y"""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Compute my distance from the origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
p = Point(3, 4)
print(p.x)