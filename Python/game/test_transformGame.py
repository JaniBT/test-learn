import unittest
from transformGame import transformLetters

class Test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(transformLetters("Szeretem a tejet"), "Sz.r.t.m . t.j.t")
        self.assertEqual(transformLetters("Kecskén ül a medve tegnap"), "K.csk.n .l . m.dv. t.gn.p")
        self.assertEqual(transformLetters("NÉha ő a kedvenc tyúk"), "N.h. . . k.dv.nc ty.k")

    def test_exception(self):
        with self.assertRaises(TypeError):
            result = transformLetters(21)

if __name__ == '__main__':
    unittest.main()