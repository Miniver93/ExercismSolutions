def square(number):
    value_accumulated = 0
    array_chest = []
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    for i in range(65):
        if i == 1:
            value_accumulated = 1
            array_chest.append(value_accumulated)
        else:
            value_accumulated *=2
            array_chest.append(value_accumulated)

    return array_chest[number]
            
        
    


def total():
    return square(64) * 2 - 1
