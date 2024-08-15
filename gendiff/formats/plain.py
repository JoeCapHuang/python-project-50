

START_PATH = ''


def normalize_val(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    match value:
        case False:
            return 'false'
        case True:
            return 'true'
        case None:
            return 'null'
    return value


def gen_line(path, value_type, value):
    action = ''
    value = normalize_val(value)
    match value_type:
        case 'added':
            action = f'added with value: {value}'
        case 'deleted':
            action = 'removed'
        case 'changed':
            old_value, new_value = value
            action = (f'updated. From '
                      f'{normalize_val(old_value)}'
                      f' to {normalize_val(new_value)}')
    if action:
        return f"Property '{path}' was {action}"


def gen_plain(tree):
    def inner(node, current_path):
        lines = []

        for key, value in node.items():
            value_type = value.get('type')
            in_value = value.get('value')
            old_value = value.get('old_value')
            new_value = value.get('new_value')
            children = value.get('children')
            new_path = f"{current_path}.{key}" if current_path else key

            match value_type:
                case 'nested':
                    lines.extend(inner(children, new_path))
                case 'added' | 'deleted' | 'changed':
                    lines.append(
                        gen_line(new_path, value_type,
                                 in_value if value_type != 'changed'
                                 else (old_value, new_value)))
        return lines

    return '\n'.join(inner(tree, START_PATH))
