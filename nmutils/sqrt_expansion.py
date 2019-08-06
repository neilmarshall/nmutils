from fractions import Fraction

class SqrtExpansion():
    """
    Generates square root expansion of an irrational number

    >>> expansion = SqrtExpansion(24)

    >>> expansion.root
    4

    >>> expansion.key
    (1, 8)

    >>> expansion = SqrtExpansion(25)
    Traceback (most recent call last):
        ...
    ValueError: Input to SqrtExpansion cannot be a square
    """

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

    def __repr__(self):
        return f"SqrtExpansion({self.root, self.key})"

    @staticmethod
    def get_root_and_key(n):
        """
        Return square root expansion root and key for square root of n

        >>> SqrtExpansion.get_root_and_key(24)
        (4, (1, 8))
        """
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
        """
        Return nth fractional estimate of square root of n

        >>> expansion = SqrtExpansion(24)

        >>> expansion.get_nth_fraction(1)
        Fraction(4, 1)

        >>> expansion.get_nth_fraction(2)
        Fraction(5, 1)

        >>> expansion.get_nth_fraction(3)
        Fraction(44, 9)

        >>> expansion.get_nth_fraction(4)
        Fraction(49, 10)
        """
        expansion = [self.key[i % len(self.key)] for i in range(n)]
        numerator, denominator = 0, 1
        for exp in reversed(expansion[:n - 1]):
            numerator, denominator = denominator, numerator + denominator * exp
        return Fraction(self.root, 1) + Fraction(numerator, denominator)

    @property
    def period(self):
        """
        Return length of key

        >>> expansion = SqrtExpansion(24)

        >>> expansion.period
        2
        """
        return len(self.key)

    def coefficient(self, n):
        """
        Return nth element of key, allowing repeats where n > period

        >>> expansion = SqrtExpansion(24)

        >>> expansion.coefficient(3)
        8

        >>> expansion.coefficient(4)
        1
        """
        return self.key[n % self.period]
