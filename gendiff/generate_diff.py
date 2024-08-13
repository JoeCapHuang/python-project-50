import argparse
from gendiff.pars_file import pars_file


def normalize_value(value):
    if value is False or True:
        return str(value).lower()
    else:
        return value


def pars_arg():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser.parse_args()


def gen_diff(filepath1, filepath2) -> str:
    with (
        open(filepath1) as file1,
        open(filepath2) as file2,
    ):
        file1 = pars_file(file1)
        file2 = pars_file(file2)

        result = '{\n'
        for key, value in sorted(file1.items()):
            value = normalize_value(value)
            if key in file2 and value == file2[key]:
                result += f'    {key}: {value}\n'
            elif key not in file2 or value != file2[key]:
                result += f'  - {key}: {value}\n'
        for key, value in sorted(file2.items()):
            value = normalize_value(value)
            if key not in file1 or value != file1[key]:
                result += f'  + {key}: {value}\n'
        result += '}'
        return result
