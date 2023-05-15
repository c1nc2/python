#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 15:43:25 2023

@author: office
"""

def find_integer(n):
    """Find the first positive integer between 101 and less than n that is divisible by 21"""
    for i in range(101, n):
        if (i % 21 == 0):
            return i

def test(condition): 
    assert condition, "Test failed"
    print("Test passed")

test(find_integer(110) == 105)
test(find_integer(1000000) == 105)

