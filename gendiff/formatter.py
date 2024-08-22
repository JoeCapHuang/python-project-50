from gendiff.formats.json import format_json
from gendiff.formats.stylish import format_stylish
from gendiff.formats.plain import format_plain


def formatter(tree: dict, format_name):
    match format_name:
        case 'stylish':
            return format_stylish(tree)
        case 'plain':
            return format_plain(tree)
        case 'json':
            return format_json(tree)
