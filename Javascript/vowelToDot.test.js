import { changeVowelToDot } from "./vowelToDot.js"

test('KÖpés Alma returns K.p.s .lm.', () => {
    expect(changeVowelToDot("KÖpés Alma")).toBe("K.p.s .lm.")
})

test('Szereti a tejet returns Sz.r.t. . t.j.t', () => {
    expect(changeVowelToDot("Szereti a tejet")).toBe("Sz.r.t. . t.j.t")
})