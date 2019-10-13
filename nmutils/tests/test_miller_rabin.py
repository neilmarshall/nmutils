import unittest

from nmutils.miller_rabin import MillerRabin

class TestMillerRabin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.miller_rabin = MillerRabin()

    def test_miller_rabin_produces_primes_under_100(self):
        miller_rabin_output = [n for n in range(100) if self.miller_rabin.is_prime(n)]
        primes_under_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, \
                            47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(miller_rabin_output, primes_under_100)

    def test_miller_rabin_produces_sum_of_primes_under_1000(self):
        miller_rabin_output = sum(n for n in range(1000) if self.miller_rabin.is_prime(n))
        self.assertEqual(miller_rabin_output, 76127)

    def test_miller_rabin_produces_sum_of_pries_between_100000_and_120000(self):
        miller_rabin_output = sum(n for n in range(100000, 120000) if self.miller_rabin.is_prime(n))
        self.assertEqual(miller_rabin_output, 187964655)
