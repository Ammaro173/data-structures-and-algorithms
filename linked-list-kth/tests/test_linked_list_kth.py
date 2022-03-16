from linked_list_kth.linked_list_kth import LinkedList
import pytest


def test_k_is_greather_than_len_ll():
    insertList = LinkedList()
    insertList.append(111)
    insertList.append(222)
    insertList.append(333)
    with pytest.raises(Exception):
        insertList.find_kth_value_from_end(4)


def test_k_len_is_qual_to_len_ll():
    insertList = LinkedList()
    insertList.append(111)
    insertList.append(222)
    insertList.append(333)
    actual = insertList.find_kth_value_from_end(2)
    expected = 111
    assert actual == expected


def test_k_is_negative_num():
    insertList = LinkedList()
    insertList.append(111)
    insertList.append(222)
    insertList.append(333)
    with pytest.raises(Exception):
        insertList.find_kth_value_from_end(-3)


def test_ll_len_is_one():
    insertList = LinkedList()
    insertList.append("WON")
    actual = [
        insertList.head.data,
    ]
    expected = ["WON"]
    assert actual == expected


def test_k_in_the_middle():
    insertList = LinkedList()
    insertList.append(111)
    insertList.append(222)
    insertList.append(333)
    actual = insertList.find_kth_value_from_end(1)
    expected = 222
    assert actual == expected
