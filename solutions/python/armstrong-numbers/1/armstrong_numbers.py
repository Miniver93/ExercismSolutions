def is_armstrong_number(number):
    digits = list(str(number))
    result = 0
    for d in digits:
        result += int(d)**len(digits)
    if result == number:
        return True
    elif number == 0:
        return True
    return False
