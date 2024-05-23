import { isThereNegativeNum } from "./negativeNum.js";

test("This array has a negative number returns true", () => {
    expect(isThereNegativeNum([1, 2, 3, 10, 100, -1, 20, 50])).toBe(true)
})

test("This array doesn't have a negative number so returns false", () => {
    expect(isThereNegativeNum([1, 2, 3, 10, 100, 1, 20, 50])).toBe(false)
})