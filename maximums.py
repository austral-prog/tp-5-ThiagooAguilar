def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x <= y :
       return y
    else:
       return x
def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x <= y and z <= y :
       return y
    elif y <= z and x <= z :
       return z
    else:
       return x
max_of_two(5,4)
max_of_two(-2,-3)
max_of_two(0,0)
max_of_three(-2,-3,-1)
max_of_three(0,0,0)
