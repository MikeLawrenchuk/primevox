from sympy import primerange, isprime
from typing import List, Tuple
import csv


def is_twin_prime(p1: int, p2: int) -> bool:
    """
    Check clearly if two prime numbers form a twin prime pair.

    Args:
        p1 (int): First prime number.
        p2 (int): Second prime number.

    Returns:
        bool: True if twin primes; False otherwise.
    """
    return abs(p1 - p2) == 2 and isprime(p1) and isprime(p2)


def find_twin_primes(limit: int) -> List[Tuple[int, int]]:
    """
    Generate list of all twin primes clearly defined up to a given limit.

    Args:
        limit (int): Upper boundary for prime search (inclusive).

    Returns:
        List[Tuple[int, int]]: List of clearly structured twin-prime pairs.
    """
    primes = list(primerange(2, limit + 1))
    twin_prime_pairs = [
        (primes[i], primes[i + 1])
        for i in range(len(primes) - 1)
        if primes[i + 1] - primes[i] == 2
    ]
    return twin_prime_pairs


def save_twin_primes_to_csv(
    twin_primes: List[Tuple[int, int]], filepath="twin_primes.csv"
):
    """
    Save discovered twin primes to a CSV file clearly structured for analysis.

    Args:
        twin_primes (List[Tuple[int, int]]): Clearly identified twin primes.
        filepath (str): Filename/path for CSV clearly defined.
    """
    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Twin Prime 1", "Twin Prime 2"])
        writer.writerows(twin_primes)
    print(f"Twin primes successfully saved clearly to {filepath}.")


def count_twin_primes(limit: int) -> int:
    """
    Clearly count the number of twin primes under or equal to given limit.

    Args:
        limit (int): Upper boundary for counting twin primes inclusive.

    Returns:
        int: Count of twin primes clearly identified under or equal to limit.
    """
    return len(find_twin_primes(limit))


def count_twin_primes_in_range(start: int, end: int) -> int:
    """
    Clearly count twin primes within a specified range inclusively.

    Args:
        start (int): Clearly provided lower bound (inclusive).
        end (int): Clearly provided upper bound (inclusive).

    Returns:
        int: Count of twin primes clearly found within the range.
    """
    if start > end:
        start, end = end, start  # Ensure start <= end clearly

    all_twin_primes = find_twin_primes(end)
    range_twin_primes = [
        (p1, p2) for p1, p2 in all_twin_primes if p1 >= start and p2 <= end
    ]

    return len(range_twin_primes)


def interactive_twin_prime_finder():
    """Interactive console clearly structured for user analysis and twin prime counting."""
    try:
        limit_input = input(
            "Enter positive integer limit to find twin primes: "
        ).strip()
        limit = int(limit_input)
        if limit <= 2:
            raise ValueError("Limit must be greater than 2.")

        twin_primes = find_twin_primes(limit)

        print("\nTwin primes clearly identified:")
        for tp in twin_primes:
            print(tp)

        twin_primes_count = len(twin_primes)
        print(
            f"\nTotal twin primes clearly counted under or equal to {limit}: {twin_primes_count}"
        )

        # Prompt user for range clearly
        print("\nCheck twin primes clearly within a specific range:")
        start_range = int(input("Enter clearly provided start of range: ").strip())
        end_range = int(input("Enter clearly provided end of range: ").strip())

        range_count = count_twin_primes_in_range(start_range, end_range)

        print(
            f"\nTwin primes count clearly within range ({start_range}, {end_range}): {range_count}"
        )

        # Save results clearly to CSV
        save_twin_primes_to_csv(twin_primes)

    except ValueError as e:
        print(f"Error: {e}")


# Interactive main execution clearly provided
if __name__ == "__main__":
    interactive_twin_prime_finder()
