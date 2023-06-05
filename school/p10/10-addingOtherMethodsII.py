#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:12:51 2023

@author: office
"""

def print_point (pt):
print ("({0}, {1})". format (pt.x, pt.y))

class Point:
    #

    def to_string (self):
        return "({0}, {1})". format (self.x, self.y)


class Point:
# ..

engedef _str__(self): # ALL we have done is renamed the method
return " ({0}, {1})". format (self.x, self.y)