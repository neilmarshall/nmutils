import doctest

from nmutils import miller_rabin, primes, pythagorean_triples, sqrt_expansion

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(miller_rabin))
    tests.addTests(doctest.DocTestSuite(primes))
    tests.addTests(doctest.DocTestSuite(pythagorean_triples))
    tests.addTests(doctest.DocTestSuite(sqrt_expansion))
    return tests

