from linked_list_zip.linked_list_zip import LinkedList
import pytest


def test_zip_list_megrge():
    "test file for zip function which merges two linked lists"
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append(111)
    ll1.append(222)
    ll1.append(333)
    ll2.append("A")
    ll2.append("B")
    ll2.append("C")
    y = ll1.zipLists(ll1, ll2)
    actual = repr(y)
    # actual = (
    #     "{"
    #     + str(ll1.head.data)
    #     + "}"
    #     + "-->"
    #     + "{"
    #     + str(ll1.head.nextNode.data)
    #     + "}"
    #     + "-->"
    #     + "{"
    #     + str(ll1.head.nextNode.nextNode.data)
    #     + "}"
    #     + "-->"
    #     + "{"
    #     + str(ll1.head.nextNode.nextNode.nextNode.data)
    #     + "}"
    #     + "-->"
    #     + "{"
    #     + str(ll1.head.nextNode.nextNode.nextNode.nextNode.data)
    #     + "}"
    #     + "-->"
    #     + "{"
    #     + str(ll1.head.nextNode.nextNode.nextNode.nextNode.nextNode.data)
    #     + "}"
    #     + "-->NULL"
    # )

    expected = "{111}-->{A}-->{222}-->{B}-->{333}-->{C}-->NULL"
    # "{111}-->{A}-->{222}-->{B}-->{333}-->{C}-->Null"
    assert actual == expected


def test_zip_list_megrge_2():
    "test file for zip function which merges two linked lists"
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append(555)
    ll1.append(777)
    ll1.append(999)
    ll2.append("F")
    ll2.append("S")

    actual = ll1.zipLists(ll1, ll2)

    expected = ll1.stringfy()
    # "{555}-->{F}-->{777}-->{S}-->{999}-->Null"
    assert actual == expected
