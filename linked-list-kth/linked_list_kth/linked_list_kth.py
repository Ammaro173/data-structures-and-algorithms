import copy


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

    def find_kth_value_from_end(self, kth):
        # count = 0
        # leader = self.head
        # follower = self.head

        # if kth < 0:
        #     raise ValueError("You cannot enter a negative integer")
        # while count <= kth and leader:
        #     leader = leader.nextNode
        #     count += 1
        #     print("count1 :", count)
        # while leader:
        #     leader = leader.nextNode
        #     follower = follower.nextNode
        #     count += 1
        #     print("count2 :", count)
        # if kth > count:
        #     raise IndexError("The list is not that big")
        # return follower.data
        length_LL = 0
        counter = copy.copy(self.head)
        while counter:
            length_LL += 1
            counter = counter.nextNode
        if kth > length_LL or kth == 0:
            raise IndexError("The list is not that big")
        else:
            counter = self.head
            for _ in range(length_LL - kth - 1):
                counter = counter.nextNode
            return counter.data

    def reverse_LL(self, node=None):
        """
        Reverse the LL
        """
        prev = None
        current = self.head
        while current:
            next = current.nextNode
            current.nextNode = prev
            prev = current
            current = next
        self.head = prev
        return self


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(0)
    print("-->", ll.find_kth_value_from_end(1))
    ll.stringfy()
    ll.reverse_LL().stringfy()
    pass
