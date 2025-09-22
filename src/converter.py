import csv
import json
import os
import pandas as pd
import sys

def csv_to_json(csv_file_path, json_file_path):
    try:
        data = []

        with open(csv_file_path, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")
        sys.exit(1)

def csv_to_excel(csv_file_path, excel_file_path):
    try:
        df = pd.read_csv(csv_file_path)
        df.to_excel(excel_file_path, index=False)

    except Exception as e:
        print(f"Error converting CSV to Excel: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) !=3:
        print("Usage: python converter.py <csv_file_path> <output_file_type (json|excel)>")
        sys.exit(1)

    csv_file = sys.argv[1]
    output_file_type = sys.argv[2].lower()
    file_name = os.path.splitext(os.path.basename(csv_file))[0]

    if not os.path.exists(csv_file):
        print("File not found!")
        sys.exit(1)

    if output_file_type == "json":
        csv_to_json(csv_file, file_name + ".json")
        print(f"Successfully converted {csv_file} to {file_name}.json")
    elif output_file_type == "excel":
        csv_to_excel(csv_file, file_name + ".xlsx")
        print(f"Successfully converted {csv_file} to {file_name}.xlsx")
    else:
        print("Unsupported output file type! Use 'json' or 'excel'.")
        sys.exit(1)