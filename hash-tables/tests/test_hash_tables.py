import pytest
from hash_tables.hash_tables import HashTable, Bucket, Node

# Successfully hash a key to an in-range value
def test_hash():
    ht = HashTable()
    hash_val = ht._hash("apple")
    assert hash_val == 847
    assert ht._hash("apple") == hash_val


# Adding a key/value to your hashtable results in the value being in the data structure
def test_add_to_hash_table():
    ht = HashTable()
    ht.add("apple", 43)
    hash_val = ht._hash("apple")
    assert ht._hash_table[hash_val].head.key == "apple"
    assert ht._hash_table[hash_val].head.value == 43


def test_bucket_includes():
    ht = HashTable()
    ht.add("apple", 43)
    hash_val = ht._hash("apple")
    assert ht._hash_table[hash_val].includes("apple") == True
    assert ht._hash_table[hash_val].includes("mango") == False


def test_bucket_add_duplicates_includes():
    ht = HashTable()
    ht.add("apple", 43)
    ht.add("apple", 6)
    ht.add("apple", 643)
    apple_index = ht._hash("apple")
    ht.add("mango", "steen")
    mango_index = ht._hash("mango")

    assert ht._hash_table[mango_index].includes("mango") == True
    assert ht._hash_table[apple_index].includes("mango") == False
    assert ht._hash_table[apple_index].includes("apple") == True


# Retrieving based on a key returns the value stored
def test_get_hash_table():
    ht = HashTable()
    ht.add("apple", 43)
    assert ht.get("apple") == 43


def test_get_many():
    ht = HashTable()
    ht.add("apple", 43)
    ht.add("banana", 32)
    ht.add("mango", 21)
    ht.add("pear", 54)
    ht.add("strawbery", 65)

    assert ht.get("apple") == 43
    assert ht.get("banana") == 32
    assert ht.get("mango") == 21
    assert ht.get("pear") == 54
    assert ht.get("strawbery") == 65
    assert ht.get("tomato") == None


# Successfully returns None for a key that does not exist in the hashtable
def test_contains():
    ht = HashTable()
    ht.add("apple", 43)
    assert ht.contains("apple") == True
    assert ht.contains("mango") == None


# Successfully handle a collision within the hashtable
def test_collision_at_index_fourty():
    ht = HashTable()
    ht._hash_table[40] = Bucket()
    node_one = Node("apple", 43)
    node_two = Node("mango", 21)
    ht._hash_table[40].add(node_one)
    ht._hash_table[40].add(node_two)

    assert ht._hash_table[40].head.key == "apple"  # first node
    assert ht._hash_table[40].head.next.key == "mango"  # second node added
    assert ht._hash_table[40].head.next.next == None  # no other nodes added


# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_value_at_index_fourty():
    ht = HashTable()
    ht._hash_table[40] = Bucket()

    node_one = Node("apple", 43)
    node_two = Node("mango", 21)
    node_three = Node("pear", 65)
    node_four = Node("tomato", "potato")

    ht._hash_table[40].add(node_one)
    ht._hash_table[40].add(node_two)
    ht._hash_table[40].add(node_three)
    ht._hash_table[40].add(node_four)

    assert ht._hash_table[40].return_value("apple") == 43
    assert ht._hash_table[40].return_value("mango") == 21
    assert ht._hash_table[40].return_value("tomato") == "potato"
    assert ht._hash_table[40].return_value("pear") == 65
    assert ht._hash_table[40].return_value("banana") == None
