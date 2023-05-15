#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:02:39 2023

@author: office
"""

def final_amt(p, r, n, t):
    """Apply the compound interest formula to p to produce the final amount"""
    a = p * (1 + r/n) ** (n*t)
    return a # this is new, and makes the function fruitful

# now that we have the function above, let us call it 
toInvest = float(input("How much do you want to invest? "))
fn1 = final_amt(toInvest, 0.08, 12, 5)
print("At the end of the period you'll have", fn1)


#Naming
#def final_amt_v2(principalAmount, nominalPercentageRate, numTimesPerYear, years):
 #   """Apply the compound interest formula to p to produce the final amount"""
  #  a = principalAmount * (1 + nominalPercentageRate/numTimesPerYear) ** (numTimesPerYear*years)
   # return a # this is new, and makes the function fruitful