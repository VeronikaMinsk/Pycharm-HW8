# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

from pathlib import Path
import os
from file_formats.pickle_utils import convert_json_to_pickle

if __name__ == '__main__':
    current_directory = os.getcwd()
    convert_json_to_pickle(current_directory)
# import os
# import json
# import pickle
#
# def convert_json_to_pickle(directory):
#     script_directory = os.path.dirname(__file__)
#     directory_path = os.path.join(script_directory, directory)
#
#     for filename in os.listdir(directory_path):
#         if filename.endswith('.json'):
#             json_file = os.path.join(directory_path, filename)
#             pickle_file = os.path.join(directory_path, filename[:-5] + '.pickle')
#
#             with open(json_file, 'r', encoding='utf-8') as json_f:
#                 data = json.load(json_f)
#
#             with open(pickle_file, 'wb') as pickle_f:
#                 pickle.dump(data, pickle_f)

