

START_PATH = ''


def normalize_val(value):
    if isinstance(value, dict):
        return '[complex value]'
    match value:
        case False | 'false':
            return 'false'

        case True | 'true':
            return 'true'

        case None:
            return 'null'

    if isinstance(value, str):
        return f"'{value}'"

    return value


def gen_plain(tree):
    def inner(node, current_path):
        lines = []

        for key, value in node.items():
            in_value = normalize_val(value.get('value'))
            old_value = normalize_val(value.get('old_value'))
            new_value = normalize_val(value.get('new_value'))
            new_path = f"{current_path}.{key}" if current_path else key
            action = ''

            match value.get('type'):
                case 'nested':
                    lines.extend(inner(value.get('children'), new_path))

                case 'added':
                    action = f'added with value: {in_value}'

                case 'deleted':
                    action = 'removed'

                case 'changed':
                    action = f'updated. From {old_value} to {new_value}'

            if action:
                lines.append(f"Property '{new_path}' was {action}")

        return lines

    return '\n'.join(inner(tree, START_PATH))
