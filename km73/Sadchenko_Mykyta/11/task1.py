def input_data():
    """
    This function is enters data

    Args:
        Function takes no args
    Returns:
        Set of symbols - string
        Amount of rows - natural integer
    Raises:
        No raises
    """
    return input("set of symbols: "), get_natural(input("amount of rows: "))


def get_natural(number):
    """
    This function is checking data(data must be int)

    Args:
        number - characters, that will be testing
    Returns:
        number - natural integer
    Raises:
        ValueError
    """
    if number.isdigit() != 0:
        return int(number)
    return get_natural(input("enter natural number: "))


def input_rows(amount):
    """
    This function is append words to list

    Args:
        amount - quantity of user input
    Returns:
        init_list - list of user inputs
    Raises:
        No raises
    """
    if amount == 0:
        return init_list
    init_list.append(input("words: "))
    return input_rows(amount-1)


def counting(word, amount, upd_list, i=0, meet=0):
    """
    This function is counting meetings word in list

    Args:
        word - string of characters
        amount - natural integer
        upd_list - list of words where counts word
        i - counter
        meet - value of meetings
    Returns:
        meet - value of meetings
    Raises:
        ValueError
    """
    meet += upd_list[i].count(word)
    if amount == 1:
        return meet
    return counting(word, amount-1, upd_list, i+1, meet)


def test_counting():
    """
    This function is testing function 'counting'

    Args:
        Function takes no args
    Returns:
        None
    Raises:
        AssertionError
    """
    assert counting('ex', 1, ['kexy']) == 1
    assert counting('tru', 2, ['kex', 'das']) == 0
    assert counting('3th', 3, ['fsfgf3th', 'sdsjth3', 'da3th3th']) == 3
    return None


def test_get_natural():
    """
    This function is testing function 'get_natural'

    Args:
        Function takes no args
    Returns:
        None
    Raises:
        AssertionError
    """
    assert get_natural('4') == 4
    assert get_natural('7') == 7
    assert get_natural('123') == 123
    return None


init_list = []
tuple_data = input_data()
test_counting()
test_get_natural()
print("\nmeetings:", counting(tuple_data[0], tuple_data[1], input_rows(tuple_data[1])))
