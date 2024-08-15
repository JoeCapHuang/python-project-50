from gendiff.formats import stylish


def formatter(tree: dict, format_name):
    match format_name:
        case 'stylish':
            return stylish(tree)
