#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:17:54 2023

@author: office
"""

def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
            return wd
    
    return ""