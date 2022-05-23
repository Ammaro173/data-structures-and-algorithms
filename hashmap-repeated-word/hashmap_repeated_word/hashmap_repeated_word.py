import re


def repeated_word(string):
    """
    Accepts a string as an arguement.
    Returns a list: [first_repeated_word, dictionary_of_all_words, sorted_list_of_most_frequent_words]

    ################################################################
    # repeated_word returns a list
    #### index 0: first_repeated_word
    #### index 1: Dictionary of all the words and their individual counts
    #### index 2: Sorted list of the most frequent words
    ################################################################
    """

    string = re.sub(r"[^\w\s]", "", string)
    hash_map = {}
    first_matching_word = ""
    most_frequent_words = []

    # Modify your function to return a count of each of the words in the provided string #stretch_goal
    for word in string.split():
        word = word.lower()
        try:
            hash_map[word] += 1
            first_matching_word = first_matching_word or word
        except:
            hash_map[word] = 1

    # Modify your function to return a list of the words most frequently used in the provided string #stretch_goal
    for key in hash_map:
        most_frequent_words.append((hash_map[key], key))
    most_frequent_words.sort(reverse=True)

    # check if any words matched
    if first_matching_word:
        return [first_matching_word, hash_map, most_frequent_words]
    return ["No repeating words found", hash_map, most_frequent_words]
