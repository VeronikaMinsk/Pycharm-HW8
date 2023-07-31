import os
import json
import pickle
import csv

def convert_json_to_pickle(directory):
    script_directory = os.path.dirname(__file__)
    directory_path = os.path.join(script_directory, directory)

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            json_file = os.path.join(directory_path, filename)
            pickle_file = os.path.join(directory_path, filename[:-5] + '.pickle')

            with open(json_file, 'r', encoding='utf-8') as json_f:
                data = json.load(json_f)
            with open(pickle_file, 'wb') as pickle_f:
                pickle.dump(data, pickle_f)

def pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as pickle_f:
        data = pickle.load(pickle_f)
    if not data:
        return

    fieldnames = list(data[0].keys())

    with open(csv_file, 'w', encoding='UTF-8', newline='') as csv_f:
        writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def read_csv_as_pickle_string(csv_file):
    data = []

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            data.append(row)

    pickle_string = pickle.dumps(data)
    return pickle_string
