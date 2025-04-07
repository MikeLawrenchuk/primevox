import csv
import json
import os
from datetime import datetime

def save_to_text(filename: str, content: str):
    """
    Save content clearly and simply in a text file.

    Args:
        filename (str): Filename clearly structured for text output.
        content (str): Text content clearly documented.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"[✅] Data clearly saved to text file: {filename}")

def save_to_json(filename: str, content: dict):
    """
    Save dictionary content clearly structured into a JSON file.

    Args:
        filename (str): JSON file clearly named for structured saving.
        content (dict): Dictionary data clearly structured for saving.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=4)
    print(f"[✅] Data clearly saved to JSON file: {filename}")

def save_to_csv(filename: str, headers: list, rows: list):
    """
    Save tabular data clearly structured into a CSV file.

    Args:
        filename (str): CSV file clearly named for structured saving.
        headers (list): Column headers clearly defined.
        rows (list): Rows of data clearly structured as a list of lists.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"[✅] Data clearly saved to CSV file: {filename}")

def append_timestamp(filename: str) -> str:
    """
    Append a clear, unique timestamp to filename to prevent overwriting.

    Args:
        filename (str): Original filename clearly structured for appending.

    Returns:
        str: Filename clearly appended with current timestamp.
    """
    base, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{base}_{timestamp}{ext}"

# Example interactive feature for quick usage
if __name__ == "__main__":
    # Clearly separated example usage
    sample_content = "PrimeVox Documentation Example - Quick Notes."
    text_filename = append_timestamp('notes.txt')
    save_to_text(text_filename, sample_content)

    sample_json = {"project": "PrimeVox", "module": "Documentation", "status": "complete"}
    json_filename = append_timestamp('docs.json')
    save_to_json(json_filename, sample_json)

    csv_headers = ["Prime Number", "Corresponding Vowel"]
    csv_rows = [[2, "E"], [3, "I"], [5, "O"], [7, "U"]]
    csv_filename = append_timestamp('primes_vowels.csv')
    save_to_csv(csv_filename, csv_headers, csv_rows)