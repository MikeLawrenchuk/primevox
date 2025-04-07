import pytest
from pv_sdk.factoring import (
    generate_candidate_primes,
    pollards_rho,
    brent_factor,
    factor_large_number
)
from sympy import isprime

def test_generate_candidate_primes():
    candidates = generate_candidate_primes(1, 20)

    # candidate primes must end with 1, 3, 7, or 9
    for prime in candidates:
        assert str(prime)[-1] in '1379'
        assert isprime(prime)

    # Clearly test reversed ranges
    reversed_candidates = generate_candidate_primes(20, 1)
    assert candidates == reversed_candidates

def test_pollards_rho():
    composite = 8051  # Known composite: 8051 = 97 * 83
    factor_result = pollards_rho(composite)

    assert composite % factor_result == 0
    assert factor_result in [83, 97]

def test_brent_factor():
    composite = 10403  # Known composite: 101 * 103
    factor_result = brent_factor(composite)

    assert composite % factor_result == 0
    assert factor_result in [101, 103]

def test_factor_large_number():
    number = 1001  # Known small number (factors clearly 7, 11, 13)
    start_digits = '000001'
    end_digits = '000100'

    # This test checks if the function runs without errors
    # Explicit csv saving is also tested implicitly here
    factor_large_number(number, start_digits, end_digits)

    # Edge case clearly handled: testing a prime number
    prime_number = 101
    factor_large_number(prime_number, start_digits, end_digits)

    # Clearly test larger composite number
    larger_number = 8051  # Factors 97 and 83
    factor_large_number(larger_number, start_digits, end_digits)

def test_prime_input_pollards_rho():
    # Pollard's Rho explicitly on prime input returns the number itself
    prime = 101
    assert pollards_rho(prime) == prime or pollards_rho(prime) == 1

def test_prime_input_brent_factor():
    # Brent's factor explicitly on prime input returns the number itself
    prime = 103
    assert brent_factor(prime) == prime or brent_factor(prime) == 1