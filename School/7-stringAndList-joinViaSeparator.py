#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 15:28:20 2023

@author: office
"""


song = "The rain in Spain..."
wds = song.split()

glue = ";"
s = glue.join(wds)

# join with a separator

print(" --- ".join(wds))

print("".join(wds))
