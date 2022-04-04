from stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_valid_brackets():
    """
    Random Test for the validity of brackets function
    """
    actual = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected


def test_emt_valid_brackets():
    """returns True if brackets are valid, since there is no error on brackets return True"""

    actual = validate_brackets("")
    expected = True
    assert actual == expected


def test_all_types_but_true():
    """
    Test for all types of brackets
    """
    actual = validate_brackets("{}()[]")
    expected = True
    assert actual == expected


def test_all_types_valid_true_2():
    """
    Test for all types of brackets retrun True
    """
    actual = validate_brackets("(){}[[]]")
    expected = True
    assert actual == expected


def test_all_types_but_false():
    """
    Test for all types of brackets retrun False
    """
    actual = validate_brackets("{}[)]")
    expected = False
    assert actual == expected


def test_all_types_but_false_2():
    """
    Test for all types of brackets retrun False
    """
    actual = validate_brackets("[")
    expected = False
    assert actual == expected


def test_all_types_but_false_3():
    """
    Test for all types of brackets retrun False
    """
    actual = validate_brackets("[}")
    expected = False
    assert actual == expected
