class Node:
    """
    creat Node for LL  (data and next node pointer)
    """

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def __repr__(self):
        return self.data


class LinkedList:
    """
    create LL using Nodes which has a head
    """

    def __init__(self):
        self.head = None  # or self.head=head and have head as None default value!!

    def __str__(self):
        return str(self.stringfy())

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.nextNode
        nodes.append("None")
        return " -> ".join(nodes)

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
        print('"' + str(llstr) + '"')

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

    def zipLists(self, list1, list2):
        """
        Helped from https://www.geeksforgeeks.org/merge-a-linked-list-into-another-linked-list-at-alternate-positions/

        This function takes Two differemt L.Lists as an argument and then zips them together ex, also takes in consideration the difference in lengths between the two linked lists :
        LL1:
        [1] -> [3] -> [2] -> null

        LL2:
        [5] -> [9] -> [4] -> null

        Output:
        [1] -> [5] -> [3] -> [9] -> [2] -> [4] -> null
        """
        leader = list1.head  # declare the heads
        follower = list2.head  # declare the heads

        # remeber when ever u see leader its List1 , and follower is List2

        # swap their positions until one finishes off
        while leader != None and follower != None:

            leader_next = leader.nextNode  # declare next Node pointers
            follower_next = follower.nextNode  # declare next Node pointers

            follower.nextNode = leader_next  # list2 go point at list1
            leader.nextNode = follower  #  list1 go point at list 2 next head !

            leader = leader_next  # now list1 jump to the next Node
            follower = follower.nextNode  # now list2 jump to the next Node
            list2.head = (
                follower_next  # follower # list2  make the the head the next node
            )
            # \\ Notice only list2 is actually added to list1 not the opposite so we can keep the space_comp (1)


if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append(1)
    ll1.append(2)
    ll1.append(3)
    # ll1.append(2)
    # ll1.append(3)
    # ll2.append(111)
    # ll2.append(222)
    ll2.append(333)
    ll2.append(222)
    ll2.append(111)
    # ll1.zipLists(ll1, ll2)
    ll1.stringfy()
    ll2.stringfy()
    ll1.zipLists(list1=ll1, list2=ll2)
    ll1.stringfy()
    str(ll1)

    # print(ll2.zipLists)
