"""References:
https://www.youtube.com/watch?v=6oL-0TdVy28

https://www.youtube.com/watch?v=4r_XR9fUPhQ
"""


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


class BinaryTree:
    """
    Creates an instance of a Binary tree.
    Has a root property.
    Has three methods: pre_order, in_order, and post_order.
    """

    def __init__(self):
        self.root = None

    def pre_order(self, root=None, arr=None):
        """
        Returns an array of the values, ordered from the start(root!), going far left, then finishing to the right.
        """

        # start with the try/except block, and append the root.value to the arr.

        try:
            if arr == None:  # if arr is None, then create a new array.
                arr = []

            arr.append(root.value)

            if (
                root.left
            ):  # if the root.left is not None, then we want to call the pre_order method on the root.left.
                self.pre_order(root.left, arr)

            if (
                root.right
            ):  # if the root.right is not None, then we want to call the pre_order method on the root.right.
                self.pre_order(root.right, arr)

            return arr
        except AttributeError:
            return "A root element parameter is required. Please invoke the pre_order method with a root node as an arguement."

    def post_order(self, root=None, arr=[]):

        """
        Returns an array of the values, ordered starting from the far left, traversing to the top, then finishing to the right.
        """

        try:
            if arr == None:
                arr = []

            if root.left:
                self.post_order(root.left, arr)

            if root.right:
                self.post_order(root.right, arr)

            arr.append(root.value)

            return arr
        except AttributeError:
            return "A root element parameter is required. Please invoke the post_order method with a root node as an arguement."

    def in_order(self, root=None, arr=[]):
        """
        Returns an array of the values, ordered starting from the far left, traversing to the far right, then finishing to at the root.
        """
        try:
            if arr == None:
                arr = []

            if root.left:
                self.in_order(root.left, arr)

            arr.append(root.value)

            if root.right:
                self.in_order(root.right, arr)

            return arr
        ## raise AttributeError
        except AttributeError:
            return "A root element parameter is required. Please invoke the in_order method with a root node as an arguement."

    def get_max_BT(self):
        """
        Returns the max value in the tree.
        """
        try:
            if self.root:
                return self.in_order(self.root)[-1]
            else:
                return "A root element parameter is required. Please invoke the get_max_BT method with a root node as an arguement."
        except AttributeError:
            return "A root element parameter is required. Please invoke the get_max_BT method with a root node as an arguement."

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.in_order_traversal()

        return elements


class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Method that accepts one value.
        Adds a node to the binary search tree
        Conditionals that check if the node's value is greater than or less than the "top" node
        Greater values go to the right. Lesser values go to the left.
        Continues until leaf is hit
        """
        try:
            node = Node(value)
            if not self.root:
                self.root = node
            else:
                top = self.root
                while True:
                    if value < top.value and top.left:
                        top = top.left
                    elif value < top.value:
                        top.left = node
                        return
                    elif value > top.value and top.right:
                        top = top.right
                    else:
                        top.right = node
                        return
        except ValueError:
            return "Please enter a valid integer for the BinarySearchTree."

    def contains(self, value):
        """
        Method that accepts one value.
        Traverses the tree untill it reaches a node with the value that was sent in as an arguement
        Returns True or False if the value is in the tree at least once
        """
        if self.root.value != None:
            current = self.root
            # if current.value == value:
            #     return True
            # else:
            while current:
                if current.value == value:
                    return True
                elif value < current.value:
                    if current.left:
                        current = current.left
                        if current.value == value:
                            return True
                    else:
                        return False
                elif value > current.value:
                    if current.right:
                        current = current.right
                        if current.value == value:
                            return True
                    else:
                        return False
        else:
            return False

    ## traverse the max of tree
    def get_max_BST(self):
        """
        Method that returns the max value in the tree
        """
        if self.root.value != None:
            current = self.root
            while current.right:
                current = current.right
            return current.value
        else:
            return "Please enter a valid integer for the BinarySearchTree."

    def in_order_traversal(self):

        elements = []
        current = self.root
        if current.left:
            self = current.left
            elements += self.in_order_traversal()

        elements.append(current.data)

        if current.right:
            self = current.right
            elements += self.in_order_traversal()

        return elements


if __name__ == "__main__":
    new_tree = BinarySearchTree()
    # new_tree1 = BinarySearchTree(0)
    # new_tree.root = Node(10)
    # new_tree.add(10)
    # print(new_tree.root.value)
    # new_tree.pre_order(new_tree.root)
    new_tree.add(5)
    new_tree.add(20)
    new_tree.add(3)
    new_tree.add(100)
    new_tree.add(1)
    new_tree.add(15)
    new_tree.add(13)
    new_tree.add(2)
    new_tree.add(90)
    print("im the max of BST ! ", new_tree.get_max_BST())
    print("im the max of BT ! ", new_tree.get_max_BT())
    print(new_tree.contains(90))
    print(new_tree.contains(13))
    print(new_tree.pre_order(new_tree.root))
    print(new_tree.post_order(new_tree.root))
    print(new_tree.in_order(new_tree.root))

    # print(new_tree.in_order_traversal())
