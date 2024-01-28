import csv
import json

def csv_to_json(csv_filepath, json_filepath):
    data = []

    # Read CSV file and convert to a list of dictionaries
    with open(csv_filepath, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            data.append(row)

    # Writes the list of dictionaries to a JSON file
    with open(json_filepath, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f'Arquivo JSON gerado com sucesso em: {json_filepath}')

# Replace '../fakedb.csv' with the actual path of your CSV file
# and './fakedb.json' with the desired path to the output JSON file.
csv_filepath = '../fakedb.csv'
json_filepath = './fakedb.json'

csv_to_json(csv_filepath, json_filepath)
