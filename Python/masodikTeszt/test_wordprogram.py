from wordprogram import whichWordIsLonger
import unittest

class TestFunction(unittest.TestCase):
    def test_validate(self):
        self.assertEqual(whichWordIsLonger("Almasasas", "Alma"), "Almasasas")
        self.assertEqual(whichWordIsLonger("Alma", "Alma"), "Egyformák")
        self.assertEqual(whichWordIsLonger("Alma", "Almasasasa"), "Almasasasa")

    def test_type(self):
        with self.assertRaises(TypeError):
            result = whichWordIsLonger(21, 21)


if __name__ == '__main__':
    unittest.main()