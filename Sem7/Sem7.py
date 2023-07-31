# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import os
from file_formats.pickle_utils import read_csv_as_pickle_string


# import csv
# import pickle
#
# def read_csv_as_pickle_string(csv_file):
#     data = []
#
#     with open(csv_file, 'r') as file:
#         reader = csv.reader(file)
#         header = next(reader)
#
#         for row in reader:
#             data.append(row)
#
#     pickle_string = pickle.dumps(data)
#     return pickle_string

if __name__ == '__main__':
    current_directory = os.getcwd()
    files_in_directory = os.listdir(current_directory)
    csv_files = [file for file in files_in_directory if file.endswith('.csv')]

    for csv_file in csv_files:
        csv_file_path = os.path.join(current_directory, csv_file)
        pickle_string = read_csv_as_pickle_string(csv_file_path)
        print(f"Файл '{csv_file}' прочитан и преобразован в pickle строку:\n{pickle_string}\n")


