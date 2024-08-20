from gendiff.pars_file import pars_file
from gendiff.diff_tree import build_diff_tree
from gendiff.formatter import formatter
import os


def open_and_get_ext(filepath):
    return open(filepath), os.path.splitext(filepath)[-1].lower()


def gen_diff(filepath1, filepath2, format_name="stylish") -> str:
    file1, file_ext1 = open_and_get_ext(filepath1)
    file2, file_ext2 = open_and_get_ext(filepath2)

    try:
        first_file = pars_file(file1, file_ext1)
        second_file = pars_file(file2, file_ext2)

        diff_tree = build_diff_tree(first_file, second_file)
        result = formatter(diff_tree, format_name)

    finally:
        file1.close()
        file2.close()

    return result
