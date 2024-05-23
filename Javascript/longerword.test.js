import { getLongerWord } from "./longerword.js"

test("if two words are the same length return 'Egyformák'", () => {
    expect(getLongerWord("Sanyi", "Sanyi")).toBe("Egyformák")
})

test("if first word longer than second return with that", () => {
    expect(getLongerWord("SanyiHalo", "Sanyi")).toBe("SanyiHalo")
})

test("if second word longer than first return with that", () => {
    expect(getLongerWord("Sanyi", "SanyiHallo")).toBe("SanyiHallo")
})