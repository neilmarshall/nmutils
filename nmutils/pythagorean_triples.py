from heapq import heappush, heappop

from .c_pythagorean_triples import Triple

class PythagoreanTripleGenerator():
    """
    Class that continuously generates distinct, primitive Pythagorean triples

    Source: https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

    The class stores triples in a priority queue; triples are stored from smallest to
    largest, where size is taken as the sum of the elements of the triple (so if
    the triple were considered to form a right-angled triangle then the "size" would
    be equal to the sum of the side lengths, i.e. the perimeter)

    >>> ptg = PythagoreanTripleGenerator()
    >>> ptg.GetNextTriple()
    (3, 4, 5)
    """

    def __init__(self):
        self.triples = [Triple(3, 4, 5)]

    def GetNextTriple(self):
        next_triple = heappop(self.triples);
        a, b, c = next_triple.a, next_triple.b, next_triple.c
        self._add_new_triples(a, b, c)
        return a, b, c

    def _add_new_triples(self, a, b, c): 
        # matrix multiplication using [[1, -2, 2], [2, -1, 2], [2, -2, 3]]
        elements = sorted((a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c))
        heappush(self.triples, Triple(*elements))

        # matrix multiplication using [[1, 2, 2], [2, 1, 2], [2, 2, 3]]
        elements = sorted((a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c))
        heappush(self.triples, Triple(*elements))

        # matrix multiplication using [[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]]
        elements = sorted((-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c))
        heappush(self.triples, Triple(*elements))

