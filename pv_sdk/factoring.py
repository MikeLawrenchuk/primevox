from sympy import primerange, factorint, isprime
import random
import csv
import time
import math

def generate_candidate_primes(start, end):
    """Generate primes excluding those ending with even digits."""
    start, end = sorted([start, end])
    primes = primerange(start, end)
    return [p for p in primes if str(p)[-1] in '1379']

def pollards_rho(n):
    """Pollard's Rho algorithm for integer factorization."""
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3
    c = random.randint(1, n - 1)
    f = lambda x: (pow(x, 2, n) + c) % n
    x, y, d = 2, 2, 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)
    return d

def brent_factor(n):
    """Brent's Algorithm for integer factorization."""
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3
    y, c, m = random.randrange(1, n), random.randrange(1, n), random.randrange(1, n)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for _ in range(r):
            y = (pow(y, 2, n) + c) % n
        k = 0
        while k < r and g == 1:
            ys = y
            for _ in range(min(m, r - k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x - y) % n
            g = math.gcd(q, n)
            k += m
        r *= 2
        if g == n:
            while True:
                ys = (pow(ys, 2, n) + c) % n
                g = math.gcd(abs(x - ys), n)
                if g > 1:
                    break
    return g

def save_factors_csv(number, factors, filename):
    """Save factorization results clearly to CSV."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Number', 'Prime Factor', 'Power', 'Timestamp'])
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        for prime, power in factors.items():
            writer.writerow([number, prime, power, timestamp])
    print(f"Results saved to {filename}")

def factor_large_number(number, start_digits, end_digits):
    """Factorize a number utilizing candidate primes, Brent, and Pollard algorithms."""
    factors, original_number = {}, number
    start_time = time.time()

    print(f"Starting factorization...\nNumber: {number}")
    
    while number > 1:
        if isprime(number):
            factors[number] = factors.get(number, 0) + 1
            print(f"Remaining prime identified: {number}")
            break

        start_range = int(f"{start_digits}0000")
        end_range = int(f"{end_digits}9999")
        candidates = generate_candidate_primes(start_range, end_range)
        factored = False

        # Prime candidates
        for prime in candidates:
            count = 0
            while number % prime == 0:
                count += 1
                number //= prime
                factored = True
            if count:
                factors[prime] = factors.get(prime, 0) + count
                print(f"Identified factor (candidate primes): {prime}^{count}")

        # Brent’s Algorithm
        if not factored:
            print("Trying Brent’s Algorithm...")
            factor = brent_factor(number)
            if factor and factor != number:
                count = 0
                while number % factor == 0:
                    count += 1
                    number //= factor
                factors[factor] = factors.get(factor, 0) + count
                print(f"Identified factor (Brent’s): {factor}^{count}")
                factored = True

        # Pollard’s Rho as fallback
        if not factored:
            print("Trying Pollard’s Rho Algorithm...")
            factor = pollards_rho(number)
            if factor and factor != number:
                count = 0
                while number % factor == 0:
                    count += 1
                    number //= factor
                factors[factor] = factors.get(factor, 0) + count
                print(f"Identified factor (Pollard’s): {factor}^{count}")
                factored = True

        # Sympy as ultimate fallback
        if not factored:
            print("Using sympy's factorization as final fallback...")
            sympy_factors = factorint(number)
            for prime, power in sympy_factors.items():
                factors[prime] = factors.get(prime, 0) + power
                print(f"Sympy Identified: {prime}^{power}")
            break

        # Adjust digits for subsequent iterations
        start_digits = str(int(start_digits) + 2).zfill(6)
        end_digits = str(int(end_digits) + 2).zfill(6)

    end_time = time.time()
    duration = end_time - start_time

    print("\nFinal Factorization Results:")
    for prime, power in factors.items():
        print(f"{prime}^{power}")

    print(f"\nTotal factorization time: {duration:.2f} seconds.")
    save_factors_csv(original_number, factors, f"factoring_results_{int(time.time())}.csv")

def interactive_factorization():
    """Interactive console for factoring large numbers."""
    try:
        number_str = input("Enter number (up to 50 digits): ").strip()
        if not number_str.isdigit() or len(number_str) > 50:
            raise ValueError("Input must be numeric with up to 50 digits.")
        number = int(number_str)
        start_digits = input("Enter start digits for prime candidate generation (6 digits recommended): ").strip()
        end_digits = input("Enter end digits for prime candidate generation (6 digits recommended): ").strip()
        factor_large_number(number, start_digits, end_digits)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

# Optional: Execute interactive factorization directly when running this module
if __name__ == "__main__":
    interactive_factorization()