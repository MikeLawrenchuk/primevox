from pv_sdk.prime import generate_primes_and_map, create_composite_mappings
from pv_sdk.factoring import factor_large_number
from pv_sdk.analysis import (
    explore_modular_arithmetic,
    analyze_graph_properties,
    perform_statistical_analysis,
)
from pv_sdk.visualization import (
    graphical_representation_with_labels,
    detect_graph_communities,
    calculate_centrality_measures,
)
from pv_sdk.twin_primes import find_twin_primes, count_twin_primes
from pv_sdk.documentation import save_to_json, append_timestamp
from pv_sdk.historical_analysis import append_historical_record, load_historical_data
from pv_sdk.coloring import colorize, TerminalColors
import networkx as nx


def main():
    print(
        colorize(
            "\n🚀 PrimeVox SDK Example Execution Started 🚀\n",
            TerminalColors.HEADER,
            bold=True,
        )
    )

    # Prime Module usage clearly demonstrated
    prime_limit = 50
    primes, vowels = generate_primes_and_map(prime_limit)
    print(colorize(f"✅ Generated primes up to {prime_limit}:", TerminalColors.GREEN))
    print(primes)

    # Generate composite mappings clearly defined
    composites = create_composite_mappings(primes, vowels)
    print(colorize(f"\n✅ Composite mappings sample (first 3):", TerminalColors.GREEN))
    print(composites[:3])

    # Factoring Module clearly demonstrated
    number_to_factor = 1001  # factors: 7, 11, 13
    start_digits = "000001"
    end_digits = "000100"
    print(colorize(f"\n🧮 Factoring number: {number_to_factor}", TerminalColors.CYAN))
    factor_large_number(number_to_factor, start_digits, end_digits)

    # Analysis Module explicitly shown
    modulus = 7
    modular_results = explore_modular_arithmetic(primes, modulus)
    print(
        colorize(
            f"\n📊 Modular arithmetic results modulo {modulus}:", TerminalColors.CYAN
        )
    )
    print(modular_results)

    sample_graph = nx.Graph([(1, 2), (2, 3), (3, 1)])
    graph_analysis = analyze_graph_properties(sample_graph)
    print(colorize(f"\n📈 Graph analysis results:", TerminalColors.CYAN))
    print(graph_analysis)

    freq = {"A": 24, "E": 30, "I": 18, "O": 20, "U": 8}
    p_val = perform_statistical_analysis(freq)
    print(colorize(f"\n📌 Chi-square test p-value: {p_val:.4f}", TerminalColors.CYAN))

    # Visualization Module widely and clearly utilized
    graphical_representation_with_labels(primes, vowels)
    prime_graph = nx.Graph()
    prime_graph.add_edges_from([(2, 3), (3, 5), (5, 7), (7, 2)])
    communities = detect_graph_communities(prime_graph)
    centralities = calculate_centrality_measures(prime_graph)
    print(colorize(f"\n👥 Graph communities detected:", TerminalColors.BLUE))
    print(communities)
    print(colorize(f"\n📍 Graph centrality measures:", TerminalColors.BLUE))
    print(centralities)

    # Twin Prime Module demonstrated explicitly
    twin_primes = find_twin_primes(prime_limit)
    twin_prime_count = count_twin_primes(prime_limit)
    print(
        colorize(f"\n🔢 Twin primes clearly up to {prime_limit}:", TerminalColors.GREEN)
    )
    print(twin_primes)
    print(
        colorize(
            f"\n✔️ Total twin primes found: {twin_prime_count}", TerminalColors.GREEN
        )
    )

    # Documentation module clearly utilized
    results = {
        "primes": primes,
        "modular_results": modular_results,
        "twin_primes": twin_primes[:5],
    }
    json_filename = append_timestamp("PrimeVox_results_summary.json")
    save_to_json(json_filename, results)

    # Historical Analysis Module explicitly demonstrated
    append_historical_record(
        "historical_data.json",
        "recent_prime_analysis",
        {"prime_limit": prime_limit, "found_primes": len(primes)},
    )
    historical_data = load_historical_data("historical_data.json")
    print(colorize(f"\n🗃️ Historical data loaded:", TerminalColors.GREEN))
    print(historical_data)

    print(
        colorize(
            "\n🎯 PrimeVox SDK Example Execution Completed 🎯\n", TerminalColors.BOLD
        )
    )


# Clear Python entry point for structured custom execution
if __name__ == "__main__":
    main()
