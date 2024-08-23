from gendiff.pars_file import open_and_parse_file
from gendiff.diff_tree import build_diff_tree
from gendiff.formats.formatter import formatter


def gendiff(filepath1, filepath2, format_name="stylish") -> str:
    data1, data2 = open_and_parse_file(filepath1), open_and_parse_file(filepath2)
    diff_tree = build_diff_tree(data1, data2)
    return formatter(diff_tree, format_name)
