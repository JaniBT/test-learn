import { gradeValidation } from "./grade.js"

test("if grade is between 1 and 5 return true", () => {
    expect(gradeValidation(5)).toBe(true)
})

test("if grade is NOT between 1 and 5 return false", () => {
    expect(gradeValidation(7)).toBe(false)
})