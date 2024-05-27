export const gradeValidation = (grade) => {
    if (typeof grade != "number")
        throw new TypeError("Invalid type");
    return grade >= 1 && grade <= 5;
}