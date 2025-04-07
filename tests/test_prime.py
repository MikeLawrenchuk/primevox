import pytest
from pv_sdk.prime import (
    is_prime,
    prime_to_vowel,
    generate_primes_and_map,
    create_composite_mappings
)

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(12) is False
    assert is_prime(1) is False
    assert is_prime(-3) is False

def test_prime_to_vowel():
    assert prime_to_vowel(2) == 'E'
    assert prime_to_vowel(5) == 'O'
    assert prime_to_vowel(13) == 'I'
    assert prime_to_vowel(29) == 'Y'

def test_generate_primes_and_map():
    limit = 10
    primes, vowels = generate_primes_and_map(limit, pickle_file=' test_prime_cache.pkl')
    assert primes == [2, 3, 5, 7]
    assert vowels == ['E', 'I', 'O', 'U']

def test_create_composite_mappings():
    primes = [2, 3, 5]
    vowels = ['E', 'I', 'O']
    composites = create_composite_mappings(primes, vowels)

    assert isinstance(composites, list)
    assert len(composites) == 3  # Combinations: (2,3), (2,5), (3,5)

    # Check the structure of the composites explicitly
    composite_example = composites[0]
    expected_keys = {'pair', 'vowel_pair', 'sum', 'product', 'exponent'}
    assert set(composite_example.keys()) == expected_keys