# linked-list-insertions

> [Back to Home](../README.md)

## Question is

> Write the following methods for the Linked List class:

    append
    arguments: new value
    adds a new node with the given value to the end of the list

    insert before
    arguments: value, new value
    adds a new node with the given new value immediately before the first node that has the value specified

    insert after
    arguments: value, new value
    adds a new node with the given new value immediately after the first node that has the value specified

## **Whiteboard Process**

**will be added soon!!**

![image](./)

## Approach & Efficiency

-   Create 3 methods & Test files for them:

        def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return

        ______________________________________________________


        def insert_before(self, value, newValue):
        """
        insert a value(newValue) , before a specific (value)
        """
        iter = self.head
        # to check the Head First !!
        if iter == None:
            return "No Nodes '-_- to insert beofore"
        else:
            if iter.data == value:
                node = Node(newValue, self.head)
                self.head = node
                # print("i was here 1")
                return
        # Checker Status (boolean T/F)
        checker = None
        # Jump Between Nodes and check the value if it exists (since we checked the head first we start from nexNode)
        while iter.nextNode:
            if iter.nextNode.data == value:  # <-
                checker = True
                iter.nextNode = Node(newValue, iter.nextNode)
                # print("i was here 2")
                return
            else:
                iter = iter.nextNode
                # print("i was here 3")
        if checker != True:
            # print("i was here 4")
            return "Value doesn`t exist `-_-"

        ______________________________________________________


        def insert_after(self, value, newValue):
        """
        insert a value(newValue) , before a specific (value)
        """
        if not self.head:
            return
        iter = self.head
        # Jump between nodes and no need to check the head since we are adding values after we start from the Head!
        while iter:
            if iter.data == value:  # <-
                iter.nextNode = Node(newValue, iter.nextNode)
                return
            iter = iter.nextNode

-   also some test files for these Methods

> [Back to Home](../README.md)
