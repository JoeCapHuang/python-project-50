from formats.plain import gen_plain
from formats.stylish import gen_stylish


def formatter(tree: dict, format_name):
    match format_name:
        case 'stylish':
            return gen_stylish(tree)
        case 'plain':
            return gen_plain(tree)
