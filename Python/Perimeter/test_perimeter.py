import unittest
from perimeter import perimeter

class Test(unittest.TestCase):
    def testCase(self):
        self.assertEqual(perimeter(8), 32)
        self.assertEqual(perimeter(5, 8), 26)
        self.assertEqual(perimeter(5, 8, 10), 23)
        self.assertEqual(perimeter(5, 8, 12, 7), 32)

    def typetest(self):
        with self.assertRaises(TypeError):
            result = perimeter("21")

if __name__ == '__main__':
    unittest.main()