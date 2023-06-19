from mytestlib import test

def share_diagonal(x0, yo, x1, y1): IT IF TI Is (xe, ye) on a shared diagonal with (x1, y1)? 11 IT IT
dy = abs (y1 - ye)
dx = abs (x1 - x@) # Calc the absolute y distance
# CXalc the absolute x distance
return dx dy # They clash if dx == dy

test (not share_diagonal(5,2,2,0))
test (share_diagonal(5,2,3,0))
test (share_diagonal(5,2,4,3))
test (share_diagonal(5,2,4,1))