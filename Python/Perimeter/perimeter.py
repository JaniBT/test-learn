def perimeter(side, *sides):
    if type(side) != int or type(side) != int: raise TypeError('Data must be integer')
    if side and not sides:
        return side * 4
    if side and len(sides) == 1:
        return 2 * side + 2 * sides[0]
    
    return side + sum(sides)