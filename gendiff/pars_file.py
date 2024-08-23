import json
import yaml
import os


def get_data_and_file_extension(filepath):
    with open(filepath, 'r') as file:
        return file.read(), os.path.splitext(filepath)[-1].lower()


def parse_data(data, file_extension):
    match file_extension:
        case '.json':
            return json.loads(data)
        case '.yaml' | '.yml':
            return yaml.safe_load(data)
        case _:
            print('invalid file extension')


def open_and_parse_file(filepath):
    data, file_extension = get_data_and_file_extension(filepath)
    return parse_data(data, file_extension)
