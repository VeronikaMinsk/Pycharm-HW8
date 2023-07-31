# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import os
from file_formats.pickle_utils import pickle_to_csv

# import pickle
# import csv
#
# def pickle_to_csv(pickle_file, csv_file):
#     with open(pickle_file, 'rb') as pickle_f:
#         data = pickle.load(pickle_f)
# #     if not data:
#         return
# #     fieldnames = list(data[0].keys())
# #     with open(csv_file, 'w', encoding='UTF-8', newline='') as csv_f:
#         writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)

if __name__ == '__main__':
    script_directory = os.path.dirname(os.path.abspath(__file__))
    pickle_file_path = os.path.join(script_directory, 'file2.pickle')
    csv_file_path = os.path.join(script_directory, 'file2.csv')
    pickle_to_csv(pickle_file_path, csv_file_path)


