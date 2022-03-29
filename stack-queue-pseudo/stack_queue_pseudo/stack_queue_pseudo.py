from .stacks_and_queues import InvalidOperationError, Node, Stack


class Pseudo_queue:
    """
    Implemetation of a queue using two stacks."""

    def __init__(self):
        self.go_in = Stack()  # push #2 stack
        self.go_out_from = Stack()  # pop stack
        self.size = 0

    def enqueue(self, value):

        self.go_out_from.push(value)

        # self.go_in.push(self.go_out_from.pop())
        self.size += 1

    def dequeue(self):

        """Fifo"""
        y = self.size
        # while self.size > 0:
        #     self.go_in.pop()
        #     self.size -= 1
        # while y > 0:
        #     self.go_in.pop()
        #     y -= 1

        # while y > 0:

        #     if not self.go_out_from.is_empty():
        #         self.go_in.push(self.go_out_from.top.value)

        #         # self.go_out_from.push(self.go_out_from.pop())
        #         # self.go_out_from.top = self.go_out_from.top.next

        #         print("ive benn here")

        #     else:

        #         print("i was here")
        #         pass

        #     y -= 1

        # else:
        #     print("i was here")

        if self.go_in.is_empty():
            while not self.go_out_from.is_empty():
                self.go_in.push(self.go_out_from.pop())
        # else:
        #     print("list is empty")

        return self.go_in.pop()

    ####### Failed Trials #######
    # if self.go_in.is_empty():
    #     raise InvalidOperationError("Method not allowed on empty collection")

    # else:

    #     self.size -= 1
    #     return self.go_in.pop()
    # if not self.go_in.is_empty():
    #     while not self.go_out_from.is_empty():
    #         self.go_in.push(self.go_out_from.pop())

    # if not self.go_out_from.is_empty():
    #     return self.go_out_from.pop()
    # else:
    #     return "wtf"
    # if not self.go_out_from.is_empty():
    #     while not self.go_in.is_empty():
    #         self.go_in.push(self.go_out_from.pop())
    # if not self.go_out_from.is_empty():
    #     return self.go_out_from.pop()
    # else:
    #     return self.go_out_from.top

    def is_empty(self):
        if self.go_out_from.is_empty() and self.go_in.is_empty():
            return True

        return False

    def sizes(self):
        """returns the size of the queue"""
        print("the size is: ", self.size)

    # def printme_stack1(self):
    #     while not self.go_in.is_empty():
    #         print(self.go_in.top.value)
    #         self.go_in.top = self.go_in.top.next

    # print(self.go_in.top.value)
    # print(self.go_out_from.top)

    # def __str__(self):
    #     node = self.go_in.top

    #     nodes = []
    #     while node is not None:
    #         nodes.append(node.value)
    #         node = node.next
    #     nodes.append("None")
    #     return " -> ".join(str(nodes))


if __name__ == "__main__":
    ins = Pseudo_queue()
    ins.enqueue("A")

    ins.enqueue("B")

    ins.enqueue("C")
    # print("->>>>", ins.printme_stack1())

    # # ins.dequeue()
    # ins.sizes()
    print("i should be 'a'", ins.dequeue())
    ins.enqueue("D")
    ins.enqueue("E")

    print("i shoudl be 'b'", ins.dequeue())
    print("i shoudl be 'c'", ins.dequeue())
    print("i shoudl be 'd'", ins.dequeue())
    print("i shoudl be 'e'", ins.dequeue())
    # print("i shoudl be 'e'", ins.dequeue())

    # print("i shoudl be 'c'", ins.dequeue())
    # print("i shoudl be 'c'", ins.dequeue())
    # print(ins.dequeue())
    # print(ins.dequeue())
    # print(ins.dequeue())
