import itertools

SPACES_PER_LEVEL = 4
LEFT_SHIFT = 2
SPACE = ' '
START_DEPTH = 1


def normalize_val(value, depth=1):
    if isinstance(value, dict):
        return flat_dict(value, depth + 1)
    match value:
        case False:
            return 'false'
        case True:
            return 'true'
        case None:
            return 'null'
    return value


def flat_dict(some_dict, depth):
    indent = SPACE * (SPACES_PER_LEVEL * depth)
    lines = []
    for key, value in some_dict.items():
        if isinstance(value, dict):
            lines.append(f"{indent}{key}: {flat_dict(value, depth + 1)}")
        else:
            lines.append(f"{indent}{key}: {value}")
    indent = SPACE * (SPACES_PER_LEVEL * depth - SPACES_PER_LEVEL)
    result = itertools.chain("{", lines, [indent + "}"])
    return '\n'.join(result)


def gen_stylish(tree):
    def inner(node, depth):
        lines = []
        current_indent = SPACE * (SPACES_PER_LEVEL * depth - LEFT_SHIFT)

        for key, value in node.items():
            value_type = value.get('type')
            in_value = value.get('value')
            old_value = value.get('old_value')
            new_value = value.get('new_value')
            children = value.get('children')

            match value_type:
                case 'nested':
                    lines.append(f"{current_indent}"
                                 f"  {key}: {inner(children, depth + 1)}")
                case 'unchanged':
                    lines.append(f"{current_indent}"
                                 f"  {key}: {normalize_val(in_value)}")
                case 'changed':
                    lines.append(f"{current_indent}"
                                 f"- {key}: {normalize_val(old_value, depth)}")
                    lines.append(f"{current_indent}"
                                 f"+ {key}: {normalize_val(new_value, depth)}")
                case 'added':
                    lines.append(f"{current_indent}"
                                 f"+ {key}: {normalize_val(in_value, depth)}")
                case 'deleted':
                    lines.append(f"{current_indent}"
                                 f"- {key}: {normalize_val(in_value, depth)}")
        current_indent = SPACE * (SPACES_PER_LEVEL * depth - SPACES_PER_LEVEL)
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return inner(tree, START_DEPTH)
