from validate import openingHoursInStore
import unittest

class ValidateOpeningHours(unittest.TestCase):
    def test_validation(self):
        self.assertEqual(openingHoursInStore(12), True)
        self.assertEqual(openingHoursInStore(16), False)
        self.assertEqual(openingHoursInStore(18), False)

    def test_type(self):
        with self.assertRaises(TypeError):
            result = openingHoursInStore("hsfsahfaskl")

if __name__ == '__main__':
    unittest.main()