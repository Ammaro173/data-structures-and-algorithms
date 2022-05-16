def insertion_sort(list_of_ints):
    """Sorts a list of integers 'in-place' from least to greatest"""

    for i in range(1, len(list_of_ints)):  # starting outer loop at index 1
        j = i - 1
        int_to_insert = list_of_ints[i]

        while j >= 0 and int_to_insert < list_of_ints[j]:
            list_of_ints[j + 1] = list_of_ints[j]
            j -= 1
        list_of_ints[j + 1] = int_to_insert


if __name__ == "__main__":
    lst = [5, 2, 4, 6, 1, 3]
    insertion_sort(lst)
    print(lst)
