

def build_diff_tree(node1, node2):
    diff_tree = {}
    keys = sorted(set(node1.keys()) | set(node2.keys()))
    for key in keys:
        if key not in node2:
            diff_tree[key] = {
                'type': 'deleted',
                'value': node1[key],
            }
        elif key not in node1:
            diff_tree[key] = {
                'type': 'added',
                'value': node2[key],
            }
        elif isinstance(node1[key], dict) and isinstance(node2[key], dict):
            diff_tree[key] = {
                'type': 'nested',
                'children': build_diff_tree(node1[key], node2[key]),
            }
        elif node1[key] == node2[key]:
            diff_tree[key] = {
                'type': 'unchanged',
                'value': node1[key],
            }
        else:
            diff_tree[key] = {
                'type': 'changed',
                'old_value': node1[key],
                'new_value': node2[key],
            }
    return diff_tree
