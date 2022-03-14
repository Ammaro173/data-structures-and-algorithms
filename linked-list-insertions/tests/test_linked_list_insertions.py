from linked_list_insertions.linked_list_insertions import LinkedList, Node


# insert Node @ end Test
def test_insert_new_node_added_to_end():
    insertList = LinkedList()
    insertList.append("string")
    expected = "string"
    actual = insertList.head.data
    assert expected == actual


# Multi_Value_@ the end (append)   Test
def test_multi_value_insert_at_end():
    multiInputList = LinkedList()
    multiInputList.append("WON")
    multiInputList.append("TOO")
    multiInputList.append("THR33")

    actual = [
        multiInputList.head.data,
        multiInputList.head.nextNode.data,
        multiInputList.head.nextNode.nextNode.data,
    ]
    expected = ["WON", "TOO", "THR33"]
    assert actual == expected


# insert a node before a node located i the middle of a linked list
def test_insert_value_before_node_in_the_middle():
    multiInputList = LinkedList()
    multiInputList.append("WON")
    multiInputList.append("TOO")
    multiInputList.append("THR33")
    multiInputList.insert_before("TOO", "HI")
    actual = [
        multiInputList.head.data,
        multiInputList.head.nextNode.data,
        multiInputList.head.nextNode.nextNode.data,
        multiInputList.head.nextNode.nextNode.nextNode.data,
    ]
    expected = ["WON", "HI", "TOO", "THR33"]
    assert actual == expected


# insert a node before the first node of a linked list
def test_insert_value_before_first_node():
    multiInputList = LinkedList()
    multiInputList.append("WON")
    multiInputList.append("TOO")
    multiInputList.append("THR33")
    multiInputList.insert_before("WON", "HI")
    actual = [
        multiInputList.head.data,
        multiInputList.head.nextNode.data,
        multiInputList.head.nextNode.nextNode.data,
        multiInputList.head.nextNode.nextNode.nextNode.data,
    ]
    expected = ["HI", "WON", "TOO", "THR33"]
    assert actual == expected


# insert after a node in the middle of the linked list
def test_insert_value_after_node_in_the_middle():
    multiInputList = LinkedList()
    multiInputList.append("WON")
    multiInputList.append("TOO")
    multiInputList.append("THR33")
    multiInputList.insert_after("TOO", "HI")
    actual = [
        multiInputList.head.data,
        multiInputList.head.nextNode.data,
        multiInputList.head.nextNode.nextNode.data,
        multiInputList.head.nextNode.nextNode.nextNode.data,
    ]
    expected = ["WON", "TOO", "HI", "THR33"]
    assert actual == expected


#  insert a node after the last node of the linked list
def test_insert_value_adter_last_node():
    multiInputList = LinkedList()
    multiInputList.append("WON")
    multiInputList.append("TOO")
    multiInputList.append("THR33")
    multiInputList.insert_after("THR33", "HI")
    actual = [
        multiInputList.head.data,
        multiInputList.head.nextNode.data,
        multiInputList.head.nextNode.nextNode.data,
        multiInputList.head.nextNode.nextNode.nextNode.data,
    ]
    expected = ["WON", "TOO", "THR33", "HI"]
    assert actual == expected
