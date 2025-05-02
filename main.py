import networkx as nx

from pv_sdk.analysis import (
    analyze_graph_properties,
    explore_modular_arithmetic,
    perform_statistical_analysis,
)
from pv_sdk.coloring import TerminalColors, colorize
from pv_sdk.documentation import append_timestamp, save_to_json
from pv_sdk.factoring import factor, factor_and_map
from pv_sdk.historical_analysis import append_historical_record, load_historical_data
from pv_sdk.prime import create_composite_mappings, generate_primes_and_map
from pv_sdk.twin_primes import count_twin_primes, find_twin_primes
from pv_sdk.visualization import (
    calculate_centrality_measures,
    detect_graph_communities,
    graphical_representation_with_labels,
)


def main():
    print(
        colorize(
            "\n🚀 PrimeVox SDK Example Execution Started 🚀\n",
            TerminalColors.HEADER,
            bold=True,
        )
    )

    # —— Prime Module usage ——
    prime_limit = 50
    orig_primes, orig_vowels = generate_primes_and_map(prime_limit)
    print(colorize(f"✅ Generated primes up to {prime_limit}:", TerminalColors.GREEN))
    print(orig_primes)

    # —— Composite Mappings ——
    composites = create_composite_mappings(orig_primes, orig_vowels)
    print(colorize("\n✅ Composite mappings sample (first 3):", TerminalColors.GREEN))
    print(composites[:3])

    # —— High-performance Factoring Module ——
    number_to_factor = 1001  # factors: 7, 11, 13
    print(colorize(f"\n🧮 Factoring number: {number_to_factor}", TerminalColors.CYAN))

    factored_primes = factor(number_to_factor)
    print(colorize(f"✔ Found prime factors: {factored_primes}", TerminalColors.GREEN))

    mapped = factor_and_map(number_to_factor)
    print(colorize(f"🔤 Vowel-mapped factors: {mapped}", TerminalColors.CYAN))

    # —— Analysis Module ——
    modulus = 7
    modular_results = explore_modular_arithmetic(orig_primes, modulus)
    print(
        colorize(
            f"\n📊 Modular arithmetic results modulo {modulus}:", TerminalColors.CYAN
        )
    )
    print(modular_results)

    sample_graph = nx.Graph([(1, 2), (2, 3), (3, 1)])
    graph_analysis = analyze_graph_properties(sample_graph)
    print(colorize("\n📈 Graph analysis results:", TerminalColors.CYAN))
    print(graph_analysis)

    freq = {"A": 24, "E": 30, "I": 18, "O": 20, "U": 8}
    p_val = perform_statistical_analysis(freq)
    print(colorize(f"\n📌 Chi-square test p-value: {p_val:.4f}", TerminalColors.CYAN))

    # —— Visualization Module ——
    # Use the ORIGINAL lists so you see all 15 primes up to 50
    graphical_representation_with_labels(orig_primes, orig_vowels)

    prime_graph = nx.Graph()
    prime_graph.add_edges_from([(2, 3), (3, 5), (5, 7), (7, 2)])
    communities = detect_graph_communities(prime_graph)
    centralities = calculate_centrality_measures(prime_graph)
    print(colorize("\n👥 Graph communities detected:", TerminalColors.BLUE))
    print(communities)
    print(colorize("\n📍 Graph centrality measures:", TerminalColors.BLUE))
    print(centralities)

    # —— Twin Prime Module ——
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

    # —— Documentation Module ——
    results = {
        "primes": orig_primes,
        "modular_results": modular_results,
        "twin_primes": twin_primes[:5],
    }
    json_filename = append_timestamp("PrimeVox_results_summary.json")
    save_to_json(json_filename, results)

    # —— Historical Analysis Module ——
    append_historical_record(
        "historical_data.json",
        "recent_prime_analysis",
        {"prime_limit": prime_limit, "found_primes": len(orig_primes)},
    )
    historical_data = load_historical_data("historical_data.json")
    print(colorize("\n🗃️ Historical data loaded:", TerminalColors.GREEN))
    print(historical_data)

    print(
        colorize(
            "\n🎯 PrimeVox SDK Example Execution Completed 🎯\n", TerminalColors.BOLD
        )
    )


if __name__ == "__main__":
    main()
