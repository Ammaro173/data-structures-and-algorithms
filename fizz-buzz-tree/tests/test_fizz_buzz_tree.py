import pytest
from fizz_buzz_tree.fizz_buzz_tree import KTreeNode, build_tree, fizz_buzz_tree


def test_build_tree():
    root = build_tree()
    assert root.value == 1
    assert root.children[0].value == 2
    assert root.children[1].value == 3
    assert root.children[2].value == 4
    assert root.children[0].children[0].value == 5
    assert root.children[0].children[1].value == 6
    assert root.children[0].children[2].value == 7
    assert root.children[1].children[0].value == 8
    assert root.children[1].children[1].value == 9
    assert root.children[1].children[2].value == 10
    assert root.children[2].children[0].value == 11
    assert root.children[2].children[1].value == 12
    assert root.children[2].children[2].value == 13
    assert root.children[2].children[3].value == 14
    assert root.children[2].children[4].value == 15


def test_fizz_buzz_tree():
    tree = build_tree()
    fizz_buzz_tree(tree)
    assert tree.value == "1"
    assert tree.children[0].value == "2"
    assert tree.children[1].value == "Fizz"
    assert tree.children[2].value == "4"
    assert tree.children[0].children[0].value == "Buzz"
    assert tree.children[0].children[1].value == "Fizz"
    assert tree.children[0].children[2].value == "7"
    assert tree.children[1].children[0].value == "8"
    assert tree.children[1].children[1].value == "Fizz"
    assert tree.children[1].children[2].value == "Buzz"
    assert tree.children[2].children[0].value == "11"
    assert tree.children[2].children[1].value == "Fizz"
    assert tree.children[2].children[2].value == "13"
    assert tree.children[2].children[3].value == "14"
    assert tree.children[2].children[4].value == "FizzBuzz"
