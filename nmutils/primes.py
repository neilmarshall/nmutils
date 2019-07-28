"""Module containing functions to identify primes, generate primes, and
factorize numbers into primes"""

class PrimeError(Exception):
    """Base class for exceptions raised by prime functions"""
    pass


def is_prime(n, known_primes=None):
    """
    Return primality of n

    If a list of known primes is passed then these are checked as potential
    factors, else all numbers from 2 up to the square root of n are checked.

    A list of known primes should be passed in sorted order (this is not checked
    for performance reasons, it is the user's responsibility to ensure primes
    are passed in sorted order), but a PrimeError is thrown if the largest prime
    is less than the square root of n.

    >>> is_prime(5)
    True

    >>> is_prime(6)
    False

    >>> primes = [2, 3, 5]
    >>> is_prime(17)
    True
    """
    if n <= 1:
        return False

    if known_primes is not None:
        if known_primes[-1] < int(n**0.5):
            error_msg = f"Known primes passed must be at least as great as "
            error_msg += f"square root of n (max prime = {known_primes[-1]}, "
            error_msg += f"square root of n = {int(n**0.5)})"
            raise PrimeError(error_msg)
        test_factors = (prime for prime in known_primes if prime <= int(n**0.5))
    else:
        test_factors = range(2, int(n**0.5) + 1)

    for p in test_factors:
        if n % p == 0:
            return False
    else:
        return True


def get_primes_under_n(n):
    """
    Return list of primes less than n

    >>> get_primes_under_n(23)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    if n <= 1:
        return []

    flags = [False, False] + [True for _ in range(2, n + 1)]
    for p in range(2, n // 2 + 1):
        if flags[p]:
            for q in range(2, n // p + 1):
                flags[p * q] = False

    return [i for i, prime in enumerate(flags) if prime and i < n]


def get_primes_up_to_n(n):
    """
    Return list of primes up to and including n

    >>> get_primes_up_to_n(23)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
    """
    return get_primes_under_n(n + 1)


def get_prime_factors(n):
    """
    Return list of (non-unique) prime factors of n

    >>> get_prime_factors(100)
    [2, 2, 5, 5]
    """
    if n <= 1:
        return []

    factors = []
    primes = get_primes_up_to_n(int(n**0.5))
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n /= prime

    if n > 1:
        factors.append(n)

    return factors


def get_unique_prime_factors(n):
    """
    Return list of unique prime factors of n

    >>> get_unique_prime_factors(100)
    [2, 5]
    """
    return sorted(set(get_prime_factors(n)))

