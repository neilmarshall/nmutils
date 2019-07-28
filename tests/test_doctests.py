import doctest

from nmutils import primes
from nmutils import pythagorean_triples

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(primes))
    tests.addTests(doctest.DocTestSuite(pythagorean_triples))
    return tests

