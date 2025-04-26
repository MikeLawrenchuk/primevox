import pytest
from pv_sdk.factoring import (
    generate_candidate_primes,
    pollards_rho,
    brent_factor,
    factor_large_number
)
from sympy import isprime

@pytest.mark.timeout(5)
def test_generate_candidate_primes():
    candidates = generate_candidate_primes(1, 20)
    for prime in candidates:
        assert str(prime)[-1] in '1379'
        assert isprime(prime)

    reversed_candidates = generate_candidate_primes(20, 1)
    assert candidates == reversed_candidates

@pytest.mark.timeout(5)
def test_pollards_rho():
    composite = 8051
    factor_result = pollards_rho(composite)
    assert composite % factor_result == 0
    assert factor_result in [83, 97]
    assert factor_result not in [1, composite]

@pytest.mark.timeout(5)
def test_brent_factor():
    composite = 10403
    factor_result = brent_factor(composite)
    assert composite % factor_result == 0
    assert factor_result in [101, 103]
    assert factor_result not in [1, composite]

@pytest.mark.timeout(5)
def test_factor_large_number():
    number = 1001
    start_digits = '000001'
    end_digits = '000100'
    factor_large_number(number, start_digits, end_digits)

    prime_number = 101
    factor_large_number(prime_number, start_digits, end_digits)

    larger_number = 8051
    factor_large_number(larger_number, start_digits, end_digits)

@pytest.mark.timeout(5)
def test_prime_input_pollards_rho():
    prime = 101
    factor_result = pollards_rho(prime)
    assert factor_result in [prime, 1]

@pytest.mark.timeout(5)
def test_prime_input_brent_factor():
    prime = 103
    factor_result = brent_factor(prime)
    assert factor_result in [prime, 1]
