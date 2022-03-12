from linked_list.linked_list import LinkedList, Node


# import test
def test_import():
    assert LinkedList


# Empty list Handle test
def test_creates_empty_list():
    emptyList = LinkedList()
    actual = emptyList.head
    expected = None
    assert expected == actual


# insert Node Test
def test_insert_new_node_added_to_head():
    insertList = LinkedList()
    insertList.insert("string")
    expected = "string"
    actual = insertList.head.data
    assert expected == actual


# Point @ Head Test
def test_create_head_and_point_to_first_value():
    pointToHeadList = LinkedList()
    pointToHeadList.insert("TOO")
    pointToHeadList.insert("WON")
    expected = "WON"
    actual = pointToHeadList.head.data
    assert actual == expected


# Multi_Value Test
def test_multi_value_insert():
    multiInputList = LinkedList()
    multiInputList.insert("THR33")
    multiInputList.insert("TOO")
    multiInputList.insert("WON")
    actual = [multiInputList.head.data, multiInputList.head.nextNode.data,
              multiInputList.head.nextNode.nextNode.data]
    expected = ["WON", "TOO", "THR33"]
    assert actual == expected


# Include True LL test
def test_true_boolean_return_for_existing_in_list():
    trueList = LinkedList()
    trueList.insert("WON")
    trueList.insert("TOO")
    trueList.insert("THR33")
    actual = trueList.includes("WON")
    expected = True
    assert actual == expected


# Include False LL test
def test_false_boolean_return_for_existing_in_list():
    falseList = LinkedList()
    falseList.insert("WON")
    falseList.insert("TOO")
    falseList.insert("THR33")
    actual = falseList.includes("FOR")
    expected = False
    assert actual == expected


def test_complete_list_return_as_string():
    returnedList = LinkedList()
    returnedList.insert("THR33")
    returnedList.insert("TOO")
    returnedList.insert("WON")
    actual = [returnedList.head.data, returnedList.head.nextNode.data,
              returnedList.head.nextNode.nextNode.data]
    expected = ["WON", "TOO", "THR33"]
    assert actual == expected


# Stringfy LL
def test_stringfy():
    returnedList = LinkedList()
    returnedList.insert("THR33")
    returnedList.insert("TOO")
    returnedList.insert("WON")
    returnedList.stringfy()
    actual = "{"+str(returnedList.head.data)+"}"+'-->'+"{"+str(returnedList.head.nextNode.data) + \
        "}"+'-->' + "{" + \
            str(returnedList.head.nextNode.nextNode.data)+"}" + '-->NULL'
    expected = "{WON}-->{TOO}-->{THR33}-->NULL"
    assert actual == expected


# get the length of LL
def test_get_len():
    returnedList = LinkedList()
    returnedList.insert("THR33")
    returnedList.insert("TOO")
    returnedList.insert("WON")
    actual = returnedList.get_len()
    expected = 3
    assert actual == expected
