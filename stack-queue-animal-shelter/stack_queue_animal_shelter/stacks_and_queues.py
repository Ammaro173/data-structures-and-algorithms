class InvalidOperationError(BaseException):
    pass


class Node:
    def __init__(self, value, next=None):
        """
        The Famous Node Calss which contatins a value and pointer for the next Value
        """
        self.value = value
        self.next = next


class Stack:

    """Stack class that has a top property. It creates an empty Stack when instantiated"""

    def __init__(self, node=None):
        self.top = node
        self.size = 0

    def push(self, value):
        """
        Nodes or items that are put into the stack are pushed
        """
        node = Node(value)  ##
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        """
        Nodes or items that are removed from the stack are popped. When you attempt to pop an empty stack an exception will be raised."""
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.value

    def peek(self):
        """
        When you peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised."""
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        """
        returns true when stack is empty otherwise returns false."""
        # or-> return self.top == None   directly !!!
        if self.top is None:
            return True
        else:
            return False

    def size(self):
        """returns the size of the stack"""
        return self.size


class Queue:

    """
    Queue class that has a front property. It creates an empty Queue when instantiated
    """

    def __init__(self, node=None):
        self.front = node
        self.rear = node

    def enqueue(self, rear):
        """
        Nodes or items that are added to the queue.
        """
        node = Node(rear)  ##
        if self.is_empty():
            self.front = node
            self.rear = node
            return node
        self.rear.next = node
        return node

    def dequeue(self):
        """
        Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised."""
        remove = self.front
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        self.front = self.front.next
        remove.next = None
        self.rear = None
        return remove.value

    def peek(self):
        """
        When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised."""
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        """returns true when queue is empty otherwise returns false."""
        if self.front is None and self.rear is None:
            return True
        else:
            return False
