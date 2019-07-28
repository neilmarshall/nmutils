import unittest

from nmutils.pythagorean_triples import PythagoreanTripleGenerator

class TestGeneratePythagoreanTriples(unittest.TestCase): 

    def test_calls_to_PythagoreanTripleGenerator_return_correct_values(self):
        ptg = PythagoreanTripleGenerator()
        actual_values = [ptg.GetNextTriple() for _ in range(7)]
        expected_values = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
                           (20, 21, 29), (12, 35, 37), (9, 40, 41)]
        self.assertEqual(actual_values, expected_values)

