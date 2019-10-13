import unittest

from nmutils.primes import *

class TestIsPrimeWithoutPassingKnownPrimesAsArgument(unittest.TestCase):

    def test_is_prime_returns_false_for_zero(self):
        self.assertEqual(is_prime(0), False)

    def test_is_prime_returns_false_for_one(self):
        self.assertEqual(is_prime(1), False)

    def test_is_prime_returns_true_for_two(self):
        self.assertEqual(is_prime(2), True)

    def test_is_prime_returns_true_for_odd_prime(self):
        self.assertEqual(is_prime(17), True)

    def test_is_prime_returns_false_for_compound_number(self):
        self.assertEqual(is_prime(15), False)


class TestIsPrimeWithKnownPrimesPassedAsArgument(unittest.TestCase):

    def setUp(self):
        self.known_primes = [2, 3, 5]

    def test_is_prime_returns_false_for_zero(self):
        self.assertEqual(is_prime(0, self.known_primes), False)

    def test_is_prime_returns_false_for_one(self):
        self.assertEqual(is_prime(1, self.known_primes), False)

    def test_is_prime_returns_true_for_two(self):
        self.assertEqual(is_prime(2, self.known_primes), True)

    def test_is_prime_returns_true_for_odd_prime(self):
        self.assertEqual(is_prime(17, self.known_primes), True)

    def test_is_prime_returns_false_for_compound_number(self):
        self.assertEqual(is_prime(15, self.known_primes), False)

    def test_is_prime_throws_error_if_insufficient_known_primes_passed(self):
        self.assertRaises(PrimeError, is_prime, 40, self.known_primes)


class TestGetPrimesUnderN(unittest.TestCase):

    def test_get_primes_under_n_returns_empty_list_for_input_less_than_one(self):
        self.assertEqual(get_primes_under_n(1), [])

    def test_get_primes_under_n_returns_primes_strictly_less_than_input(self):
        self.assertEqual(get_primes_under_n(23), [2, 3, 5, 7, 11, 13, 17, 19])


class TestGetPrimesUpToN(unittest.TestCase):

    def test_get_primes_up_to_n_returns_empty_list_for_input_less_than_one(self):
        self.assertEqual(get_primes_up_to_n(1), [])

    def test_get_primes_up_to_n_returns_primes_up_to_input(self):
        self.assertEqual(get_primes_up_to_n(23), [2, 3, 5, 7, 11, 13, 17, 19, 23])


class TestGetPrimeFactors(unittest.TestCase):

    def test_get_prime_factors_returns_empty_list_for_input_less_than_two(self):
        self.assertEqual(get_prime_factors(1), [])

    def test_get_prime_factors_returns_one_element_list_for_prime_input(self):
        self.assertEqual(get_prime_factors(13), [13])

    def test_get_prime_factors_returns_all_factors_for_compound_number(self):
        self.assertEqual(get_prime_factors(100), [2, 2, 5, 5])


class TestGetUniquePrimeFactors(unittest.TestCase):

    def test_get_unique_prime_factors_returns_empty_list_for_input_less_than_two(self):
        self.assertEqual(get_unique_prime_factors(1), [])

    def test_get_unique_prime_factors_returns_one_element_list_for_prime_input(self):
        self.assertEqual(get_unique_prime_factors(13), [13])

    def test_get_unique_prime_factors_returns_all_factors_for_compound_number(self):
        self.assertEqual(get_unique_prime_factors(100), [2, 5])
