class KTreeNode:
    """
    Create a k-tree from a list of values. has value, children, and parent.
    """

    def __init__(self, value):
        # just like linked list, each node has a value and a pointer to the next node(childern).
        self.value = value
        self.children = []
        self.parent = None

    # function to add a child to the node
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    # gets level for print methods (just to add |-- to the beginning of each line)
    def get_lvl(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    # print the basic tree structure
    def prnt_tree(self):
        spaces = " " * self.get_lvl() * 2
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + str(self.value))
        if self.children:
            for child in self.children:
                child.prnt_tree()

    # this is an extra function that I added to the k-tree class.
    def prnt_fizz_buzz_tree(self):
        try:
            spaces = " " * self.get_lvl() * 4
            prefix = spaces + "|--" if self.parent else ""
            if self.value % 3 == 0 and self.value % 5 == 0:
                self.value = "FizzBuzz"
            elif self.value % 3 == 0:
                self.value = "Fizz"
            elif self.value % 5 == 0:
                self.value = "Buzz"
            print(prefix + str(self.value))
            if self.children:
                for child in self.children:
                    child.prnt_fizz_buzz_tree()

        except AttributeError:
            return "Wrong Entry please enter a root"


def build_tree():

    root = KTreeNode(1)
    sec_lvl_1 = KTreeNode(2)
    sec_lvl_2 = KTreeNode(3)
    sec_lvl_3 = KTreeNode(4)

    sec_lvl_1.add_child(KTreeNode(5))
    sec_lvl_1.add_child(KTreeNode(6))
    sec_lvl_1.add_child(KTreeNode(7))

    sec_lvl_2.add_child(KTreeNode(8))
    sec_lvl_2.add_child(KTreeNode(9))
    sec_lvl_2.add_child(KTreeNode(10))

    sec_lvl_3.add_child(KTreeNode(11))
    sec_lvl_3.add_child(KTreeNode(12))
    sec_lvl_3.add_child(KTreeNode(13))
    sec_lvl_3.add_child(KTreeNode(14))
    sec_lvl_3.add_child(KTreeNode(15))
    root.add_child(sec_lvl_1)
    root.add_child(sec_lvl_2)
    root.add_child(sec_lvl_3)

    return root


def fizz_buzz_tree(root):

    try:
        spaces = " " * root.get_lvl() * 4
        prefix = spaces + "|--" if root.parent else ""
        if root.value % 3 == 0 and root.value % 5 == 0:
            root.value = "FizzBuzz"
        elif root.value % 3 == 0:
            root.value = "Fizz"
        elif root.value % 5 == 0:
            root.value = "Buzz"
        else:
            root.value = str(root.value)
        print(prefix + str(root.value))
        if root.children:
            for child in root.children:
                fizz_buzz_tree(child)

    except AttributeError:
        return "Wrong Entry please enter a root"


if __name__ == "__main__":
    root = build_tree()
    root2 = build_tree()
    # root.add_child(KTreeNode(16))
    root.prnt_tree()

    root.prnt_fizz_buzz_tree()

    fizz_buzz_tree(root2)
