import matplotlib.pyplot as plt
import networkx as nx
from sympy import factorint

digit_to_vowel = {
    "1": "A",
    "3": "E",
    "5": "Y",
    "7": "I",
    "9": "O",
}


def prime_to_vowel_notation(prime):
    prime_str = str(prime)

    # Special case for prime number 2
    if prime == 2:
        return "U"

    # General mapping for other primes
    return "".join(
        digit_to_vowel[digit] if digit in digit_to_vowel else "1" for digit in prime_str
    )


# Factorize the number and map factors to vowel notation
def factor_and_map(number):
    factors = factorint(number)
    mapped_factors = []

    for prime, exponent in factors.items():
        vowel_prime = prime_to_vowel_notation(prime)
        if exponent > 1:
            mapped_factor = vowel_prime[0].lower() + vowel_prime[1:] + str(exponent)
        else:
            mapped_factor = vowel_prime

        mapped_factors.append(mapped_factor)

    return mapped_factors, factors


# Visualize factorization graph
def visualize_factors(number, factors):
    G = nx.DiGraph()
    G.add_node(str(number), color="lightblue", style="filled")

    for prime, exponent in factors.items():
        prime_node = f"{prime}^{exponent}" if exponent > 1 else str(prime)
        G.add_node(prime_node, color="lightgreen", style="filled")
        G.add_edge(str(number), prime_node)

    colors = [data["color"] for _, data in G.nodes(data=True)]
    pos = nx.spring_layout(G)
    nx.draw(
        G, pos, with_labels=True, node_color=colors, node_size=2000, font_weight="bold"
    )
    plt.title(f"Factorization Graph for {number}")
    plt.show()


# Main function
def main():
    composite_number = int(
        input("Enter composite number to factor (up to 25 digits): ")
    )
    mapped_factors, numeric_factors = factor_and_map(composite_number)

    print(f"Prime factors of {composite_number} mapped to vowels:")
    for factor in mapped_factors:
        print(factor)

    visualize_factors(composite_number, numeric_factors)


if __name__ == "__main__":
    main()
