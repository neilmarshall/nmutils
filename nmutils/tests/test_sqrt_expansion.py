import unittest
from fractions import Fraction

from nmutils.sqrt_expansion import SqrtExpansion

class TestSqrtExpansion(unittest.TestCase):

    def test_generates_root_for_expansion_of_2_when_given_key_and_root(self):
        expansion = SqrtExpansion(1, (2,))
        self.assertEqual(expansion.root, 1)

    def test_generates_key_for_expansion_of_2_when_given_key_and_root(self):
        expansion = SqrtExpansion(1, (2,))
        self.assertEqual(expansion.key, (2,))

    def test_generates_root_for_expansion_of_2_when_initialised_with_2(self):
        expansion = SqrtExpansion(2)
        self.assertEqual(expansion.root, 1)

    def test_generates_key_for_expansion_of_2_when_initialised_with_2(self):
        expansion = SqrtExpansion(2)
        self.assertEqual(expansion.key, (2,))

    def test_generates_root_for_expansion_of_13_when_initialised_with_13(self):
        expansion = SqrtExpansion(13)
        self.assertEqual(expansion.root, 3)

    def test_generates_key_for_expansion_of_13_when_initialised_with_13(self):
        expansion = SqrtExpansion(13)
        self.assertEqual(expansion.key, (1, 1, 1, 1, 6))

    def test_generates_first_four_fractions_for_expansion_of_2(self):
        expansion = SqrtExpansion(2)
        actual = tuple((expansion.get_nth_fraction(1), expansion.get_nth_fraction(2),
                        expansion.get_nth_fraction(3), expansion.get_nth_fraction(4)))
        expected = tuple((Fraction(1, 1), Fraction(3, 2),
                          Fraction(7, 5), Fraction(17, 12)))
        self.assertEqual(actual, expected)

    def test_generates_first_five_fractions_for_expansion_of_e(self):
        expansion = SqrtExpansion(2, (1, 2, 1, 1, 4))
        actual = tuple((expansion.get_nth_fraction(1), expansion.get_nth_fraction(2),
                        expansion.get_nth_fraction(3), expansion.get_nth_fraction(4),
                        expansion.get_nth_fraction(5)))
        expected = tuple((Fraction(2, 1), Fraction(3, 1), Fraction(8, 3),
                          Fraction(11, 4), Fraction(19, 7)))
        self.assertEqual(actual, expected)

    def test_generates_eighth_fraction_for_expansion_of_23(self):
        expansion = SqrtExpansion(23)
        self.assertEqual(expansion.get_nth_fraction(8), Fraction(1151, 240))

    def test_string_representation_of_expansion_of_23(self):
        expansion = SqrtExpansion(23)
        self.assertEqual(str(expansion), "[4; (1, 3, 1, 8)]")

    def test_throws_error_if_input_is_square(self):
        self.assertRaises(ValueError, SqrtExpansion, 9)

    def test_period_property(self):
        expansion = SqrtExpansion(23)
        self.assertEqual(expansion.period, 4)

    def test_coefficient_calls_correct_element_of_key(self):
        expansion = SqrtExpansion(23)
        self.assertEqual(expansion.coefficient(0), 1)
        self.assertEqual(expansion.coefficient(1), 3)
        self.assertEqual(expansion.coefficient(2), 1)
        self.assertEqual(expansion.coefficient(3), 8)
        self.assertEqual(expansion.coefficient(4), 1)
        self.assertEqual(expansion.coefficient(5), 3)
        self.assertEqual(expansion.coefficient(6), 1)
        self.assertEqual(expansion.coefficient(7), 8)
