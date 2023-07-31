# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.


from pathlib import Path
from file_formats.csv_utils import csv_to_json

# def csv_to_json(csv_file, json_file):
#     lst = []
#     with open(csv_file, "r", encoding="UTF-8") as csv_f:
#         file = list(csv.reader(csv_f))
#         headers_id, headers_name, headers_access = file[0]
#
#         for i, line in enumerate(file[1:]):
#             level, user_id, name = line
#             lst.append({headers_id: user_id.zfill(10), headers_name: name.title(), headers_access: level, 'hash': hash(name+user_id)})
#
#     with open(json_file, "w", encoding="UTF-8") as json_f:
#         json.dump(lst, json_f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    csv_to_json("file2.csv", "file2.json")