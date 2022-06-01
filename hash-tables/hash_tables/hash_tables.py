# class HashTable:
#     def __init__(self, length=1024):
#         self._length_of_hash_table = length
#         self._hash_table = [None] * self._length_of_hash_table
#         # or [None for i in range(self._length_of_hash_table)] or for collision handling [[] for i in range(self._length_of_hash_table)]

#     def add(self, key, value):
#         """
#         Takes key and value as arguements
#         Hashes the key; returns hash-index
#         Adds key/value pair to the HashTable at hash-index
#         Handles collisions
#         """
#         # hash the key and assign index
#         hashed_index = self._hash(key)
#         # check for collision
#         if not self._hash_table[hashed_index]:
#             # no collision
#             # create bucket at that index
#             self._hash_table[hashed_index] = Bucket()
#             # add the key/value to bucket at hashed_index

#         # when there is and is not a collision we will be adding to the bucket
#         node = Node(key, value)
#         self._hash_table[hashed_index].add(node)

#     def get(self, key):
#         """
#         Takes key as arguement
#         Hashes key; returns hash-index
#         Returns value from table at the hash-index
#         """
#         key_index = self._hash(key)
#         _includes_the_key = False
#         if self._hash_table[key_index]:
#             _includes_the_key = self._hash_table[key_index].includes(key)
#         if _includes_the_key:
#             return self._hash_table[key_index].return_value(key)

#     def contains(self, key):
#         """
#         Takes key as arguement
#         Returns boolean if key is already in HashTable
#         """
#         key_index = self._hash(key)
#         if self._hash_table[key_index]:
#             return self._hash_table[key_index].includes(key)
#         return self._hash_table[key_index]

#     def _hash(self, key):
#         """
#         Takes key as arguement
#         Returns hash-index
#         """
#         # add ascii values of char together
#         sum_chars = 0
#         for char in key:
#             sum_chars += ord(str(char))
#         # Square the sum
#         square_sum = sum_chars**2
#         # Floor devide by the first ascii value in key
#         divide_square = square_sum // ord(key[0])
#         # Mod length of hash table and return
#         return divide_square % self._length_of_hash_table


# class Bucket:
#     """Bucket used at filled index in HashTable"""

#     """Has Three methods: add, includes, and return_value"""

#     def __init__(self):
#         self.head = None

#     def add(self, node):
#         """Adds a node to the end of the linked list"""
#         _next_node = None
#         if not self.head:
#             self.head = node
#             return

#         if self.head.next:
#             _next_node = self.head.next
#         else:
#             self.head.next = node

#         while _next_node:
#             if not _next_node.next:
#                 _next_node.next = node
#                 break
#             _next_node = _next_node.next

#     def includes(self, key):
#         """Determines if a given key is in the linked list"""
#         _next_node = self.head
#         while _next_node:
#             if _next_node.key == key:
#                 return True
#             _next_node = _next_node.next
#         return False

#     def return_value(self, key):
#         """Returns the value in a node at a given node with matching key"""
#         _current_node = self.head
#         while _current_node:
#             if _current_node.key == key:
#                 return _current_node.value
#             _current_node = _current_node.next
#         return None


# class Node:
#     """Object that stores key / value pairs in Hash Table"""

#     def __init__(self, key, value):
#         self.next = None
#         self.key = key
#         self.value = value

#####################


class HashTable:
    def __init__(self, length=1024):
        self._length = length
        self._hash_table = [None] * self._length
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > self._length - 1:
            # self.idx = 0
            raise StopIteration
        else:
            self.idx += 1
            return self._hash_table[self.idx - 1]

    def add(self, key, value=None):
        hsh = self._hash(key)

        if not self._hash_table[hsh]:
            self._hash_table[hsh] = []

        self._hash_table[hsh].append([key, value])

    def get(self, key):
        """Takes key as arguement; returns value from table at the hashed-key-index"""
        hashed_key = self._hash(key)
        key_index = self._hash_table[hashed_key]

        if key_index:
            for i in range(len(key_index)):
                if key == key_index[i][0]:
                    return key_index[i][1]
        return None

    def contains(self, key):
        """Takes key as arguement; Returns boolean if key is already in HashTable"""
        hashed_key = self._hash(key)
        key_index = self._hash_table[hashed_key]

        if key_index:
            if key == key_index[0][0]:
                return True
        return False

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
        return divide_square % self._length

    def get_length(self):
        return self._length
