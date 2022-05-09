class Node:
    """
    Creates an instance of a node.
    Has value, left, and right properties.
    """

    def __init__(self, value):
        # just like linked list, each node has a value and a pointer to the next node. but, with binary trees, we need to keep track of the left and right nodes.
        self.value = value
        self.left = None
        self.right = None


# Breadth-first Traversal.
def breadth_first(root=None):
    """this function travers the tree in a breadth-first manner. for a binary tree, this means that we visit the left node first, then the right node, then the left node of the left node, then the right node of the left node, and so on."""
    try:
        queue = [root]
        node_list = []
        while queue:
            current_node = queue.pop(0)
            # print("herere", current_node.value)
            node_list.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return node_list

    except AttributeError:
        return "Wrong Entry please enter a root"


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(breadth_first(root))
