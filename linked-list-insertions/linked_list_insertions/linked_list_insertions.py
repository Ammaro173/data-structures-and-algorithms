class Node:
    """
    creat Node for LL  (data and next node pointer)
    """

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode


class LinkedList:
    """
    create LL using Nodes which has a head
    """

    def __init__(self):
        self.head = None  # or self.head=head and have head as None default value!!

    def __str__(self):
        return self.stringfy()

    def stringfy(self):
        """
        stringfy the Node into a represntable way + for Testing purposes
        """
        if self.head is None:
            print("Linked list is empty")
            return
        iter = self.head

        # print("me", iter.__dict__)
        # llstr : link list stringfy
        llstr = ""
        while iter:
            llstr += (
                "{" + str(iter.data) + "}" + "-->"
                if iter.nextNode
                else "{" + str(iter.data) + "}" + "-->Null"
            )
            iter = iter.nextNode
        print('"' + llstr + '"')

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return

        iter = self.head
        # print("menene", iter.__dict__)
        while iter.nextNode:
            iter = iter.nextNode
            # print("meei", iter.nextNode)

        iter.nextNode = Node(value, None)

    # def insert_at_the_beg(self, value):
    #     node = Node(value, self.head)
    #     self.head = node

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

    def insert_after(self, value, newValue):
        """
        insert a value(newValue) , after a specific (value)
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


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(0)
    ll.append(88)
    ll.insert_before(1, "A")
    ll.insert_after(88, "B")
    ll.stringfy()
