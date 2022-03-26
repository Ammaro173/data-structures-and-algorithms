from stacks_and_queues.stacks_and_queues import Stack, InvalidOperationError, Queue
import pytest


"""https://docs.pytest.org/en/6.2.x/assert.html 

Helped with Pytest assertion
"""

######################################
# Stacks Tests
def test_stack_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


def test_stack_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cheese")
    actual = s.top.value
    expected = "cheese"
    assert actual == expected


def test_stack_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


def test_stack_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cheese")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected


def test_stack_check_not_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.is_empty()
    expected = False
    assert actual == expected


def test_stack_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cheese")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


def test_stack_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


def test_stack_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as error:
        s.peek()

    assert str(error.value) == "Method not allowed on empty collection"


def test_stack_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as error:
        s.pop()

    assert str(error.value) == "Method not allowed on empty collection"


##########################################
# Queues Tests


# def test_Queue_enqueue():
#     q = Queue()
#     q.enqueue(111)
#     actual = q.front.value
#     expected = 111
#     assert actual == expected


def test_Queue_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected


def test_Queue_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cheese")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


def test_Queue_peek_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError) as error:
        q.peek()

    assert str(error.value) == "Method not allowed on empty collection"


def test_Queue_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


def test_Queue_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


def test_Queue_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


def test_Queue_dequeue_empty_list():
    q = Queue()
    with pytest.raises(InvalidOperationError) as error:
        q.dequeue()

    assert str(error.value) == "Method not allowed on empty collection"


def test_Queue_empty():
    assert Queue().front == None
    assert Queue().rear == None
