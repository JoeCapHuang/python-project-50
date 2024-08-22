import json
import yaml
import os


def open_and_parse_file(filepath):
    file, file_extension = open(filepath), os.path.splitext(filepath)[-1].lower()

    match file_extension:
        case '.json':
            return json.load(file)
        case '.yaml' | '.yml':
            return yaml.safe_load(file)
        case _:
            print('invalid file extension')
