import json
import os
import glob
import csv
from datetime import datetime

def extract_lighthouse_data(json_file_path):
    """
    Extracts specific data points from a Lighthouse JSON report.

    Args:
        json_file_path (str): The path to the Lighthouse JSON report.

    Returns:
        tuple: A tuple containing (performance, FCP, LCP, total_byte_weight)
               or (None, None, None, None) if an error occurs or data is missing.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Extract performance score
        performance = data.get('categories', {}).get('performance', {}).get('score')
        if performance is not None:
            performance = round(performance * 100, 1)

        # Extract first-contentful-paint (FCP)
        fcp = None
        metrics = data.get('audits', {}).get('first-contentful-paint', {})
        if metrics:
            fcp = metrics.get('numericValue')
            if fcp is not None:
                fcp = round(fcp, 1)

        # Extract largest-contentful-paint (LCP)
        lcp = None
        metrics = data.get('audits', {}).get('largest-contentful-paint', {})
        if metrics:
            lcp = metrics.get('numericValue')
            if lcp is not None:
                lcp = round(lcp, 1)

        # Extract total byte weight
        total_byte_weight = None
        metrics = data.get('audits', {}).get('total-byte-weight', {})
        if metrics:
            total_byte_weight = metrics.get('numericValue')
            if total_byte_weight is not None:
                total_byte_weight = round(total_byte_weight, 1)

        # Extract URL from the report
        url = data.get('requestedUrl')

        return url, performance, fcp, lcp, total_byte_weight

    except FileNotFoundError:
        print(f"Error: File not found at {json_file_path}")
        return None, None, None, None, None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {json_file_path}")
        return None, None, None, None, None
    except Exception as e:
        print(f"An unexpected error occurred while processing {json_file_path}: {e}")
        return None, None, None, None, None

def create_lighthouse_csv():
    """
    Reads Lighthouse JSON reports from the 'results' subfolder,
    transforms them into CSV lines, and saves them to a CSV file.
    """
    results_dir = 'results'
    if not os.path.exists(results_dir):
        print(f"Error: The directory '{results_dir}' does not exist. Please create it and place your Lighthouse JSON reports inside.")
        return

    json_files = glob.glob(os.path.join(results_dir, '*.json'))

    if not json_files:
        print(f"No JSON files found in the '{results_dir}' directory.")
        return

    csv_data = []
    current_datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for json_file in json_files:
        url, performance, fcp, lcp, total_byte_weight = extract_lighthouse_data(json_file)

        if url:  # Only add if we successfully extracted a URL
            csv_data.append({
                'date': current_datetime_str,
                'url': url,
                'source_file': os.path.basename(json_file),
                'performance_percent': performance if performance is not None else '',
                'fcp': fcp if fcp is not None else '',
                'lcp': lcp if lcp is not None else '',
                'total_byte_weight': total_byte_weight if total_byte_weight is not None else ''
            })

    # Sort the data by URL
    csv_data.sort(key=lambda x: x['url'])

    # Define CSV file name
    csv_filename = f"lh-results-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    csv_filepath = os.path.join(results_dir, csv_filename)

    if not csv_data:
        print("No valid data extracted to create a CSV file.")
        return

    # Write data to CSV
    try:
        with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['date', 'url', 'source_file', 'performance_percent', 'fcp', 'lcp', 'total_byte_weight']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in csv_data:
                writer.writerow(row)
        print(f"Successfully created CSV file: {csv_filepath}")
    except IOError as e:
        print(f"Error writing CSV file {csv_filepath}: {e}")

if __name__ == "__main__":
    create_lighthouse_csv()