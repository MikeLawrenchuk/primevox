import networkx as nx
import pytest

from pv_sdk.analysis import (
    analyze_graph_properties,
    explore_modular_arithmetic,
    perform_statistical_analysis,
)


def test_explore_modular_arithmetic():
    primes = [2, 3, 5, 7, 11, 13]
    modulus = 5
    expected_result = {2: 2, 3: 3, 5: 0, 7: 2, 11: 1, 13: 3}

    assert explore_modular_arithmetic(primes, modulus) == expected_result

    # Test invalid modulus clearly raises error
    with pytest.raises(ValueError):
        explore_modular_arithmetic(primes, 0)


def test_analyze_graph_properties():
    graph = nx.Graph([(1, 2), (2, 3), (3, 4), (4, 1)])
    result = analyze_graph_properties(graph)

    assert result["connectivity"] is True
    assert result["total_cliques"] >= 0
    assert result["maximal_cliques_count"] >= 1
    assert "degree_distribution" in result
    assert all(isinstance(v, int) for v in result["degree_distribution"].values())
    assert "avg_degree" in result
    assert isinstance(result["avg_degree"], float)

    # Test empty graph clearly handled
    empty_graph = nx.Graph()
    result_empty = analyze_graph_properties(empty_graph)
    assert result_empty["connectivity"] is False
    assert result_empty["avg_degree"] == 0
    assert result_empty["degree_distribution"] == {}


def test_perform_statistical_analysis():
    frequency = {"A": 10, "B": 20, "C": 30, "D": 40}
    p_value = perform_statistical_analysis(frequency)

    assert isinstance(p_value, float)
    assert 0 <= p_value <= 1

    # Test empty frequency invoking the explicit warning and returning 1.0
    empty_frequency = {}
    p_value_empty = perform_statistical_analysis(empty_frequency)
    assert p_value_empty == 1.0
