def whichWordIsLonger(firstWord, secondWord):
    if firstWord or secondWord == int:
        raise TypeError("Data must be string")
    firstWordLength = len(firstWord)
    secondWordLength = len(secondWord)

    if firstWordLength == secondWordLength:
        return "Egyformák"
    return firstWord if firstWordLength > secondWordLength else secondWord

# print(whichWordIsLonger("Almasadsa", "Alma"))