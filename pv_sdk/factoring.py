"""
High-performance integer factorization module for PrimeVox SDK.

This module provides functions to factor large composites (up to ~40 digits)
using Pollard's Rho with Brent's cycle detection, plus a deterministic Miller-Rabin
primality test for 64-bit numbers.

Public API:
  - prime_to_vowel_notation(prime: int) -> str
  - factor(n: int) -> List[int]
  - factor_frequencies(n: int) -> Dict[int, int]
  - factor_and_map(n: int) -> List[str]
"""
import logging
import math
import random
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)

_digit_to_vowel: Dict[str, str] = {
    "1": "A",  # primes ending in 1 → A
    "3": "E",  # primes ending in 3 → E
    "5": "Y",  # primes ending in 5 → Y
    "7": "I",  # primes ending in 7 → I
    "9": "O",  # primes ending in 9 → O
}


def prime_to_vowel_notation(prime: int) -> str:
    """
    Map a prime number to its vowel notation based on its final digit.

    Special case:
      - 2 -> 'U'

    Args:
        prime: A prime integer.
    Returns:
        A string of vowel characters representing the prime.
    """
    if prime == 2:
        return "U"
    return "".join(_digit_to_vowel.get(d, d) for d in str(prime))


def _pollards_rho_brent(n: int, max_iter: int = 100_000) -> Optional[int]:
    """
    Pollard's Rho algorithm with Brent's cycle detection to find a nontrivial factor.

    Args:
        n: Composite integer to factor.
        max_iter: Maximum cycle iterations before giving up.
    Returns:
        A nontrivial factor of n, or None if it fails.
    """
    if n % 2 == 0:
        return 2
    y = random.randrange(1, n)
    c = random.randrange(1, n)
    m = random.randrange(1, n)
    g = r = q = 1
    x = y

    while g == 1 and r < max_iter:
        x = y
        for _ in range(r):
            y = (y * y + c) % n
        k = 0
        while k < r and g == 1:
            ys = y
            for _ in range(min(m, r - k)):
                y = (y * y + c) % n
                q = (q * abs(x - y)) % n
            g = math.gcd(q, n)
            k += m
        r *= 2

    if g is None or g == n:
        while True:
            ys = (ys * ys + c) % n  # type: ignore
            g = math.gcd(abs(x - ys), n)
            if g and g < n:
                break

    return g if g and g < n else None


def _is_prime(n: int) -> bool:
    """
    Deterministic Miller-Rabin for n < 2^64 using fixed bases.

    Args:
        n: Integer to test.
    Returns:
        True if n is (probably) prime, False otherwise.
    """
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    d, s = n - 1, 0
    while not d & 1:
        d >>= 1
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def factor(n: int) -> List[int]:
    """
    Recursively factor an integer into its prime factors.

    Args:
        n: Integer > 1 to factor.
    Returns:
        A list of prime factors (unsorted).
    """
    if n <= 1:
        return []
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n % p == 0:
            return [p] + factor(n // p)
    if _is_prime(n):
        return [n]
    divisor = None
    while divisor is None:
        divisor = _pollards_rho_brent(n)
    return factor(divisor) + factor(n // divisor)


def factor_frequencies(n: int) -> Dict[int, int]:
    """
    Count prime factor multiplicities for a composite number.

    Args:
        n: Integer > 1.
    Returns:
        A dict mapping prime -> exponent.
    """
    freqs: Dict[int, int] = {}
    for p in factor(n):
        freqs[p] = freqs.get(p, 0) + 1
    return freqs


def factor_and_map(number: int) -> List[str]:
    """
    Factor a composite into primes and map each to vowel notation.

    Args:
        number: Composite integer to factor.
    Returns:
        A list of vowel-mapped factor strings.
    """
    from pv_sdk.factoring import prime_to_vowel_notation

    return [prime_to_vowel_notation(p) for p in factor(number)]
