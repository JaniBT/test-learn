import { gradeValidation } from "./grade.js"

describe("Happy path", function () {
    test.each([
        [1, true],
        [2, true],
        [3, true],
        [6, false],
        [-1, false],
        [0, false],
    ])("if grade is %p return %p", (grade, expected) => {
        expect(gradeValidation(grade)).toBe(expected)
    })
})

describe("Error path", function () {
    test("type error", function () {
        expect(() => gradeValidation('alma')).toThrow(TypeError("Invalid type"))
    })
})