import pytest
import networkx as nx
from pv_sdk.visualization import (
    graphical_representation_with_labels,
    detect_graph_communities,
    calculate_centrality_measures
)

def test_graphical_representation_with_labels():
    primes = [2, 3, 5, 7, 11]
    vowels = ["E", "I", "O", "U", "A"]

    # Test that the returned object is a valid NetworkX Graph object explicitly
    graph = graphical_representation_with_labels(primes, vowels, "test_graph.png")
    assert isinstance(graph, nx.Graph)

def test_detect_graph_communities():
    graph = nx.Graph([(1, 2), (2, 3), (4, 5), (5, 6)])
    communities = detect_graph_communities(graph)

    # Basic correctness checks explicitly defined
    assert isinstance(communities, list)
    assert len(communities) >= 1
    for community in communities:
        assert isinstance(community, list)

def test_calculate_centrality_measures():
    graph = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1)])
    centralities = calculate_centrality_measures(graph)

    expected_measures = {"degree_centrality", "betweenness_centrality", "closeness_centrality"}
    assert set(centralities.keys()) == expected_measures

    for measure_values in centralities.values():
        assert isinstance(measure_values, dict)
        assert all(isinstance(v, float) for v in measure_values.values())