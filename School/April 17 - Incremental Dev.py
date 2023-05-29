

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    print(" \n ===== \n X difference: ", dx)
    dy = y2 - y1
    print("dy: ", dy)
    dsq = dx**2 + dy**2
    print("dsq: ", dsq)
    result = dsq**0.5
    return result

def take_input_from_user():
    xx1 = float(input("\n Please Enter x1: 1"))
    yy1 = float(input("\n Please Enter y1: "))
    xx2 = float(input("\n Please Enter x2: "))
    yy2 = float(input("\n Please Enter y2: "))
    return distance (xx1, yy1, xx2, yy2)

the_distance = take_input_from_user()
print(the_distance)



