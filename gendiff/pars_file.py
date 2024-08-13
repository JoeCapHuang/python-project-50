import json
import yaml
import os


def pars_file(file):

    file_ext = os.path.splitext(file)[-1].lower()

    match file_ext:
        case '.json':
            return json.load(file)
        case '.yaml' | '.yml':
            return yaml.safe_load(file)
        case _:
            print('invalid file extension')
