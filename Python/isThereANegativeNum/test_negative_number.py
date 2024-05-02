from negative_number import isThereANegativeNumber
import unittest

class TestNegativeNumber(unittest.TestCase):
    def test_validate(self):
        self.assertEqual(isThereANegativeNumber([2, 12, 55, -2]), True)
        self.assertEqual(isThereANegativeNumber([2, 12, 55, 2]), False)

    def test_type(self):
        with self.assertRaises(TypeError):
            result = isThereANegativeNumber([2, 10, "Sanyi"])

if __name__ == '__main__':
    unittest.main()