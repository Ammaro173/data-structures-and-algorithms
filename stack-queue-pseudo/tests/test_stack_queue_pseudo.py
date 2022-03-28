from stack_queue_pseudo.stack_queue_pseudo import Pseudo_queue
import pytest


def test_enqueue_and_dequeue_Pseudo_queue():
    q = Pseudo_queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cheese")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


def test_is_empty():
    q = Pseudo_queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected
