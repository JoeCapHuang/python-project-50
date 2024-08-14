from gendiff.formats import stylish

def formatter(tree: dict, form = 'stylish'):
    match form:
        case 'stylish':
            return stylish(tree)
