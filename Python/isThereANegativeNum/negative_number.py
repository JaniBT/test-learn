def isThereANegativeNumber(list):
    for num in list:
        if type(num) != int: raise TypeError("Data must be integer")
        if num < 0:
            return True
    return False