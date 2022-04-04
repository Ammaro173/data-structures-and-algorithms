class InvalidOperationError(Exception):
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
        node = Node(value)
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


def validate_brackets(string: str):
    """
    This function will validate the brackets in the string.

    idea : https://www.youtube.com/watch?v=QZOLb0xHB_Q

    """

    stack = Stack()

    # brackets = input("Enter the brackets: ")

    for bracket in string:
        if bracket == "(" or bracket == "[" or bracket == "{":
            stack.push(bracket)
        elif bracket == ")" or bracket == "]" or bracket == "}":
            if stack.is_empty():
                return False
            else:
                if bracket == ")" and stack.peek() == "(":
                    stack.pop()
                elif bracket == "]" and stack.peek() == "[":
                    stack.pop()
                elif bracket == "}" and stack.peek() == "{":
                    stack.pop()
                else:
                    return False

    if stack.is_empty():
        return True
    else:
        return False


def main():

    """
    This is the main function which will be called when the program is run. and the main function will call the validate_brackets function. which will validate the brackets in the string and return True or False. when the user enters the brackets in the string.
    """

    brackets = input("Enter the brackets: ")
    if validate_brackets(brackets):
        print("The brackets are valid")
    else:
        print("The brackets are invalid")


if __name__ == "__main__":

    print(validate_brackets("{}"))
    print(validate_brackets("{}(){}"))
    print(validate_brackets("()[[Extra Characters]]"))
    print(validate_brackets("[({}]"))
    print(validate_brackets("(]("))
    print(validate_brackets("{(})"))
    print(validate_brackets("((()))"))
