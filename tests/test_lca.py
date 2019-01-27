from bongotest.datastructure import Node, create_bst, get_node
from bongotest.lca import lca

bst = create_bst()


def test_same_node_lca():
    node_1 = bst[2]
    node_2 = bst[2]
    assert lca(node_1, node_2).value == node_1.value == node_2.value


def test_parent_child_lca():
    child = bst[3]
    assert lca(child.parent, child).value == child.parent.value


def test_different_nodes_lca():
    cases = [
        (6, 7, 3),
        (4, 3, 1),
        (8, 6, 1),
        (9, 5, 2)
    ]

    for case in cases:
        node_a = get_node(case[0], bst)
        node_b = get_node(case[1], bst)
        assert lca(node_a, node_b).value == case[2]
