import itertools

SPACES_PER_LEVEL = 4
LEFT_SHIFT = 2
SPACE = ' '


def normalize_value(value, depth=1):
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
            value_type = value['type']
            if value_type == 'nested':
                lines.append(f"{current_indent}  {key}: {inner(value['children'], depth + 1)}")
            elif value_type == 'unchanged':
                lines.append(f"{current_indent}  {key}: {normalize_value(value['value'])}")
            elif value_type == 'changed':
                lines.append(f"{current_indent}- {key}: {normalize_value(value['old_value'], depth)}")
                lines.append(f"{current_indent}+ {key}: {normalize_value(value['new_value'], depth)}")
            elif value_type == 'added':
                lines.append(f"{current_indent}+ {key}: {normalize_value(value['value'], depth)}")
            elif value_type == 'deleted':
                lines.append(f"{current_indent}- {key}: {normalize_value(value['value'], depth)}")

        current_indent = SPACE * (SPACES_PER_LEVEL * depth - SPACES_PER_LEVEL)
        result = itertools.chain(["{"], lines, [current_indent + "}"])
        return '\n'.join(result)

    return inner(tree, 1)

kek = {
    'common': {
        'type': 'nested',
        'children': {
            'follow': {'type': 'added', 'value': False},
            'setting1': {'type': 'unchanged', 'value': 'Value 1'},
            'setting2': {'type': 'deleted', 'value': 200},
            'setting3': {'type': 'changed', 'old_value': True, 'new_value': None},
            'setting4': {'type': 'added', 'value': 'blah blah'},
            'setting5': {'type': 'added', 'value': {'key5': 'value5'}},
            'setting6': {
                'type': 'nested',
                'children': {
                    'doge': {
                        'type': 'nested',
                        'children': {
                            'wow': {'type': 'changed', 'old_value': '', 'new_value': 'so much'}
                        }
                    },
                    'key': {'type': 'unchanged', 'value': 'value'},
                    'ops': {'type': 'added', 'value': 'vops'}
                }
            }
        }
    },
    'group1': {
        'type': 'nested',
        'children': {
            'baz': {'type': 'changed', 'old_value': 'bas', 'new_value': 'bars'},
            'foo': {'type': 'unchanged', 'value': 'bar'},
            'nest': {'type': 'changed', 'old_value': {'key': 'value'}, 'new_value': 'str'}
        }
    },
    'group2': {'type': 'deleted', 'value': {'abc': 12345, 'deep': {'id': 45}}},
    'group3': {'type': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
}

print(stylish(kek))