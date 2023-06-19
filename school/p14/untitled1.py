def col_clashes(bs, c):
"" Return True if the queen at column c clashes
with any queen to its Left. TE IF IF

for i in range(c): # Look at all columns to the left of C
if share_diagonal(i, bs[i], c, bs[c]):
return True

return False # No clashes col c has a safe placement.

# Solutions cases that should not have any clashes
test (not col_clashes ([6,4,2,0,5], 4))
test (not col_clashes([6,4,2,0,5,7,1,3], 7))

# More test cases that should mostly clash
test (col_clashes ([0,1], 1))
test (col_clashes([5,6],
test (col_clashes([6,5], 1))
test (col_clashes([0,6,4,3], 3))
test (col_clashes ([5,0,7], 2))
test (not col_clashes([2,0,1,3], 1))
test (col_clashes([2,0,1,3], 2))