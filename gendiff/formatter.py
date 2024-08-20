from gendiff.formats.json import format_json
from gendiff.formats.stylish import gen_stylish
from gendiff.formats.plain import gen_plain


def formatter(tree: dict, format_name):
    match format_name:
        case 'stylish':
            return gen_stylish(tree)
        case 'plain':
            return gen_plain(tree)
        case 'json':
            return format_json(tree)
