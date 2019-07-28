from fractions import Fraction

class SqrtExpansion():
    """Generates square root expansion of an irrational number"""

    def __init__(self, n, iterable=None):
        if iterable is None:
            if int(n**0.5) * int(n**0.5) == n:
                raise ValueError("Input to SqrtExpansion cannot be a square")
            self.root, self.key = self.get_root_and_key(n)
        else:
            self.root = n
            self.key = iterable

    def __str__(self):
        return "[{0}; ({1})]".format(self.root, ', '.join(map(str, self.key)))

    def get_root_and_key(self, n):
        """Return square root expansion root and key for square root of n"""
        root = int(n**0.5)
        a_0 = epsilon_0 = int(n**0.5)
        gamma_0 = n - epsilon_0**2
        a, epsilon, gamma = a_0, epsilon_0, gamma_0
        expansion = []
        while (True):
            a = (int(n**0.5) + epsilon) // gamma
            epsilon = a * gamma - epsilon
            gamma = (n - epsilon**2) // gamma
            expansion.append(a)
            if (epsilon == epsilon_0 and gamma == gamma_0):
                break
        return root, tuple(expansion)

    def get_nth_fraction(self, n):
        """Return nth fractional estimate of square root of n"""
        expansion = [self.key[i % len(self.key)] for i in range(n)]
        numerator, denominator = 0, 1
        for exp in reversed(expansion[:n - 1]):
            numerator, denominator = denominator, numerator + denominator * exp
        return Fraction(self.root, 1) + Fraction(numerator, denominator)

    @property
    def period(self):
        """Return length of key"""
        return len(self.key)

    def coefficient(self, n):
        """Return nth element of key, allowing repeats where n > period"""
        return self.key[n % self.period]
