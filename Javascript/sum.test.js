import { sum, substract, multiply, divide } from "./sum.js"

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});

test('substraction 3 - 2 to equal 1', () => {
    expect(substract(3, 2)).toBe(1)
})

test('multiply 3 * 2 to equal 6', () => {
    expect(multiply(3, 2)).toBe(6)
})

test('divide 3 / 3 to equal 61', () => {
    expect(divide(3, 3)).toBe(1)
})