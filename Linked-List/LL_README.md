# Singly Linked List

A Linked List is a sequence of `Nodes` that are connected/linked to each other. The most defining feature of a Linked List is that each `Node` references the next `Node` in the link.

## Challenge

### Functionallity

-   Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

-   Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

    -   Define a method called `insert` which takes any value as an argument and adds a new node with that value to the `head` of the list with an O(1) Time performance.

    -   Define a method called `includes` which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.

    -   Define a method called `toString` (or `__str__` in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
        -   `"{ a } -> { b } -> { c } -> NULL"`

-   Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

-   Be sure to follow your language/frameworks standard naming conventions (e.g. C# uses PascalCasing for all method and class names).

### Testing

Write tests to prove the following functionality:

1. Can successfully instantiate an empty linked list
2. Can properly insert into the linked list
3. The head property will properly point to the first node in the linked list
4. Can properly insert multiple nodes into the linked list
5. Will return true when finding a value within the linked list that exists
6. Will return false when searching for a value in the linked list that does not exist
7. Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API

-   strigfy
-   get_len
-   insert
-   insert_at_the_beg
-   insert_at_the_end
-   includes
-   Tests for all of the above

<!-- Description of each method publicly available to your Linked List -->
