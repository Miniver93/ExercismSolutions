def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    steps = 0
    acumulator = number
    
    while acumulator != 1:
        if acumulator % 2 == 0:
            acumulator = acumulator // 2
        else:
            acumulator = acumulator * 3 + 1
        steps += 1
    
    return steps
    
