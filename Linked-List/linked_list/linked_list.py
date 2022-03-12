

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

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        return self.stringfy()

    def stringfy(self):
        if self.head is None:
            print("Linked list is empty")
            return
        iter = self.head
        # llstr : link list stringfy
        llstr = ""
        while iter:
            llstr += "{"+str(iter.data)+"}" + \
                '-->' if iter.nextNode else "{" + \
                str(iter.data)+"}" + '-->Null'
            iter = iter.nextNode
        print('"' + llstr + '"')

    def get_len(self):
        count = 0
        iter = self.head
        while iter:
            count += 1
            iter = iter.nextNode
        return count

    def insert(self, value):
        stringifiedValue = str(value)
        node = Node(stringifiedValue)

        if self.head is not None:
            node.nextNode = self.head
        self.head = node

    def insert_at_the_beg(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_at_the_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return

        iter = self.head

        while iter.nextNode:
            iter = iter.nextNode

        iter.nextNode = Node(value, None)

    def includes(self, value):
        headVal = self.head
        if headVal == None:
            return False
        while headVal != None:
            if headVal.data != value and headVal.nextNode == None:
                return False
            elif value == headVal.data:
                return True
            elif value != headVal.data:
                headVal = headVal.nextNode


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_the_beg(1)
    ll.insert_at_the_beg(33)
    ll.insert_at_the_beg("A")
    ll.insert_at_the_end(3333)
    ll.insert_at_the_end("b")
    print(ll.get_len())
    ll.stringfy()
