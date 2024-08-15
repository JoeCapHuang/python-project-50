from gendiff.pars_file import pars_file
from gendiff.diff_tree import build_diff_tree
from gendiff.formatter import formatter
import os


def gen_diff(filepath1, filepath2, format_name="stylish") -> str:
    with (
        open(filepath1) as file1,
        open(filepath2) as file2,
    ):
        file_ext1 = os.path.splitext(filepath1)[-1].lower()
        file_ext2 = os.path.splitext(filepath2)[-1].lower()
        file1 = pars_file(file1, file_ext1)
        file2 = pars_file(file2, file_ext2)
        diff_tree = build_diff_tree(file1, file2)
        result = formatter(diff_tree, format_name)
        return result
