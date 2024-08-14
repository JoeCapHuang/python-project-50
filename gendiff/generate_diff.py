import argparse
from gendiff.pars_file import pars_file
from gendiff.diff_tree import build_diff_tree
from gendiff.formatter import formatter
import os

# def normalize_value(value):
#     if value is False or True:
#         return str(value).lower()
#     else:
#         return value


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
        file_ext1 = os.path.splitext(filepath1)[-1].lower()
        file_ext2 = os.path.splitext(filepath2)[-1].lower()
        file1 = pars_file(file1, file_ext1)
        file2 = pars_file(file2, file_ext2)
        diff_tree = build_diff_tree(file1, file2)
        result = formatter(diff_tree)
        return result
