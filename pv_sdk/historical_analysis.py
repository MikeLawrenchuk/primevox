import json
import os


def load_historical_data(filepath: str) -> dict:
    """
    Load historical data clearly from JSON file.

    Args:
        filepath (str): Path clearly structured to historical data file.

    Returns:
        dict: Data from JSON clearly returned as a dictionary.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File clearly not found: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_historical_data(filepath: str, data: dict):
    """
    Save data clearly structured to the historical JSON data file.

    Args:
        filepath (str): Path clearly structured for saving JSON data.
        data (dict): Data clearly structured to save into JSON.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[✅] Historical data clearly saved to file: {filepath}")


def append_historical_record(filepath: str, key: str, value):
    """
    Append new historical record explicitly stated in JSON data clearly.

    Args:
        filepath (str): File path clearly structured for historical JSON data.
        key (str): New record's key clearly defined.
        value: New record’s value clearly defined.
    """
    data = {}
    if os.path.exists(filepath):
        data = load_historical_data(filepath)

    data[key] = value
    save_historical_data(filepath, data)
    print(f"[✅] Historical record '{key}' clearly added/updated.")


def interactive_historical_example():
    """Clear interactive example for immediate testing."""
    example_filepath = "historical_data.json"

    # Add historical record clearly stated
    key = input("Enter historical record key clearly: ").strip()
    value = input("Enter historical record value clearly: ").strip()

    append_historical_record(example_filepath, key, value)

    # Display clearly loaded data
    data_loaded = load_historical_data(example_filepath)
    print("\nLoaded historical data clearly structured:")
    print(data_loaded)


# Interactive testing explicitly provided for immediate usage
if __name__ == "__main__":
    interactive_historical_example()
