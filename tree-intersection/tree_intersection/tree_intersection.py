def tree_intersection(tree_1, tree_2):

    lst = []
    ht = HashTable()

    # def inorder(tree):
    #     if tree is None:
    #         return
    #     inorder(tree.left)
    #     ht.set(tree.value)
    #     inorder(tree.right)

    def recurse_traverse(node, second_tree):

        if not node:
            return

        recurse_traverse(node.left, second_tree)
        recurse_traverse(node.right, second_tree)

        # if node.value in second_tree.values:
        #     if not ht.contains(node.value):
        #         lst.append(node.value)
        #         ht.add(node.value)
        if second_tree:

            # if node.value is in the hash table append it to the list
            if ht.contains(node.value):
                lst.append(node.value)

        else:

            ht.add(node.value)  # add to hash table

    recurse_traverse(tree_1.root, False)
    recurse_traverse(tree_2.root, True)

    return lst


################################################


class HashTable:
    def __init__(self, length=1024):
        self._length_of_hash_table = length
        self._hash_table = [None] * self._length_of_hash_table

    def add(self, key, value=None):
        """
        Takes key and value as arguements
        Hashes the key; returns hash-index
        Adds key/value pair to the HashTable at hash-index
        Handles collisions
        """
        # hash the key and assign index
        hashed_index = self._hash(key)
        # check for collision
        if not self._hash_table[hashed_index]:
            # no collision
            # create bucket at that index
            self._hash_table[hashed_index] = Bucket()
            # add the key/value to bucket at hashed_index

        # when there is and is not a collision we will be adding to the bucket
        node = Node(key, value)
        self._hash_table[hashed_index].add(node)

    def get(self, key):
        """
        Takes key as arguement
        Hashes key; returns hash-index
        Returns value from table at the hash-index
        """
        key_index = self._hash(key)
        _includes_the_key = False
        if self._hash_table[key_index]:
            _includes_the_key = self._hash_table[key_index].includes(key)
        if _includes_the_key:
            return self._hash_table[key_index].return_value(key)

    def contains(self, key):
        """
        Takes key as arguement
        Returns boolean if key is already in HashTable
        """
        key_index = self._hash(key)
        if self._hash_table[key_index]:
            return self._hash_table[key_index].includes(key)
        return self._hash_table[key_index]

    def _hash(self, key):
        """
        Takes key as arguement
        Returns hash-index
        """
        # add ascii values of char together
        sum_chars = 0
        key = str(key)
        for char in key:
            sum_chars += ord(str(char))
        # Square the sum
        square_sum = sum_chars**2
        # Floor devide by the first ascii value in key
        divide_square = square_sum // ord(key[0])
        # Mod length of hash table and return
        return divide_square % self._length_of_hash_table


class Node:
    """Object that stores key / value pairs in Hash Table"""

    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value


class _Node:
    """
    Creates an instance of a node.
    Has value, left, and right properties.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class BinaryTree:
    """
    Creates an instance of a Binary tree.
    Has a root property.
    Has three methods: pre_order, in_order, and post_order.
    """

    def __init__(self):
        self.root = None

    def add(self, value):
        node = _Node(value)

        if not self.root:
            self.root = node
            return

        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            current = q.dequeue()

            if not current.left:
                current.left = node
                return
            if not current.right:
                current.right = node
                return

            q.enqueue(current.left)
            q.enqueue(current.right)

    def pre_order(self, root=None, arr=None):
        """
        Method that takes no parameters.
        Returns an array of the values, ordered from the start, going far left, then finishing to the right.
        """
        try:
            if arr == None:
                arr = []

            arr.append(root.value)

            if root.left:
                self.pre_order(root.left, arr)

            if root.right:
                self.pre_order(root.right, arr)

            return arr
        except AttributeError:
            return "A root element parameter is required. Please invoke the pre_order method with a root node as an arguement."

    def post_order(self, root=None, arr=[]):
        """
        Method that takes no parameters.
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
        Method that takes no parameters.
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
        except AttributeError:
            return "A root element parameter is required. Please invoke the in_order method with a root node as an arguement."


class Queue:
    """
    An instance of a Queue
    Has a front property that points to the front of the queue
    enqueue method takes a value and adds a node to the end of the queue (O(1))
    dequeue method removes the front node of the queue, returns its value
    peek method returns the value of the front node in the queue
    is_empty method returns True or False if the queue is empty
    """

    def __init__(self, front=None):
        self.front = front
        self.end = None

    def enqueue(self, node):
        if not self.front:
            self.front = node
        elif not self.end:
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def dequeue(self):
        try:
            first_node = self.front
            self.front = first_node.next
            first_node.next = None
            return first_node
        except AttributeError:
            return None

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return None

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False


class Bucket:
    """Bucket used at filled index in HashTable"""

    """Has Three methods: add, includes, and return_value"""

    def __init__(self):
        self.head = None

    def add(self, node):
        """Adds a node to the end of the linked list"""
        _next_node = None
        if not self.head:
            self.head = node
            return

        if self.head.next:
            _next_node = self.head.next
        else:
            self.head.next = node

        while _next_node:
            if not _next_node.next:
                _next_node.next = node
                break
            _next_node = _next_node.next

    def includes(self, key):
        """Determines if a given key is in the linked list"""
        _next_node = self.head
        while _next_node:
            if _next_node.key == key:
                return True
            _next_node = _next_node.next
        return False

    def return_value(self, key):
        """Returns the value in a node at a given node with matching key"""
        _current_node = self.head
        while _current_node:
            if _current_node.key == key:
                return _current_node.value
            _current_node = _current_node.next
        return None
