class Node(object):
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent


def create_bst(node_value=1, max_depth=4):
    """
    Generates a binary search tree similar to given example in problem definition
    Args:
        node_value (int): Root node value
        max_depth (int): How deep it should generate from the root
    Returns:
        list: List of nodes in the bst, sorted by their value
    """
    root = Node(node_value)
    bst = [root]

    max_depth -= 1

    if max_depth > 0:
        left_nodes = create_bst(root.value * 2, max_depth)
        right_nodes = create_bst(root.value * 2 + 1, max_depth)
        left_nodes[0].parent = root
        right_nodes[0].parent = root
        bst += left_nodes + right_nodes

    return sorted(bst, key=lambda node: node.value)


def get_node(value, bst):
    """
    Returns node with the given value
    Args:
        value (int): For which value to search for
        bst (list): Nodes present in the bst as list
    Returns:
        Node: The node with that value, None if not found
    """
    subset = filter(lambda n: n.value == value, bst)
    return subset[0] if subset else None
