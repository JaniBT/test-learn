def scaleExchanger(number):
    if type(number) != int: raise TypeError('Data must be integer')
    if number < 0: raise ValueError('Data must be greater than zero')

    binary_string = bin(number)[2:]
    return binary_string