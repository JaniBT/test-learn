export const changeVowelToDot = (word) => {
    const vowels = "aáeéiíoóöőuúüű"
    let newWord = ""

    for (const letter of word) {
        newWord += vowels.includes(letter.toLowerCase()) ? "." : letter
    }

    return newWord
}