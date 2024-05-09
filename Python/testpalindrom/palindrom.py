def palindrom(word):
    if type(word) != str: raise TypeError("Data must be string")
    
    listOfWord = word.split(" ")
    if (len(listOfWord) == 1):
        newList = list(listOfWord[0])
        newList.reverse()
        stringOfList = ''.join(newList)

        if stringOfList == word:
            return True
        return False
    
    reveresedListOfWords = []

    for word in listOfWord:
        newWordList = list(word)
        newWordList.reverse()
        stringOfNewWord = ''.join(newWordList)

        reveresedListOfWords.append(stringOfNewWord)

    reveresedListOfWords.reverse()
    finalList = ' '.join(reveresedListOfWords)
    if (finalList.lower() == word.lower()):
        return True
    return False
    
print(palindrom("kerek görög kerek"))