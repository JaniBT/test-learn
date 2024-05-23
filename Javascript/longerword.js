export const getLongerWord = (wordOne, wordTwo) => {
    if (wordOne === wordTwo) {
        return "Egyformák";
    }
    return wordOne.length > wordTwo.length ? wordOne : wordTwo;
}