def r sum(nested num list):
tot 0
for element in nested num list:
if type(element) type([]):
tot += r_sum (element)
else
tot += element
return tot

print (r_sum([1,2, [3, [3,5]],4]))