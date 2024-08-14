import json
import yaml


def pars_file(file, ext):
    match ext:
        case '.json':
            return json.load(file)
        case '.yaml' | '.yml':
            return yaml.safe_load(file)
        case _:
            print('invalid file extension')
