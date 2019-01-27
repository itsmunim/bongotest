def lca(node_a, node_b):
    """
    Finds least common ancestor for given two nodes
    Args:
        node_a (Node): First node
        node_b (Node): Second node
    Returns:
        Node: Least common ancestor of node_a and node_b
    Remarks:
        Runtime of the algorithm is O(n); whereas Space complexity is O(1)
    """

    depth_a = depth(node_a)
    depth_b = depth(node_b)

    traversal_node_a = node_a
    traversal_node_b = node_b

    while depth_a != depth_b:
        if depth_a > depth_b:
            traversal_node_a = node_a.parent
            depth_a -= 1
        else:
            traversal_node_b = node_b.parent
            depth_b -= 1

    while traversal_node_a.value != traversal_node_b.value:
        traversal_node_a = traversal_node_a.parent
        traversal_node_b = traversal_node_b.parent

    return traversal_node_a


def depth(node):
    """
    Finds the depth of a node from root; considering a root node is having parent = None
    Args:
        node (Node): The node for which we need to find depth.
    Returns:
        int: Depth of the node from root
    """
    __depth = 0

    current_node = node

    while current_node.parent:
        current_node = current_node.parent
        __depth += 1

    return __depth
