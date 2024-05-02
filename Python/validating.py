def validate(grade):
    if type(grade) != int: raise TypeError("Data must be integer")
    return True if grade >= 1 and grade <= 5 else False
