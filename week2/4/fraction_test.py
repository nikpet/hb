import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    def setUp(self):
        self.fract = Fraction(1, 2)

    def test_init(self):
        self.assertEqual(1, self.fract.numerator)
        self.assertEqual(2, self.fract.denominator)
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_gets_simplified(self):
        fract = Fraction(2, 4)
        self.assertEqual(1, fract.numerator)
        self.assertEqual(2, fract.denominator)

    def test_greatest_common_divisor(self):
        self.assertEqual(self.fract._gcd(5, 10), 5)
        self.assertEqual(self.fract._gcd(5, 7), 35)

    def test_add(self):
        fract_two = Fraction(1, 3)
        result_fraction = self.fract + fract_two
        self.assertFalse(result_fraction is self.fract)
        self.assertFalse(result_fraction is fract_two)
        self.assertEqual(result_fraction.numerator, 5)
        self.assertEqual(result_fraction.denominator, 6)

    def test_substract(self):
        fract_two = Fraction(1, 3)
        result_fraction = self.fract - fract_two
        self.assertFalse(result_fraction is self.fract)
        self.assertFalse(result_fraction is fract_two)
        self.assertEqual(result_fraction.numerator, 1)
        self.assertEqual(result_fraction.denominator, 6)

    def test_multiply(self):
        fract_two = Fraction(1, 3)
        result_fraction = self.fract * fract_two
        self.assertFalse(result_fraction is self.fract)
        self.assertFalse(result_fraction is fract_two)
        self.assertEqual(result_fraction.numerator, 1)
        self.assertEqual(result_fraction.denominator, 6)

    def test_simplify(self):
        fract = Fraction(2, 4)
        self.assertEqual(fract.numerator, 1)
        self.assertEqual(fract.denominator, 2)

    def test_stringify(self):
        self.assertEqual(str(self.fract), '1 / 2')
        self.assertEqual(str(Fraction(4, 1)), '4')
        self.assertEqual(str(Fraction(0, 5)), '0')

if __name__ == '__main__':
    unittest.main()
