from pathlib import Path
import os
import json
import csv
import pickle


def get_directory_size(directory: Path) -> int:
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)

        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            total_size += get_directory_size(dir_path)

    return total_size



def save_to_json_csv_pickle(directory: Path):
    results = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            size = get_directory_size(dir_path)
            results.append({
                'path': dir_path,
                'type': 'directory',
                'size': size
            })

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            size = os.path.getsize(file_path)
            results.append({
                'path': file_path,
                'type': 'file',
                'size': size
            })

    with open('result.json', 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, indent=2)

    with open('result.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['path', 'type', 'size'])
        csv_writer.writeheader()
        csv_writer.writerows(results)

    with open('result.pickle', 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

def fill_bd(file: Path):
    current_set = set()

    if Path.exists(file):
        with open(file, 'r', encoding='utf-8') as fj:
            dict_bd = json.load(fj)
            for _, value in dict_bd.items():
                current_set.update(value.keys())
    else:
        dict_bd = {i: {} for i in range(1, 8)}

        current_data = input(f'введите Имя, id, уровень доступа (от 1 до 7) через пробел: \n ')
        while current_data != "":
            name, id_cod, level = current_data.split()

            if id_cod not in current_set:
                current_set.add(id_cod)
                dict_bd[int(level)] = {id_cod: name}

                with open(file, "w", encoding='utf-8') as fj:
                    json.dump(dict_bd, fj, indent=2, ensure_ascii=False)

            current_data = input(f'введите Имя, id, уровень доступа (от 1 до 7) через пробел: \n ')