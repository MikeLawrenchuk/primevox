import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Dict
from networkx.algorithms.community import girvan_newman

def graphical_representation_with_labels(primes: List[int], vowel_mappings: List[str], output_file='prime_vowel_graph.png') -> nx.Graph:
    """
    Visualize prime-vowel mappings with explicit labels and save to a specified file.

    Args:
        primes (List[int]): List of prime numbers.
        vowel_mappings (List[str]): Corresponding vowels for each prime.
        output_file (str): Filename for saving graph.

    Returns:
        nx.Graph: The constructed NetworkX graph.
    """
    graph = nx.Graph()

    # Define node colors according to vowel assignments
    color_map = {
        'A': 'red', 'E': 'blue', 'I': 'green',
        'O': 'orange', 'U': 'purple', 'Y': 'gray'
    }
    node_colors = [color_map.get(vowel, 'black') for vowel in vowel_mappings]

    vowel_groups = {}
    for prime, vowel in zip(primes, vowel_mappings):
        vowel_groups.setdefault(vowel, []).append(prime)

    # Connect nodes sharing the same vowel
    for primes_list in vowel_groups.values():
        graph.add_edges_from(
            (primes_list[i], primes_list[j])
            for i in range(len(primes_list))
            for j in range(i+1, len(primes_list))
        )

    # Graph visualization setup
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(12, 9))
    nx.draw_networkx(
        graph,
        pos=pos,
        node_color=node_colors,
        edge_color='gray',
        alpha=0.8,
        with_labels=True,
        font_size=8,
        node_size=200
    )

    # Title and save visualization
    plt.title('Prime-Vowel Graph with Labels')
    plt.savefig(output_file, format='png', dpi=300)
    plt.show()

    return graph

def detect_graph_communities(graph: nx.Graph) -> List[List[int]]:
    """
    Detect and return communities within a graph using Girvan-Newman algorithm.

    Args:
        graph (nx.Graph): NetworkX graph to analyze.

    Returns:
        List[List[int]]: Detected communities represented as lists of nodes.
    """
    communities_generator = girvan_newman(graph)
    communities = next(communities_generator)
    return [list(community) for community in communities]

def calculate_centrality_measures(graph: nx.Graph) -> Dict[str, Dict[int, float]]:
    """
    Calculates centrality measures (degree, betweenness, closeness).

    Args:
        graph (nx.Graph): Graph for which centralities will be calculated.

    Returns:
        Dict[str, Dict[int, float]]: A dictionary of centrality dictionaries.
    """
    return {
        'degree_centrality': nx.degree_centrality(graph),
        'betweenness_centrality': nx.betweenness_centrality(graph),
        'closeness_centrality': nx.closeness_centrality(graph)
    }

def interactive_visualization():
    """Interactive visualization and analysis tool for quick validation."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    vowels = ['E', 'I', 'O', 'U', 'A', 'I', 'U', 'Y', 'A', 'I']

    print("Generating Graph Visualization...")
    graph = graphical_representation_with_labels(primes, vowels)

    print("\nDetecting Graph Communities...")
    communities = detect_graph_communities(graph)
    for idx, community in enumerate(communities, start=1):
        print(f"Community {idx}: {community}")

    print("\nCalculating Centrality Measures...")
    centralities = calculate_centrality_measures(graph)
    for measure, values in centralities.items():
        print(f"\n{measure.capitalize()}:")
        for node, centrality_value in values.items():
            print(f"Prime {node}: {centrality_value:.3f}")

# Interactive main execution clearly provided
if __name__ == "__main__":
    interactive_visualization()