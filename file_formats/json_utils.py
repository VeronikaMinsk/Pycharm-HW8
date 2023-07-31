import json
from pathlib import Path

def text_json(file: Path) -> None:
    file_data = {}
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            name, number = line.split(" ")
            file_data[name.capitalize()] = float(number)
        with open(file.stem + ".json", "w") as f:
            json.dump(file_data, f, indent = 2)
    pass

