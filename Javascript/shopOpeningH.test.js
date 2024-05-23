import { openingHours } from "./shopOpeningH.js"

test("Opening hours are between 8 && 16, 8 should be true", () => {
    expect(openingHours(8)).toBe(true)
})

test("Opening hours are between 8 && 16, 16 should be false", () => {
    expect(openingHours(16)).toBe(false)
})
test("Opening hours are between 8 && 16, 11 should be true", () => {
    expect(openingHours(11)).toBe(true)
})

test("Opening hours are between 8 && 16, 19 should be false", () => {
    expect(openingHours(19)).toBe(false)
})