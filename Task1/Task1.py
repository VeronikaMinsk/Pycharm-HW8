# 2.Напишите функцию, которая получает на вход директорию и
# рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json,
# csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех
# вложенных файлов и директорий.

from file_formats.file_utils import save_to_json_csv_pickle
import os
import json
import csv
import pickle
from pathlib import Path

# def get_directory_size(directory: Path) -> int:
#     total_size = 0
#     for dirpath, dirnames, filenames in os.walk(directory):
#         for filename in filenames:
#             file_path = os.path.join(dirpath, filename)
#             total_size += os.path.getsize(file_path)
#
#         for dirname in dirnames:
#             dir_path = os.path.join(dirpath, dirname)
#             total_size += get_directory_size(dir_path)
#
#     return total_size
#
# def save_to_json_csv_pickle(directory: Path):
#     results = []
#     for dirpath, dirnames, filenames in os.walk(directory):
#         for dirname in dirnames:
#             dir_path = os.path.join(dirpath, dirname)
#             size = get_directory_size(dir_path)
#             results.append({
#                 'path': dir_path,
#                 'type': 'directory',
#                 'size': size
#             })
#
#         for filename in filenames:
#             file_path = os.path.join(dirpath, filename)
#             size = os.path.getsize(file_path)
#             results.append({
#                 'path': file_path,
#                 'type': 'file',
#                 'size': size
#             })
#
#     with open('result.json', 'w', encoding='utf-8') as json_file:
#         json.dump(results, json_file, indent=2)
#
#     with open('result.csv', 'w', encoding='utf-8', newline='') as csv_file:
#         csv_writer = csv.DictWriter(csv_file, fieldnames=['path', 'type', 'size'])
#         csv_writer.writeheader()
#         csv_writer.writerows(results)
#
#     with open('result.pickle', 'wb') as pickle_file:
#         pickle.dump(results, pickle_file)

if __name__ == '__main__':
    current_directory = os.path.dirname(os.getcwd())
    save_to_json_csv_pickle(current_directory)