#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 16:12:31 2023

@author: office
"""
range_promise = range(10) # Create a lazy promise

list_from_range_promise = list(range_promise) # Call in promise, to produce a list

print(list_from_range_promise)