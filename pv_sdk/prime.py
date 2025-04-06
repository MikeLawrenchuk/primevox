import os
import pickle
import itertools
from sympy import primerange, isprime
import csv

# Efficient vowel mapping dictionary
PRIME_VOWEL_MAP = {
    1: 'A',
    3: 'I',
    7: 'U',
    9: 'Y',
    2: 'E',  # Unique prime case
    5: 'O'   # Unique prime case
}

def is_prime(n: int) -> bool:
    """Reliably check if a number is prime using sympy."""
    return isprime(n)

def prime_to_vowel(prime: int) -> str:
    """Map prime numbers specifically based on the last digit or unique prime."""
    if prime in (2, 5):
        return PRIME_VOWEL_MAP[prime]
    return PRIME_VOWEL_MAP.get(prime % 10, '?')

def generate_primes_and_map(limit: int, pickle_file='prime_cache.pkl'):
    """Generate primes up to limit, map to vowels, cache results efficiently."""
    # Load cached data if available
    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as f:
            data = pickle.load(f)
            if data.get('limit', 0) >= limit:
                return data['primes'], data['vowel_mappings']

    # Generate primes and map vowels
    primes = list(primerange(2, limit + 1))
    vowel_mappings = [prime_to_vowel(p) for p in primes]

    # Cache the results
    data = {'limit': limit, 'primes': primes, 'vowel_mappings': vowel_mappings}
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f)

    return primes, vowel_mappings

def create_composite_mappings(primes, vowel_mappings, exponent_limit=20):
    """Create composites from prime pairs, labeling clearly using itertools."""
    composite_list = []

    for (p1, v1), (p2, v2) in itertools.combinations(zip(primes, vowel_mappings), 2):
        composites = {
            'pair': (p1, p2),
            'vowel_pair': (v1, v2),
            'sum': p1 + p2,
            'product': p1 * p2
        }

        base, exponent = sorted((p1, p2))
        if exponent < exponent_limit:  # Controlled exponentiation for performance
            composites['exponent'] = base ** exponent
        else:
            composites['exponent'] = None

        composite_list.append(composites)

    return composite_list

def save_composites_to_csv(composites, filepath='composite_data.csv'):
    """Save composite data to CSV for easy analysis."""
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Prime1', 'Prime2', 'Vowel1', 'Vowel2', 'Sum', 'Product', 'Exponentiation'])
        for comp in composites:
            p1, p2 = comp['pair']
            v1, v2 = comp['vowel_pair']
            writer.writerow([
                p1, p2, v1, v2,
                comp['sum'],
                comp['product'],
                comp['exponent']
            ])

def interactive_prime_analysis():
    """Interactive console for prime analysis clearly structured."""
    try:
        limit = int(input("Enter prime generation upper limit: ").strip())
        if limit <= 0:
            raise ValueError("Limit must be positive integer.")

        primes, vowels = generate_primes_and_map(limit)
        composites = create_composite_mappings(primes, vowels)
        save_composites_to_csv(composites)

        print(f"Primes and composite data successfully generated up to {limit} and saved.")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

# Direct execution for quick testing/debugging purposes
if __name__ == "__main__":
    interactive_prime_analysis()