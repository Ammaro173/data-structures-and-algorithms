def _mergeSort(arr):
    """
    Function that accepts a list of integers as an arguement
    Sorts the integers in place by value using a merge-sort algorithm; low to high
    No return; sorts the list 'in-place'
    """
    n = len(arr)

    if n > 1:  # list is more than one element(for sorting)
        mid = n // 2
        # TypeError: slice indices must be integers or None or have an __index__ method

        left = arr[:mid]  # left half
        right = arr[mid:]  # right half

        _mergeSort(left)  # recursion down to 1 element
        _mergeSort(right)  # recursion down to 1 element
        _merge(left, right, arr)  # helper function to merge left and right


def _merge(left, right, arr):
    """Responsible for merging a sorted right list of ints and sorted left list of ints together into one list"""
    i, j, k = 0, 0, 0

    # Assigns values of the final list starting at index 0 (k) the values of the lesser between left and right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # you have exhausted all values in the left
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    # you have exhausted all values in right
    else:
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
