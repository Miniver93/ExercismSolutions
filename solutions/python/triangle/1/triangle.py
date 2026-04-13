def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return a == b == c and (a + b + c) > 1

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    current_s = 0 
    actual_value = 0 
    sorted_array = sorted(sides, reverse=True)
    for i in sorted_array:
        if i != 0:
            if current_s / i == 1:
                actual_value += 1
        current_s = i
    return (actual_value == 1 or actual_value == 2) and ((a + b >= c) and (b + c >= a) and (a + c >= b))
        


def scalene(sides):
    sides_sorted = sorted(sides, reverse=True)
    a = sides_sorted[0]
    b = sides_sorted[1]
    c = sides_sorted[2]

    if(a != b and b != c and b + c >= a):
        return True
    else: 
        return False
                
        
