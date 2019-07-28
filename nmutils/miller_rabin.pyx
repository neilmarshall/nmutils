from nmutils.primes import get_primes_up_to_n

cdef class MillerRabin():
    """
    Miller-Rabin primality test

    Deterministic implementation of Miller-Rabin primality test, based on
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test

    Class loads primes below 5,000. For given n, assuming n odd (returning False
    if n is not 2 otherwise), trial division is first attempted versus these
    initial primes.

    If trial division fails to identify primality, the full Miller-Rabin algorithm
    is employed, with witnesses chosen based on the value of n.

    Empirically, the MillerRabin class appears to out-perform trial division for
    primes larger than 1,000,000 (trial division tested all primes up to 1,000,000
    in just over 6s; Miller-Rabin achieved the same in just under 6s).
    """
    cdef readonly list known

    def __init__(self):
        self.known = get_primes_up_to_n(5000)

    cpdef bint is_prime(self, unsigned long long n):
        """
        Return primality of n
        
        Uses trial division for small n and Miller-Rabin for larger values.
        """
        # discount even numbers
        if n <= 2 or n % 2 == 0:
            return n == 2

        # perform trial division based on initial primes
        cdef unsigned long long p
        for p in self.known:
            if n % p == 0:
                return n == p

        # test compositeness using Miller-Rabin algorithm, with suitable witnesses
        cdef list witnesses
        if n < 2047:
            witnesses = [2]
        elif n < 1373653:
            witnesses = [2, 3]
        elif n < 9080191:
            witnesses = [31, 73]
        elif n < 25326001:
            witnesses = [2, 3, 5]
        elif n < 3215031751:
            witnesses = [2, 3, 5, 7]
        elif n < 4759123141:
            witnesses = [2, 7, 61]
        elif n < 1122004669633:
            witnesses = [2, 13, 23, 1662803]
        elif n < 2152302898747:
            witnesses = [2, 3, 5, 7, 11]
        elif n < 3474749660383:
            witnesses = [2, 3, 5, 7, 11, 13]
        elif n < 341550071728321:
            witnesses = [2, 3, 5, 7, 11, 13, 17]
        elif n < 3825123056546413051:
            witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        elif n < 18446744073709551616:
            witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        else:
            raise OverflowError(f"Value of n too high :: {n}")

        cdef unsigned long long s, d, a
        s, d = self._factorise_powers_of_two(n)
        for a in witnesses:
            if pow(a, d, n) != 1:
                for r in range(s):
                    if pow(a, pow(2, r) * d, n) == n - 1:
                        break
                else:
                    return False
        return True

    cdef (unsigned long long, unsigned long long) _factorise_powers_of_two(self, unsigned long long n):
        cdef unsigned long long s, m, d
        s, m = 0, n - 1
        while m % 2 == 0:
            s += 1
            m >>= 1
        d = n >> s
        return s, d
