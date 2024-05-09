import unittest
from palindrom import palindrom

class TestValidate(unittest.TestCase):
    def validateTest(self):
        self.assertEqual(palindrom("Sanyi"), "iynaS")


    def validateTypeErrorDef(self):
        with self.assertRaises(TypeError):
            result = palindrom(22)


if __name__ == "__main__":
    unittest.main()