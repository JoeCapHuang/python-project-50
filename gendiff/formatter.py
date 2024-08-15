from gendiff.formats.json import gen_json
from gendiff.formats.stylish import gen_stylish
from gendiff.formats.plain import gen_plain


def formatter(tree: dict, format_name):
    match format_name:
        case 'stylish':
            return gen_stylish(tree)
        case 'plain':
            return gen_plain(tree)
        case 'json':
            return gen_json(tree)
