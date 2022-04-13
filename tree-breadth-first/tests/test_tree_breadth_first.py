from tree_breadth_first.tree_breadth_first import Node, breadth_first


# Testing for a simple Breadth-first Traversal expected [1, 2, 3, 4, 5] .
def test_Breadth_first():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    assert breadth_first(root) == [1, 2, 3, 4, 5]


# Test for Breafth function error handling. Expected a message.
def test_Breadth_first_Error_Handling():
    assert breadth_first() == "Wrong Entry please enter a root"


# Testing for a the given visual of Breadth-first Traversal expected [2, 7, 5, 2, 6, 9, 5, 11, 4]
def test_Breadth_first_v2():

    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.right.right = Node(9)
    root.right.right.left = Node(4)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(11)

    assert breadth_first(root) == [2, 7, 5, 2, 6, 9, 5, 11, 4]
