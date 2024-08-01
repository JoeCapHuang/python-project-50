import json
import yaml
import os


def open_and_pars(filepath):
    with (
        open(filepath) as file,
    ):
        ext = os.path.splitext(filepath)[-1].lower()
        match ext:
            case '.json':
                return json.load(file)
            case '.yaml' | '.yml':
                return yaml.safe_load(file)
            case _:
                print('invalid file extension')
