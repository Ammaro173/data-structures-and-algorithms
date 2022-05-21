import pytest
from merge_sort.merge_sort import _mergeSort


def test_merge_sort_simple():
    lst = [1, 2, 3, 9, 4, 5]
    _mergeSort(lst)
    assert lst == [1, 2, 3, 4, 5, 9]


def test_blog_merge_sort():
    lst = [8, 4, 23, 42, 16, 15]
    _mergeSort(lst)
    assert lst == [4, 8, 15, 16, 23, 42]


def test_reverse_sorted_merge_sort():
    lst = [20, 18, 12, 8, 5, -2]
    _mergeSort(lst)
    assert lst == [-2, 5, 8, 12, 18, 20]


def test_few_uniques_merge_sort():
    lst = [5, 12, 7, 5, 5, 7]
    _mergeSort(lst)
    assert lst == [5, 5, 5, 7, 7, 12]


def test_nearly_sorted_merge_sort():
    lst = [2, 3, 5, 7, 13, 11]
    _mergeSort(lst)
    assert lst == [2, 3, 5, 7, 11, 13]


def test_large_list_merge_sort():
    lst = [
        3,
        44,
        38,
        5,
        47,
        15,
        36,
        26,
        27,
        2,
        46,
        4,
        19,
        50,
        48,
        71,
        -2,
        -60,
        16,
        40,
        8,
    ]
    _mergeSort(lst)
    assert lst == [
        -60,
        -2,
        2,
        3,
        4,
        5,
        8,
        15,
        16,
        19,
        26,
        27,
        36,
        38,
        40,
        44,
        46,
        47,
        48,
        50,
        71,
    ]


def test_empty_list_merge_sort():
    lst = []
    _mergeSort(lst)
    assert lst == []
