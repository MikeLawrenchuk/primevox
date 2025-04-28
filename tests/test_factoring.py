import pytest
from sympy import isprime

from pv_sdk.factoring import (
    brent_factor,
    factor_large_number,
    generate_candidate_primes,
    pollards_rho,
)


@pytest.mark.timeout(5)
def test_generate_candidate_primes():
    candidates = generate_candidate_primes(1, 20)
    for prime in candidates:
        assert str(prime)[-1] in '1379'
        assert isprime(prime)

    reversed_candidates = generate_candidate_primes(20, 1)
    assert candidates == reversed_candidates

@pytest.mark.timeout(5)
def test_generate_candidate_primes_empty():
    candidates = generate_candidate_primes(14, 16)
    assert candidates == [], "Expected empty list for range without primes"

@pytest.mark.timeout(5)
def test_pollards_rho():
    composite = 8051
    factor_result = None
    for _ in range(5):
        factor_result = pollards_rho(composite)
        if factor_result in [83, 97]:
            break
    assert factor_result in [83, 97], f"Failed Pollard's Rho factoring: got {factor_result}"

@pytest.mark.timeout(5)
def test_brent_factor():
    composite = 10403
    factor_result = None
    for _ in range(5):
        factor_result = brent_factor(composite)
        if factor_result in [101, 103]:
            break
    assert factor_result in [101, 103], f"Failed Brent factoring: got {factor_result}"

@pytest.mark.timeout(5)
def test_factor_large_number():
    number = 1001
    start_digits = '000001'
    end_digits = '000100'
    result = factor_large_number(number, start_digits, end_digits)
    assert set(result) == {7, 11, 13}, f"Incorrect factors for 1001: {result}"

    prime_number = 101
    result_prime = factor_large_number(prime_number, start_digits, end_digits)
    assert result_prime == [101], f"Incorrect prime handling: {result_prime}"

    larger_number = 8051
    result_large = factor_large_number(larger_number, start_digits, end_digits)
    assert set(result_large) == {83, 97}, f"Incorrect factors for 8051: {result_large}"

@pytest.mark.timeout(5)
def test_prime_input_pollards_rho():
    prime = 101
    factor_result = pollards_rho(prime)
    assert factor_result in [prime, 1], f"Unexpected result for prime input: {factor_result}"

@pytest.mark.timeout(5)
def test_prime_input_brent_factor():
    prime = 103
    factor_result = brent_factor(prime)
    assert factor_result in [prime, 1], f"Unexpected result for prime input: {factor_result}"
