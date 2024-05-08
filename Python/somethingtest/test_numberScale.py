import unittest
from numberScale import scaleExchanger

# 10-ből 2-es számrendszerbe vált át
class TestExchanger(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(scaleExchanger(52), "110100")
        self.assertEqual(scaleExchanger(1), "1")
        self.assertEqual(scaleExchanger(20), "10100")
        self.assertEqual(scaleExchanger(10), "10010")

    def test_type_validation(self):
        with self.assertRaises(TypeError):
            result = scaleExchanger("Szia")

    def test_value_validation(self):
        with self.assertRaises(ValueError):
            result = scaleExchanger(-1)


if __name__ == '__main__':
    unittest.main()
