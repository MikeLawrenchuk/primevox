import networkx as nx
from scipy.stats import chisquare
from typing import List, Dict


def explore_modular_arithmetic(primes: List[int], modulus: int) -> Dict[int, int]:
    """
    Explores modular arithmetic properties for a list of prime numbers.

    Args:
        primes (List[int]): List of prime numbers.
        modulus (int): Modulus for arithmetic (must be > 0).

    Returns:
        Dict[int, int]: Dictionary mapping each prime to its modulus result.
    """
    if modulus <= 0:
        raise ValueError("Modulus must be positive.")

    modular_results = {prime: prime % modulus for prime in primes}
    return modular_results


def analyze_graph_properties(graph: nx.Graph) -> Dict:
    """
    Analyzes various properties of a given NetworkX graph.

    Args:
        graph (nx.Graph): Graph to analyze.

    Returns:
        Dict: Dictionary of graph properties, including connectivity,
              degree distribution, cliques information, and average degree.
    """
    if len(graph) == 0:
        connectivity = False
        degree_distribution = {}
        total_cliques = 0
        maximal_cliques_count = 0
        avg_degree = 0.0
    else:
        connectivity = nx.is_connected(graph)
        degree_distribution = dict(graph.degree())
        total_cliques = sum(nx.number_of_cliques(graph).values())
        maximal_cliques = list(nx.find_cliques(graph))
        avg_degree = sum(degree_distribution.values()) / len(degree_distribution)
        maximal_cliques_count = len(maximal_cliques)

    return {
        "connectivity": connectivity,
        "degree_distribution": degree_distribution,
        "total_cliques": total_cliques,
        "maximal_cliques_count": maximal_cliques_count,
        "avg_degree": avg_degree,
    }


def perform_statistical_analysis(frequency: Dict[str, int]) -> float:
    """
    Conducts a chi-square test on frequency distribution to detect significant patterns.

    Args:
        frequency (Dict[str, int]): Observed frequency count.

    Returns:
        float: p-value from the chi-square test indicating pattern significance.
    """
    if not frequency:
        print("Warning: Frequency dictionary empty. Returning p-value of 1.0.")
        return 1.0

    observed_values = list(frequency.values())
    expected_values = [sum(observed_values) / len(observed_values)] * len(
        observed_values
    )

    chi2_stat, p_value = chisquare(observed_values, f_exp=expected_values)

    return p_value


def interactive_analysis():
    """Interactive testing clearly structured for immediate use."""
    # Modular arithmetic exploration clear example:
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    modulus = 5
    print(
        "Modular Arithmetic Exploration:", explore_modular_arithmetic(primes, modulus)
    )

    # Graph analysis clear example:
    graph = nx.Graph()
    graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4), (3, 1)])
    print("Graph Properties Analysis:", analyze_graph_properties(graph))

    # Statistical analysis clear example:
    frequency_data = {"A": 15, "E": 12, "I": 13, "O": 10, "U": 20}
    p_value = perform_statistical_analysis(frequency_data)
    print(f"Statistical Analysis result - chi-square p-value: {p_value:.4f}")


if __name__ == "__main__":
    interactive_analysis()
