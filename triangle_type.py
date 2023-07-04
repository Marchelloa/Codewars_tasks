# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    
    check_triangle = [a + b > c, b + c > a, a + c > b]
    if not all(check_triangle):
        return 0
    
    c1, c2, h = sorted([a, b, c]) 
    if pow(c1, 2) + pow(c2, 2) == pow(h, 2):
        return 2
    if pow(h, 2) > pow(c1, 2) + pow(c2, 2):
        return 3
    else:
        return 1 
