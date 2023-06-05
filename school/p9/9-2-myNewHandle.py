#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:47:55 2023

@author: office
"""

mynewhandle = open("test. txt", "r")
while True:                             # Keep reading forever
    theline = mynewhandle.readline()   #  Try to read next line
    if len(theline) == 0:              # if there are no more Lines
        break                         # Leave the Loop

    # Now process the Line we've just read
    print(theline, end="")

mynewhandle.close()