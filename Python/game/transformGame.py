def transformLetters(word):
    letters = "aáeéiíoóöőuúüű"

    if type(word) != str: raise TypeError("Data must be string")

    changedWord = ""
    for letter in word:
        if letter.lower() in letters:
            letter = "."
            changedWord += letter
        else:
            changedWord += letter
    
    return changedWord
