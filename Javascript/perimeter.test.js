import { perimeter } from "./perimeter.js"

test('if one parameter is given it returns a squares perimeter', () => {
    expect(perimeter(20, [])).toBe(80)
})

test('if two parameters is given it returns a rectangle perimeter', () => {
    expect(perimeter(20, [20])).toBe(80)
})

test('if three parameter is given it returns a triangles perimeter', () => {
    expect(perimeter(20, [10, 20])).toBe(50)
})

test('if three parameter is given it returns a polygon perimeter', () => {
    expect(perimeter(20, [10, 20, 10])).toBe(60)
})