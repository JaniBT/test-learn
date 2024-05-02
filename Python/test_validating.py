import unittest
from validating import validate

class Validate(unittest.TestCase):
    def test_validate(self):
        self.assertEqual(validate(6), False)
        self.assertEqual(validate(4), True)
        self.assertEqual(validate(2), True)
        self.assertEqual(validate(1), True)
        self.assertEqual(validate(0), False)
    
    def test_type(self):
        with self.assertRaises(TypeError):
            result = validate('alma')


if __name__ == '__main__':
    unittest.main()