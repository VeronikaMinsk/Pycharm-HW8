
import json
import csv
from pathlib import Path

def convert_csv(file: Path):
    with (open(file, 'r', encoding='utf-8') as fj,
          open(f'{file.stem}.csv', 'w', encoding='utf-8', newline='') as fc):

        spam = json.load(fj)
        temp_list = []
        for level, value in spam.items():
            for id_cod, name in value.items():
                temp_list.append({'level': int(level), 'id_cod': id_cod, 'name': name})

        csv_temp = csv.DictWriter(fc, dialect='excel', fieldnames=['level', 'id_cod', 'name'])
        csv_temp.writeheader()
        csv_temp.writerows(temp_list)


def csv_to_json(csv_file, json_file):
    lst = []
    with open(csv_file, "r", encoding="UTF-8") as csv_f:
        file = list(csv.reader(csv_f))
        headers_id, headers_name, headers_access = file[0]

        for i, line in enumerate(file[1:]):
            level, user_id, name = line
            lst.append({headers_id: user_id.zfill(10), headers_name: name.title(), headers_access: level, 'hash': hash(name+user_id)})

    with open(json_file, "w", encoding="UTF-8") as json_f:
        json.dump(lst, json_f, ensure_ascii=False, indent=2)