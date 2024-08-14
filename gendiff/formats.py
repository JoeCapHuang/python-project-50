import itertools

SPACES_PER_LEVEL = 4
LEFT_SHIFT = 2
SPACE = ' '


def norm_value(value, depth=1):
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
    result = itertools.chain(["{"], lines, [indent + "}"])
    return '\n'.join(result)


def stylish(tree):
    def inner(node, depth):
        lines = []
        current_indent = SPACE * (SPACES_PER_LEVEL * depth - LEFT_SHIFT)

        for key, value in node.items():
            value_type = value.get('type')
            in_value = value.get('value')
            old_value = value.get('old_value')
            new_value = value.get('new_value')
            children = value.get('children')
            if value_type == 'nested':
                lines.append(f"{current_indent}"
                             f"  {key}: {inner(children, depth + 1)}")
            elif value_type == 'unchanged':
                lines.append(f"{current_indent}"
                             f"  {key}: {norm_value(in_value)}")
            elif value_type == 'changed':
                lines.append(f"{current_indent}"
                             f"- {key}: {norm_value(old_value, depth)}")
                lines.append(f"{current_indent}"
                             f"+ {key}: {norm_value(new_value, depth)}")
            elif value_type == 'added':
                lines.append(f"{current_indent}"
                             f"+ {key}: {norm_value(in_value, depth)}")
            elif value_type == 'deleted':
                lines.append(f"{current_indent}"
                             f"- {key}: {norm_value(in_value, depth)}")

        current_indent = SPACE * (SPACES_PER_LEVEL * depth - SPACES_PER_LEVEL)
        result = itertools.chain(["{"], lines, [current_indent + "}"])
        return '\n'.join(result)

    return inner(tree, 1)
