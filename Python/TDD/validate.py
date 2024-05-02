def openingHoursInStore(hour):
    if type(hour) != int: raise TypeError("Data must be integer")
    return True if hour >= 8 and hour < 16 else False