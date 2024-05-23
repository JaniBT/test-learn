export const isThereNegativeNum = (numList) => {
    for (const num of numList) {
        if (num < 0) {
            return true;
        }
    }
    return false;
} 