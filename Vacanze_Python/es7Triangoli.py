
def is_triangle(sides):
    for i in sides:
        if any(sides) <= 0:
            return False
        if sum(sides) - i < i:
            return False
    return True
    
def equilateral(sides):
    if not is_triangle(sides):
        test = False
    else:
        test: True = len(set(sides)) == 1
    return test
    
def isosceles(sides):
    if not is_triangle(sides):
        test = False
    else:
        test: True = len(set(sides)) in [1, 2]
    return test
    
def scalene(sides):
    if is_triangle(sides) and not isosceles(sides) and not equilateral(sides):
        return True
    return False
    
triangle = [0, 0, 0]
equilateral(triangle)
isosceles(triangle)
scalene(triangle)