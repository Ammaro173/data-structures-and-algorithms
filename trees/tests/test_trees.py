import pytest
from trees.binary_tree import Node, BinaryTree, BinarySearchTree


# PYTEST FIXTURES FOR TESTING
@pytest.fixture()
def binary_search_tree_ten():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    new_tree.add(5)
    new_tree.add(20)
    new_tree.add(3)
    new_tree.add(100)
    new_tree.add(1)
    new_tree.add(15)
    new_tree.add(13)
    new_tree.add(2)
    new_tree.add(90)
    return new_tree


# @pytest.fixture(autouse=True)
# def reset_arr():
#     arr = []
#     return arr


# Can successfully instantiate an empty tree
def test_binary_search_tree_instance():
    new_tree = BinarySearchTree()
    assert new_tree.root == None


# Can successfully instantiate a tree with a single root node
def test_binary_search_tree_add_one():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    assert new_tree.root.value == 10


# Can successfully add a left children and right children to a single root tree
def test_binary_search_tree_add_three():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    new_tree.add(5)
    new_tree.add(20)
    assert new_tree.root.value == 10
    assert new_tree.root.right.value == 20
    assert new_tree.root.left.value == 5


def test_binary_search_tree_add_six():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    new_tree.add(5)
    new_tree.add(20)
    new_tree.add(2)
    new_tree.add(7)
    new_tree.add(25)
    assert new_tree.root.value == 10
    assert new_tree.root.right.right.value == 25
    assert new_tree.root.left.left.value == 2
    assert new_tree.root.left.right.value == 7


def test_binary_search_tree_add_ten():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    new_tree.add(5)
    new_tree.add(20)
    new_tree.add(3)
    new_tree.add(100)
    new_tree.add(1)
    new_tree.add(15)
    new_tree.add(13)
    new_tree.add(2)
    new_tree.add(90)
    assert new_tree.root.value == 10
    assert new_tree.root.right.right.left.value == 90
    assert new_tree.root.left.left.left.right.value == 2


# Can successfully return a collection from a pre_order traversal
# @pytest.mark.skip()
def test_pre_order_one():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    expected = [10]
    assert new_tree.pre_order(new_tree.root) == expected


# @pytest.mark.skip()
def test_pre_order_one_again():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    expected = [10]
    assert new_tree.pre_order(new_tree.root) == expected


# @pytest.mark.skip()
def test_pre_order_ten(binary_search_tree_ten):
    expected = [10, 5, 3, 1, 2, 20, 15, 13, 100, 90]
    assert binary_search_tree_ten.pre_order(binary_search_tree_ten.root) == expected


# Can successfully return a collection from an in_order traversal
# @pytest.mark.skip()
def test_in_order_ten(binary_search_tree_ten):
    expected = [1, 2, 3, 5, 10, 13, 15, 20, 90, 100]
    assert binary_search_tree_ten.in_order(binary_search_tree_ten.root) == expected


# Can successfully return a collection from a post_order traversal
# @pytest.mark.skip()
def test_post_order_ten(binary_search_tree_ten):
    expected = [2, 1, 3, 5, 13, 15, 90, 100, 20, 10]
    assert binary_search_tree_ten.post_order(binary_search_tree_ten.root) == expected


# Can sucessfully search for a given value
def test_contains_tree_of_ten(binary_search_tree_ten):
    expected = True
    assert binary_search_tree_ten.contains(10) == expected
    assert binary_search_tree_ten.contains(2) == expected
    assert binary_search_tree_ten.contains(1) == expected
    assert binary_search_tree_ten.contains(3) == expected
    assert binary_search_tree_ten.contains(5) == expected
    assert binary_search_tree_ten.contains(13) == expected
    assert binary_search_tree_ten.contains(15) == expected
    assert binary_search_tree_ten.contains(90) == expected
    assert binary_search_tree_ten.contains(100) == expected
    assert binary_search_tree_ten.contains(20) == expected
    assert binary_search_tree_ten.contains(60) == False
